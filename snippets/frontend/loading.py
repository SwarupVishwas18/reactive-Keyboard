from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

app = QApplication([])

win=uic.loadUi("front-end.ui")
win.show()
app.exec()

# pyuic6 front-end.ui -o front-end.py