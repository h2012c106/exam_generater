import sys
import os
from hello import *
from read_one import *
from read_two import *
from read_config import *
from preview_table import *
from preview_uneditable_table import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox
from PyQt5.QtCore import *
import docx2xlsx
import xlsx2docx
import duplicate_detector


class main_window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(main_window, self).__init__()
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.read_one.clicked.connect(self.show_read_one)
        self.read_two.clicked.connect(self.show_read_two)
        self.generate.clicked.connect(self.show_read_config)
        self.detect.clicked.connect(self.start_detect)

    def show_read_one(self):
        self.read_one_widget = read_one()
        self.read_one_widget.show()

    def show_read_two(self):
        self.read_two_widget = read_two()
        self.read_two_widget.show()

    def show_read_config(self):
        self.read_config_widget = read_config()
        self.read_config_widget.show()

    def start_detect(self):
        try:
            has_dup = duplicate_detector.detect()
            if has_dup:
                QMessageBox.information(self, '成功', '检测完成\n请至"重复题目序号.txt"中查看', QMessageBox.Yes)
            else:
                QMessageBox.information(self, '成功', '检测完成\n暂未发现重复题目', QMessageBox.Yes)
        except:
            QMessageBox.critical(self, '错误', str(sys.exc_info()[1]))


class read_one(QWidget, Ui_Read_One):
    def __init__(self):
        super(read_one, self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

    def path(self):
        file_path, ok = QFileDialog.getOpenFileName(self, '读取', './', 'Word文件(*.doc *.docx)')
        if ok:
            self.label.setText(file_path)

    def init(self):
        self.dst_dir = self.dir_name.toPlainText().strip()
        src_doc = self.label.text()

        new_doc, ok = docx2xlsx.init(self.dst_dir, [src_doc])
        if not ok:
            raise RuntimeError(new_doc)
        new_doc = new_doc[0]
        return new_doc

    def do(self):
        try:
            res = docx2xlsx.read_with_one_doc(self.new_doc)
            self.preview = preview_table()
            self.preview.fill(res)
            self.preview.set_dir_and_src(self.dst_dir, self.new_doc)
            self.preview.show()
            self.close()
        except:
            QMessageBox.critical(self, '错误', str(sys.exc_info()[1]))
            os.startfile(self.new_doc)
            if not hasattr(self, 'retry'):
                self.retry = QtWidgets.QPushButton(self)
                self.retry.setGeometry(QtCore.QRect(385, 20, 85, 50))
                self.retry.setObjectName("retry")
                _translate = QtCore.QCoreApplication.translate
                self.retry.setText(_translate("Read_One", "重试"))
                self.retry.clicked.connect(self.do)
                self.retry.show()

    def run(self):
        try:
            self.new_doc = self.init()
            self.do()
        except:
            QMessageBox.critical(self, '错误', str(sys.exc_info()[1]))


class read_two(QWidget, Ui_Read_Two):
    def __init__(self):
        super(read_two, self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

    def path_1(self):
        file_path, ok = QFileDialog.getOpenFileName(self, '读取', './', 'Word文件(*.doc *.docx)')
        if ok:
            self.label_1.setText(file_path)

    def path_2(self):
        file_path, ok = QFileDialog.getOpenFileName(self, '读取', './', 'Word文件(*.doc *.docx)')
        if ok:
            self.label_2.setText(file_path)

    def init(self):
        self.dst_dir = self.dir_name.toPlainText().strip()
        src_doc = [self.label_1.text(), self.label_2.text()]

        new_doc, ok = docx2xlsx.init(self.dst_dir, src_doc)
        if not ok:
            raise RuntimeError(new_doc)
        return new_doc

    def do(self):
        try:
            res = docx2xlsx.read_with_two_doc(self.new_doc[0], self.new_doc[1])
            self.preview = preview_table()
            self.preview.fill(res)
            self.preview.set_dir_and_src(self.dst_dir, self.new_doc)
            self.preview.show()
            self.close()
        except:
            QMessageBox.critical(self, '错误', str(sys.exc_info()[1]))
            os.startfile(self.new_doc[0])
            os.startfile(self.new_doc[1])
            if not hasattr(self, 'retry'):
                self.retry = QtWidgets.QPushButton(self)
                self.retry.setGeometry(QtCore.QRect(505, 20, 85, 50))
                self.retry.setObjectName("retry")
                _translate = QtCore.QCoreApplication.translate
                self.retry.setText(_translate("Read_Two", "重试"))
                self.retry.clicked.connect(self.do)
                self.retry.show()

    def run(self):
        try:
            self.new_doc = self.init()
            self.do()
        except:
            QMessageBox.critical(self, '错误', str(sys.exc_info()[1]))


class preview_table(QMainWindow, Ui_In_Preview):
    def __init__(self):
        super(preview_table, self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

    def set_dir_and_src(self, dir, src):
        self.dst_dir = dir
        self.src_doc = src

    def read(self):
        res = [{
            'question': [],
            'point': [],
            'importance': [],
            'answer': [],
            'number': []
        }, {
            'question': '',
            'answer': []
        }, {
            'question': [],
            'point': [],
            'importance': [],
            'answer': [],
            'number': []
        }, {
            'question': [],
            'point': [],
            'importance': [],
            'answer': [],
            'number': []
        }]

        for i in range(self.sele_table.rowCount()):
            res[0]['number'].append(self.sele_table.item(i, 0).text())
            res[0]['question'].append(
                [self.sele_table.item(i, 1).text(), [self.sele_table.item(i, j).text() for j in range(2, 6)]])
            res[0]['answer'].append(self.sele_table.item(i, 6).text())
            res[0]['point'].append(self.sele_table.item(i, 7).text())
            res[0]['importance'].append(self.sele_table.item(i, 8).text())

        res[1]['question'] = self.src_doc
        for i in range(self.fish_table.rowCount()):
            res[1]['answer'].append(self.fish_table.item(i, 2).text())

        for i in range(self.alt_word_table.rowCount()):
            res[2]['number'].append(self.alt_word_table.item(i, 0).text())
            res[2]['question'].append(self.alt_word_table.item(i, 1).text())
            res[2]['answer'].append(self.alt_word_table.item(i, 2).text())
            res[2]['point'].append(self.alt_word_table.item(i, 3).text())
            res[2]['importance'].append(self.alt_word_table.item(i, 4).text())

        for i in range(self.alt_sent_table.rowCount()):
            res[3]['number'].append(self.alt_sent_table.item(i, 0).text())
            res[3]['question'].append([self.alt_sent_table.item(i, 1).text(), self.alt_sent_table.item(i, 2).text()])
            res[3]['answer'].append(self.alt_sent_table.item(i, 3).text())
            res[3]['point'].append(self.alt_sent_table.item(i, 4).text())
            res[3]['importance'].append(self.alt_sent_table.item(i, 5).text())

        return res

    def save(self):
        try:
            res = self.read()
            docx2xlsx.save_and_sheet(res, self.dst_dir, self.src_doc)
            QMessageBox.information(self, '成功', '录入成功', QMessageBox.Yes)
            self.close()
        except:
            QMessageBox.critical(self, '错误', str(sys.exc_info()[1]))


class read_config(QWidget, Ui_Read_Conf):
    def __init__(self):
        super(read_config, self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

    def path(self):
        file_path, ok = QFileDialog.getOpenFileName(self, '读取', './', 'Json文件(*.json)')
        if ok:
            self.label.setText(file_path)

    def run(self):
        config_json = self.label.text()
        dst_dir = self.dir_name.toPlainText().strip()
        try:
            info, ok = xlsx2docx.judge_dst_dir(dst_dir)
            if not ok:
                raise RuntimeError(info)
            res = xlsx2docx.assemble(config_json)
            self.preview = preview_tacle()
            self.preview.fill(res)
            self.preview.set_dst_dir(dst_dir)
            self.preview.show()
            self.close()
        except:
            QMessageBox.critical(self, '错误', str(sys.exc_info()[1]))
            # os.startfile(config_json)


class preview_tacle(QMainWindow, Ui_Out_Preview):
    def __init__(self):
        super(preview_tacle, self).__init__()
        self.setWindowModality(Qt.ApplicationModal)
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

    def set_dst_dir(self, dst_dir):
        self.dst_dir = dst_dir

    def save(self):
        try:
            xlsx2docx.generate_paper_and_ans(self.info, self.dst_dir)
            QMessageBox.information(self, '成功', '制作成功', QMessageBox.Yes)
            self.close()
        except:
            QMessageBox.critical(self, '错误', str(sys.exc_info()[1]))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    home = main_window()
    home.show()
    sys.exit(app.exec_())
