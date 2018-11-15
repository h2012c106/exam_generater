# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Read_Two(object):
    def setupUi(self, Read_Two):
        Read_Two.setObjectName("Read_Two")
        Read_Two.resize(620, 200)
        self.get_path_1 = QtWidgets.QPushButton(Read_Two)
        self.get_path_1.setGeometry(QtCore.QRect(20, 20, 100, 50))
        self.get_path_1.setObjectName("get_path_1")
        self.get_path_2 = QtWidgets.QPushButton(Read_Two)
        self.get_path_2.setGeometry(QtCore.QRect(140, 20, 100, 50))
        self.get_path_2.setObjectName("get_path_2")
        self.dir_name = QtWidgets.QPlainTextEdit(Read_Two)
        self.dir_name.setGeometry(QtCore.QRect(260, 20, 120, 50))
        self.dir_name.setPlaceholderText('请输入试卷名')
        self.dir_name.setObjectName("dir_name")
        self.confirm = QtWidgets.QPushButton(Read_Two)
        self.confirm.setGeometry(QtCore.QRect(400, 20, 85, 50))
        self.confirm.setObjectName("confirm")
        self.label_1 = QtWidgets.QLabel(Read_Two)
        self.label_1.setGeometry(QtCore.QRect(30, 80, 560, 40))
        self.label_1.setWordWrap(True)
        self.label_1.setText("")
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(Read_Two)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 560, 40))
        self.label_2.setWordWrap(True)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Read_Two)
        self.get_path_1.clicked.connect(Read_Two.path_1)
        self.get_path_2.clicked.connect(Read_Two.path_2)
        self.confirm.clicked.connect(Read_Two.run)
        QtCore.QMetaObject.connectSlotsByName(Read_Two)

    def retranslateUi(self, Read_Two):
        _translate = QtCore.QCoreApplication.translate
        Read_Two.setWindowTitle(_translate("Read_Two", "Form"))
        self.get_path_1.setText(_translate("Read_Two", "读取试卷"))
        self.get_path_2.setText(_translate("Read_Two", "读取答案"))
        self.confirm.setText(_translate("Read_Two", "确定"))
