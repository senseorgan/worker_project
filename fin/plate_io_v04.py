import sys
import shutil
import re
import typing
import time
import logging
import pathlib
import datetime
import importlib
import OpenEXR
import xlsxwriter
import os


from PySide6 import QtWidgets, QtCore


from ui import plate_in_out_ui
from libs.system import sys_library as sys_lib
from libs.qt import library as qt_lib  # Qt 관련 라이브러리를 가져옵니다.
from libs.qt import stylesheet  # Qt 스타일시트를 가져옵니다.

importlib.reload(plate_in_out_ui)
importlib.reload(sys_lib)
importlib.reload(qt_lib)  #
importlib.reload(stylesheet)


class MessageSig:
    message = ""
    is_err = False


class Signals(QtCore.QObject):
    progress_update = QtCore.Signal(int)
    message = QtCore.Signal(MessageSig)


class UIThread(QtCore.QThread):
    def __init__(
        self,
        endPath,
        startPath,
        all_files,
        udone,
        udone_v02,
        udone_v03,
        udtwo,
        udthree,
        udtwo_v02,
    ):
        super().__init__()
        self.signals = Signals()
        self.lineEdit__endPath = endPath
        self.lineEdit__startPath = startPath
        self.__is_stop = False
        self.__is_pause = False

        self.all_files = all_files
        self.checkBox__udone = udone
        self.checkBox__udone_v02 = udone_v02
        self.checkBox__udone_v03 = udone_v03
        self.checkBox__udtwo = udtwo
        self.checkBox__udtwo_v02 = udtwo_v02
        self.checkBox__udthree = udthree

    def set_checkBox_udone_status(self, val: bool):
        self.checkBox__udone = val

    def set_checkBox_udone_v02_status(self, val: bool):
        self.checkBox__udone_v02 = val

    def set_checkBox_udone_v03_status(self, val: bool):
        self.checkBox__udone_v03 = val

    def set_checkBox_udtwo_status(self, val: bool):
        self.checkBox__udtwo = val

    def set_checkBox_udtwo_v02_status(self, val: bool):
        self.checkBox__udtwo_v02 = val

    def set_checkBox_udthree_status(self, val: bool):
        self.checkBox__udthree = val

    def set_lineEdit__startPath(self, val):
        self.lineEdit__startPath = val

    def set_lineEdit__endpath(self, val):
        self.lineEdit__endPath = val

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

    def extract_frame_number(self, filename):
        match = re.search(r"\d+", filename)
        return int(match.group()) if match else None

    def move_files(self, condition_func):  # 메타 데이터 추출 및 메타데이터 헤더로 등록해서 정보기록
        current_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        excelFilePath = os.path.join(self.lineEdit__startPath.text(), "metadata.xlsx")
        workbook = xlsxwriter.Workbook(excelFilePath)
        worksheet = workbook.add_worksheet()

        # 수정된 엑셀 헤더
        headers = [
            "Filename",
            "arriraw/reelName",
            "timeCode",
            "framesPerSecond",
            "arriraw/capDate",
            "arriraw/cameraIdentifier",
            "arriraw/cameraModel",
            "cameraSerialNumber",
            "arriraw/focalLength",
            "arriraw/lensModel",
            "arriraw/lensSerialNumber",
            "lensMake",
            "chromaticities",
            "compression",
            "dataWindow",
            "displayWindow",
            "focus",
            "start_path",
            "end_path",
            "date",
        ]

        for i, _header in enumerate(headers):
            worksheet.write(0, i, _header)

        row = 1
        # os.walk와 shutil을 사용해서 파일 이동
        for root, dirs, files in os.walk(self.lineEdit__startPath.text()):
            for file in files:
                if file.endswith(".exr"):
                    filePath = os.path.join(root, file)
                    exrFile = OpenEXR.InputFile(filePath)
                    exr_header = exrFile.header()

                    worksheet.write(row, 0, file)

                    for i, key in enumerate(headers[1:], start=1):
                        if key == "start_path":
                            worksheet.write(row, i, root)
                        else:
                            adjusted_key = (
                                key.replace("arriraw/", "").replace("interim.", "").replace("com.arri.camera.", "")
                            )
                            value = str(exr_header.get(adjusted_key, "N/A"))
                            worksheet.write(row, i, repr(value))

                    seq, seq_id, mid_name, folder_name = condition_func(file)
                    endPath = os.path.join(
                        self.lineEdit__endPath.text(), "sequences", seq, seq_id, "plate", mid_name, folder_name, file
                    )

                    worksheet.write(row, headers.index("end_path"), endPath)
                    worksheet.write(row, headers.index("date"), current_date_time)

                    row += 1

        workbook.close()

        if not os.path.exists(self.lineEdit__endPath.text()):
            os.makedirs(self.lineEdit__endPath.text())

        for i, f in enumerate(self.all_files):
            ratio = int((i / len(self.all_files)) * 100)
            self.signals.progress_update.emit(ratio)
            filename = os.path.basename(f)
            seq, seq_id, mid_name, folder_name = condition_func(filename)
            move_dir = os.path.join(
                self.lineEdit__endPath.text(), "sequences", seq, seq_id, "plate", mid_name, folder_name
            )
            copy_path = os.path.join(move_dir, filename)
            os.makedirs(move_dir, exist_ok=True)

            msg_sig = MessageSig()
            try:
                shutil.move(f, copy_path)
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
                    time.sleep(0.2)

        self.signals.progress_update.emit(100)
        if not self.__is_stop:
            msg_sig = MessageSig()
            msg_sig.message = "파일이 모두 옮겨졌습니다."
            msg_sig.is_err = False
            self.signals.message.emit(msg_sig)

    def run(self):
        if self.checkBox__udone:
            self.move_files(
                lambda filename: (
                    filename[:3],
                    filename[:8],
                    "_".join(filename.strip().split("_"))[9:12],
                    filename.rsplit(".", 2)[0],
                )
            )
        elif self.checkBox__udone_v02:
            self.move_files(
                lambda filename: (
                    filename[:4],
                    filename[:9],
                    "_".join(filename.strip().split("_"))[10:13],
                    filename.rsplit(".", 1)[0],
                )
            )
        elif self.checkBox__udone_v03:
            self.move_files(lambda filename: (filename[:5], filename[:9], "", filename.rsplit(".", 2)[0]))

        elif self.checkBox__udtwo:
            self.move_files(
                lambda filename: (
                    filename[:9],
                    filename[:14],
                    "_".join(filename.strip().split("_")[-2:])[:-9],
                    filename.rsplit(".", 2)[0],
                )
            )

        elif self.checkBox__udtwo_v02:
            self.move_files(
                lambda filename: (
                    filename[6:9],
                    filename[:14],
                    "_".join(filename.strip().split("_")[-2:])[:-9],
                    filename.rsplit(".", 2)[0],
                )
            )

        elif self.checkBox__udthree:
            self.move_files(
                lambda filename: (
                    filename[4:11],
                    filename[:16],
                    "_".join(filename.strip().split("_")[-2:])[:-9],
                    filename.rsplit(".", 2)[0],
                )
            )


class PLATEMover(QtWidgets.QWidget, plate_in_out_ui.Ui_Form):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.__ui_thread = None

        self.lineEdit__endPath  # 사용자가 UI에서 입력한 종료 경로
        self.lineEdit__startPath
        self.__handler = qt_lib.LogHandler(out_stream=self.textBrowser__file)

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
            self.__handler.log_msg(logging.error, "파일 경로를 설정해주세요.")
            return
        all_files = self.get_all_files()
        if not len(all_files):
            self.__handler.log_msg(logging.error, "이미 작업된 파일 입니다")
            return

        if self.__ui_thread is None or not self.__ui_thread.isRunning():
            self.pushButton__stop.setEnabled(True)
            self.__ui_thread = UIThread(
                self.lineEdit__endPath,
                self.lineEdit__startPath,
                all_files,
                self.checkBox__udone,
                self.checkBox__udone_v02,
                self.checkBox__udone_v03,
                self.checkBox__udtwo,
                self.checkBox__udthree,
                self.checkBox__udtwo_v02,
            )
            self.__ui_thread.signals.progress_update.connect(self.slot_update_progress)
            self.__ui_thread.signals.message.connect(self.slot_print_message)
            self.__ui_thread.set_checkBox_udone_status(self.checkBox__udone.isChecked())
            self.__ui_thread.set_checkBox_udone_v02_status(self.checkBox__udone_v02.isChecked())
            self.__ui_thread.set_checkBox_udone_v03_status(self.checkBox__udone_v03.isChecked())
            self.__ui_thread.set_checkBox_udtwo_status(self.checkBox__udtwo.isChecked())
            self.__ui_thread.set_checkBox_udthree_status(self.checkBox__udthree.isChecked())
            self.__ui_thread.set_checkBox_udtwo_v02_status(self.checkBox__udtwo_v02.isChecked())
            self.__ui_thread.finished.connect(self.slot_finished_work)

            if not all_files:
                self.__handler.log_msg(logging.error, "파일이 없습니다.")
                return
        else:
            self.pauseOrResumeWork()

        if self.state & 0b01:  # 현재 pause 상태
            self.state = 0b10  # pause 상태로 전환
            self.pushButton__start_pause.setText("Start")
            self.__ui_thread.is_pause = True
        else:  # 현재 start 상태
            self.state = 0b01  # start 상태로 전환
            self.pushButton__start_pause.setText("Pause")
            if not self.__ui_thread.isRunning():
                self.__ui_thread.start()
                self.__ui_thread.daemon = True  # 이 작업은 메인 프로그램 종료시 자동 종료
            else:
                self.__ui_thread.is_pause = False

    def slot_finished_work(self):
        self.state = 0b00
        self.pushButton__start_pause.setText("Start")

    def slot_stop_file(self):
        self.pushButton__stop.setEnabled(False)
        self.pushButton__start_pause.setEnabled(True)

        self.__ui_thread.is_start = False
        self.__ui_thread.is_stop = True

    def slot_finished_work(self):
        self.state = 0b00
        self.pushButton__start_pause.setText("Start")
        # UI 초기화 코드를 여기에 추가합니다.
        self.lineEdit__startPath.clear()
        self.lineEdit__endPath.clear()
        self.progressBar__remaining.setValue(0)
        self.checkBox__udone.setChecked(False)
        self.checkBox__udone_v02.setChecked(False)
        self.checkBox__udone_v03.setChecked(False)
        self.checkBox__udtwo.setChecked(False)
        self.checkBox__udtwo_v02.setChecked(False)
        self.checkBox__udthree.setChecked(False)

    def slot_source_dir(self):
        btn: QtWidgets.QToolButton = self.sender()
        sel_dir: pathlib.Path = qt_lib.QtLibs.dir_dialog("/home/rapa")

        if sel_dir is not None:
            if btn.objectName() == "toolButton__startPath":
                self.lineEdit__startPath.setText(sel_dir.as_posix())
            elif btn.objectName() == "toolButton__endPath":
                self.lineEdit__endPath.setText(sel_dir.as_posix())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    FLM = PLATEMover()
    FLM.show()
    sys.exit(app.exec())
