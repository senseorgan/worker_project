#!/usr/bin/env python
# encoding=utf-8
import sys
import importlib


# author : jy
# created date: 2024.03.11
# modified data: 2024.03.11
# description

from fin import rename
from fin import watermark_mov
from fin import xml_info
from fin import excel_thumb
from fin import excel_timeline
from fin import plate_io_v04
from fin import data_io_v01
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QWidget, QGridLayout, QTabWidget, QApplication, QSizePolicy


importlib.reload(rename)
importlib.reload(watermark_mov)
importlib.reload(xml_info)
importlib.reload(excel_thumb)
importlib.reload(excel_timeline)
importlib.reload(plate_io_v04)
importlib.reload(data_io_v01)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(800, 600)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # 탭 위젯을 생성하고 설정합니다.
        self.tabWidget = QTabWidget(self)

        # 탭에 추가할 위젯들을 생성합니다.
        self.tab1Content = QWidget()
        self.tab2Content = QWidget()
        self.tab3Content = QWidget()
        self.tab4Content = QWidget()

        # 탭 위젯에 탭을 추가합니다.
        self.tabWidget.addTab(self.tab1Content, "Rename_Worker")
        self.tabWidget.addTab(self.tab2Content, "Plate_Woker")
        self.tabWidget.addTab(self.tab3Content, "Data_Woker")
        self.tabWidget.addTab(self.tab4Content, "Mini_Worker")

        # 각 탭에 대한 내용을 구성합니다.
        self._configureTab1()
        self._configureTab2()
        self._configureTab3()
        self._configureTab4()

        # 탭 위젯을 중앙 위젯으로 설정합니다.
        self.setCentralWidget(self.tabWidget)

    def _configureTab1(self):
        layout = QGridLayout()
        self._renamer = rename.renameUI()
        layout.addWidget(self._renamer)
        self._renamer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.tab1Content.setLayout(layout)

    def _configureTab2(self):
        layout = QtWidgets.QVBoxLayout()
        self._plateio = plate_io_v04.PLATEMover()
        layout.addWidget(self._plateio)
        self.tab2Content.setLayout(layout)

    def _configureTab3(self):
        layout = QtWidgets.QVBoxLayout()
        self._dataio = data_io_v01.FileMover()
        layout.addWidget(self._dataio)
        self.tab3Content.setLayout(layout)

    def _configureTab4(self):
        layout = QGridLayout()
        self._excel = excel_thumb.CustomExcel()
        self._water = watermark_mov.WatermarkMOV()
        self._timeline = excel_timeline.ExcelSchedule()
        self._xmlinfo = xml_info.xmlinfo()
        layout.addWidget(self._excel, 0, 0)
        layout.addWidget(self._water, 0, 1)
        layout.addWidget(self._xmlinfo, 2, 0)
        layout.addWidget(self._timeline, 2, 1, 2, 2)
        self._excel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self._water.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self._timeline.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self._xmlinfo.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.tab4Content.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(
        """

            QWidget {
            background-color:#f4eeee;
            color: #333;
        }
            QPushButton {
            background-color:  #cdbcdc;
            border: 1px solid #fef9f5;
            color: white;
            padding: 10px 20px;
            text-align: center;
            font-size: 10px;
            border-radius: 10px;

        }

        QPushButton:hover {
            background-color: #9ab2d4;
            color: #F8BBD0;
        }
        
        QWidget {
        background-color:#f4eeee;
        color: #333;
    }
    QPushButton {
        background-color: #cdbcdc;
        border: 1px solid #fef9f5;
        color: white;
        padding: 10px 20px;
        text-align: center;
        font-size: 10px;
        border-radius: 10px;
    }
    QPushButton:hover {
        background-color: #5f5e66;
        color:  #ede7e7;
    }
    QLineEdit {
        border: 2px solid #bdbdbd;
        border-radius: 5px;
        padding: 0 8px;
        background: #ffffff;
        color: #333333;
    }
    QLineEdit:focus {
        border: 2px solid #9ab2d4;
    }
    
    QTextEdit {
        border: 2px solid #bdbdbd;
        border-radius: 5px;
        padding: 8px;
        background: #ffffff;
        color: #333333;
    }
    QTextEdit:focus {
        border: 2px solid #9ab2d4;
    }
    
    QToolButton {
    background-color: #f4eeee; /* 배경색 */
    border: 1px solid #bdbdbd; /* 테두리 */
    border-radius: 4px; /* 모서리 둥글게 */
    padding: 5px; /* 내부 여백 */
    color: #333333; /* 글자 색상 */
    }

    QToolButton:hover {
        background-color: #9ab2d4; /* 호버 상태의 배경색 */
        color: #F8BBD0; /* 호버 상태의 글자 색상 */
    }

    QToolButton:pressed {
        background-color: #cdbcdc; /* 눌렸을 때의 배경색 */
        border: 1px solid #9ab2d4; /* 눌렸을 때의 테두리 색상 */
    }
            """
    )
    m = MainWindow()
    m.show()
    sys.exit(app.exec())
