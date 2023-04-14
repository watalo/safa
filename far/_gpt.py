#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   _response.py
@Time    :   2023/04/13 00:20:03
@Author  :   watalo 
@Version :   1.0
@Contact :   watalo@163.com
'''

# here put the import lib
from transformers import AutoTokenizer, AutoModel
from . import _config
import re


'''
Glm类
用来调用ChatGLM的返回信息
- 属性
    .model_path 指定存放模型的文件夹路径
- 方法
    .response() 唯一的,用来接受prompt列表,并返回‘回复’列表
        调整_text.py内容，
'''

class Glm():
    def __init__(self):
        self.model_path = _config.Path.model
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path, trust_remote_code=True)
       
    def __model(self,type='GPU'):
        model = AutoModel.from_pretrained(self.model_path, trust_remote_code=True)
        if type == 'GPU':
            model = model.quantize(4).half().cuda()
        elif type == 'CPU':
            model = model.float()
        model = model.eval()   
        return model
    
    def response(self,prompt):
        res,his = self.__model('CPU').chat(self.tokenizer, prompt, history=[])
        res = res.strip(r'\r').strip(r'\n').strip(r'\t')
        return res

    # 清楚字符串中的‘\r'、'\n’和‘\t’
    
    
    

class Prompt(object):
    p2 = '请分析申请人的资本结构。'
    p3 = '请分析申请人的盈利能力。'
    p4 = '请分析申请人的现金流量。'
    p5 = '请分析申请人的资产质量。'
    p6 = '请分析申请人的流动性。'
    


