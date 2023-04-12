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

class GLM():
    
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
    
    def __response(self,input:str):
        response, history = self.__model().chat(self.tokenizer, input, history=[])
        return response
       
    def normol(self,):
        input = []
        res = []
        for i in input:
            res.append(self.__response(i))
    
    @property 
    def no_year3(self):
        pass
    
    @property     
    def no_year2(self):
        pass
    
    @property 
    def no_year1(self):
        pass

    @property 
    def all_years(self):
        pass
    
    @property 
    def two_years(self):
        pass
    
if __name__ == '__main__':
    pass