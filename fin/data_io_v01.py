import sys
import shutil
import os
import typing
import time
import logging
import pathlib
import importlib
import datetime
import xlsxwriter
import re


from PySide6 import QtWidgets, QtCore


from ui import Data_io_ui
from libs.system import sys_library as sys_lib
from libs.qt import library as qt_lib
from libs.qt import stylesheet

importlib.reload(Data_io_ui)
importlib.reload(sys_lib)
importlib.reload(qt_lib)
importlib.reload(stylesheet)


class MessageSig:
    message = ""
    is_err = False


class Signals(QtCore.QObject):
    progress_update = QtCore.Signal(int)
    message = QtCore.Signal(MessageSig)


class DT_UIThread(QtCore.QThread):
    def __init__(
        self,
        filedata,
        endPath,
        startPath,
        all_files,
        DTone,
        DTone_v02,
        DTone_v03,
        DTtwo,
        DTtwo_SH3,
        DTthree,
        part,
        status,
    ):
        super().__init__()
        self.signals = Signals()
        self.lineEdit__endPath = endPath
        self.lineEdit__startPath = startPath

        self.lineEdit__Part = part
        self.lineEdit__Status = status

        self.__is_stop = False
        self.__is_pause = False

        self.textBrowser__filedata = filedata
        self.all_files = all_files
        self.checkBox__DTone = DTone
        self.checkBox__DTone_v02 = DTone_v02
        self.checkBox__DTone_v03 = DTone_v03
        self.checkBox__DTtwo = DTtwo
        self.checkBox__DTtwo_SH3 = DTtwo_SH3
        self.checkBox__DTthree = DTthree

    def set_lineEdit__startPath(self, val):
        self.lineEdit__startPath = val

    def set_lineEdit__endpath(self, val):
        self.lineEdit__endPath = val

    def set_part(self, val):
        self.lineEdit__Part = val

    def set_status(self, val):
        self.lineEdit__Status = val

    def set_checkBox_DTone_status(self, val: bool):
        self.checkBox__DTone = val

    def set_checkBox_DTone_v02_status(self, val: bool):
        self.checkBox__DTone_v02 = val

    def set_checkBox_DTone_v03_status(self, val: bool):
        self.checkBox__DTone_v03 = val

    def set_checkBox_DTtwo_status(self, val: bool):
        self.checkBox__DTtwo = val

    def set_checkBox_DTtwo_SH3_status(self, val: bool):
        self.checkBox__DTtwo_SH3 = val

    def set_checkBox_DTthree_status(self, val: bool):
        self.checkBox__DTthree = val

    @property
    def is_stop(self):
        return self.__is_stop

    @is_stop.setter
    def is_stop(self, flag: bool):
        self.__is_stop = flag

    @property
    def is_pause(self):
        return self.__is_pause

    @is_pause.setter
    def is_pause(self, flag):
        self.__is_pause = flag

    def move_files(self, condition_func):
        current_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        excelFilePath = os.path.join(self.lineEdit__startPath.text(), "metadata.xlsx")
        workbook = xlsxwriter.Workbook(excelFilePath)
        worksheet = workbook.add_worksheet()
        worksheet.write("A1", "Filename")
        worksheet.write("B1", "Date")
        worksheet.write("C1", "Destination")

        if not os.path.exists(self.lineEdit__endPath.text()):
            os.makedirs(self.lineEdit__endPath.text())

        for i, f in enumerate(self.all_files):
            filename = os.path.basename(f)
            if filename == ".DS_Store":
                continue
            seq, seq_id = condition_func(filename)
            version_match = re.search(r"(v\d+)$", filename)
            if version_match:
                version = version_match.group()
            else:
                version = "v01"
            move_dir = os.path.join(
                self.lineEdit__endPath.text(),
                "sequences",
                seq,
                seq_id,
                self.lineEdit__Part.text(),
                self.lineEdit__Status.text(),
                version,
            )

            copy_path = os.path.join(move_dir, filename)
            os.makedirs(move_dir, exist_ok=True)
            ratio = int((i / len(self.all_files)) * 100)
            msg_sig = MessageSig()

            try:
                shutil.move(f, copy_path)
                worksheet.write(i + 1, 0, filename)
                worksheet.write(i + 1, 1, current_date_time)
                worksheet.write(i + 1, 2, copy_path)
                msg_sig.message = f"Successfully copied {f} to {copy_path}"
                msg_sig.is_err = False
            except shutil.SameFileError:
                msg_sig.message = f"{copy_path} 해당 파일이 존재합니다."
                msg_sig.is_err = True
            except Exception as e:
                msg_sig.message = f"Error copying {f} to {copy_path}: {e}"
                msg_sig.is_err = True
            finally:
                self.signals.message.emit(msg_sig)

            if self.__is_stop:
                break

            if self.__is_pause:
                while True:
                    time.sleep(0.5)

            self.signals.progress_update.emit(ratio)
            self.signals.progress_update.emit(100)
        if not self.__is_stop:
            msg_sig = MessageSig()
            msg_sig.message = "파일이 모두 옮겨졌습니다."
            msg_sig.is_err = False
            self.signals.message.emit(msg_sig)
        workbook.close()

    def run(self):
        if self.checkBox__DTone:
            self.move_files(lambda filename: (filename[:3], filename[:8]))
        elif self.checkBox__DTone_v02:
            self.move_files(lambda filename: (filename[:4], filename[:9]))
        elif self.checkBox__DTone_v03:
            self.move_files(lambda filename: (filename[:5], filename[:9]))
        elif self.checkBox__DTtwo:
            self.move_files(lambda filename: (filename[:9], filename[:14]))
        elif self.checkBox__DTtwo_SH3:
            self.move_files(lambda filename: (filename[6:9], filename[:14]))
        elif self.checkBox__DTthree:
            self.move_files(lambda filename: (filename[4:11], filename[:16]))


class FileMover(QtWidgets.QWidget, Data_io_ui.Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.__ui_thread = None

        # self.lineEdit__endPath  # 사용자가 UI에서 입력한 종료 경로
        # self.lineEdit__startPath

        self.__handler = qt_lib.LogHandler(out_stream=self.textBrowser__filedata)

        self.setAutoFillBackground(True)
        self.signals = Signals()
        self.progressBar__remaining.setValue(0)

        self.pushButton__start_pause.clicked.connect(self.toggle_start_pause)
        self.pushButton__stop.clicked.connect(self.slot_stop_file)
        self.toolButton__startPath.clicked.connect(self.slot_source_dir)
        self.toolButton__endPath.clicked.connect(self.slot_source_dir)

        self.state = 0b00

    @QtCore.Slot(MessageSig)
    def slot_print_message(self, msg: MessageSig):
        if msg.is_err:
            self.__handler.log_msg(logging.error, msg.message)
        else:
            self.__handler.log_msg(logging.info, msg.message)

    @QtCore.Slot(int)
    def slot_update_progress(self, val):
        self.progressBar__remaining.setValue(val)

    def get_all_files(self) -> typing.List[str]:
        dpath = self.lineEdit__startPath.text()
        return list(sys_lib.System.get_files_recursion(dpath, ["*"]))

    def is_exists_target_dir(self):
        return QtCore.QDir(self.lineEdit__endPath.text()).exists() and len(self.lineEdit__endPath.text())

    def toggle_start_pause(self):
        if not self.is_exists_target_dir():
            self.__handler.log_msg(logging.error, "파일 경로를 설정하라 휴먼!")
            return
        all_files = self.get_all_files()
        if not len(all_files):
            self.handler.log_msg(logging.error, "파일이 없지않나 휴먼!!")
            return

        if self.__ui_thread is None or not self.__ui_thread.isRunning():
            all_files = self.get_all_files()
            self.__ui_thread = DT_UIThread(
                self.textBrowser__filedata,
                self.lineEdit__endPath,
                self.lineEdit__startPath,
                all_files,
                self.checkBox__DTone,
                self.checkBox__DTone_v02,
                self.checkBox__DTone_v03,
                self.checkBox__DTtwo,
                self.checkBox__DTtwo_SH3,
                self.checkBox__DTthree,
                self.lineEdit__Status,
                self.lineEdit__Part,
            )
            self.__ui_thread.signals.progress_update.connect(self.slot_update_progress)
            self.__ui_thread.signals.message.connect(self.slot_print_message)
            self.__ui_thread.set_checkBox_DTone_status(self.checkBox__DTone.isChecked())
            self.__ui_thread.set_checkBox_DTone_v02_status(self.checkBox__DTone_v02.isChecked())
            self.__ui_thread.set_checkBox_DTone_v03_status(self.checkBox__DTone_v03.isChecked())
            self.__ui_thread.set_checkBox_DTtwo_status(self.checkBox__DTtwo.isChecked())
            self.__ui_thread.set_checkBox_DTtwo_SH3_status(self.checkBox__DTtwo_SH3.isChecked())
            self.__ui_thread.set_checkBox_DTthree_status(self.checkBox__DTthree.isChecked())

            if not all_files:
                self.__handler.log_msg(logging.error, "파일이 없지않나 휴먼! .")
                return

        if self.state & 0b01:  # 현재 pause 상태
            self.state = 0b10  # pause 상태로 전환
            self.pushButton__start_pause.setText("Start")
            self.__ui_thread.is_pause = True
        else:  # 현재 start 상태
            self.state = 0b01  # start 상태로 전환
            self.pushButton__start_pause.setText("Pause")
            if not self.__ui_thread.isRunning():
                self.__ui_thread.start()
            else:
                self.__ui_thread.is_pause = False

            self.__ui_thread.start()
            self.__ui_thread.daemon = True  # 이 작업은 메인 프로그램 종료시 자동 종료

    def slot_stop_file(self):
        self.pushButton__stop.setEnabled(False)
        self.pushButton__start_pause.setEnabled(True)

        self.__ui_thread.is_start = False
        self.__ui_thread.is_stop = True

    def slot_source_dir(self):
        btn: QtWidgets.QToolButton = self.sender()
        sel_dir: pathlib.Path = qt_lib.QtLibs.dir_dialog("/home/rapa")

        if sel_dir is not None:
            if btn.text() == "start":
                self.lineEdit__startPath.setText(sel_dir.as_posix())
            else:
                self.lineEdit__endPath.setText(sel_dir.as_posix())

    # 사용 예시


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    FLM = FileMover()
    FLM.show()
    sys.exit(app.exec_())
