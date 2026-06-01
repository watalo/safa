#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
# @Time: 2020/3/22 22:59
# @Site    :
# @File    : _para.py
# @Software: PyCharm


import os
from tinydb import TinyDB ,Query
from far import _text ,_config
from far._analysis_s2d1 import AnalysisS2d1Mixin
from far._analysis_s2d2 import AnalysisS2d2Mixin
from far._analysis_s2d3 import AnalysisS2d3Mixin
from far._analysis_s2d5 import AnalysisS2d5Mixin



'''
1 判断数据结构的年份构成
    normal
    no_year3
    no_year2
    no_year1
    all_years
    two_years
2 对text类中的text进行匹配

    2.1 可直接读取的数据
        从数据中读取
    2.2 需进行分析的文字
        直接形成分析结果，按字符串形式存储


'''

class dict_(AnalysisS2d5Mixin, AnalysisS2d3Mixin, AnalysisS2d2Mixin, AnalysisS2d1Mixin):
    '''
    设定变量字典

    analysis_s2d1/2/3/5 拆到 _analysis_s2dN.py 五个 mixin 文件,
    通过多重继承拼到 dict_ 类上。MRO 顺序:AnalysisS2d1Mixin(最后)→ S2d2 → S2d3 → S2d5(最先)。
    '''
    def __init__(self):
        self.db_path = _config.DB_PATH
        self.db_file_path = '/'.join([self.db_path, os.listdir(self.db_path)[0]])
        # print(db_file_path)
        self.db = TinyDB(self.db_file_path)
        self.table = self.db.table('without_nodata')
        self.Q = Query()
        self.s2d1 = {'总资产3': ['资产总计','year3'], '总资产2': ['资产总计','year2'],
                     '总资产1': ['资产总计','year1'], '总资产m': ['资产总计','month'],
                     '总负债3': ['负债合计','year3'], '总负债2': ['负债合计','year2'],
                     '总负债1': ['负债合计','year1'], '总负债m': ['负债合计','month'],
                     '资产负债率3': ['资产负债率','year3'], '资产负债率2': ['资产负债率','year2'],
                     '资产负债率1': ['资产负债率','year1'], '资产负债率m': ['资产负债率','month'],
                     '分析s2d1':str(),
                     }
        self.s2d2 = {'分析s2d2': str(),
                     '流动负债3': ['流动负债合计','year3'], '流动负债2': ['流动负债合计','year2'],
                     '流动负债1': ['流动负债合计','year1'], '流动负债m': ['流动负债合计','month'],
                     '短债占比3': ['短债占比','year3'], '短债占比2': ['短债占比','year2'],
                     '短债占比1': ['短债占比','year1'], '短债占比m': ['短债占比','month'],
                     '刚性负债3': ['刚性负债','year3'], '刚性负债2': ['刚性负债','year2'],
                     '刚性负债1': ['刚性负债','year1'], '刚性负债m': ['刚性负债','month'],
                     '刚性兑付占比3': ['刚兑占比','year3'], '刚性兑付占比2': ['刚兑占比','year2'],
                     '刚性兑付占比1': ['刚兑占比','year1'], '刚性兑付占比m': ['刚兑占比','month'],
                     '短期刚兑m': ['短期刚兑','month'],'短期刚兑1':['短期刚兑','year1'],
                     '短期借款m': ['短期借款','month'],'短期借款1':['短期借款','year1'],
                     '一年内非流m': ['一年内到期的非流动负债','month'],'一年内非流1': ['一年内到期的非流动负债','year1'],
                     }
        self.s2d3 = {'营业收入3': ['营业收入','year3'], '营业收入2': ['营业收入','year2'],
                     '营业收入1': ['营业收入','year1'], '分析s2d3':str(),
                     '营业成本3': ['营业成本','year3'], '营业成本2': ['营业成本','year2'],
                     '营业成本1': ['营业成本','year1'],
                     '毛利率3': ['毛利率','year3'], '毛利率2':['毛利率','year2'], '毛利率1':['毛利率','year1'],
                     '期间费用3': ['期间费用','year3'], '期间费用2': ['期间费用','year2'], '期间费用1': ['期间费用','year1'],
                     '费用收入比3': ['费用收入比','year3'], '费用收入比2': ['费用收入比','year2'],
                     '费用收入比1': ['费用收入比','year1'],
                     '净利润3': ['净利润','year3'], '净利润2': ['净利润','year2'], '净利润1': ['净利润','year1'],
                     '净利润率3': ['净利润率','year3'], '净利润率2': ['净利润率','year2'], '净利润率1': ['净利润率','year1'],
                     '营业收入m':['营业收入','month'], '营业成本m':['营业成本','month'], '毛利率m':['毛利率','month'],
                     '期间费用m':['期间费用','month'], '投资收益m':['投资收益','month'], '净利润率m':['净利润率','month'],
                     }
        self.s2d4 = {'净现金流入3':['现金净流入','year3'], '净现金流入2':['现金净流入','year2'],
                     '净现金流入1':['现金净流入','year1'], '净现金流入m':['现金净流入','month'],
                     '经营活动现金净流入3':['经营活动净现金流入','year3'], '经营活动现金净流入2':['经营活动净现金流入','year2'],
                     '经营活动现金净流入1':['经营活动净现金流入','year1'], '经营活动现金净流入m':['经营活动净现金流入','month'],
                     '投资活动现金净流入3':['投资活动现金净流入','year3'], '投资活动现金净流入2':['投资活动现金净流入','year2'],
                     '投资活动现金净流入1':['投资活动现金净流入','year1'], '投资活动现金净流入m':['投资活动现金净流入','month'],
                     '筹资活动现金净流入3':['筹资活动现金净流入','year3'], '筹资活动现金净流入2':['筹资活动现金净流入','year2'],
                     '筹资活动现金净流入1':['筹资活动现金净流入','year1'], '筹资活动现金净流入m':['筹资活动现金净流入','month'],
                     }
        self.s2d5 = {'流动资产3':['流动资产合计','year3'], '流动资产2':['流动资产合计','year2'],
                     '流动资产1':['流动资产合计','year1'], '流动资产m':['流动资产合计','month'],
                     '流动资产占比3':['流动资产占比','year3'], '流动资产占比2':['流动资产占比','year2'],
                     '流动资产占比1':['流动资产占比','year1'], '流动资产占比m':['流动资产占比','month'],
                     '分析s2d5':str(),
                     }
        self.s2d6 = {'流动比率3':['流动比率','year3'], '流动比率2':['流动比率','year2'],
                     '流动比率1':['流动比率','year1'], '流动比率m':['流动比率','month'],
                     '流动比率av':['流动比率','averg'], '流动比率delta':['流动比率','delta'],
                     '速动比率3':['速动比率','year3'], '速动比率2':['速动比率','year2'],
                     '速动比率1':['速动比率','year1'], '速动比率m':['速动比率','month'],
                     '速动比率av':['速动比率','averg'], '速动比率delta':['速动比率','delta'],
                      }

    @property
    def data_type(self):
        '''
        判断数据类型
        :return: 数据结构的类型[normal,no_year3,no_year2,no_year1,all_years,two_years]
        '''
        Q = Query()
        table = self.db.table('without_nodata')
        dict_years = table.search(Q.items == '项目')
        type_list = list(dict_years[0].keys())
        if ('year3' in type_list and 'year2' in type_list and
                'year1' in type_list and  'month' in type_list):
            return 'normal'
        elif ('year3' not in type_list and 'year2' in type_list and
                'year1' in type_list and 'month' in type_list):
            return 'no_year3'
        elif ('year3' not in type_list and 'year2' not in type_list and
                'year1' in type_list and 'month' in type_list):
            return 'no_year2'
        elif ('year3' not in type_list and 'year2' not in type_list and
                'year1' not in type_list and 'month' in type_list):
            return 'no_year1'
        elif ('year3' in type_list and 'year2' in type_list and
                'year1' in type_list and 'month' not in type_list):
            return 'all_years'
        elif ('year3' not in type_list and 'year2' in type_list and
                'year1' in type_list and 'month' not in type_list):
            return 'two_years'
        else:
            return '无法识别'

    def data(self,para_dict,text_key,item,key): # 在set函数中用来读取数据
        try:
            para_dict[text_key] = self.table.get(self.Q.items == item)[key]
        except Exception as error:
            para_dict[text_key] = 0

    def set(self):
        '''
        给变量赋值,不考虑智能分析文件的问题。
        :return: 变量赋值后的字典
        '''
        #第一段
        for key in self.s2d1:
            if key == '分析s2d1':
                pass
            else:
                self.data(self.s2d1, key,self.s2d1[key][0], self.s2d1[key][1])
        #第二段
        for key in self.s2d2:
            if key == '分析s2d2':
                pass
            else:
                self.data(self.s2d2, key,self.s2d2[key][0], self.s2d2[key][1])
        #第三段
        for key in self.s2d3:
            if key == '分析s2d3':
                pass
            else:
                self.data(self.s2d3, key,self.s2d3[key][0], self.s2d3[key][1])
        #第四段
        for key in self.s2d4:
            if key == '分析s2d4':
                pass
            elif key == '分析s2d4_经营':
                pass
            elif key == '分析s2d4_投资':
                pass
            elif key == '分析s2d4_筹资':
                pass
            else:
                self.data(self.s2d4, key,self.s2d4[key][0], self.s2d4[key][1])
        #第五段
        for key in self.s2d5:
            if key == '分析s2d5':
                pass
            else:
                self.data(self.s2d5, key,self.s2d5[key][0], self.s2d5[key][1])
        #第六段
        for key in self.s2d6:
            self.data(self.s2d6, key,self.s2d6[key][0], self.s2d6[key][1])

    def db_data(self,item , key): #从数据库读取值 在analysis系列函数中使用
        return self.table.get(self.Q.items == item)[key]
