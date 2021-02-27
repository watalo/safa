#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
# @Time: 2020/3/22 22:59
# @Site    : 
# @File    : _para.py
# @Software: PyCharm


import os
from tinydb import TinyDB ,Query
from . import _text
from . import _config


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
                     '净现金流入1':['现金净流入','year1'],
                     '经营活动现金净流入3':['经营活动净现金流入','year3'], '经营活动现金净流入2':['经营活动净现金流入','year2'],
                     '经营活动现金净流入1':['经营活动净现金流入','year1'],
                     '投资活动现金净流入3':['投资活动现金净流入','year3'], '投资活动现金净流入2':['投资活动现金净流入','year2'],
                     '投资活动现金净流入1':['投资活动现金净流入','year1'],
                     '筹资活动现金净流入3':['筹资活动现金净流入','year3'], '筹资活动现金净流入2':['筹资活动现金净流入','year2'],
                     '筹资活动现金净流入1':['筹资活动现金净流入','year1'],
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
        :return: 数据结构的类型[normal,no_3year,no_2year,no_1year,all_years,two_years]
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
            return 'no_3year'
        elif ('year3' not in type_list and 'year2' not in type_list and
                'year1' in type_list and 'month' in type_list):
            return 'no_2year'
        elif ('year3' not in type_list and 'year2' not in type_list and
                'year1' not in type_list and 'month' in type_list):
            return 'no_1year'
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

    # analysis系列函数对text中的需要做简单分析的部分进行处理
    def analysis_s2d1(self):
        commit = ''
        if self.data_type == 'normal':
            if (self.db_data('资产负债率','year3')<self.db_data('资产负债率','year2')<self.db_data('资产负债率', 'year1')
                    <self.db_data('资产负债率','month') ):
                commit = '逐年增加，有加大资本杠杆的趋势。'
            elif (self.db_data('资产负债率','year3')>self.db_data('资产负债率','year2')>self.db_data('资产负债率', 'year1')
                    >self.db_data('资产负债率','month') ):
                commit = '持续下降，资产负债结构有所改善。'
            elif (self.db_data('资产负债率','year3')==self.db_data('资产负债率','year2')==self.db_data('资产负债率', 'year1')
                    ==self.db_data('资产负债率','month')==0 ):
                commit = '一直为0，近三年及最近一期均无负债。'
            else:
                num = self.db_data('资产负债率','averg')
                commit = '在{:.2f}}上下波动，资产负债结构相对稳定。'.format(num)
        elif self.data_type == 'no_3year':
            if (self.db_data('资产负债率','year2')<self.db_data('资产负债率', 'year1')<self.db_data('资产负债率','month')):
                commit = '逐年增加，有加大资本杠杆的趋势。'
            elif (self.db_data('资产负债率','year2')>self.db_data('资产负债率', 'year1')>self.db_data('资产负债率','month')):
                commit = '持续下降，资产负债结构有所改善。'
            elif (self.db_data('资产负债率','year2')==self.db_data('资产负债率', 'year1')==self.db_data('资产负债率','month')==0 ):
                commit = '一直为0%，申请人近两年及最近一期均无负债。'
            else:
                num = self.db_data('资产负债率','averg')
                commit = '在{:.2f}}上下波动，资产负债结构相对稳定。'.format(num)
        elif self.data_type == 'no_2year':
            if (self.db_data('资产负债率', 'year1') < self.db_data('资产负债率', 'month')):
                commit = '有所增加，有加大资本杠杆的趋势。'
            elif (self.db_data('资产负债率', 'year1') > self.db_data('资产负债率', 'month')):
                commit = '有所下降，资产负债结构有所改善。'
            elif (self.db_data('资产负债率', 'year1') == self.db_data('资产负债率','month') == 0):
                commit = '一直为0，处于无负债状态。'
            else:
                pass
        elif self.data_type == 'no_1year':
            if self.db_data('资产负债率','month') >= 0.5:
                commit = '超过了50%。'
            else:
                commit = '低于50%，资产负债率相对较低。'
        elif self.data_type == 'all_years':
            if (self.db_data('资产负债率','year3')<self.db_data('资产负债率','year2')<self.db_data('资产负债率', 'year1')):
                commit = '逐年增加，有加大资本杠杆的趋势。'
            elif (self.db_data('资产负债率','year3')>self.db_data('资产负债率','year2')>self.db_data('资产负债率', 'year1')):
                commit = '持续下降，资产负债结构有所改善。'
            elif (self.db_data('资产负债率','year3')==self.db_data('资产负债率','year2')==self.db_data('资产负债率','year1')==0 ):
                commit = '申请人近三年均无负债。'
            else:
                num = self.db_data('资产负债率','averg')
                commit = '在{:.2f}}%上下波动，资产负债结构相对稳定。'.format(num)
        elif self.data_type == 'two_years':
            if (self.db_data('资产负债率','year2')<self.db_data('资产负债率', 'year1')):
                commit = '逐年增加，有加大资本杠杆的趋势。'
            elif (self.db_data('资产负债率','year2')>self.db_data('资产负债率', 'year1')):
                commit = '持续下降，资产负债结构有所改善。'
            elif self.db_data('资产负债率','year2')==self.db_data('资产负债率','year1')==0:
                commit = '申请人近两年均无负债。'
            else:
                num = self.db_data('资产负债率','averg')
                commit = '在{:.2f}}%上下波动，资产负债结构相对稳定。'.format(num)
        else:
            pass
        self.s2d1['分析s2d1'] = commit

    def analysis_s2d2(self):
        commit = ''
        if self.data_type == 'normal':
            # 极端情况：资产负债率始终为0
            if (self.db_data('资产负债率','year3')==self.db_data('资产负债率','year2')==self.db_data('资产负债率', 'year1')
                    ==self.db_data('资产负债率','month')==0 ):
                commit = '为零>>>请删除本段文字<<<'
            else:
                if self.db_data('短债占比','month') > 0.5:
                    commit = '以短期债务为主，流动负债占比高于50%。近三年及最新一期'
                elif self.db_data('短债占比','month') < 0.5:
                    commit = '以长期负债为主，非流动负债占比高于50%。近三年及最新一期'
                else:
                    commit = '期限结构均衡，流动负债占比等于50%。'
        elif self.data_type == 'no_3year':
            # 极端情况：资产负债率始终为0
            if (self.db_data('资产负债率','year2')==self.db_data('资产负债率', 'year1')
                    ==self.db_data('资产负债率','month')==0 ):
                commit = '为零>>>请删除本段文字<<<'
            else:
                if self.db_data('短债占比','month') > 0.5:
                    commit = '以短期债务为主，流动负债占比高于50%。近两年及最新一期'
                elif self.db_data('短债占比','month') < 0.5:
                    commit = '以长期负债为主，非流动负债占比高于50%。近两年及最新一期'
                else:
                    commit = '期限结构均衡，流动负债占比等于50%。'
        elif self.data_type == 'no_2year':
            # 极端情况：资产负债率始终为0
            if (self.db_data('资产负债率', 'year1') == self.db_data('资产负债率', 'month') == 0):
                commit = '为零>>>请删除本段文字<<<'
            else:
                if self.db_data('短债占比', 'month') > 0.5:
                    commit = '以短期债务为主，流动负债占比高于50%。上一年及最新一期'
                elif self.db_data('短债占比', 'month') < 0.5:
                    commit = '以长期负债为主，非流动负债占比高于50%。上一年及最新一期'
                else:
                    commit = '期限结构均衡，流动负债占比等于50%。'
        elif self.data_type == 'no_1year':
            # 极端情况：资产负债率始终为0
            if self.db_data('资产负债率', 'month') == 0:
                commit = '为零>>>请删除本段文字<<<'
            else:
                if self.db_data('短债占比', 'month') > 0.5:
                    commit = '以短期债务为主，流动负债占比高于50%。'
                elif self.db_data('短债占比', 'month') < 0.5:
                    commit = '以长期负债为主，非流动负债占比高于50%。'
                else:
                    commit = '期限结构均衡，流动负债占比等于50%。'
        elif self.data_type == 'all_years':
            # 极端情况：资产负债率始终为0
            if (self.db_data('资产负债率','year3')==self.db_data('资产负债率','year2')
                    ==self.db_data('资产负债率', 'year1')==0 ):
                commit = '为零>>>请删除本段文字<<<'
            else:
                if self.db_data('短债占比','year1') > 0.5:
                    commit = '以短期债务为主，流动负债占比高于50%。近三年'
                elif self.db_data('短债占比','year1') < 0.5:
                    commit = '以长期负债为主，非流动负债占比高于50%。近三年'
                else:
                    commit = '期限结构均衡，流动负债占比等于50%。'
        elif self.data_type == 'two_years':
            # 极端情况：资产负债率始终为0
            if (self.db_data('资产负债率', 'year2') == self.db_data('资产负债率', 'year1') == 0):
                commit = '为零>>>请删除本段文字<<<'
            else:
                if self.db_data('短债占比', 'year1') > 0.5:
                    commit = '以短期债务为主，流动负债占比高于50%。近两年'
                elif self.db_data('短债占比', 'year1') < 0.5:
                    commit = '以长期负债为主，非流动负债占比高于50%。近两年'
                else:
                    commit = '期限结构均衡，流动负债占比等于50%。'

        else:
            pass
        self.s2d2['分析s2d2'] = commit

    def analysis_s2d3(self):
        commit = '营业收入{com1}，盈利能力{com2}'

        if self.data_type == 'normal':
            # com1
            com1 = ''
            if self.db_data('营业收入','year3') == self.db_data('营业收入','year2') == self.db_data('营业收入','year1') == 0:
                commit = '连续三年未实现销售收入。'
            else:
                if 0 < self.db_data('营业收入','year3') < self.db_data('营业收入','year2'):
                    if self.db_data('营业收入','year2') < self.db_data('营业收入','year1'):
                        tag = (self.db_data('营业收入','year1') - self.db_data('营业收入','year3'))/self.db_data('营业收入','year3')
                        ave = tag/2
                        com1 = '持续三年增长，平均增长率为{:,.2%}'.format(ave)
                    elif self.db_data('营业收入','year2') > self.db_data('营业收入','year1'):
                        com1 = '出现波动，最近一年营收出现回落'
                    else:
                        com1 = '近来年相对稳定，相比前三年营收有所提升'
                elif self.db_data('营业收入','year3') > self.db_data('营业收入','year2'):
                    if self.db_data('营业收入','year2') > self.db_data('营业收入','year1'):
                        tag = (self.db_data('营业收入','year3') - self.db_data('营业收入','year1'))/self.db_data('营业收入','year1')
                        ave = tag/2
                        com1 = '持续三年下降，平均降幅为{:,.2%}'.format(ave)
                    elif self.db_data('营业收入','year2') < self.db_data('营业收入','year1'):
                        com1 = '出现波动，但最近一年营收有所回升'
                    else:
                        com1 = '近来年相对稳定，相比前三年营收有所回落'
            # com2
            if self.db_data('净利润','month') > 0:
                if (self.db_data('净利润','year3') < self.db_data('净利润','year2')
                        < self.db_data('净利润','year1') < self.db_data('净利润','month')):
                    com2 = '逐年提升'
                elif (self.db_data('净利润','year3') > self.db_data('净利润','year2')
                        > self.db_data('净利润','year1') > self.db_data('净利润','month')):
                    com2 = '逐年下降'
                else:
                    com2 = '有所波动'
            else:
                com2 = '较弱，出现亏损情况'

        elif self.data_type == 'no_3year':
            # com1
            if self.db_data('营业收入', 'year2') == self.db_data('营业收入', 'year1') == 0:
                commit = '连续两年未实现销售收入。'
            else:
                if 0 < self.db_data('营业收入', 'year2'):
                    if self.db_data('营业收入', 'year2') < self.db_data('营业收入', 'year1'):
                        tag = (self.db_data('营业收入', 'year1') - self.db_data('营业收入', 'year2')) / self.db_data('营业收入','year2')
                        ave = tag
                        com1 = '持续两年增长，增长率为{:,.2%}'.format(ave)
                    elif self.db_data('营业收入', 'year2') > self.db_data('营业收入', 'year1'):
                        com1 = '出现波动，最近一年营收出现回落'
                    else:
                        com1 = '近来年相对稳定'
            # com2
            if self.db_data('净利润', 'month') >= 0:
                if (self.db_data('净利润', 'year2') < self.db_data('净利润', 'year1') < self.db_data('净利润', 'month')):
                    com2 = '逐年提升'
                elif (self.db_data('净利润', 'year2') > self.db_data('净利润', 'year1') > self.db_data('净利润', 'month')):
                    com2 = '逐年下降'
                else:
                    com2 = '有所波动'
            else:
                com2 = '较弱，出现亏损情况'

        elif self.data_type == 'no_2year':
            # com1
            if self.db_data('营业收入', 'year1') > 0:
                com1 = '已实现销售收入'
            else:
                if self.db_data('营业收入', 'month') > 0:
                    com1 = '连续实现销售收入'
                else:
                    com1 = '不稳定，较难判断'
            # com2
            if self.db_data('净利润', 'month') >= 0:
                if self.db_data('净利润', 'year1') <= self.db_data('净利润', 'month'):
                    com2 = '逐渐提升'
                else:
                    com2 = '有所下降'
            else:
                com2 = '较弱，出现亏损情况'

        elif self.data_type == 'no_1year':
            com1 = '{:,.f}'.format(self.db_data('营业收入','month'))
            com2 = '{:,.f}'.format(self.db_data('净利润','month'))

        elif self.data_type == 'all_years':
            # com1
            com1 = ''
            if self.db_data('营业收入','year3') == self.db_data('营业收入','year2') == self.db_data('营业收入','year1') == 0:
                commit = '连续三年未实现销售收入。'
            else:
                if 0 < self.db_data('营业收入','year3') < self.db_data('营业收入','year2'):
                    if self.db_data('营业收入','year2') < self.db_data('营业收入','year1'):
                        tag = (self.db_data('营业收入','year1') - self.db_data('营业收入','year3'))/self.db_data('营业收入','year3')
                        ave = tag/2
                        com1 = '持续三年增长，平均增长率为{:,.2%}'.format(ave)
                    elif self.db_data('营业收入','year2') > self.db_data('营业收入','year1'):
                        com1 = '出现波动，最近一年营收出现回落'
                    else:
                        com1 = '近来年相对稳定，相比前三年营收有所提升'
                elif self.db_data('营业收入','year3') > self.db_data('营业收入','year2'):
                    if self.db_data('营业收入','year2') > self.db_data('营业收入','year1'):
                        tag = (self.db_data('营业收入','year3') - self.db_data('营业收入','year1'))/self.db_data('营业收入','year1')
                        ave = tag/2
                        com1 = '持续三年下降，平均降幅为{:,.2%}'.format(ave)
                    elif self.db_data('营业收入','year2') < self.db_data('营业收入','year1'):
                        com1 = '出现波动，但最近一年营收有所回升'
                    else:
                        com1 = '近来年相对稳定，相比前三年营收有所回落'
            # com2
            if self.db_data('净利润','year1') >= 0:
                if (self.db_data('净利润','year3') < self.db_data('净利润','year2')
                        < self.db_data('净利润','year1')):
                    com2 = '逐年提升'
                elif (self.db_data('净利润','year3') > self.db_data('净利润','year2')
                        > self.db_data('净利润','year1')):
                    com2 = '逐年下降'
                else:
                    com2 = '有所波动'
            else:
                com2 = '较弱，出现亏损情况'

        elif self.data_type == 'two_years':
            # com1
            com1 = ''
            if self.db_data('营业收入','year2') == self.db_data('营业收入','year1') == 0:
                commit = '连续两年未实现销售收入。'
            elif self.db_data('营业收入','year2') < self.db_data('营业收入','year1'):
                pass
            elif self.db_data('营业收入','year2') > self.db_data('营业收入','year1'):
                pass
            # com2
            if self.db_data('净利润','year1') >= 0:
                if self.db_data('净利润','year2') < self.db_data('净利润','year1'):
                    com2 = '较上年有所提升'
                elif self.db_data('净利润','year2') > self.db_data('净利润','year1'):
                    com2 = '较上年有所下降'
                else:
                    com2 = '保持不变'
            else:
                com2 = '较弱，出现亏损情况'

        self.s2d3['分析s2d3'] = commit.format(com1=com1,com2=com2)

    def sort_asset(self, year, output):
        Item = self.table.search((self.Q.type == '流动资产') | (self.Q.type == '非流动资产'))
        list_sorted_dict = sorted(Item, key=lambda Item: Item[year], reverse=True)
        list_item = []
        for sorted_dict in list_sorted_dict:
            list_item.append(sorted_dict[output])
        return list_item

    def analysis_s2d5(self):
        commit = '%s，在总资产构成中的占比分别为%s'
        text_sorted_asset = ''
        text_sorted_ratio = ''
        if (self.data_type == 'normal' or self.data_type == 'no_3year' or self.data_type == 'no_2year' or
            self.data_type == 'all_years' or self.data_type == 'two_years'):
            text_sorted_asset = '、'.join(self.sort_asset('year1', 'items')[:5])
            sorted_ratio = []
            for value in self.sort_asset('year1', 'year1')[:5]:
                ratio = 100 * value / self.db_data('资产总计', 'year1')
                sorted_ratio.append('%.2f%%' % ratio)
            text_sorted_ratio = '、'.join(sorted_ratio)
        elif self.data_type == 'no_1year':
            text_sorted_asset = '、'.join(self.sort_asset('month', 'items')[:5])
            sorted_ratio = []
            for value in self.sort_asset('month', 'month')[:5]:
                ratio = 100 * value / self.db_data('资产总计', 'month')
                sorted_ratio.append('%.2f%%' % ratio)
            text_sorted_ratio = '、'.join(sorted_ratio)
        else:
            pass
        self.s2d5['分析s2d5'] = commit%(text_sorted_asset,text_sorted_ratio)

# if __name__ == '__main__':
#
#     dict_ = dict_()
#     dict_.set()
#     dict_.analysis_s2d1()
#     dict_.analysis_s2d2()
#     dict_.analysis_s2d3()
#     dict_.analysis_s2d5()
#
#     # print(dict_.s2d5)
#
#     doc1 = _text.no_year3().s2d1
#     doc2 = _text.no_year3().s2d2
#     doc3 = _text.no_year3().s2d3
#     doc4 = _text.no_year3().s2d4
#     doc5 = _text.no_year3().s2d5
#
#     a = doc1.format(**dict_.s2d1)
#     b = doc2.format(**dict_.s2d2)
#     c = doc3.format(**dict_.s2d3)
#     d = doc4.format(**dict_.s2d4)
#     e = doc5.format(**dict_.s2d5)
#
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#     print(e)





