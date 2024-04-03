#!/usr/bin/env python
# encoding=utf-8

# author        : seongcheol jeon
# created date  : 2024.03.02
# modified date : 2024.03.02
# description   :

import pathlib

from PySide6 import QtWidgets, QtCore

from libs.qt import qt_lib


# count work threads
# timer value
# command items


class Preference(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()

        self.ini_file_path = pathlib.Path.home() / "multiple_timer.ini"
        self.cfg_file_path = pathlib.Path.home() / "multiple_timer.cfg"

        #
        dbl_lbl_work_threads = QtWidgets.QLabel("Work Threads:")
        self.dbl_spinbox_work_threads = QtWidgets.QSpinBox()
        hbox_work_threads = QtWidgets.QHBoxLayout()
        hbox_work_threads.addWidget(dbl_lbl_work_threads)
        hbox_work_threads.addWidget(self.dbl_spinbox_work_threads)

        #
        self.time_edit = QtWidgets.QTimeEdit()
        timer_val_lbl = QtWidgets.QLabel("Timer")
        hbox_timer = QtWidgets.QHBoxLayout()
        hbox_timer.addWidget(timer_val_lbl)
        hbox_timer.addWidget(self.time_edit)

        #
        btn_ok = QtWidgets.QPushButton("Ok")
        btn_cancel = QtWidgets.QPushButton("Cancel")
        btn_apply = QtWidgets.QPushButton("Apply")
        hbox_btns = QtWidgets.QHBoxLayout()
        btn_ok.clicked.connect(self.__slot_btn_ok)
        btn_cancel.clicked.connect(self.__slot_btn_cancel)
        btn_apply.clicked.connect(self.__slot_btn_apply)
        hbox_btns.addWidget(btn_ok)
        hbox_btns.addWidget(btn_apply)
        hbox_btns.addWidget(btn_cancel)

        #
        parent_vbox = QtWidgets.QVBoxLayout()
        parent_vbox.addLayout(hbox_work_threads)
        parent_vbox.addLayout(hbox_timer)
        parent_vbox.addLayout(hbox_btns)

        self.setLayout(parent_vbox)

        self.__ui_settings = qt_lib.UISettings(parent, self.ini_file_path, self.cfg_file_path)

        self.load_pref()

    def __slot_btn_ok(self):
        self.__slot_btn_apply()
        self.close()

    def __slot_btn_cancel(self):
        self.close()

    def __slot_btn_apply(self):
        work_threads = self.dbl_spinbox_work_threads.value()
        sec = Preference.qtime2sec(self.time_edit.time())

        data = {"work_threads": work_threads, "sec": sec}

        self.__ui_settings.save_main_window_geometry()
        self.__ui_settings.save_cfg_file(data)

    def load_pref(self):
        self.__ui_settings.load_main_window_geometry()
        cfg_data = self.__ui_settings.load_cfg_dict_from_file()
        if not len(list(cfg_data.keys())):
            return
        self.dbl_spinbox_work_threads.setValue(cfg_data.get("work_threads"))
        self.time_edit.setTime(Preference.sec2qtime(cfg_data.get("sec")))

    @staticmethod
    def qtime2sec(qtime) -> int:
        h, m, s = qtime.hour(), qtime.minute(), qtime.second()
        total_sec = h * 3600 + m * 60 + s
        return total_sec

    @staticmethod
    def sec2qtime(sec: int) -> QtCore.QTime:
        h, m = divmod(sec, 3600)
        m = m // 60
        s = sec % 60
        return QtCore.QTime(h, m, s)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    pref = Preference()
    pref.show()
    app.exec_()
