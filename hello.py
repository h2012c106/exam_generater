# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hello.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(30, 20, 141, 31))
        self.label_1.setObjectName("label_1")
        self.read_one = QtWidgets.QPushButton(self.centralwidget)
        self.read_one.setGeometry(QtCore.QRect(40, 60, 151, 41))
        self.read_one.setObjectName("read_one")
        self.read_two = QtWidgets.QPushButton(self.centralwidget)
        self.read_two.setGeometry(QtCore.QRect(200, 60, 151, 41))
        self.read_two.setObjectName("read_two")
        self.read_diy = QtWidgets.QPushButton(self.centralwidget)
        self.read_diy.setGeometry(QtCore.QRect(360, 60, 151, 41))
        self.read_diy.setObjectName("read_diy")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 170, 141, 31))
        self.label_2.setObjectName("label_2")
        self.generate = QtWidgets.QPushButton(self.centralwidget)
        self.generate.setGeometry(QtCore.QRect(40, 210, 151, 41))
        self.generate.setObjectName("generate")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 320, 141, 31))
        self.label_3.setObjectName("label_3")
        self.detect = QtWidgets.QPushButton(self.centralwidget)
        self.detect.setGeometry(QtCore.QRect(40, 360, 151, 41))
        self.detect.setObjectName("detect")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_1.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">试卷录入</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">试卷生成</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">题目查重</span></p></body></html>"))
        self.read_one.setText(_translate("MainWindow", "试卷答案不分离"))
        self.read_two.setText(_translate("MainWindow", "试卷答案分离"))
        self.read_diy.setText(_translate("MainWindow", "手动录入"))
        self.generate.setText(_translate("MainWindow", "开始生成"))
        self.detect.setText(_translate("MainWindow", "开始检查"))

