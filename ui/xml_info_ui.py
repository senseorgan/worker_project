# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'xml_info_ui.ui'
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
        Form.resize(366, 219)
        self.pushButton_xml_start_stop = QPushButton(Form)
        self.pushButton_xml_start_stop.setObjectName("pushButton_xml_start_stop")
        self.pushButton_xml_start_stop.setGeometry(QRect(260, 170, 72, 32))
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 29, 291, 131))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_edl = QLabel(self.layoutWidget)
        self.label_edl.setObjectName("label_edl")

        self.verticalLayout_2.addWidget(self.label_edl)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEdit_xml_path = QTextEdit(self.layoutWidget)
        self.textEdit_xml_path.setObjectName("textEdit_xml_path")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_xml_path.sizePolicy().hasHeightForWidth())
        self.textEdit_xml_path.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.textEdit_xml_path)

        self.toolButton__xml_start = QToolButton(self.layoutWidget)
        self.toolButton__xml_start.setObjectName("toolButton__xml_start")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toolButton__xml_start.sizePolicy().hasHeightForWidth())
        self.toolButton__xml_start.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.toolButton__xml_start)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit_xmlsave_path = QTextEdit(self.layoutWidget)
        self.textEdit_xmlsave_path.setObjectName("textEdit_xmlsave_path")
        sizePolicy.setHeightForWidth(self.textEdit_xmlsave_path.sizePolicy().hasHeightForWidth())
        self.textEdit_xmlsave_path.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.textEdit_xmlsave_path)

        self.toolButton__save = QToolButton(self.layoutWidget)
        self.toolButton__save.setObjectName("toolButton__save")
        sizePolicy1.setHeightForWidth(self.toolButton__save.sizePolicy().hasHeightForWidth())
        self.toolButton__save.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.toolButton__save)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.pushButton_xml_start_stop.setText(QCoreApplication.translate("Form", "Start", None))
        self.label_edl.setText(QCoreApplication.translate("Form", "xml \uc815\ubcf4 \ucd94\ucd9c", None))
        self.toolButton__xml_start.setText(QCoreApplication.translate("Form", "xml_path", None))
        self.toolButton__save.setText(QCoreApplication.translate("Form", "save_path", None))

    # retranslateUi
