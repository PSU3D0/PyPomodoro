# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AppWindow(object):
    def setupUi(self, AppWindow):
        AppWindow.setObjectName("AppWindow")
        AppWindow.resize(335, 250)
        self.startButton = QtWidgets.QPushButton(AppWindow)
        self.startButton.setGeometry(QtCore.QRect(230, 210, 89, 25))
        self.startButton.setObjectName("startButton")
        self.resetButton = QtWidgets.QPushButton(AppWindow)
        self.resetButton.setGeometry(QtCore.QRect(10, 210, 89, 25))
        self.resetButton.setObjectName("resetButton")
        self.pauseButton = QtWidgets.QPushButton(AppWindow)
        self.pauseButton.setGeometry(QtCore.QRect(120, 210, 89, 25))
        self.pauseButton.setObjectName("pauseButton")
        self.workTimer = QtWidgets.QLCDNumber(AppWindow)
        self.workTimer.setGeometry(QtCore.QRect(30, 120, 101, 61))
        self.workTimer.setStyleSheet("QLCDNumber{\n"
"    background: rgb(78, 154, 6);\n"
"}")
        self.workTimer.setObjectName("workTimer")
        self.restTimer = QtWidgets.QLCDNumber(AppWindow)
        self.restTimer.setGeometry(QtCore.QRect(200, 120, 101, 61))
        self.restTimer.setAutoFillBackground(False)
        self.restTimer.setStyleSheet("QLCDNumber {\n"
"    background: rgb(252, 233, 79);\n"
"}")
        self.restTimer.setSmallDecimalPoint(False)
        self.restTimer.setObjectName("restTimer")
        self.twentyfiveFivePreset = QtWidgets.QPushButton(AppWindow)
        self.twentyfiveFivePreset.setGeometry(QtCore.QRect(120, 40, 89, 25))
        self.twentyfiveFivePreset.setObjectName("twentyfiveFivePreset")
        self.fortyfiveFivePreset = QtWidgets.QPushButton(AppWindow)
        self.fortyfiveFivePreset.setGeometry(QtCore.QRect(230, 40, 89, 25))
        self.fortyfiveFivePreset.setObjectName("fortyfiveFivePreset")
        self.fifteenFivePreset = QtWidgets.QPushButton(AppWindow)
        self.fifteenFivePreset.setGeometry(QtCore.QRect(10, 40, 89, 25))
        self.fifteenFivePreset.setObjectName("fifteenFivePreset")
        self.workSlider = QtWidgets.QSlider(AppWindow)
        self.workSlider.setGeometry(QtCore.QRect(10, 100, 141, 16))
        self.workSlider.setMinimum(5)
        self.workSlider.setMaximum(120)
        self.workSlider.setProperty("value", 5)
        self.workSlider.setOrientation(QtCore.Qt.Horizontal)
        self.workSlider.setObjectName("workSlider")
        self.restSlider = QtWidgets.QSlider(AppWindow)
        self.restSlider.setGeometry(QtCore.QRect(180, 100, 141, 16))
        self.restSlider.setMinimum(5)
        self.restSlider.setMaximum(60)
        self.restSlider.setOrientation(QtCore.Qt.Horizontal)
        self.restSlider.setObjectName("restSlider")

        self.retranslateUi(AppWindow)
        QtCore.QMetaObject.connectSlotsByName(AppWindow)

    def retranslateUi(self, AppWindow):
        _translate = QtCore.QCoreApplication.translate
        AppWindow.setWindowTitle(_translate("AppWindow", "PyPomodoro"))
        self.startButton.setText(_translate("AppWindow", "Start"))
        self.resetButton.setText(_translate("AppWindow", "Reset"))
        self.pauseButton.setText(_translate("AppWindow", "Pause"))
        self.twentyfiveFivePreset.setText(_translate("AppWindow", "25:5"))
        self.fortyfiveFivePreset.setText(_translate("AppWindow", "45:10"))
        self.fifteenFivePreset.setText(_translate("AppWindow", "15:5"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AppWindow = QtWidgets.QDialog()
    ui = Ui_AppWindow()
    ui.setupUi(AppWindow)
    AppWindow.show()
    sys.exit(app.exec_())
