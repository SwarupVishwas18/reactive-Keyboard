import sys
from PyQt6 import QtWidgets, uic

from .front import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, data, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self, data)
        self.retranslateUi(self, data)
