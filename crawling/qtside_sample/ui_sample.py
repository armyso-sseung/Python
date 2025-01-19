from PySide6.QtWidgets import QApplication, QWidget 
from login_ui import Ui_Form
import sys

class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.login_btn.clicked.connect(self.login)

    def login(self):
        print(self.id.text())
        print(self.password.text())


app = QApplication()

window = MainWindow()
window.show()

sys.exit(app.exec())