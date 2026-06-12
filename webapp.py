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
from pathlib import Path
from werkzeug.utils import secure_filename
from start import *
from safa import _config

app = Flask(__name__)

# 允许的清理目录（仅 xlsx 后缀；只接受 INPUT_PATH 之内）
_ALLOWED_CLEAN_DIRS = {
    Path(_config.INPUT_PATH).resolve(),
    Path(_config.OUTPUT_PATH).resolve(),
    Path(_config.DB_PATH).resolve(),
}

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
    for dirpath in (
        _config.INPUT_PATH,
        _config.OUTPUT_PATH,
        _config.DB_PATH,
    ):
        base = Path(dirpath).resolve()
        if not base.is_dir():
            continue
        for candidate in base.iterdir():
            if not candidate.is_file():
                continue
            # 只清理 .xlsx 文件（保护 docx/json/图片等）
            if candidate.suffix.lower() != '.xlsx':
                continue
            # 路径穿越校验：必须位于 base 之内
            try:
                if not candidate.resolve().is_relative_to(base):
                    continue
            except (ValueError, OSError):
                continue
            try:
                candidate.unlink()
            except OSError:
                pass

    if request.method == 'POST':
        file = request.files['file']  # 获取上传的文件
        # 文件名安全化 + 强制 .xlsx 后缀 + 路径穿越校验
        safe_name = secure_filename(file.filename or '')
        if not safe_name:
            return render_template('index.html', success=False, error='非法文件名')
        # 去掉原后缀再强制 .xlsx（防止 .xlsx.exe 之类的双扩展名）
        stem = Path(safe_name).stem
        final_name = f'{stem}.xlsx'
        target = (Path(_config.INPUT_PATH) / final_name).resolve()
        try:
            if not target.is_relative_to(Path(_config.INPUT_PATH).resolve()):
                return render_template('index.html', success=False, error='路径穿越被拦截')
        except (ValueError, OSError):
            return render_template('index.html', success=False, error='路径校验失败')
        # 确保目标目录存在
        target.parent.mkdir(parents=True, exist_ok=True)
        file.save(str(target))
        return render_template('index.html', success=True)
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
    app.run(debug=False, host='127.0.0.1', port=5000)