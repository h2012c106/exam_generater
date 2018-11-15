# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Read_Conf(object):
    def setupUi(self, Read_Conf):
        Read_Conf.setObjectName("Read_Conf")
        Read_Conf.resize(500, 200)
        self.get_path = QtWidgets.QPushButton(Read_Conf)
        self.get_path.setGeometry(QtCore.QRect(20, 20, 100, 50))
        self.get_path.setObjectName("get_path")
        self.dir_name = QtWidgets.QPlainTextEdit(Read_Conf)
        self.dir_name.setGeometry(QtCore.QRect(140, 20, 120, 50))
        self.dir_name.setPlaceholderText('请输入试卷名')
        self.dir_name.setObjectName("dir_name")
        self.confirm = QtWidgets.QPushButton(Read_Conf)
        self.confirm.setGeometry(QtCore.QRect(280, 20, 85, 50))
        self.confirm.setObjectName("confirm")
        self.label = QtWidgets.QLabel(Read_Conf)
        self.label.setGeometry(QtCore.QRect(30, 80, 440, 100))
        self.label.setWordWrap(True)
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Read_Conf)
        self.get_path.clicked.connect(Read_Conf.path)
        self.confirm.clicked.connect(Read_Conf.run)
        QtCore.QMetaObject.connectSlotsByName(Read_Conf)

    def retranslateUi(self, Read_One):
        _translate = QtCore.QCoreApplication.translate
        Read_One.setWindowTitle(_translate("Read_One", "Form"))
        self.get_path.setText(_translate("Read_One", "读取配置"))
        self.confirm.setText(_translate("Read_One", "确定"))
