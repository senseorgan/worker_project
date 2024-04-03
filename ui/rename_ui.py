# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rename_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(561, 487)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit__file_path = QLineEdit(Form)
        self.lineEdit__file_path.setObjectName("lineEdit__file_path")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit__file_path.sizePolicy().hasHeightForWidth())
        self.lineEdit__file_path.setSizePolicy(sizePolicy)
        self.lineEdit__file_path.setMinimumSize(QSize(0, 20))

        self.horizontalLayout.addWidget(self.lineEdit__file_path)

        self.toolButton__file = QPushButton(Form)
        self.toolButton__file.setObjectName("toolButton__file")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toolButton__file.sizePolicy().hasHeightForWidth())
        self.toolButton__file.setSizePolicy(sizePolicy1)
        self.toolButton__file.setMinimumSize(QSize(0, 20))

        self.horizontalLayout.addWidget(self.toolButton__file)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit__excel_path = QLineEdit(Form)
        self.lineEdit__excel_path.setObjectName("lineEdit__excel_path")
        sizePolicy.setHeightForWidth(self.lineEdit__excel_path.sizePolicy().hasHeightForWidth())
        self.lineEdit__excel_path.setSizePolicy(sizePolicy)
        self.lineEdit__excel_path.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_2.addWidget(self.lineEdit__excel_path)

        self.toolButton__excel = QPushButton(Form)
        self.toolButton__excel.setObjectName("toolButton__excel")
        sizePolicy1.setHeightForWidth(self.toolButton__excel.sizePolicy().hasHeightForWidth())
        self.toolButton__excel.setSizePolicy(sizePolicy1)
        self.toolButton__excel.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_2.addWidget(self.toolButton__excel)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(30, 40, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.pushButton__start_stop = QPushButton(Form)
        self.pushButton__start_stop.setObjectName("pushButton__start_stop")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton__start_stop.sizePolicy().hasHeightForWidth())
        self.pushButton__start_stop.setSizePolicy(sizePolicy2)
        self.pushButton__start_stop.setMinimumSize(QSize(30, 40))

        self.horizontalLayout_3.addWidget(self.pushButton__start_stop)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.progressBar_inpro = QProgressBar(Form)
        self.progressBar_inpro.setObjectName("progressBar_inpro")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.progressBar_inpro.sizePolicy().hasHeightForWidth())
        self.progressBar_inpro.setSizePolicy(sizePolicy3)
        self.progressBar_inpro.setValue(0)

        self.verticalLayout_2.addWidget(self.progressBar_inpro)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.textBrowser_org = QTextBrowser(Form)
        self.textBrowser_org.setObjectName("textBrowser_org")

        self.horizontalLayout_4.addWidget(self.textBrowser_org)

        self.textBrowser_after = QTextBrowser(Form)
        self.textBrowser_after.setObjectName("textBrowser_after")

        self.horizontalLayout_4.addWidget(self.textBrowser_after)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.toolButton__file.setText(QCoreApplication.translate("Form", "  file_path  ", None))
        self.toolButton__excel.setText(QCoreApplication.translate("Form", "excel_path", None))
        self.pushButton__start_stop.setText(QCoreApplication.translate("Form", "      start      ", None))

    # retranslateUi
