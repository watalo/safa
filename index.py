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
from docx import Document
import docx

class Test(object):
    def __init__(self,name):
        self.name = name

    def test(self,doc,text):
        p = doc.add_paragragh(text)

if __name__ == '__main__':
    D = Document()
    D.add_paragragh('1123')