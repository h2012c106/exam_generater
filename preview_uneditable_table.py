# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alt_word_table.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Out_Preview(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 800)

        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        # self.scrollArea.setMinimumHeight(2000)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1200, 2000))
        self.scrollAreaWidgetContents.setMinimumHeight(2000)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.sele_name = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.sele_name.setGeometry(QtCore.QRect(10, 10, 140, 30))
        self.sele_name.setText("语法-选择")
        self.sele_name.setStyleSheet('font-size:14pt')
        self.sele_name.setObjectName("label")
        self.sele_table = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.sele_table.setGeometry(QtCore.QRect(10, 45, 1160, 800))
        # self.sele_table.setMaximumSize(QtCore.QSize(256, 192))
        self.sele_table.setObjectName("sele_table")
        self.sele_table.verticalHeader().setVisible(False)
        self.sele_table.setColumnCount(11)
        self.sele_table.setWordWrap(True)

        item = QtWidgets.QTableWidgetItem()
        self.sele_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.sele_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.sele_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.sele_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.sele_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.sele_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.sele_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.sele_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.sele_table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.sele_table.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.sele_table.setHorizontalHeaderItem(10, item)

        self.fish_name = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.fish_name.setGeometry(QtCore.QRect(10, 860, 140, 30))
        self.fish_name.setText("语法-钓鱼")
        self.fish_name.setStyleSheet('font-size:14pt')
        self.fish_name.setObjectName("label")
        self.fish_table = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.fish_table.setGeometry(QtCore.QRect(10, 895, 1160, 275))
        # self.fish_table.setMaximumSize(QtCore.QSize(256, 192))
        self.fish_table.setObjectName("fish_table")
        self.fish_table.verticalHeader().setVisible(False)
        self.fish_table.setColumnCount(4)
        self.fish_table.setWordWrap(True)

        item = QtWidgets.QTableWidgetItem()
        self.fish_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.fish_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.fish_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.fish_table.setHorizontalHeaderItem(3, item)

        self.alt_word_name = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.alt_word_name.setGeometry(QtCore.QRect(10, 1185, 140, 30))
        self.alt_word_name.setText("语法-改词")
        self.alt_word_name.setStyleSheet('font-size:14pt')
        self.alt_word_name.setObjectName("label")
        self.alt_word_table = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.alt_word_table.setGeometry(QtCore.QRect(10, 1220, 1160, 285))
        # self.alt_word_table.setMaximumSize(QtCore.QSize(256, 192))
        self.alt_word_table.setObjectName("alt_word_table")
        self.alt_word_table.verticalHeader().setVisible(False)
        self.alt_word_table.setColumnCount(7)
        self.alt_word_table.setWordWrap(True)

        item = QtWidgets.QTableWidgetItem()
        self.alt_word_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.alt_word_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.alt_word_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.alt_word_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.alt_word_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.alt_word_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.alt_word_table.setHorizontalHeaderItem(6, item)

        self.alt_sent_name = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.alt_sent_name.setGeometry(QtCore.QRect(10, 1520, 140, 30))
        self.alt_sent_name.setText("语法-改句")
        self.alt_sent_name.setStyleSheet('font-size:14pt')
        self.alt_sent_name.setObjectName("label")
        self.alt_sent_table = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.alt_sent_table.setGeometry(QtCore.QRect(10, 1555, 1160, 310))
        # self.alt_sent_table.setMaximumSize(QtCore.QSize(256, 192))
        self.alt_sent_table.setObjectName("alt_sent_table")
        self.alt_sent_table.verticalHeader().setVisible(False)
        self.alt_sent_table.setColumnCount(8)
        self.alt_sent_table.setWordWrap(True)

        item = QtWidgets.QTableWidgetItem()
        self.alt_sent_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.alt_sent_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.alt_sent_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.alt_sent_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.alt_sent_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.alt_sent_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.alt_sent_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.alt_sent_table.setHorizontalHeaderItem(7, item)

        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setGeometry(QtCore.QRect(535, 1900, 90, 50))
        self.pushButton.setObjectName("pushButton")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.save)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

        item = self.sele_table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "题号"))
        item = self.sele_table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "题目"))
        item = self.sele_table.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "选项A"))
        item = self.sele_table.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "选项B"))
        item = self.sele_table.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "选项C"))
        item = self.sele_table.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "选项D"))
        item = self.sele_table.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "答案"))
        item = self.sele_table.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "类型"))
        item = self.sele_table.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "重要性"))
        item = self.sele_table.horizontalHeaderItem(9)
        item.setText(_translate("Dialog", "已出"))
        item = self.sele_table.horizontalHeaderItem(10)
        item.setText(_translate("Dialog", "题目出处"))

        item = self.fish_table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "题号"))
        item = self.fish_table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "题目出处"))
        item = self.fish_table.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "答案"))
        item = self.fish_table.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "已出"))

        item = self.alt_word_table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "题号"))
        item = self.alt_word_table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "题目"))
        item = self.alt_word_table.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "答案"))
        item = self.alt_word_table.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "类型"))
        item = self.alt_word_table.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "重要性"))
        item = self.alt_word_table.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "已出"))
        item = self.alt_word_table.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "题目出处"))

        item = self.alt_sent_table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "题号"))
        item = self.alt_sent_table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "题目"))
        item = self.alt_sent_table.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "答句"))
        item = self.alt_sent_table.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "答案"))
        item = self.alt_sent_table.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "类型"))
        item = self.alt_sent_table.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "重要性"))
        item = self.alt_sent_table.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "已出"))
        item = self.alt_sent_table.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "题目出处"))

        self.pushButton.setText(_translate("Dialog", "确定"))

    def fill(self, info):
        self.info = info
        question_num = info[4]
        self.sele_table.setRowCount(len(info[0]))
        for i in range(0, self.sele_table.rowCount()):
            self.sele_table.setItem(i, 0, QtWidgets.QTableWidgetItem(str(question_num)))
            self.sele_table.item(i, 0).setFlags(QtCore.Qt.NoItemFlags)

            self.sele_table.setItem(i, 1, QtWidgets.QTableWidgetItem(info[0][i]['question'][0]))
            for j in range(0, 4):
                self.sele_table.setItem(i, j + 2, QtWidgets.QTableWidgetItem(info[0][i]['question'][1][j]))
            self.sele_table.setItem(i, 6, QtWidgets.QTableWidgetItem(info[0][i]['answer']))
            self.sele_table.setItem(i, 7, QtWidgets.QTableWidgetItem(info[0][i]['point']))
            self.sele_table.setItem(i, 8, QtWidgets.QTableWidgetItem(str(info[0][i]['importance'])))
            self.sele_table.setItem(i, 9, QtWidgets.QTableWidgetItem(str(info[0][i]['times'])))
            self.sele_table.setItem(i, 10, QtWidgets.QTableWidgetItem(info[0][i]['path']))

            question_num += 1

        for i in range(self.sele_table.columnCount()):
            if i != 1:
                for j in range(self.sele_table.rowCount()):
                    self.sele_table.item(j, i).setTextAlignment(QtCore.Qt.AlignCenter)
        for i in range(1, self.sele_table.columnCount() - 1):
            for j in range(self.sele_table.rowCount()):
                self.sele_table.item(j, i).setFlags(QtCore.Qt.ItemIsEnabled)
        self.sele_table.setColumnWidth(0, 70)
        self.sele_table.setColumnWidth(1, 500)
        for i in range(2, 6):
            self.sele_table.setColumnWidth(i, 100)
        self.sele_table.setColumnWidth(6, 70)
        self.sele_table.setColumnWidth(7, 100)
        self.sele_table.setColumnWidth(8, 70)
        self.sele_table.setColumnWidth(9, 70)
        self.sele_table.setColumnWidth(10, 500)
        self.sele_table.resizeRowsToContents()

        self.fish_table.setRowCount(len(info[1]) * 8)
        for i in range(0, self.fish_table.rowCount()):
            m = int(i / 8)
            n = i % 8
            self.fish_table.setItem(i, 0, QtWidgets.QTableWidgetItem(str(question_num)))
            self.fish_table.item(i, 0).setFlags(QtCore.Qt.NoItemFlags)
            self.fish_table.setItem(i, 1, QtWidgets.QTableWidgetItem(info[1][m]['path']))
            self.fish_table.setItem(i, 2, QtWidgets.QTableWidgetItem(info[1][m]['answer'][n]))
            self.fish_table.setItem(i, 3, QtWidgets.QTableWidgetItem(str(info[1][m]['times'])))

            question_num += 1

        for i in range(self.fish_table.columnCount()):
            for j in range(self.fish_table.rowCount()):
                self.fish_table.item(j, i).setTextAlignment(QtCore.Qt.AlignCenter)
        for i in range(1, self.fish_table.columnCount() - 1):
            for j in range(self.fish_table.rowCount()):
                self.fish_table.item(j, i).setFlags(QtCore.Qt.ItemIsEnabled)
        for i in range(len(info[1])):
            self.fish_table.setSpan(i * 8, 1, 8, 1)
            self.fish_table.setSpan(i * 8, 3, 8, 1)
        self.fish_table.setColumnWidth(0, 70)
        self.fish_table.setColumnWidth(1, 500)
        self.fish_table.setColumnWidth(2, 70)
        self.fish_table.setColumnWidth(3, 70)
        self.fish_table.resizeRowsToContents()

        self.alt_word_table.setRowCount(len(info[2]))
        for i in range(0, self.alt_word_table.rowCount()):
            self.alt_word_table.setItem(i, 0, QtWidgets.QTableWidgetItem(str(question_num)))
            self.alt_word_table.item(i, 0).setFlags(QtCore.Qt.NoItemFlags)

            self.alt_word_table.setItem(i, 1, QtWidgets.QTableWidgetItem(info[2][i]['question']))
            self.alt_word_table.setItem(i, 2, QtWidgets.QTableWidgetItem(info[2][i]['answer']))
            self.alt_word_table.setItem(i, 3, QtWidgets.QTableWidgetItem(info[2][i]['point']))
            self.alt_word_table.setItem(i, 4, QtWidgets.QTableWidgetItem(str(info[2][i]['importance'])))
            self.alt_word_table.setItem(i, 5, QtWidgets.QTableWidgetItem(str(info[2][i]['times'])))
            self.alt_word_table.setItem(i, 6, QtWidgets.QTableWidgetItem(info[2][i]['path']))

            question_num += 1

        for i in range(self.alt_word_table.columnCount()):
            if i != 1:
                for j in range(self.alt_word_table.rowCount()):
                    self.alt_word_table.item(j, i).setTextAlignment(QtCore.Qt.AlignCenter)
        for i in range(1, self.alt_word_table.columnCount() - 1):
            for j in range(self.alt_word_table.rowCount()):
                self.alt_word_table.item(j, i).setFlags(QtCore.Qt.ItemIsEnabled)
        self.alt_word_table.setColumnWidth(0, 70)
        self.alt_word_table.setColumnWidth(1, 500)
        self.alt_word_table.setColumnWidth(2, 150)
        self.alt_word_table.setColumnWidth(3, 100)
        self.alt_word_table.setColumnWidth(4, 70)
        self.alt_word_table.setColumnWidth(5, 70)
        self.alt_word_table.setColumnWidth(6, 500)
        self.alt_word_table.resizeRowsToContents()

        self.alt_sent_table.setRowCount(len(info[3]))
        for i in range(0, self.alt_sent_table.rowCount()):
            self.alt_sent_table.setItem(i, 0, QtWidgets.QTableWidgetItem(str(question_num)))
            self.alt_sent_table.item(i, 0).setFlags(QtCore.Qt.NoItemFlags)

            self.alt_sent_table.setItem(i, 1, QtWidgets.QTableWidgetItem(info[3][i]['question'][0]))
            self.alt_sent_table.setItem(i, 2, QtWidgets.QTableWidgetItem(info[3][i]['question'][1]))
            self.alt_sent_table.setItem(i, 3, QtWidgets.QTableWidgetItem(info[3][i]['answer']))
            self.alt_sent_table.setItem(i, 4, QtWidgets.QTableWidgetItem(info[3][i]['point']))
            self.alt_sent_table.setItem(i, 5, QtWidgets.QTableWidgetItem(str(info[3][i]['importance'])))
            self.alt_sent_table.setItem(i, 6, QtWidgets.QTableWidgetItem(str(info[3][i]['times'])))
            self.alt_sent_table.setItem(i, 7, QtWidgets.QTableWidgetItem(info[3][i]['path']))

            question_num += 1

        for i in range(self.alt_sent_table.columnCount()):
            if i not in [1, 2]:
                for j in range(self.alt_sent_table.rowCount()):
                    self.alt_sent_table.item(j, i).setTextAlignment(QtCore.Qt.AlignCenter)
        for i in range(1, self.alt_sent_table.columnCount() - 1):
            for j in range(self.alt_sent_table.rowCount()):
                self.alt_sent_table.item(j, i).setFlags(QtCore.Qt.ItemIsEnabled)
        self.alt_sent_table.setColumnWidth(0, 70)
        self.alt_sent_table.setColumnWidth(1, 500)
        self.alt_sent_table.setColumnWidth(2, 500)
        self.alt_sent_table.setColumnWidth(3, 150)
        self.alt_sent_table.setColumnWidth(4, 100)
        self.alt_sent_table.setColumnWidth(5, 70)
        self.alt_sent_table.setColumnWidth(6, 70)
        self.alt_sent_table.setColumnWidth(7, 500)
        self.alt_sent_table.resizeRowsToContents()
