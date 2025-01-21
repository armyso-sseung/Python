from PySide6.QtWidgets import QApplication, QWidget, QTableView, QVBoxLayout
from PySide6.QtGui import QStandardItemModel, QStandardItem, QPixmap, QIcon
from plateer_user_ui import Ui_Plateer

import os
import sys
import sqlite3


class MainWindow(QWidget, Ui_Plateer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 테이블 뷰와 모델 설정
        self.model = QStandardItemModel(self)
        self.user_table_view.setModel(self.model)

        # 헤더 설정
        self.model.setHorizontalHeaderLabels(["이미지", "이름", "아이디", "부서", "생년월일"])

        # 프로그램 타이틀
        self.setWindowTitle("Plateer User View")

    """
        SQLite Database Initialization
    """
    def init_database(self):
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

        db_path = os.path.join(app_path, 'plateer_user.db')
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
        URL를 통핸 사용자 정보에 주입
    """
    def load_image_from_url(self, url, user):
        # URL을 통해 이미지를 로드
        pixmap = QPixmap(url)

        # 이미지를 로드한 후 아이콘으로 설정 (로드 실패의 경우 기본 이미지)
        user.setIcon(pixmap if pixmap.isNull() else QPixmap(100, 100))


app = QApplication()

window = MainWindow()
window.show()

sys.exit(app.exec())
