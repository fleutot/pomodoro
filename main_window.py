# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(415, 86)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.spinBox_focus_time_minutes = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_focus_time_minutes.setGeometry(QtCore.QRect(340, 10, 48, 26))
        self.spinBox_focus_time_minutes.setProperty("value", 25)
        self.spinBox_focus_time_minutes.setObjectName("spinBox_focus_time_minutes")
        self.spinBox_rest_time_minutes = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_rest_time_minutes.setGeometry(QtCore.QRect(340, 40, 48, 26))
        self.spinBox_rest_time_minutes.setProperty("value", 5)
        self.spinBox_rest_time_minutes.setObjectName("spinBox_rest_time_minutes")
        self.pushButton_focus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_focus.setGeometry(QtCore.QRect(250, 10, 82, 25))
        self.pushButton_focus.setObjectName("pushButton_focus")
        self.pushButton_rest = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_rest.setGeometry(QtCore.QRect(250, 40, 82, 25))
        self.pushButton_rest.setObjectName("pushButton_rest")
        self.pushButton_status = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_status.setGeometry(QtCore.QRect(10, 10, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.pushButton_status.setFont(font)
        self.pushButton_status.setObjectName("pushButton_status")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pomodoro"))
        self.pushButton_focus.setText(_translate("MainWindow", "Focus"))
        self.pushButton_rest.setText(_translate("MainWindow", "Rest"))
        self.pushButton_status.setText(_translate("MainWindow", "Inactive"))
