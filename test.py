#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
# @Time: 2020/3/30 1:23
# @Site    : 
# @File    : test.py
# @Software: PyCharm

from docx import Document

doc = Document()
doc.add_paragragh('I love python-docx')
doc.save('test.docx')