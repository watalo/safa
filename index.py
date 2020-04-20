#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
# @Time: 2020/3/27 1:51
# @Site    : 
# @File    : index.py
# @Software: PyCharm

'''
python-docx库运用中出现的问题

'''
import os
from far import _config
from core import getDB
from main import get_docx


def init_dir():
    # root_path = r'D:\watalo\projects\ddipy_e.1.0\ddipy\core'
    # root_path = os.path.abspath(os.path.join(os.getcwd(), ".."))
    for i in ['\safa\db', '\safa\output']:
        dirpath = ''.join([_config.Path.root, r"\%s" % i])
        namelist = os.listdir(dirpath)
        for filename in namelist:
            os.remove(dirpath+'\\' + filename)

init_dir()

name = 'temple'
output_path = '\\'.join([_config.Path.output, name +'.docx'])
db_path = '\\'.join([_config.Path.db, name + '.json'])
db = getDB(name = name)
get_docx(name=name,
         output_path=output_path)

