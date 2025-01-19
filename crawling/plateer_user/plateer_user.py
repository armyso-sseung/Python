from PySide6.QtWidgets import QApplication, QWidget, QTableView, QVBoxLayout
from PySide6.QtGui import QStandardItemModel, QStandardItem, QPixmap
from plateer_user_ui import Ui_Plateer
import sys

class MainWindow(QWidget, Ui_Plateer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 테이블 뷰와 모델 설정
        self.user_table_view = QTableView(self)
        self.model = QStandardItemModel(self)
        self.user_table_view.setModel(self.model)

        # 헤더 설정
        self.model.setHorizontalHeaderLabels(["이미지", "이름", "아이디", "부서", "생년월일"])

        layout = QVBoxLayout()
        layout.addWidget(self.user_table_view)

        # 프로그램 타이틀
        self.setWindowTitle("Plateer User View")



app = QApplication()

window = MainWindow()
window.show()

sys.exit(app.exec())