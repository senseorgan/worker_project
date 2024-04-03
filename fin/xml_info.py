import os
import sys
import importlib
import time
import xml.etree.ElementTree as ET
import pandas as pd
from ui import xml_info_ui

from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QFileDialog
from libs.qt import qt_lib

importlib.reload(xml_info_ui)
importlib.reload(qt_lib)


class XMLToExcel(QtCore.QThread):
    def __init__(self, xml_file_path: str, save_path: str):
        super().__init__()
        self.textEdit_xml_path = xml_file_path
        self.textEdit_xmlsave_path = save_path
        self.text_content = []
        self.__is_stop = False

    def set_textEdit_xml_path(self, val):
        self.textEdit_xml_path = val

    def set_textEdit_xmlsave_path(self, val):
        self.textEdit_xmlsave_path = val

    @property
    def is_stop(self):
        return self.__is_stop

    @is_stop.setter
    def is_stop(self, flag: bool):
        self.__is_stop = flag

    def run(self):
        tree = ET.parse(self.textEdit_xml_path)  # 변경: 사용자가 선택한 XML 파일 경로 사용
        root = tree.getroot()

        titles = root.findall(".//title")
        for title in titles:
            text_tag = title.find("text")
            if text_tag is not None:
                full_text = "".join(
                    text_style.text for text_style in text_tag.findall(".//text-style") if text_style.text
                )
                part1 = full_text[:12]
                part2 = full_text[13:].strip()
                self.text_content.append([part1, part2])

        if self.text_content:  # 텍스트가 실제로 추출되었는지 확인
            df = pd.DataFrame(self.text_content, columns=["shot_name", "description"])
            excel_file_path = os.path.join(self.textEdit_xmlsave_path, "output.xlsx")
            df.to_excel(excel_file_path, index=False, engine="openpyxl")
            print(f"Text extracted from XML has been saved to '{excel_file_path}'")

        if self.__is_stop:
            while True:
                time.sleep(0.2)
                print(self.__is_stop)
                if not self.__is_stop:
                    break


class xmlinfo(QtWidgets.QWidget, xml_info_ui.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.__ui_thread = XMLToExcel("", "")
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.toolButton__xml_start.clicked.connect(self.slot_source_dir)
        self.toolButton__save.clicked.connect(self.slot_source_dir)
        self.pushButton_xml_start_stop.clicked.connect(self.toggle_start_stop)
        self.state = 0b01

    def toggle_start_stop(self):
        if self.state & 0b01:
            self.state = 0b10
            self.pushButton_xml_start_stop.setText("Start")  # 버튼 텍스트를 Start로 변경

        else:  # 현재 stop 상태인 경우
            self.state = 0b01  # start 상태로 변경
            self.pushButton_xml_start_stop.setText("Stop")  # 버튼 텍스트를 Stop으로 변경

        xml_path = self.textEdit_xml_path.toPlainText()
        xml_save_path = self.textEdit_xmlsave_path.toPlainText()

        self.__ui_thread.set_textEdit_xml_path(self.textEdit_xml_path.toPlainText())
        self.__ui_thread.set_textEdit_xmlsave_path(self.textEdit_xmlsave_path.toPlainText())
        self.__ui_thread = XMLToExcel(xml_path, xml_save_path)

        self.__ui_thread.start()

        self.__ui_thread.daemon = True

    def slot_source_dir(self):
        btn: QtWidgets.QToolButton = self.sender()
        options = QFileDialog.Options()

        # 'xml_path' 버튼을 눌렀을 경우 파일 선택 대화상자를 사용
        if btn.text() == "xml_path":
            file_path, _ = QFileDialog.getOpenFileName(self, "Select a file", "", "All Files (*)", options=options)
            if file_path:
                self.textEdit_xml_path.setText(file_path)
        else:
            # 다른 버튼을 눌렀을 경우 폴더 선택 대화상자를 사용
            folder_path = QFileDialog.getExistingDirectory(
                self, "Select a directory", "/Users/ijiyeong/Desktop/1_program/mov", options=options
            )
            if folder_path:
                self.textEdit_xmlsave_path.setText(folder_path)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    xml = xmlinfo()
    xml.show()
    sys.exit(app.exec())
