
# -*- coding: utf-8 -*-
#__author__:"watalo"
# @Time: 2020/3/27 1:51
# @Site    : 
# @File    : start.py
# @Software: 

'''
经典方法执行文件
'''
import os
from far._config import INPUT_PATH, OUTPUT_PATH, DB_PATH
from far.core import getDB
from far.main import get_docx

def init_dir():
    for path in [OUTPUT_PATH, DB_PATH]:
        files = os.listdir(path)
        for file in files:
            os.remove(os.path.join(path, file))

def get_template_filename():
    return os.listdir(''.join(INPUT_PATH))[0].split('.')[0]

def start():
    name = get_template_filename()
    output_path = os.path.join(OUTPUT_PATH, f'{name}.docx')
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
    start()
    
    
