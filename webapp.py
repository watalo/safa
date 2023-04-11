#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   chatfar.py
@Time    :   2023/04/11 13:15:26
@Author  :   watalo 
@Version :   1.0
@Contact :   watalo@163.com
'''

from flask import Flask, render_template, request, send_file
import os
from start import *
from far import _config

app = Flask(__name__)

# 文件下载功能
@app.route('/download')
def download_file():
    filename = './templates/模板.xlsx'  # 要下载的文件名
    directory = os.getcwd()  # 获取当前目录
    path = os.path.join(directory, filename)  # 获取文件完整路径
    return send_file(path, as_attachment=True)  # 返回文件下载

@app.route('/download2')
def download_file2():
    filename = './templates/样品.docx'  # 要下载的文件名
    directory = os.getcwd()  # 获取当前目录
    path = os.path.join(directory, filename)  # 获取文件完整路径
    return send_file(path, as_attachment=True)  # 返回文件下载

# 文件上传功能
@app.route('/upload', methods=['get','POST'])
def upload_file():
    for i in ['/safa/db', '/safa/output', '/safa/input']:
        dirpath = ''.join([_config.Path.root, r"/%s" % i])
        namelist = os.listdir(dirpath)
        for file_name in namelist:
            os.remove(dirpath+'/' + file_name)
    
    if request.method == 'POST':
        file = request.files['file']  # 获取上传的文件
        filename = file.filename  # 获取文件名
        file.save('./input/'+filename)  # 将上传的文件保存到当前目录下
        return render_template('index.html',success=True)
    return render_template('index.html')

# 生成报告功能
@app.route('/generate_report')
def generate_report():
    
    # 进行后台程序的处理，生成新的报告文件
    init_dir()
    new_filename = get_start()
    
    return send_file(new_filename, as_attachment=True)  # 返回生成的报告文件下载

# 页面渲染
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)