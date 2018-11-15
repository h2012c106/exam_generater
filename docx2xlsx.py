import os
import win32com
from win32com.client import Dispatch
from enum import Enum
import pandas as pd
import time
import shutil
import codecs
import doc_disassembler

TXT_SPLIT = '\n+===========================+\n'
SELE_SPLIT = '#==#'

LIB_PATH = os.getcwd() + '/题库/'
BACKUP_PATH = os.getcwd() + '/备份/'
MAIN_XLS = os.getcwd() + '/核心表格(请勿删除,移动,改名).xlsx'


def get_doc_names(path):
    path, name = os.path.split(path)
    name, exten = os.path.splitext(name)
    return [path, name, exten]


def copy_doc(old_path, new_dir):
    wordApp = win32com.client.Dispatch('Word.Application')
    # wordApp.Visible = True
    wordApp.DisplayAlerts = 0

    if get_doc_names(old_path)[2] == '.doc' or get_doc_names(old_path)[2] == '.docx':
        doc = wordApp.Documents.Open(old_path)
        new_path = new_dir + get_doc_names(old_path)[1] + '.docx'
        doc.SaveAs(new_path, 16)  # 转化后路径下的文件
        doc.Close()
        wordApp.Quit()
        return new_path
    else:
        return None


def copy_sheet(method):
    if not os.path.exists(MAIN_XLS):
        return True
    if not os.path.exists(BACKUP_PATH):
        os.mkdir(BACKUP_PATH)
    try:
        new_name = '备份-' + time.strftime('%Y-%m-%d %H@%M@%S', time.localtime(time.time())) + '-' + method
        # new_name = '备份-' + method
        new_path = BACKUP_PATH + new_name + '.xlsx'
        shutil.copyfile(MAIN_XLS, new_path)
        return True
    except:
        return False

def init(dst_dir, src_doc_arr):
    if not os.path.exists(LIB_PATH):
        os.mkdir(LIB_PATH)
    for src_doc in src_doc_arr:
        if len(src_doc.strip()) == 0 or not os.path.exists(src_doc):
            return '请选择试卷文件', False
    dst_dir = dst_dir.strip()
    if len(dst_dir) == 0:
        return '请输入非空白文件名', False
    if '/' in dst_dir or '\\' in dst_dir:
        return '文件名不要出现正反斜杠', False
    else:
        dst_dir = LIB_PATH + dst_dir + '/'
        if os.path.exists(dst_dir):
            return '此文件名已存在', False
        else:
            os.mkdir(dst_dir)
            res = []
            for src_doc in src_doc_arr:
                new_path = copy_doc(src_doc, dst_dir)
                if not new_path:
                    return '请选择.doc或.docx文件', False
                else:
                    res.append(new_path)
            return res, True


def read_with_one_doc(a):
    return doc_disassembler.read_with_one_doc(a)


def read_with_two_doc(a, b):
    return doc_disassembler.read_with_two_doc(a, b)


def new_df():
    return pd.DataFrame(columns=['题目路径', '题目类型', '出处路径', '出处题号', '题目考点', '重要程度', '已出次数'])


def save_and_sheet(res, dst_dir, src_doc):
    dst_dir = LIB_PATH + dst_dir + '/'

    if not copy_sheet('录卷'):
        raise RuntimeError('备份核心表格失败')
    df = pd.read_excel(MAIN_XLS) if os.path.exists(MAIN_XLS) else new_df()

    for i in range(doc_disassembler.type2num(doc_disassembler.QUE_TYPE.GRAMA_SELE)):
        tmp_path = dst_dir + str(res[0]['number'][i]) + '-' + doc_disassembler.QUE_TYPE.GRAMA_SELE.value + '.txt'
        tmp_info = res[0]['question'][i][0] + TXT_SPLIT + SELE_SPLIT.join(res[0]['question'][i][1]) + TXT_SPLIT + \
                   res[0]['answer'][i]
        with codecs.open(tmp_path, 'w', 'utf-8') as tmp_file:
            tmp_file.write(tmp_info.strip())

        df = df.append(pd.Series({
            '题目路径': tmp_path,
            '题目类型': doc_disassembler.QUE_TYPE.GRAMA_SELE.value,
            '出处路径': src_doc,
            '出处题号': res[0]['number'][i],
            '题目考点': res[0]['point'][i],
            '重要程度': res[0]['importance'][i],
            '已出次数': 0
        }), ignore_index=True)

    for i in range(1):
        tmp_path = dst_dir + '46-53' + doc_disassembler.QUE_TYPE.GRAMA_FISH.value + '.txt'
        tmp_info = SELE_SPLIT.join(res[1]['answer'])
        with codecs.open(tmp_path, 'w', 'utf-8') as tmp_file:
            tmp_file.write(tmp_info.strip())

        df = df.append(pd.Series({
            '题目路径': tmp_path,
            '题目类型': doc_disassembler.QUE_TYPE.GRAMA_FISH.value,
            '出处路径': src_doc,
            '出处题号': '46-53',
            '题目考点': '',
            '重要程度': '',
            '已出次数': 0
        }), ignore_index=True)

    for i in range(doc_disassembler.type2num(doc_disassembler.QUE_TYPE.GRAMA_ALTER_WORD)):
        tmp_path = dst_dir + str(res[2]['number'][i]) + '-' + doc_disassembler.QUE_TYPE.GRAMA_ALTER_WORD.value + '.txt'
        tmp_info = res[2]['question'][i] + TXT_SPLIT + res[2]['answer'][i]
        with codecs.open(tmp_path, 'w', 'utf-8') as tmp_file:
            tmp_file.write(tmp_info.strip())

        df = df.append(pd.Series({
            '题目路径': tmp_path,
            '题目类型': doc_disassembler.QUE_TYPE.GRAMA_ALTER_WORD.value,
            '出处路径': src_doc,
            '出处题号': res[2]['number'][i],
            '题目考点': res[2]['point'][i],
            '重要程度': res[2]['importance'][i],
            '已出次数': 0
        }), ignore_index=True)

    for i in range(doc_disassembler.type2num(doc_disassembler.QUE_TYPE.GRAMA_ALTER_SENT)):
        tmp_path = dst_dir + str(res[3]['number'][i]) + '-' + doc_disassembler.QUE_TYPE.GRAMA_ALTER_SENT.value + '.txt'
        tmp_info = res[3]['question'][i][0] + TXT_SPLIT + res[3]['question'][i][1] + TXT_SPLIT + res[3]['answer'][i]
        with codecs.open(tmp_path, 'w', 'utf-8') as tmp_file:
            tmp_file.write(tmp_info.strip())

        df = df.append(pd.Series({
            '题目路径': tmp_path,
            '题目类型': doc_disassembler.QUE_TYPE.GRAMA_ALTER_SENT.value,
            '出处路径': src_doc,
            '出处题号': res[3]['number'][i],
            '题目考点': res[3]['point'][i],
            '重要程度': res[3]['importance'][i],
            '已出次数': 0
        }), ignore_index=True)

    df.to_excel(MAIN_XLS, index=False)
