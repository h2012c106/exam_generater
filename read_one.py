# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'read_one.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Read_One(object):
    def setupUi(self, Read_One):
        Read_One.setObjectName("Read_One")
        Read_One.resize(500, 200)
        self.get_path = QtWidgets.QPushButton(Read_One)
        self.get_path.setGeometry(QtCore.QRect(20, 20, 100, 50))
        self.get_path.setObjectName("get_path")
        self.dir_name = QtWidgets.QPlainTextEdit(Read_One)
        self.dir_name.setGeometry(QtCore.QRect(140, 20, 120, 50))
        self.dir_name.setPlaceholderText('请输入试卷名')
        self.dir_name.setObjectName("dir_name")
        self.confirm = QtWidgets.QPushButton(Read_One)
        self.confirm.setGeometry(QtCore.QRect(280, 20, 85, 50))
        self.confirm.setObjectName("confirm")
        self.label = QtWidgets.QLabel(Read_One)
        self.label.setGeometry(QtCore.QRect(30, 80, 440, 100))
        self.label.setWordWrap(True)
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Read_One)
        self.get_path.clicked.connect(Read_One.path)
        self.confirm.clicked.connect(Read_One.run)
        QtCore.QMetaObject.connectSlotsByName(Read_One)

    def retranslateUi(self, Read_One):
        _translate = QtCore.QCoreApplication.translate
        Read_One.setWindowTitle(_translate("Read_One", "Form"))
        self.get_path.setText(_translate("Read_One", "读取文件"))
        self.confirm.setText(_translate("Read_One", "确定"))
