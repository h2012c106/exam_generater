import os
import time
import codecs

TXT_SPLIT = '\n+===========================+\n'
LOG_PATH = os.getcwd() + '/错误日志(请勿移动,改名).log'


def log(err_name, err_info):
    tmp_info = TXT_SPLIT + time.strftime('%Y-%m-%d %H:%M:%S',
                                         time.localtime(time.time())) + ':\t' + err_name + TXT_SPLIT + err_info
    tmp_info = tmp_info.strip()
    with codecs.open(LOG_PATH, 'a', 'utf-8') as f:
        f.write(tmp_info)
