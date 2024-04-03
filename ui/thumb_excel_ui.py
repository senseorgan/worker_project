# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'thumb_excel.ui'
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
        Form.resize(346, 236)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 20, 281, 191))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit_thum_start = QTextEdit(self.layoutWidget)
        self.textEdit_thum_start.setObjectName("textEdit_thum_start")

        self.horizontalLayout.addWidget(self.textEdit_thum_start)

        self.toolButton__thum_start = QToolButton(self.layoutWidget)
        self.toolButton__thum_start.setObjectName("toolButton__thum_start")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton__thum_start.sizePolicy().hasHeightForWidth())
        self.toolButton__thum_start.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.toolButton__thum_start)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEdit_thum_end = QTextEdit(self.layoutWidget)
        self.textEdit_thum_end.setObjectName("textEdit_thum_end")

        self.horizontalLayout_2.addWidget(self.textEdit_thum_end)

        self.toolButton__thum_end = QToolButton(self.layoutWidget)
        self.toolButton__thum_end.setObjectName("toolButton__thum_end")
        sizePolicy.setHeightForWidth(self.toolButton__thum_end.sizePolicy().hasHeightForWidth())
        self.toolButton__thum_end.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.toolButton__thum_end)

        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 2)

        self.textBrowser__debug__thumb = QTextBrowser(self.layoutWidget)
        self.textBrowser__debug__thumb.setObjectName("textBrowser__debug__thumb")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textBrowser__debug__thumb.sizePolicy().hasHeightForWidth())
        self.textBrowser__debug__thumb.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.textBrowser__debug__thumb, 2, 0, 1, 1)

        self.pushButton_thum_start_stop = QPushButton(self.layoutWidget)
        self.pushButton_thum_start_stop.setObjectName("pushButton_thum_start_stop")
        sizePolicy1.setHeightForWidth(self.pushButton_thum_start_stop.sizePolicy().hasHeightForWidth())
        self.pushButton_thum_start_stop.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.pushButton_thum_start_stop, 2, 1, 1, 1)

        self.label_thum = QLabel(self.layoutWidget)
        self.label_thum.setObjectName("label_thum")

        self.gridLayout_2.addWidget(self.label_thum, 0, 0, 1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.toolButton__thum_start.setText(QCoreApplication.translate("Form", "start_path", None))
        self.toolButton__thum_end.setText(QCoreApplication.translate("Form", "End_path", None))
        self.pushButton_thum_start_stop.setText(QCoreApplication.translate("Form", "Start", None))
        self.label_thum.setText(QCoreApplication.translate("Form", "thumbnail \uc5d1\uc140 \uc0dd\uc131", None))

    # retranslateUi
