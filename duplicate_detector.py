import os
import re
import codecs
import hashlib
import pandas as pd
from doc_disassembler import QUE_TYPE
from docx2xlsx import MAIN_XLS
from xlsx2docx import path_to_question_and_answer

DUP_TXT = os.getcwd() + '/重复题目序号.txt'


def question_hash(path, type):
    info = path_to_question_and_answer(path, type)['question']
    question_str = ''
    if type == QUE_TYPE.GRAMA_SELE.value:
        question_str += info[0]
        question_str += ' '.join(sorted(info[1]))
    elif type == QUE_TYPE.GRAMA_ALTER_WORD.value:
        question_str += info
    elif type == QUE_TYPE.GRAMA_ALTER_SENT.value:
        question_str += info[0]
        question_str += info[1]
    question_str = re.sub(r'\s+', ' ', question_str.strip())
    question_str = question_str.lower()
    return hashlib.md5(question_str.encode(encoding='UTF-8')).hexdigest()


def detect():
    df = pd.read_excel(MAIN_XLS)
    help_map = {}
    for i in range(len(df)):
        if df.iloc[i]['题目类型'] == QUE_TYPE.GRAMA_FISH.value or int(df.iloc[i]['重要程度']) == 0:
            continue
        else:
            q_hash = question_hash(df.iloc[i]['题目路径'], df.iloc[i]['题目类型'])
            if help_map.__contains__(q_hash):
                help_map[q_hash].append(str(i + 2))
            else:
                help_map[q_hash] = [str(i + 2)]
    res = []
    for v in help_map.values():
        if len(v) <= 1:
            continue
        else:
            res.append(v[:])
    if len(res) == 0:
        return False
    else:
        res = list(map(lambda item: ', '.join(list(set(item))), res))
        res = '\n'.join(res)
        res = res.strip()
        with codecs.open(DUP_TXT, 'w', 'utf-8') as f:
            f.write(res)
        return True
