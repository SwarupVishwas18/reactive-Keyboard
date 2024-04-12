# Form implementation generated from reading ui file 'front-end.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(374, 668)
        MainWindow.setStyleSheet("background-color: #5d5d5d;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listView = QtWidgets.QListView(parent=self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(-5, 0, 381, 651))
        self.listView.setObjectName("listView")
        self.columnView = QtWidgets.QColumnView(parent=self.centralwidget)
        self.columnView.setGeometry(QtCore.QRect(20, 10, 331, 151))
        self.columnView.setStyleSheet("background-color: #000;\n"
"border-radius: 9px;")
        self.columnView.setObjectName("columnView")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 121, 131))
        self.label.setStyleSheet("border-radius: 33px;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Desktop/pexels-saveurs-secretes-5410400.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 20, 171, 51))
        self.label_2.setStyleSheet("font-size: 17px;\n"
"color: #fff;\n"
"background-color: #000;")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 30, 51, 21))
        self.label_3.setStyleSheet("font-size: 9px;\n"
"color: #fff;\n"
"background-color: #000;")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 50, 16, 16))
        self.label_4.setStyleSheet("background-color: #000;")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../Desktop/star-fill.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(180, 50, 16, 16))
        self.label_5.setStyleSheet("background-color: #000;")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../Desktop/star-fill.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(200, 50, 16, 16))
        self.label_6.setStyleSheet("background-color: #000;")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../Desktop/star-fill.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(220, 50, 16, 16))
        self.label_7.setStyleSheet("background-color: #000;")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../Desktop/star-fill.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(240, 50, 16, 16))
        self.label_8.setStyleSheet("background-color: #000;")
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("../Desktop/star-empty.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(160, 80, 16, 16))
        self.label_9.setStyleSheet("background-color: #000;")
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("../Desktop/map.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(180, 80, 141, 41))
        self.label_10.setStyleSheet("font-size: 13px;\n"
"color: #d9d9d9;\n"
"background-color: #000;")
        self.label_10.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(160, 130, 51, 21))
        self.label_11.setStyleSheet("font-size: 10px;\n"
"font-weight: 600;\n"
"color: #000;\n"
"background-color: #d9d9d9;")
        self.label_11.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(315, 130, 21, 20))
        self.label_12.setStyleSheet("background-color: #000;")
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("../Desktop/visit.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 374, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Sukhsagar Pavbhaji"))
        self.label_3.setText(_translate("MainWindow", "Open Now"))
        self.label_10.setText(_translate("MainWindow", "Chintamani Nagar, Pune 411037"))
        self.label_11.setText(_translate("MainWindow", "4 km"))
