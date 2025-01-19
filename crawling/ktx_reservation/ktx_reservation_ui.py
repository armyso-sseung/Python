# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ktx_reservation.ui'
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
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(760, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout = QVBoxLayout()
#ifndef Q_OS_MAC
        self.verticalLayout.setSpacing(-1)
#endif
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 20, -1, -1)
        self.label_15 = QLabel(Form)
        self.label_15.setObjectName(u"label_15")
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Apple SD Gothic Neo"])
        font.setPointSize(22)
        font.setBold(True)
        self.label_15.setFont(font)
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_15)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.formLayout_4.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.formLayout_4.setRowWrapPolicy(QFormLayout.RowWrapPolicy.DontWrapRows)
        self.formLayout_4.setLabelAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.formLayout_4.setFormAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)
        self.formLayout_4.setHorizontalSpacing(-1)
        self.formLayout_4.setVerticalSpacing(-1)
        self.formLayout_4.setContentsMargins(12, -1, 12, -1)
        self.cell_label = QLabel(Form)
        self.cell_label.setObjectName(u"cell_label")
        font1 = QFont()
        font1.setFamilies([u"Apple SD Gothic Neo"])
        font1.setPointSize(16)
        font1.setBold(False)
        self.cell_label.setFont(font1)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.cell_label)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy1)
        self.lineEdit_2.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_2.setStyleSheet(u"disabled")
        self.lineEdit_2.setMaxLength(32768)

        self.horizontalLayout_8.addWidget(self.lineEdit_2)

        self.cell_second = QLineEdit(Form)
        self.cell_second.setObjectName(u"cell_second")
        sizePolicy1.setHeightForWidth(self.cell_second.sizePolicy().hasHeightForWidth())
        self.cell_second.setSizePolicy(sizePolicy1)
        self.cell_second.setMaximumSize(QSize(16777215, 16777215))
        self.cell_second.setMaxLength(4)

        self.horizontalLayout_8.addWidget(self.cell_second)

        self.cell_end = QLineEdit(Form)
        self.cell_end.setObjectName(u"cell_end")
        sizePolicy1.setHeightForWidth(self.cell_end.sizePolicy().hasHeightForWidth())
        self.cell_end.setSizePolicy(sizePolicy1)
        self.cell_end.setMaximumSize(QSize(16777215, 16777215))
        self.cell_end.setMaxLength(4)

        self.horizontalLayout_8.addWidget(self.cell_end)


        self.formLayout_4.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_8)

        self.password_label = QLabel(Form)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setFont(font1)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.password_label)

        self.password = QLineEdit(Form)
        self.password.setObjectName(u"password")
        sizePolicy1.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy1)
        self.password.setMaximumSize(QSize(16777215, 16777215))
        self.password.setMaxLength(32768)
        self.password.setEchoMode(QLineEdit.EchoMode.Password)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.password)


        self.verticalLayout_4.addLayout(self.formLayout_4)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_10)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.formLayout.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayout.setContentsMargins(12, -1, 12, -1)
        self.card_number_label = QLabel(Form)
        self.card_number_label.setObjectName(u"card_number_label")
        self.card_number_label.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.card_number_label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.card_1 = QLineEdit(Form)
        self.card_1.setObjectName(u"card_1")
        sizePolicy1.setHeightForWidth(self.card_1.sizePolicy().hasHeightForWidth())
        self.card_1.setSizePolicy(sizePolicy1)
        self.card_1.setMaximumSize(QSize(16777215, 16777215))
        self.card_1.setMaxLength(4)

        self.horizontalLayout_2.addWidget(self.card_1)

        self.card_2 = QLineEdit(Form)
        self.card_2.setObjectName(u"card_2")
        sizePolicy1.setHeightForWidth(self.card_2.sizePolicy().hasHeightForWidth())
        self.card_2.setSizePolicy(sizePolicy1)
        self.card_2.setMaximumSize(QSize(16777215, 16777215))
        self.card_2.setMaxLength(4)

        self.horizontalLayout_2.addWidget(self.card_2)

        self.card_3 = QLineEdit(Form)
        self.card_3.setObjectName(u"card_3")
        sizePolicy1.setHeightForWidth(self.card_3.sizePolicy().hasHeightForWidth())
        self.card_3.setSizePolicy(sizePolicy1)
        self.card_3.setMaximumSize(QSize(16777215, 16777215))
        self.card_3.setMaxLength(4)

        self.horizontalLayout_2.addWidget(self.card_3)

        self.card_4 = QLineEdit(Form)
        self.card_4.setObjectName(u"card_4")
        sizePolicy1.setHeightForWidth(self.card_4.sizePolicy().hasHeightForWidth())
        self.card_4.setSizePolicy(sizePolicy1)
        self.card_4.setMaximumSize(QSize(16777215, 16777215))
        self.card_4.setMaxLength(4)

        self.horizontalLayout_2.addWidget(self.card_4)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.card_valid_label = QLabel(Form)
        self.card_valid_label.setObjectName(u"card_valid_label")
        self.card_valid_label.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.card_valid_label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.card_month = QLineEdit(Form)
        self.card_month.setObjectName(u"card_month")
        sizePolicy1.setHeightForWidth(self.card_month.sizePolicy().hasHeightForWidth())
        self.card_month.setSizePolicy(sizePolicy1)
        self.card_month.setMaxLength(2)

        self.horizontalLayout_3.addWidget(self.card_month)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.card_year = QLineEdit(Form)
        self.card_year.setObjectName(u"card_year")
        sizePolicy1.setHeightForWidth(self.card_year.sizePolicy().hasHeightForWidth())
        self.card_year.setSizePolicy(sizePolicy1)
        self.card_year.setMaxLength(2)

        self.horizontalLayout_3.addWidget(self.card_year)


        self.formLayout.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.card_password_label = QLabel(Form)
        self.card_password_label.setObjectName(u"card_password_label")
        self.card_password_label.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.card_password_label)

        self.card_person_number_label = QLabel(Form)
        self.card_person_number_label.setObjectName(u"card_person_number_label")
        self.card_person_number_label.setFont(font1)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.card_person_number_label)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.card_password = QLineEdit(Form)
        self.card_password.setObjectName(u"card_password")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.card_password.sizePolicy().hasHeightForWidth())
        self.card_password.setSizePolicy(sizePolicy2)
        self.card_password.setMaxLength(2)
        self.card_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_5.addWidget(self.card_password)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy3)
        self.label_8.setAutoFillBackground(True)

        self.horizontalLayout_5.addWidget(self.label_8)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.person_number = QLineEdit(Form)
        self.person_number.setObjectName(u"person_number")
        sizePolicy1.setHeightForWidth(self.person_number.sizePolicy().hasHeightForWidth())
        self.person_number.setSizePolicy(sizePolicy1)
        self.person_number.setMaxLength(6)

        self.horizontalLayout_4.addWidget(self.person_number)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_4.addWidget(self.label_7)


        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.verticalLayout_2.setStretch(1, 1)

        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.horizontalLayout_7.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 20, -1, -1)
        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setFont(font)
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_12)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.formLayout_3.setFormAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.formLayout_3.setContentsMargins(12, -1, 12, -1)
        self.place_start_label = QLabel(Form)
        self.place_start_label.setObjectName(u"place_start_label")
        self.place_start_label.setFont(font1)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.place_start_label)

        self.place_start = QLineEdit(Form)
        self.place_start.setObjectName(u"place_start")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.place_start)

        self.place_end_label = QLabel(Form)
        self.place_end_label.setObjectName(u"place_end_label")
        self.place_end_label.setFont(font1)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.place_end_label)

        self.place_end = QLineEdit(Form)
        self.place_end.setObjectName(u"place_end")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.place_end)

        self.place_ticket_label = QLabel(Form)
        self.place_ticket_label.setObjectName(u"place_ticket_label")
        self.place_ticket_label.setFont(font1)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.place_ticket_label)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.ticket_month = QLineEdit(Form)
        self.ticket_month.setObjectName(u"ticket_month")
        self.ticket_month.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.ticket_month.sizePolicy().hasHeightForWidth())
        self.ticket_month.setSizePolicy(sizePolicy1)
        self.ticket_month.setMaximumSize(QSize(16777215, 16777215))
        self.ticket_month.setStyleSheet(u"disabled")
        self.ticket_month.setMaxLength(2)

        self.horizontalLayout_6.addWidget(self.ticket_month)

        self.ticket_day = QLineEdit(Form)
        self.ticket_day.setObjectName(u"ticket_day")
        sizePolicy1.setHeightForWidth(self.ticket_day.sizePolicy().hasHeightForWidth())
        self.ticket_day.setSizePolicy(sizePolicy1)
        self.ticket_day.setMaximumSize(QSize(16777215, 16777215))
        self.ticket_day.setMaxLength(2)

        self.horizontalLayout_6.addWidget(self.ticket_day)

        self.ticket_time = QLineEdit(Form)
        self.ticket_time.setObjectName(u"ticket_time")
        sizePolicy1.setHeightForWidth(self.ticket_time.sizePolicy().hasHeightForWidth())
        self.ticket_time.setSizePolicy(sizePolicy1)
        self.ticket_time.setMaximumSize(QSize(16777215, 16777215))
        self.ticket_time.setMaxLength(2)

        self.horizontalLayout_6.addWidget(self.ticket_time)


        self.formLayout_3.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_6)


        self.verticalLayout_3.addLayout(self.formLayout_3)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ticket_btn = QPushButton(Form)
        self.ticket_btn.setObjectName(u"ticket_btn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.ticket_btn.sizePolicy().hasHeightForWidth())
        self.ticket_btn.setSizePolicy(sizePolicy4)
        font2 = QFont()
        font2.setFamilies([u"Apple SD Gothic Neo"])
        font2.setPointSize(30)
        font2.setBold(False)
        self.ticket_btn.setFont(font2)

        self.horizontalLayout.addWidget(self.ticket_btn)

        self.ticket_exit_btn = QPushButton(Form)
        self.ticket_exit_btn.setObjectName(u"ticket_exit_btn")
        self.ticket_exit_btn.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.ticket_exit_btn.sizePolicy().hasHeightForWidth())
        self.ticket_exit_btn.setSizePolicy(sizePolicy5)
        font3 = QFont()
        font3.setPointSize(30)
        self.ticket_exit_btn.setFont(font3)

        self.horizontalLayout.addWidget(self.ticket_exit_btn)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.horizontalLayout_7.addLayout(self.verticalLayout_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_5.addWidget(self.textBrowser)


        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"\uacc4\uc815 \uc815\ubcf4", None))
        self.cell_label.setText(QCoreApplication.translate("Form", u"\ud734\ub300\ud3f0 \ubc88\ud638", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Form", u"010", None))
        self.password_label.setText(QCoreApplication.translate("Form", u"\ube44\ubc00\ubc88\ud638", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\uce74\ub4dc \uc815\ubcf4", None))
        self.card_number_label.setText(QCoreApplication.translate("Form", u"\uce74\ub4dc\ubc88\ud638", None))
        self.card_valid_label.setText(QCoreApplication.translate("Form", u"\uc720\ud6a8\uae30\uac04", None))
        self.card_month.setPlaceholderText(QCoreApplication.translate("Form", u"Month", None))
        self.label.setText(QCoreApplication.translate("Form", u"/", None))
        self.card_year.setPlaceholderText(QCoreApplication.translate("Form", u"Year", None))
        self.card_password_label.setText(QCoreApplication.translate("Form", u"\ube44\ubc00\ubc88\ud638", None))
        self.card_person_number_label.setText(QCoreApplication.translate("Form", u"\uc0dd\ub144\uc6d4\uc77c", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"**", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"( \uc8fc\ubbfc\ubc88\ud638 \uc55e 6\uc790\ub9ac )", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\ud2f0\ucf13 \uc815\ubcf4", None))
        self.place_start_label.setText(QCoreApplication.translate("Form", u"\ucd9c\ubc1c\uc9c0", None))
        self.place_end_label.setText(QCoreApplication.translate("Form", u"\ub3c4\ucc29\uc9c0", None))
        self.place_ticket_label.setText(QCoreApplication.translate("Form", u"\uc608\uc57d\ub0a0\uc9dc", None))
        self.ticket_month.setText("")
        self.ticket_month.setPlaceholderText(QCoreApplication.translate("Form", u"Month", None))
        self.ticket_day.setPlaceholderText(QCoreApplication.translate("Form", u"Day", None))
        self.ticket_time.setPlaceholderText(QCoreApplication.translate("Form", u"Min Time", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"( \uc608\uc57d \ub0a0\uc9dc \ub0b4\uc6a9\uc740 2\uc790\ub9ac\ub85c \ud45c\uae30 ex) 1 -> 01 )", None))
        self.ticket_btn.setText(QCoreApplication.translate("Form", u"\ud2f0\ucf13\ud305 \uc2dc\uc791", None))
        self.ticket_exit_btn.setText(QCoreApplication.translate("Form", u"\uc885\ub8cc", None))
    # retranslateUi

