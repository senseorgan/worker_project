# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'schedule_list_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

from ui import icons

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(372, 276)
        self.label_edl_2 = QLabel(Form)
        self.label_edl_2.setObjectName(u"label_edl_2")
        self.label_edl_2.setGeometry(QRect(20, 20, 146, 16))
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 40, 321, 211))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit_schedule_name_input = QLineEdit(self.layoutWidget)
        self.textEdit_schedule_name_input.setObjectName(u"textEdit_schedule_name_input")
        font = QFont()
        font.setFamily(u"Nanum Gothic")
        font.setPointSize(11)
        self.textEdit_schedule_name_input.setFont(font)

        self.verticalLayout.addWidget(self.textEdit_schedule_name_input)

        self.listWidget_schedule = QListWidget(self.layoutWidget)
        self.listWidget_schedule.setObjectName(u"listWidget_schedule")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_schedule.sizePolicy().hasHeightForWidth())
        self.listWidget_schedule.setSizePolicy(sizePolicy)
        self.listWidget_schedule.setMaximumSize(QSize(16777215, 500))
        font1 = QFont()
        font1.setFamily(u"Nanum Gothic")
        font1.setPointSize(10)
        self.listWidget_schedule.setFont(font1)

        self.verticalLayout.addWidget(self.listWidget_schedule)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_schedule_plus = QPushButton(self.layoutWidget)
        self.pushButton_schedule_plus.setObjectName(u"pushButton_schedule_plus")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_schedule_plus.sizePolicy().hasHeightForWidth())
        self.pushButton_schedule_plus.setSizePolicy(sizePolicy1)
        self.pushButton_schedule_plus.setMinimumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u":/icons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_schedule_plus.setIcon(icon)

        self.verticalLayout_2.addWidget(self.pushButton_schedule_plus)

        self.pushButton_schedule_minus = QPushButton(self.layoutWidget)
        self.pushButton_schedule_minus.setObjectName(u"pushButton_schedule_minus")
        sizePolicy1.setHeightForWidth(self.pushButton_schedule_minus.sizePolicy().hasHeightForWidth())
        self.pushButton_schedule_minus.setSizePolicy(sizePolicy1)
        self.pushButton_schedule_minus.setMinimumSize(QSize(30, 30))
        icon1 = QIcon()
        icon1.addFile(u":/icons/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_schedule_minus.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.pushButton_schedule_minus)

        self.verticalSpacer = QSpacerItem(13, 188, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.dateEdit_shedule_in_date = QDateEdit(self.layoutWidget)
        self.dateEdit_shedule_in_date.setObjectName(u"dateEdit_shedule_in_date")

        self.gridLayout.addWidget(self.dateEdit_shedule_in_date, 0, 1, 1, 2)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.dateEdit_shedule_out_date = QDateEdit(self.layoutWidget)
        self.dateEdit_shedule_out_date.setObjectName(u"dateEdit_shedule_out_date")

        self.gridLayout.addWidget(self.dateEdit_shedule_out_date, 1, 1, 1, 2)

        self.textEdit_schedule_path = QLineEdit(self.layoutWidget)
        self.textEdit_schedule_path.setObjectName(u"textEdit_schedule_path")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textEdit_schedule_path.sizePolicy().hasHeightForWidth())
        self.textEdit_schedule_path.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.textEdit_schedule_path, 2, 0, 1, 2)

        self.toolButton__schedule_end_path = QToolButton(self.layoutWidget)
        self.toolButton__schedule_end_path.setObjectName(u"toolButton__schedule_end_path")

        self.gridLayout.addWidget(self.toolButton__schedule_end_path, 2, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 0, 1, 1)

        self.pushButton_schedule_generate = QPushButton(self.layoutWidget)
        self.pushButton_schedule_generate.setObjectName(u"pushButton_schedule_generate")

        self.gridLayout.addWidget(self.pushButton_schedule_generate, 3, 1, 1, 2)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_edl_2.setText(QCoreApplication.translate("Form", u"\uc5f0\uac04 \ud504\ub85c\uc81d\ud2b8 \uc2a4\ucf00\uc904 \ub9ac\uc2a4\ud2b8", None))
        self.textEdit_schedule_name_input.setText(QCoreApplication.translate("Form", u"\ud504\ub85c\uc81d\ud2b8 \uc774\ub984", None))
        self.pushButton_schedule_plus.setText("")
        self.pushButton_schedule_minus.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"start_date", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"end_date", None))
        self.toolButton__schedule_end_path.setText(QCoreApplication.translate("Form", u"End_path", None))
        self.pushButton_schedule_generate.setText(QCoreApplication.translate("Form", u"generate", None))
    # retranslateUi

