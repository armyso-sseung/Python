import time

from PySide6.QtWidgets import QApplication, QWidget, QTableView, QVBoxLayout, QMessageBox
from PySide6.QtGui import QStandardItemModel, QStandardItem, QPixmap, QIcon
from plateer_user_ui import Ui_Plateer

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import os
import sys
import sqlite3
import requests
import threading


"""
    DB 위치 조회 함수
"""
def current_databse_path():
    """
        하기 순차 조건
        1. PyInstaller 로 빌드된 경우
        2. 스크립트로 빌드된 경우
        3. 주피터로 빌드된 경우
    """
    if getattr(sys, 'frozebn', False):
        app_path = os.path.dirname(sys.executable)
    elif '__file__' in globals():
        app_path = os.path.dirname(os.path.abspath(__file__))
    else:
        app_path = os.getcwd()

    return os.path.join(app_path, 'plateer_user.db')


class MainWindow(QWidget, Ui_Plateer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initialization_program()

    """
        초기 셋팅
    """
    def initialization_program(self):
        # 테이블 뷰와 모델 설정
        self.model = QStandardItemModel(self)
        self.user_table_view.setModel(self.model)

        # 프로그램 타이틀
        self.setWindowTitle("Plateer User View")

        # 업데이트 버튼 연결
        self.email.returnPressed.connect(self.plateer_user_update_init)
        self.password.returnPressed.connect(self.plateer_user_update_init)
        self.update_btn.clicked.connect(self.plateer_user_update_init)

        # 검색 버튼 연결
        self.search.returnPressed.connect(self.plateer_user_search)
        self.search_btn.clicked.connect(self.plateer_user_search)

        # 데이터 조회
        self.load_user_data('')

    """
        SQLite Database 초기 셋팅
    """
    def init_database(self):
        db_path = current_databse_path()
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS data (
                no INTEGER PRIMARY KEY AUTOINCREMENT,
                id TEXT UNIQUE NOT NULL,
                name TEXT NOT NULL,
                birthday TEXT NOT NULL,
                department TEXT,
                image TEXT
            )
        ''')

        conn.commit()
        conn.close()

    """
        크롤링 쓰레드 영역
    """
    def plateer_user_update_init(self):
        if not self.email.text() or not self.password.text():
            return QMessageBox.warning(self, '', '이메일과 비밀번호는 필수값입니다.')

        self.plateer_user_update_core()
        # self.thread = threading.Thread(target=self.plateer_user_update_core)
        # self.thread.start()

    """
        크롤링 코어 영역
    """
    def plateer_user_update_core(self):
        # 셀레리움 옵션
        options = Options()
        options.add_argument("--headless")  # 브라우저 보이지 않게 실행
        options.add_argument("--disable-gpu")  # GPU 비활성화
        options.add_argument("--no-sandbox")  # 샌드박스 비활성화
        options.add_argument("--disalbe-dev-shm-usage")  # 공유 메모리 문제 해결

        # 크롬 드라이버 실행
        driver = webdriver.Chrome(options=options)
        driver.get("https://login.microsoftonline.com/")
        time.sleep(1)

        try:
            # MS 로그인
            self.login_msoffice(driver)

            # 플래티어 로그인
            self.login_plateer(driver)

            # 사용자 업데이트
            self.update_plateer_user(driver)
        except Exception as e:
            print(e)
        finally:
            driver.quit()

    """
        MS Office 로그인
    """
    def login_msoffice(self, driver):
        # 로그인
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#i0116"))
        )
        id_input = driver.find_element(By.CSS_SELECTOR, "#i0116")
        id_input.clear()
        id_input.send_keys(self.email.text(), Keys.ENTER)
        time.sleep(1)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#i0118"))
        )
        pw_input = driver.find_element(By.CSS_SELECTOR, "#i0118")
        pw_input.clear()
        pw_input.send_keys(self.password.text(), Keys.ENTER)
        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, "#idSIButton9").click()
        time.sleep(1)

    """
        플래티어 사이트 로그인
    """
    def login_plateer(self, driver):
        # MS 연동창
        driver.get("https://gw.plateer.com/")
        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, "#tilesHolder > div.tile-container > div > div.table").click()
        time.sleep(1)

    """
        사용자 API 호출 및 DB 저장
    """
    def update_plateer_user(self, driver):
        db_path = current_databse_path()

        # 쿠키 헤더 추출
        loginCookie = driver.get_cookie('loginCookie').get("value")
        header = {
            "Cookie": f"loginCookie={loginCookie}"
        }

        # DB 연결
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # 기존 테이블 초기화
        data = []
        cursor.execute('DELETE FROM data')
        cursor.execute('DELETE FROM sqlite_sequence WHERE name="data"')

        for month in range(1, 13):
            response = requests.get(
                f"https://gw.plateer.com/ezNewPortal/getMonthlyBirthdayEmployees.do?birthdayMonth={month}&birthdayCurPage=1&birthdayCount=100",
                headers=header)
            birthday_list = response.json()['birthdayList']
            db_data_info = [
                (user["userId"], user["userName"], user["userBirthday"], user["userDeptName"], user["userImg"]) for user
                in birthday_list]

            data = [*data, *db_data_info]

        cursor.executemany('INSERT INTO data (id, name, birthday, department, image) VALUES (?, ?, ?, ?, ?)', data)
        conn.commit()
        conn.close()

        # 데이터 조회
        QMessageBox.warning(self, '', '사용자 정보가 업데이트 되었습니다.')
        self.load_user_data('')

    """
        사용자 검색
    """
    def plateer_user_search(self):
        self.load_user_data(self.search.text())

    """
        URL를 통핸 사용자 정보에 주입
    """
    def load_image_from_url(self, url, user):
        result_url = f"https://gw.plateer.com{url}"
        try:
            # response = requests.get(result_url, stream=True)
            # response.raise_for_status()
            #
            # # URL을 통해 이미지를 로드
            # pixmap = QPixmap()
            #
            # # 이미지를 로드한 후 아이콘으로 설정 (로드 실패의 경우 기본 이미지)
            # user.setIcon(pixmap if pixmap.loadFromData(response.content) else QPixmap(100, 100))
            user.setIcon(QPixmap(100, 100))
        except requests.RequestException as e:
            user.setIcon(QPixmap(100, 100))

    """
        사용자 조회 및 화면 업데이트
    """
    def load_user_data(self, search):
        # 헤더 설정
        self.model.clear()
        self.model.setHorizontalHeaderLabels(["이미지", "이름", "아이디", "부서", "생년월일"])

        db_path = current_databse_path()
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        where_name = (f'%{search}%',)
        cursor.execute('SELECT * FROM data WHERE NAME like ? ORDER BY Name', where_name)
        rows = cursor.fetchall()
        conn.close()

        if rows:
            for row in rows:
                image = QStandardItem()
                self.load_image_from_url(row[5], image)

                id = QStandardItem(row[1])
                name = QStandardItem(row[2])
                dept = QStandardItem(row[4])
                birth = QStandardItem(row[3])

                image.setEditable(False)
                id.setEditable(False)
                name.setEditable(False)
                dept.setEditable(False)
                birth.setEditable(False)

                # image = self.load_image_from_url(row[5], QStandardItem())
                self.model.appendRow([image, name, id, dept, birth])


app = QApplication()

window = MainWindow()
window.show()

sys.exit(app.exec())
