import sys
from PyQt6 import QtWidgets, uic
from frontend.main_window import MainWindow
from ex import get_data
import keyboard
from new import on_key_press


data = get_data("donut")

app = QtWidgets.QApplication(sys.argv)

window = MainWindow(data=data)
window.show()
app.exec()
