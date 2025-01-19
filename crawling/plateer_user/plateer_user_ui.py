# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plateer_user.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableView, QVBoxLayout, QWidget)

class Ui_Plateer(object):
    def setupUi(self, Plateer):
        if not Plateer.objectName():
            Plateer.setObjectName(u"Plateer")
        Plateer.resize(608, 541)
        self.gridLayout = QGridLayout(Plateer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 10, 5, -1)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.formLayout.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayout.setContentsMargins(12, -1, 0, -1)
        self.email_label = QLabel(Plateer)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setMinimumSize(QSize(60, 0))
        font = QFont()
        font.setFamilies([u"Apple SD Gothic Neo"])
        font.setPointSize(15)
        font.setBold(True)
        self.email_label.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.email_label)

        self.email = QLineEdit(Plateer)
        self.email.setObjectName(u"email")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.email.sizePolicy().hasHeightForWidth())
        self.email.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.email)


        self.horizontalLayout.addLayout(self.formLayout)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.formLayout_2.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayout_2.setContentsMargins(12, -1, 0, -1)
        self.password_label = QLabel(Plateer)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setMinimumSize(QSize(60, 0))
        self.password_label.setFont(font)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.password_label)

        self.password = QLineEdit(Plateer)
        self.password.setObjectName(u"password")
        sizePolicy.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy)
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.password)


        self.horizontalLayout.addLayout(self.formLayout_2)

        self.update_btn = QPushButton(Plateer)
        self.update_btn.setObjectName(u"update_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.update_btn.sizePolicy().hasHeightForWidth())
        self.update_btn.setSizePolicy(sizePolicy1)
        self.update_btn.setMinimumSize(QSize(100, 0))
        self.update_btn.setFont(font)

        self.horizontalLayout.addWidget(self.update_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(17, 10, 5, -1)
        self.search_label = QLabel(Plateer)
        self.search_label.setObjectName(u"search_label")
        self.search_label.setMinimumSize(QSize(60, 0))
        self.search_label.setFont(font)

        self.horizontalLayout_2.addWidget(self.search_label)

        self.search = QLineEdit(Plateer)
        self.search.setObjectName(u"search")
        sizePolicy.setHeightForWidth(self.search.sizePolicy().hasHeightForWidth())
        self.search.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.search)

        self.search_btn = QPushButton(Plateer)
        self.search_btn.setObjectName(u"search_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.search_btn.sizePolicy().hasHeightForWidth())
        self.search_btn.setSizePolicy(sizePolicy2)
        self.search_btn.setMinimumSize(QSize(100, 0))
        self.search_btn.setFont(font)

        self.horizontalLayout_2.addWidget(self.search_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.user_table_view = QTableView(Plateer)
        self.user_table_view.setObjectName(u"user_table_view")

        self.verticalLayout.addWidget(self.user_table_view)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Plateer)

        QMetaObject.connectSlotsByName(Plateer)
    # setupUi

    def retranslateUi(self, Plateer):
        Plateer.setWindowTitle(QCoreApplication.translate("Plateer", u"Form", None))
        self.email_label.setText(QCoreApplication.translate("Plateer", u"\uc774\uba54\uc77c", None))
        self.password_label.setText(QCoreApplication.translate("Plateer", u"\ube44\ubc00\ubc88\ud638", None))
        self.update_btn.setText(QCoreApplication.translate("Plateer", u"\uc5c5\ub370\uc774\ud2b8", None))
        self.search_label.setText(QCoreApplication.translate("Plateer", u"\uc774\ub984", None))
        self.search_btn.setText(QCoreApplication.translate("Plateer", u"\uac80\uc0c9", None))
    # retranslateUi

