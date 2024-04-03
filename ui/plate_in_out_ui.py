# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plate_in_out.ui'
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
        Form.resize(561, 449)
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName("label_3")
        font = QFont()
        font.setPointSize(36)
        self.label_3.setFont(font)

        self.verticalLayout_3.addWidget(self.label_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_2 = QSplitter(Form)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.label = QLabel(self.splitter_2)
        self.label.setObjectName("label")
        self.splitter_2.addWidget(self.label)
        self.label_2 = QLabel(self.splitter_2)
        self.label_2.setObjectName("label_2")
        self.splitter_2.addWidget(self.label_2)

        self.gridLayout.addWidget(self.splitter_2, 0, 0, 2, 1)

        self.lineEdit__startPath = QLineEdit(Form)
        self.lineEdit__startPath.setObjectName("lineEdit__startPath")

        self.gridLayout.addWidget(self.lineEdit__startPath, 0, 1, 1, 1)

        self.toolButton__startPath = QToolButton(Form)
        self.toolButton__startPath.setObjectName("toolButton__startPath")

        self.gridLayout.addWidget(self.toolButton__startPath, 0, 2, 1, 1)

        self.pushButton__start_pause = QPushButton(Form)
        self.pushButton__start_pause.setObjectName("pushButton__start_pause")

        self.gridLayout.addWidget(self.pushButton__start_pause, 0, 3, 1, 1)

        self.toolButton__endPath = QToolButton(Form)
        self.toolButton__endPath.setObjectName("toolButton__endPath")

        self.gridLayout.addWidget(self.toolButton__endPath, 1, 2, 1, 1)

        self.pushButton__stop = QPushButton(Form)
        self.pushButton__stop.setObjectName("pushButton__stop")

        self.gridLayout.addWidget(self.pushButton__stop, 1, 3, 1, 1)

        self.lineEdit__endPath = QLineEdit(Form)
        self.lineEdit__endPath.setObjectName("lineEdit__endPath")

        self.gridLayout.addWidget(self.lineEdit__endPath, 1, 1, 1, 1)

        self.verticalLayout_3.addLayout(self.gridLayout)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox__udthree = QCheckBox(Form)
        self.checkBox__udthree.setObjectName("checkBox__udthree")

        self.verticalLayout.addWidget(self.checkBox__udthree)

        self.checkBox__udtwo = QCheckBox(Form)
        self.checkBox__udtwo.setObjectName("checkBox__udtwo")

        self.verticalLayout.addWidget(self.checkBox__udtwo)

        self.checkBox__udtwo_v02 = QCheckBox(Form)
        self.checkBox__udtwo_v02.setObjectName("checkBox__udtwo_v02")

        self.verticalLayout.addWidget(self.checkBox__udtwo_v02)

        self.checkBox__udone_v03 = QCheckBox(Form)
        self.checkBox__udone_v03.setObjectName("checkBox__udone_v03")

        self.verticalLayout.addWidget(self.checkBox__udone_v03)

        self.checkBox__udone_v02 = QCheckBox(Form)
        self.checkBox__udone_v02.setObjectName("checkBox__udone_v02")

        self.verticalLayout.addWidget(self.checkBox__udone_v02)

        self.checkBox__udone = QCheckBox(Form)
        self.checkBox__udone.setObjectName("checkBox__udone")

        self.verticalLayout.addWidget(self.checkBox__udone)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.progressBar__remaining = QProgressBar(Form)
        self.progressBar__remaining.setObjectName("progressBar__remaining")
        self.progressBar__remaining.setValue(24)

        self.verticalLayout_2.addWidget(self.progressBar__remaining)

        self.textBrowser__file = QTextBrowser(Form)
        self.textBrowser__file.setObjectName("textBrowser__file")

        self.verticalLayout_2.addWidget(self.textBrowser__file)

        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", "PLATE WORKER", None))
        self.label.setText(
            QCoreApplication.translate(
                "Form",
                '<html><head/><body><p align="center"><span style=" font-size:11pt;">Start_path</span></p></body></html>',
                None,
            )
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "Form",
                '<html><head/><body><p align="center"><span style=" font-size:11pt;">End_path</span></p></body></html>',
                None,
            )
        )
        self.toolButton__startPath.setText(QCoreApplication.translate("Form", "start", None))
        self.pushButton__start_pause.setText(QCoreApplication.translate("Form", "start", None))
        self.toolButton__endPath.setText(QCoreApplication.translate("Form", "end", None))
        self.pushButton__stop.setText(QCoreApplication.translate("Form", "stop", None))
        self.checkBox__udthree.setText(QCoreApplication.translate("Form", "ex) ABC_100_100_0010", None))
        self.checkBox__udtwo.setText(QCoreApplication.translate("Form", "ex) ABCDE_100_0010", None))
        self.checkBox__udtwo_v02.setText(QCoreApplication.translate("Form", "ex) ABCDE_100_0010[SH3]", None))
        self.checkBox__udone_v03.setText(QCoreApplication.translate("Form", "ex) ABCDE_010", None))
        self.checkBox__udone_v02.setText(QCoreApplication.translate("Form", "ex) ABCD_0010", None))
        self.checkBox__udone.setText(QCoreApplication.translate("Form", "ex) ABC_0010", None))
