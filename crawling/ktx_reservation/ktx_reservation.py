from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from ktx_reservation_ui import Ui_Form
import sys
import time
import threading

from selenium import webdriver
from selenium.common import UnexpectedAlertPresentException, StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import pyperclip


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.ticket_btn.clicked.connect(self.formValid)
        self.ticket_exit_btn.clicked.connect(self.crawlingExit)



    '''
        크롤링 멀티 쓰레드 지정
    '''
    def crawlingInit(self):
        self.textBrowser.append("티켓팅 시스템이 시작되었습니다. 별도 조작을 하지 말아주시기 바랍니다.")
        self.thread = threading.Thread(target=self.crawlingCore)
        self.thread.start()


    '''
        티켓팅 크롤링 진행
    '''
    def crawlingCore(self):
        QApplication.processEvents()

        # 크롤링 옵션 설정
        options = Options()
        options.add_argument("--headless") # 브라우저 보이지 않게 실행
        options.add_argument("--disable-gpu") # GPU 비활성화
        options.add_argument("--no-sandbox") # 샌드박스 비활성화
        options.add_argument("--disalbe-dev-shm-usage") # 공유 메모리 문제 해결

        # 크롬 드라이버 실행
        global driver
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.letskorail.com/korail/com/login.do")
        time.sleep(1)

        # 휴대폰 번호 로그인
        driver.find_element(By.CSS_SELECTOR, "#radInputFlg2").click()
        driver.find_element(By.CSS_SELECTOR, "#txtCpNo2").send_keys(self.cell_second.text())
        driver.find_element(By.CSS_SELECTOR, "#txtCpNo3").send_keys(self.cell_end.text())
        driver.find_element(By.CSS_SELECTOR, "#txtPwd1").send_keys(self.password.text())
        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, "#loginDisplay2 > ul > li.btn_login > a").click()
        time.sleep(2)

        try:
            driver.get("https://www.letskorail.com/ebizprd/EbizPrdTicketpr21100W_pr21110.do")
            time.sleep(1)
        except UnexpectedAlertPresentException as e:
            self.textBrowser.append("비밀번호 오류 입니다. 한/영키를 확인하여 재입력해주세요.")
            self.crawlingExit()
            return
        

        # 티켓팅 정보 입력
        start = driver.find_element(By.CSS_SELECTOR, "#start")
        start.clear()
        start.send_keys(self.place_start.text())

        end = driver.find_element(By.CSS_SELECTOR, "#get")
        end.clear()
        end.send_keys(self.place_end.text())

        Select(driver.find_element(By.CSS_SELECTOR, "#s_month")).select_by_value(self.ticket_month.text())
        Select(driver.find_element(By.CSS_SELECTOR, "#s_day")).select_by_value(self.ticket_day.text())
        Select(driver.find_element(By.CSS_SELECTOR, "#s_hour")).select_by_value(self.ticket_time.text())
        driver.find_element(By.CSS_SELECTOR, "#center > form > div > p > a").click()
        time.sleep(1)

        # 티켓팅 크롤링 시작
        is_fetch = False
        index = 1
        while not is_fetch:
            self.textBrowser.append(f"예약시도중...({index})")
            QApplication.processEvents()

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#tableResult"))
            )
            
            trs = driver.find_elements(By.CSS_SELECTOR, "#tableResult > tbody > tr")
            for tr in trs:
                try:
                    normal_room = tr.find_element(By.CSS_SELECTOR, "td:nth-of-type(6) img")
                    if normal_room.get_attribute("alt") == "예약하기":
                        normal_room.click()
                        time.sleep(1)
                        
                        try:
                            iframe = driver.find_element(By.CSS_SELECTOR, "#embeded-modal-traininfo")
                            driver.switch_to.frame(iframe)
                
                            driver.find_element(By.CSS_SELECTOR, "body > div > div.cont > p.btn_c > a").click()
                            time.sleep(1)
                
                            driver.switch_to.default_content()
                        except UnexpectedAlertPresentException as e:
                            alert = driver.switch_to.alert()
                            alert.accept()
                            time.sleep(1)
                        except Exception as e:
                            pass
                        finally:
                            is_fetch = True
                            break
                except StaleElementReferenceException as e:
                    time.sleep(2)
                    continue
                
            if not is_fetch:
                try:
                    button = driver.find_element(By.CSS_SELECTOR, "#divResult > table.btn > tbody > tr > td > a > img")
                    if button.get_attribute("alt") == "다음":
                        button.click()
                        time.sleep(2)
                    else:
                        driver.find_element(By.CSS_SELECTOR, "#center > div.ticket_box > p > a").click()
                        time.sleep(2)

                    index = index + 1
                except StaleElementReferenceException as e:
                    time.sleep(2)
                    continue


        # 티켓팅 정보 확인 및 결제 페이지 이동
        driver.switch_to.default_content()
        driver.find_element(By.CSS_SELECTOR, "#btn_next").click()

        # 신용카드 결제 진행
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#tabStl1"))
        )

        driver.find_element(By.CSS_SELECTOR, "#tabStl1").click()
        time.sleep(1)

        # 카드번호
        driver.find_element(By.CSS_SELECTOR, "#Div_Card > table > tbody > tr:nth-child(2) > td > input:nth-child(1)").send_keys(self.card_1.text())
        driver.find_element(By.CSS_SELECTOR, "#Div_Card > table > tbody > tr:nth-child(2) > td > input:nth-child(2)").send_keys(self.card_2.text())
        driver.find_element(By.CSS_SELECTOR, "#Div_Card > table > tbody > tr:nth-child(2) > td > input:nth-child(3)").send_keys(self.card_3.text())
        driver.find_element(By.CSS_SELECTOR, "#Div_Card > table > tbody > tr:nth-child(2) > td > input:nth-child(4)").send_keys(self.card_4.text())

        # 유효기간
        Select(driver.find_element(By.CSS_SELECTOR, "#month")).select_by_value(self.card_month.text())
        Select(driver.find_element(By.CSS_SELECTOR, "#year")).select_by_value(self.card_year.text())

        # 카드비밀번호 및 생년월일
        driver.find_element(By.CSS_SELECTOR, "#Div_Card > table > tbody > tr:nth-child(5) > td > input").send_keys(self.card_password.text())
        driver.find_element(By.CSS_SELECTOR, "#Div_Card > table > tbody > tr:nth-child(6) > td > input").send_keys(self.person_number.text())

        # 체크 동의
        driver.find_element(By.CSS_SELECTOR, "#chkAgree").click()
        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, "#fnIssuing").click()
        time.sleep(1)

        # 결제 및 발권하기
        iframe = driver.find_element(By.CSS_SELECTOR, "#mainframeSaleInfo")
        driver.switch_to.frame(iframe)
        driver.find_element(By.CSS_SELECTOR, "#btn_next1").click()

        try:
            alert = driver.switch_to.alert
            alert.accept()
        except:
            pass

        self.textBrowser.append("예약이 완료되었습니다.")
        QApplication.processEvents()
        driver.quit()


    '''
        티켓팅 종료
    '''
    def crawlingExit(self):
        driver.quit()
        self.textBrowser.append("티켓팅이 종료되었습니다.")



    '''
        Form 필수값 검증
    '''
    def formValid(self):
        # 휴대폰 번호
        if not self.cell_second.text() or not self.cell_end.text():
            self.waringAlert(self.cell_label.text())

        # 비밀번호
        elif not self.password.text():
            self.waringAlert(self.password_label.text())

        # 키드번호
        elif not self.card_1.text() or not self.card_2.text() or not self.card_3.text() or not self.card_4.text():
            self.waringAlert(self.card_number_label.text())

        # 유효기간
        elif not self.card_month.text() or not self.card_year.text():
            self.waringAlert(self.card_valid_label.text())
        
        # 카드 비밀번호
        elif not self.card_password.text():
            self.waringAlert(self.card_password_label.text())

        # 생년월일
        elif not self.person_number.text():
            self.waringAlert(self.card_person_number_label.text())

        # 출발지
        elif not self.place_start.text():
            self.waringAlert(self.place_start_label.text())

        # 도착지
        elif not self.place_end.text():
            self.waringAlert(self.place_end_label.text())

        # 예약날짜
        elif not self.ticket_month.text() or not self.ticket_day.text() or not self.ticket_time.text():
            self.waringAlert(self.place_ticket_label.text())

        # 크롤링
        self.crawlingInit()


    '''
        Alert 공통 처리
    '''
    def waringAlert(self, msg):
        QMessageBox.warning(self, "필수값", f"{msg}는(은) 필수값입니다.")


app = QApplication()

window = MainWindow()
window.show()

sys.exit(app.exec())