# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'water_mark.ui'
##
## Created by: Qt User Interface Compiler version 5.15.8
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Watermark(object):
    def setupUi(self, Watermark):
        if not Watermark.objectName():
            Watermark.setObjectName("Watermark")
        Watermark.resize(370, 268)
        self.label_thum = QLabel(Watermark)
        self.label_thum.setObjectName("label_thum")
        self.label_thum.setGeometry(QRect(30, 30, 141, 21))
        self.layoutWidget = QWidget(Watermark)
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 60, 311, 181))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.textEdit_mark_company = QTextEdit(self.layoutWidget)
        self.textEdit_mark_company.setObjectName("textEdit_mark_company")

        self.gridLayout.addWidget(self.textEdit_mark_company, 0, 0, 1, 1)

        self.dateEdit_watermark = QDateEdit(self.layoutWidget)
        self.dateEdit_watermark.setObjectName("dateEdit_watermark")

        self.gridLayout.addWidget(self.dateEdit_watermark, 0, 1, 1, 2)

        self.textEdit_mark_start_path = QTextEdit(self.layoutWidget)
        self.textEdit_mark_start_path.setObjectName("textEdit_mark_start_path")

        self.gridLayout.addWidget(self.textEdit_mark_start_path, 1, 0, 1, 2)

        self.toolButton__start_path = QToolButton(self.layoutWidget)
        self.toolButton__start_path.setObjectName("toolButton__start_path")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton__start_path.sizePolicy().hasHeightForWidth())
        self.toolButton__start_path.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.toolButton__start_path, 1, 2, 1, 1)

        self.textEdit_mark_end_path = QTextEdit(self.layoutWidget)
        self.textEdit_mark_end_path.setObjectName("textEdit_mark_end_path")

        self.gridLayout.addWidget(self.textEdit_mark_end_path, 2, 0, 1, 2)

        self.toolButton__mark_end = QToolButton(self.layoutWidget)
        self.toolButton__mark_end.setObjectName("toolButton__mark_end")
        sizePolicy.setHeightForWidth(self.toolButton__mark_end.sizePolicy().hasHeightForWidth())
        self.toolButton__mark_end.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.toolButton__mark_end, 2, 2, 1, 1)

        self.splitter = QSplitter(self.layoutWidget)
        self.splitter.setObjectName("splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.progressBar_mark = QProgressBar(self.splitter)
        self.progressBar_mark.setObjectName("progressBar_mark")
        self.progressBar_mark.setValue(0)
        self.splitter.addWidget(self.progressBar_mark)
        self.pushButton_mark_start_stop = QPushButton(self.splitter)
        self.pushButton_mark_start_stop.setObjectName("pushButton_mark_start_stop")
        self.splitter.addWidget(self.pushButton_mark_start_stop)

        self.gridLayout.addWidget(self.splitter, 3, 0, 1, 3)

        self.retranslateUi(Watermark)

        QMetaObject.connectSlotsByName(Watermark)

    # setupUi

    def retranslateUi(self, Watermark):
        Watermark.setWindowTitle(QCoreApplication.translate("Watermark", "Form", None))
        self.label_thum.setText(
            QCoreApplication.translate("Watermark", "\uc6cc\ud130\ub9c8\ud06c  mov \ucd9c\ub825", None)
        )
        self.textEdit_mark_company.setHtml(
            QCoreApplication.translate(
                "Watermark",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:11pt; color:#818181;">\ud68c\uc0ac\uc774\ub984\uc744 \uc785\ub825\ud558\uc138\uc694.</span></p></body></html>',
                None,
            )
        )
        self.toolButton__start_path.setText(QCoreApplication.translate("Watermark", "start_path", None))
        self.toolButton__mark_end.setText(QCoreApplication.translate("Watermark", " End_path", None))
        self.pushButton_mark_start_stop.setText(QCoreApplication.translate("Watermark", "Start", None))

    # retranslateUi
