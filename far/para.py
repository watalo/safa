#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
# @Time: 2020/3/22 22:59
# @Site    : 
# @File    : para.py
# @Software: PyCharm


import os
from tinydb import TinyDB ,Query
import text
import _config

'''
1 判断数据结构的年份构成
    normal
    no_3year
    no_2year
    no_1year
    all_years
2 对text类中的text进行匹配
    2.1 可直接读取的数据
        从数据中读取    
    2.2 需进行分析的文字
        直接形成分析结果，按字符串形式存储
'''

class dict_:
    '''
    设定变量字典
    '''
    def __init__(self):
        self.db_path = _config.Path.db
        self.db_file_path = '\\'.join([self.db_path, os.listdir(self.db_path)[0]])
        # print(db_file_path)
        self.db = TinyDB(self.db_file_path)
        self.db_path = _config.Path.db.listdir()[0]
        self.table = TinyDB(self.db_path).table('without_nodata')
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
                     '短期刚兑m': ['短期刚兑','month'],
                     '短期借款m': ['短期借款','month'],
                     '一年内非流m': ['一年内到期的非流动负债','month'],
                     }
        self.s2d3 = {'营业收入3': ['营业收入','year3'], '营业收入2': ['营业收入','year2'],
                     '营业收入1': ['营业收入','year1'], '分析s2d3':str(),
                     '营业成本3': ['营业成本','year3'], '营业成本2': ['营业成本','year2'],
                     '营业成本1': ['营业成本','year1'],
                     '毛利率3': ['毛利率','year3'], '毛利率2':['毛利率','year2'], '毛利率1':['毛利率','year1'],
                     '期间费用3': ['期间费用','year3'], '期间费用2': ['期间费用','year2'], '期间费用1': ['期间费用','year1'],
                     '费用收入比3': ['费用收入比','year3'], '费用收入比2': ['费用收入比','year2'], '费用收入比1': ['费用收入比','year1'],
                     '净利润3': ['净利润','year3'], '净利润2': ['净利润','year2'], '净利润1': ['净利润','year1'],
                     '净利润率3': ['净利润率','year3'], '净利润率2': ['净利润率','year2'], '净利润率1': ['净利润率','year1'],
                     '营业收入m':['营业收入','month'], '营业成本m':['营业成本','month'], '毛利率m':['毛利率','month'],
                     '期间费用m':['期间费用','month'], '投资收益m':['投资收益','month'], '净利润率m':['净利润率','month'],
                     }
        self.s2d4 = {'净现金流入3':['现金净流入','year3'], '净现金流入2':['现金净流入','year2'],
                     '净现金流入1':['现金净流入','year1'], '分析s2d4':str(),
                     '经营活动现金净流入3':['经营活动净现金流','year3'], '经营活动现金净流入2':['经营活动净现金流','year2'],
                     '经营活动现金净流入1':['经营活动净现金流','year1'],
                     '分析s2d4_经营':str(),
                     '投资活动现金净流入3':['投资活动现金净流','year3'], '投资活动现金净流入2':['投资活动现金净流','year2'],
                     '投资活动现金净流入1':['投资活动现金净流','year1'],
                     '分析s2d4_投资':str(),
                     '筹资活动现金净流入3':['筹资活动现金净流入','year3'], '筹资活动现金净流入2':['筹资活动现金净流入','year2'],
                     '筹资活动现金净流入1':['筹资活动现金净流入','year1'],
                     '分析s2d4_筹资':str(),
                     }
        self.s2d5 = {'流动资产3':['流动资产合计','year3'], '流动资产2':['流动资产合计','year2'],
                     '流动资产1':['流动资产合计','year1'], '流动资产m':['流动资产合计','month'],
                     '流动资产占比3':['流动资产占比','year3'], '流动资产2占比':['流动资产占比','year2'],
                     '流动资产占比1':['流动资产占比','year1'], '流动资产占比m':['流动资产占比','month'],
                     '分析s2d5':str(),
                     }
        self.s2d6 = {'流动比率3':['流动比率','year3'], '流动比率2':['流动比率','year2'],
                     '流动比率1':['流动比率','year1'], '流动比率m':['流动比率','month'],
                     '流动比率av':['流动比率','averg'], '流动比率delta':['流动比率','delta'],
                     '速动比率3':['流动比率','year3'], '速动比率2':['流动比率','year2'],
                     '速动比率1':['流动比率','year1'], '速动比率m':['流动比率','month'],
                     '速动比率av':['流动比率','averg'], '速动比率delta':['流动比率','delta'],
                      }

    @property
    def _type(self):
        '''
        判断数据类型
        :return: 数据结构的类型[normal,no_3year,no_2year,no_1year,all_years]
        '''
        Q = Query()
        table = self.db.table('without_nodata')
        dict_years = table.search(Q.items == '项目')
        type_list = list(dict_years[0].keys())
        if ('year3' in type_list and
                'year2' in type_list and
                'year1' in type_list and
                'month' in type_list):
            return 'normal'
        elif ('year3' not in type_list and
                'year2' in type_list and
                'year1' in type_list and
                'month' in type_list):
            return 'no_3year'
        elif ('year3' not in type_list and
                'year2' not in type_list and
                'year1' in type_list and
                'month' in type_list):
            return 'no_2year'
        elif ('year3' not in type_list and
                'year2' not in type_list and
                'year1' not in type_list and
                'month' in type_list):
            return 'no_1year'
        elif ('year3' in type_list and
                'year2' in type_list and
                'year1' in type_list and
                'month' not in type_list):
            return 'all_years'
        else:
            return '无法识别'

    def data(self,para_dict,text_key,item,key):
        try:
            para_dict[text_key] = self.table.get(self.Q.items == item)[key]
        except Exception as error:
            para_dict[text_key] = 0

    def set(self):
        '''
        给变量赋值
        :return: 变量赋值后的字典
        '''
        pass








if __name__ == '__main__':
    db_path = _config.Path.db
    db_file_path = '\\'.join([db_path, os.listdir(db_path)[0]])
    # print(db_file_path)
    db = TinyDB(db_file_path)
    table = db.table('without_nodata')
    Q = Query()

    s2d1 = {'总资产3': ['资产总计', 'year3'],
            '总资产2': ['资产总计', 'year2'],
            '总资产1': ['资产总计', 'year1'],
            '总资产m': ['资产总计', 'month'],}

    def set_data(para_dict, text_key, item, key):
        try:
            para_dict[text_key] = table.get(Q.items == item)[key]
        except Exception as error:
            para_dict[text_key] = 0

    for k in s2d1:
        set_data(s2d1, k, s2d1[k][0], s2d1[k][1])

    print(s2d1)







