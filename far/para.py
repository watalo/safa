#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
# @Time: 2020/3/22 22:59
# @Site    : 
# @File    : para.py
# @Software: PyCharm


import os
from tinydb import TinyDB,Query
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
        self.db_path = _config.Path.db.listdir()[0]
        self.db = TinyDB(self.db_path)
        self.s2d1 = {'总资产3': float(), '总资产2': float(), '总资产1': float(), '总资产m': float(),
                     '总负债3': float(), '总负债2': float(), '总负债1': float(), '总负债m': float(),
                     '资产负债率3': float(), '资产负债率2':float(), '资产负债率1':float(), '资产负债率m':float(),
                     '分析s2d1':str(),
                     }
        self.s2d2 = {'分析s2d2': str(),
                     '流动负债3': float(), '流动负债2': float(), '流动负债1': float(), '流动负债m': float(),
                     '短债占比3': float(), '短债占比2': float(), '短债占比1': float(), '短债占比m': float(),
                     '刚性负债3': float(), '刚性负债2': float(), '刚性负债1': float(), '刚性负债m': float(),
                     '刚性兑付占比3': float(), '刚性兑付占比2': float(), '刚性兑付占比1': float(), '刚性兑付占比m': float(),
                     '短期刚兑m': float(), '短期借款m': float(), '一年内非流m': float(),
                     }
        self.s2d3 = {'营业收入3':float(), '营业收入2':float(), '营业收入1':float(),
                     '分析s2d3':str(),
                     '营业成本3':float(), '营业成本2':float(), '营业成本1':float(),
                     '毛利率3':float(), '毛利率2':float(), '毛利率1':float(),
                     '期间费用3':float(), '期间费用2':float(), '期间费用1':float(),
                     '费用收入比3':float(), '费用收入比2':float(), '费用收入比1':float(),
                     '净利润3':float(), '净利润2':float(), '净利润1':float(),
                     '净利润率3':float(), '净利润率2':float(), '净利润率1':float(),
                     '营业收入m':float(), '营业成本m':float(), '毛利率m':float(),
                     '期间费用m':float(), '投资收益m':float(), '净利润率m':float(),
                     }
        self.s2d4 = {'净现金流入3':float(), '净现金流入2':float(), '净现金流入1':float(), '分析s2d4':str(),
                     '经营活动现金净流入3':float(), '经营活动现金净流入2':float(), '经营活动现金净流入1':float(),
                     '分析s2d4_经营':str(),
                     '投资活动现金净流入3':float(), '投资活动现金净流入2':float(), '投资活动现金净流入1':float(),
                     '分析s2d4_投资':str(),
                     '筹资活动现金净流入3':float(), '筹资活动现金净流入2':float(), '筹资活动现金净流入1':float(),
                     '分析s2d4_筹资':str(),
                     }
        self.s2d5 = {'流动资产3':float(), '流动资产2':float(), '流动资产1':float(), '流动资产m':float(),
                     '流动资产占比3':float(), '流动资产2占比':float(), '流动资产占比1':float(), '流动资产占比m':float(),
                     '分析s2d5':str(),
                     }
        self.s2d6 = {'流动比率3':float(), '流动比率2':float(), '流动比率1':float(),
                     '流动比率m':float(), '流动比率av':float(), '流动比率delta':float(),
                     '速动比率3':float(), '速动比率2':float(), '速动比率1':float(),
                     '速动比率m':float(), '速动比率av':float(), '速动比率delta':float(),
                      }

    @property
    def _type(self):
        '''
        判断数据类型
        :return:
        '''
        # Q = Query()
        # db = self.db.table('without_nodata')




        pass

    def report(self):
        '''
        根据数据年份类型执行文件
        :return:
        '''
        pass


if __name__ == '__main__':

    db_path = _config.Path.db
    db_file_path = '\\'.join([db_path,os.listdir(db_path)[0]])
    print(db_file_path)
    db = TinyDB(db_file_path)
    Q = Query()
    table = db.table('without_nodata')
    dict_years = table.search(Q.items == '项目')
    print(dict_years[0])