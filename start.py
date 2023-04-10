
# -*- coding: utf-8 -*-
#__author__:"watalo"
# @Time: 2020/3/27 1:51
# @Site    : 
# @File    : start.py
# @Software: 

'''
python-docx库运用中出现的问题

'''
import os
from far import _config
from far.core import getDB
from far.main import get_docx


def init_dir():
    for i in ['/safa/db', '/safa/output']:
        dirpath = ''.join([_config.Path.root, "/%s" % i])
        namelist = os.listdir(dirpath)
        for filename in namelist:
            os.remove(os.path.join(dirpath, filename))

def get_template_filename():
    return 

if __name__ == "__main__":
    init_dir()  
    name = os.listdir(''.join(_config.Path.input))[0].split('.')[0]
    output_path = '/'.join([_config.Path.output, name +'.docx'])
    db_path = '/'.join([_config.Path.db, name + '.json'])
    db = getDB(name = name)
    get_docx(name=name,output_path=output_path)

