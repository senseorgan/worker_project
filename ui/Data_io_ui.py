# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Data_io.ui'
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
        Form.resize(561, 510)
        self.verticalLayout_6 = QVBoxLayout(Form)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName("label_3")
        font = QFont()
        font.setPointSize(48)
        self.label_3.setFont(font)

        self.verticalLayout_5.addWidget(self.label_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName("label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit__startPath = QLineEdit(Form)
        self.lineEdit__startPath.setObjectName("lineEdit__startPath")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit__startPath.sizePolicy().hasHeightForWidth())
        self.lineEdit__startPath.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.lineEdit__startPath)

        self.toolButton__startPath = QToolButton(Form)
        self.toolButton__startPath.setObjectName("toolButton__startPath")

        self.horizontalLayout.addWidget(self.toolButton__startPath)

        self.pushButton__start_pause = QPushButton(Form)
        self.pushButton__start_pause.setObjectName("pushButton__start_pause")

        self.horizontalLayout.addWidget(self.pushButton__start_pause)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName("label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit__endPath = QLineEdit(Form)
        self.lineEdit__endPath.setObjectName("lineEdit__endPath")
        sizePolicy.setHeightForWidth(self.lineEdit__endPath.sizePolicy().hasHeightForWidth())
        self.lineEdit__endPath.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.lineEdit__endPath)

        self.toolButton__endPath = QToolButton(Form)
        self.toolButton__endPath.setObjectName("toolButton__endPath")

        self.horizontalLayout_2.addWidget(self.toolButton__endPath)

        self.pushButton__stop = QPushButton(Form)
        self.pushButton__stop.setObjectName("pushButton__stop")

        self.horizontalLayout_2.addWidget(self.pushButton__stop)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName("label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.lineEdit__Part = QLineEdit(Form)
        self.lineEdit__Part.setObjectName("lineEdit__Part")
        sizePolicy.setHeightForWidth(self.lineEdit__Part.sizePolicy().hasHeightForWidth())
        self.lineEdit__Part.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.lineEdit__Part)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName("label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.lineEdit__Status = QLineEdit(Form)
        self.lineEdit__Status.setObjectName("lineEdit__Status")
        sizePolicy.setHeightForWidth(self.lineEdit__Status.sizePolicy().hasHeightForWidth())
        self.lineEdit__Status.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.lineEdit__Status)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox__DTthree = QCheckBox(Form)
        self.checkBox__DTthree.setObjectName("checkBox__DTthree")

        self.verticalLayout.addWidget(self.checkBox__DTthree)

        self.checkBox__DTtwo = QCheckBox(Form)
        self.checkBox__DTtwo.setObjectName("checkBox__DTtwo")

        self.verticalLayout.addWidget(self.checkBox__DTtwo)

        self.checkBox__DTtwo_SH3 = QCheckBox(Form)
        self.checkBox__DTtwo_SH3.setObjectName("checkBox__DTtwo_SH3")

        self.verticalLayout.addWidget(self.checkBox__DTtwo_SH3)

        self.checkBox__DTone_v03 = QCheckBox(Form)
        self.checkBox__DTone_v03.setObjectName("checkBox__DTone_v03")

        self.verticalLayout.addWidget(self.checkBox__DTone_v03)

        self.checkBox__DTone_v02 = QCheckBox(Form)
        self.checkBox__DTone_v02.setObjectName("checkBox__DTone_v02")

        self.verticalLayout.addWidget(self.checkBox__DTone_v02)

        self.checkBox__DTone = QCheckBox(Form)
        self.checkBox__DTone.setObjectName("checkBox__DTone")

        self.verticalLayout.addWidget(self.checkBox__DTone)

        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.progressBar__remaining = QProgressBar(Form)
        self.progressBar__remaining.setObjectName("progressBar__remaining")
        self.progressBar__remaining.setValue(24)

        self.verticalLayout_3.addWidget(self.progressBar__remaining)

        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.textBrowser__filedata = QTextBrowser(Form)
        self.textBrowser__filedata.setObjectName("textBrowser__filedata")

        self.verticalLayout_4.addWidget(self.textBrowser__filedata)

        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", "DATA WORKER", None))
        self.label.setText(
            QCoreApplication.translate(
                "Form",
                '<html><head/><body><p align="center"><span style=" font-size:11pt;">Start_path</span></p></body></html>',
                None,
            )
        )
        self.toolButton__startPath.setText(QCoreApplication.translate("Form", "start", None))
        self.pushButton__start_pause.setText(QCoreApplication.translate("Form", "start", None))
        self.label_2.setText(
            QCoreApplication.translate(
                "Form",
                '<html><head/><body><p align="center"><span style=" font-size:11pt;">End_path</span></p></body></html>',
                None,
            )
        )
        self.toolButton__endPath.setText(QCoreApplication.translate("Form", "end", None))
        self.pushButton__stop.setText(QCoreApplication.translate("Form", "stop", None))
        self.label_5.setText(
            QCoreApplication.translate(
                "Form",
                '<html><head/><body><p align="justify"><span style=" font-size:11pt;">  Part</span></p></body></html>',
                None,
            )
        )
        self.label_6.setText(
            QCoreApplication.translate(
                "Form", '<html><head/><body><p><span style=" font-size:11pt;">Status</span></p></body></html>', None
            )
        )
        self.checkBox__DTthree.setText(QCoreApplication.translate("Form", "ex) ABC_100_100_0010", None))
        self.checkBox__DTtwo.setText(QCoreApplication.translate("Form", "ex) ABCDE_100_0010", None))
        self.checkBox__DTtwo_SH3.setText(QCoreApplication.translate("Form", "ex) ABCDE_100_0010[SH3]", None))
        self.checkBox__DTone_v03.setText(QCoreApplication.translate("Form", "ex) ABCDE_010", None))
        self.checkBox__DTone_v02.setText(QCoreApplication.translate("Form", "ex) ABCD_0010", None))
        self.checkBox__DTone.setText(QCoreApplication.translate("Form", "ex) ABC_0010", None))

    # retranslateUi
