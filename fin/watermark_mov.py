import os
import sys
import time
import pathlib
import typing
import subprocess
import importlib
from ui import water_mark_ui
from PySide6 import QtWidgets, QtCore, QtGui
from libs.qt import qt_lib

from libs.system import sys_library as sys_lib

importlib.reload(water_mark_ui)
importlib.reload(qt_lib)
importlib.reload(sys_lib)


class MessageSig_M:
    message = ""
    is_err = False


class Signals(QtCore.QObject):
    progress_update = QtCore.Signal(int)
    message = QtCore.Signal(MessageSig_M)


class WaterMark(QtCore.QThread):
    def __init__(self, str_dir: str, tar_dir: str, watermark_date: str, company_name: str):
        super().__init__()
        self.signals = Signals()
        self.__mark_start = str_dir
        self.__mark_end = tar_dir
        self.__company_name = company_name
        self.__watermark_date = watermark_date
        self.__is_stop = False

    def set_mark_start_path(self, val):
        self.__mark_start = val

    def set_mark_end_path(self, val):
        self.__mark_end = val

    def set_company(self, val):
        self.__company_name = val

    def set_watermark(self, val):
        self.__watermark_date = val

    @property
    def is_stop_m(self):
        return self.__is_stop

    @is_stop_m.setter
    def is_stop_m(self, flag: bool):
        self.__is_stop = flag

    def run(self):
        self.add_watermark_run()

    def add_watermark_run(self):
        video_files = [file for file in os.listdir(self.__mark_start) if file.endswith((".mp4", ".avi", ".mov"))]

        for i, filename in enumerate(video_files, start=1):
            ratio = int((i / len(video_files)) * 100)
            dst_file = pathlib.Path(self.__mark_end) / pathlib.Path(filename).name
            msg_sig = MessageSig_M()

            try:
                if filename.endswith((".mp4", ".avi", ".mov")):
                    video_path = os.path.join(self.__mark_start, filename)
                    fontsize = 150
                    line_spacing = 90
                    fontcolor = "white@0.1"
                    t1 = f"drawtext=text='{self.__company_name}':x=(w-text_w)/2:y=(h-text_h)/2-{line_spacing}:fontsize={fontsize}:fontcolor={fontcolor}"
                    t2 = f"drawtext=text='{self.__watermark_date}':x=(w-text_w)/2:y=(h-text_h)/2+{line_spacing}:fontsize={fontsize}:fontcolor={fontcolor}"

                    # watermark_text = f"{self.__company_name}\\n{self.__watermark_date}" #이렇게 하는데 개행이 안됨 -_-

                    subprocess.run(
                        [
                            "ffmpeg",
                            "-i",
                            video_path,
                            "-vf",
                            f"{t2},{t1}",
                            "-codec:a",
                            "copy",
                            str(dst_file),
                        ]
                    )
            except FileExistsError as err:
                msg_sig.message = f"{dst_file.as_posix()}"
                msg_sig.is_err = True
                continue

            msg_sig.message = f"[{ratio}%] {filename} -> {dst_file.as_posix()}"
            msg_sig.is_err = False

            if self.__is_stop:
                while True:
                    time.sleep(0.2)
                    if not self.__is_stop:
                        break

            self.signals.progress_update.emit(ratio)
            self.signals.message.emit(msg_sig)


class WatermarkMOV(QtWidgets.QWidget, water_mark_ui.Ui_Watermark):
    def __init__(self):
        super(WatermarkMOV, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        self.textEdit_mark_company.toPlainText()
        self.textEdit_mark_start_path.toPlainText().strip()
        self.textEdit_mark_end_path.toPlainText().strip()
        self.dateEdit_watermark.date().toString("yyyy-MM-dd").strip()

        self.toolButton__start_path.setText("start_path")
        self.toolButton__mark_end.setText("end_path")
        self.textEdit_mark_start_path.toPlainText()
        self.textEdit_mark_end_path.toPlainText()
        self.toolButton__start_path.clicked.connect(self.slot_markSrc_dir)
        self.toolButton__mark_end.clicked.connect(self.slot_markSrc_dir)
        self.first_click = True
        self.textEdit_mark_company.toPlainText().strip()
        self.textEdit_mark_company.installEventFilter(self)

        self.pushButton_mark_start_stop.clicked.connect(self.mk_toggle_start_stop)
        self.__worker = WaterMark("[]", "", "", "")  # 작업 쓰레드 인스턴스 생성
        self.__worker.signals.progress_update.connect(self.mk_slot_update_progress)  # 신호 연결

        self.__mstate = 0b01

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.FocusIn and source is self.textEdit_mark_company:
            if self.first_click:  # 첫 클릭인 경우
                self.textEdit_mark_company.clear()  # 텍스트를 지웁니다.
                self.first_click = False
                return True
        return super().eventFilter(source, event)  # 부모클래스의 이벤트를 호출함

    @QtCore.Slot(int)
    def mk_slot_update_progress(self, val):
        self.progressBar_mark.setValue(val)

    def mk_get_all_files(self) -> typing.List[str]:
        dpath = self.textEdit_mark_start_path.toPlainText().strip()
        return list(sys_lib.System.get_files_recursion(dpath, ["*"]))

    def mk_is_exists_tartget_dir(self):
        return (
            QtCore.QDir(self.textEdit_mark_end_path.toPlainText()).exists()
            and len(self.textEdit_mark_end_path.toPlainText()) > 0
        )

    def mk_toggle_start_stop(self):
        if self.__mstate & 0b01:  # 시작 상태
            # 입력 필드에서 값을 가져옴
            str_dir = self.textEdit_mark_start_path.toPlainText().strip()
            tar_dir = self.textEdit_mark_end_path.toPlainText().strip()
            company_name = self.textEdit_mark_company.toPlainText().strip()
            watermark_date = self.dateEdit_watermark.date().toString("yyyy-MM-dd").strip()

            # Worker 쓰레드 설정
            self.__worker = WaterMark(str_dir, tar_dir, watermark_date, company_name)

            # 신호 연결
            self.__worker.signals.progress_update.connect(self.mk_slot_update_progress)
            self.__worker.signals.message.connect(lambda msg: print(msg.message))  # 예시 출력 처리

            self.__worker.start()  # 쓰레드 시작
            self.pushButton_mark_start_stop.setText("Stop")
            self.__mstate = 0b10  # 상태를 정지 상태로 변경
        else:
            self.__worker.is_stop_m = True  # 쓰레드 정지
            self.pushButton_mark_start_stop.setText("Start")
            self.__mstate = 0b01  # 상태를 시작 상태로 변경

    def slot_markSrc_dir(self):
        btn: QtWidgets.QToolButton = self.sender()
        sel_dir: pathlib.Path = qt_lib.QtLibs.dir_dialog("선택된 파일")

        if sel_dir is not None:
            if btn.text() == "start_path":
                self.textEdit_mark_start_path.setText(sel_dir.as_posix())
            else:
                self.textEdit_mark_end_path.setText(sel_dir.as_posix())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    font = QtGui.QFont("Arial", 10)
    app.setFont(font)

    mkr = WatermarkMOV()
    mkr.show()
    sys.exit(app.exec_())
