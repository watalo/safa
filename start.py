
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
    return os.listdir(''.join(_config.Path.input))[0].split('.')[0]

def get_start():
    name = get_template_filename()
    output_path = '/'.join([_config.Path.output, name +'.docx'])
    db_path = ''.join([_config.Path.db, name + '.json'])
    db = getDB(name = name)
    get_docx(name=name, output_path=output_path)
    return output_path


def get_all_file_paths():
    file_paths = []
    for root, directories, files in os.walk("."):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths

if __name__ == "__main__":
    init_dir()  
    name = os.listdir(''.join(_config.Path.input))[0].split('.')[0]
    output_path = '/'.join([_config.Path.output, name +'.docx'])
    print(output_path)
    db_path = '/'.join([_config.Path.db, name + '.json'])
    db = getDB(name = name)
    get_docx(name=name,output_path=output_path)

