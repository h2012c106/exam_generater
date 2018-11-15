# import pandas as pd
# import os
#
# MAIN_XLS = os.getcwd() + '/核心表格(请勿删除,移动,改名).xlsx'
#
#
# def new_df():
#     return pd.DataFrame(columns=['题目路径', '出处路径', '出处题号', '题目类型', '重要程度', '已出次数'])
#
#
# df = pd.read_excel(MAIN_XLS) if os.path.exists(MAIN_XLS) else new_df()
# df = df.append(pd.Series({
#     '题目路径': 'sdds', '出处路径': 'dsgsd', '出处题号': 2212, '题目类型': 'ffeff', '重要程度': 'fefd', '已出次数': 0
# }), ignore_index=True)
# df.to_excel(MAIN_XLS, index=False)

import pandas as pd


def special_select(df, point_arr):
    tmp = df.copy()
    tmp.drop(df.index, inplace=True)
    for i in range(len(df)):
        if is_intersect(df.iloc[i]['哈'].split('#'), point_arr):
            tmp = tmp.append(pd.Series(df.iloc[i]), ignore_index=True)
    return tmp


def my_drop(df, has_picked):
    drop_arr = []
    for i in range(len(df)):
        if df.iloc[i]['哈'] in has_picked:
            drop_arr.append(i)

    df = df.drop(drop_arr)
    return df


def is_intersect(x, y):
    if len(list(set(x).intersection(set(y)))) == 0:
        return False
    else:
        return True


import random


def random_sele(sele_arr, ans):
    ans = ans.strip()
    tmp_arr = [(sele_arr[i], chr(i + ord('A'))) for i in range(len(sele_arr))]
    tmp_arr.sort(key=lambda item: random.random())
    new_ans = False
    for i, sele in enumerate(tmp_arr):
        if sele[1] == ans:
            new_ans = chr(i + ord('A'))
    tmp_arr = [tmp[0] for tmp in tmp_arr]
    return tmp_arr, new_ans
