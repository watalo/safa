
# -*- coding: utf-8 -*-
#__author__:"watalo"
# @Time: 2020/3/30 22:22
# @Site    : 
# @File    : _config.py
# @Software: PyCharm

import os

class Path:
    '路径类的配置文件'
    root = os.path.dirname(os.getcwd())
    db = root+ '/safa/db'
    input = root+ '/safa/input'
    output = root+ '/safa/output'
    # 设置模型路径
    model = '/media/watalo/DATA/chat/wenda0406/model/chatglm-6b-int4'
    

if __name__ == '__main__':
    print(os.getcwd()) 
    print(os.path.dirname(os.getcwd()))

