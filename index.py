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

name = 'temple'
output_path = '\\'.join([_config.Path.output, name +'.docx'])
getDB(name = name)
get_docx(name=name,
         output_path=output_path)

