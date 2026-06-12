#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
# @Time: 2020/3/22 22:59
# @Site    :
# @File    : _analysis_s2d1.py
# @Software: PyCharm

"""
analysis_s2d1 mixin — 资产负债率趋势分析。

混到 dict_ 类里用,只依赖 self.db_data() / self.data_type / self.s2d1。
不改其他 dict。
"""


class AnalysisS2d1Mixin:
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
                commit = '在{:.2f}上下波动，资产负债结构相对稳定。'.format(num)
        elif self.data_type == 'no_year3':
            if (self.db_data('资产负债率','year2')<self.db_data('资产负债率', 'year1')<self.db_data('资产负债率','month')):
                commit = '逐年增加，有加大资本杠杆的趋势。'
            elif (self.db_data('资产负债率','year2')>self.db_data('资产负债率', 'year1')>self.db_data('资产负债率','month')):
                commit = '持续下降，资产负债结构有所改善。'
            elif (self.db_data('资产负债率','year2')==self.db_data('资产负债率', 'year1')==self.db_data('资产负债率','month')==0 ):
                commit = '一直为0%，申请人近两年及最近一期均无负债。'
            else:
                num = self.db_data('资产负债率','averg')
                commit = '在{:.2f}上下波动，资产负债结构相对稳定。'.format(num)
        elif self.data_type == 'no_year2':
            if (self.db_data('资产负债率', 'year1') < self.db_data('资产负债率', 'month')):
                commit = '有所增加，有加大资本杠杆的趋势。'
            elif (self.db_data('资产负债率', 'year1') > self.db_data('资产负债率', 'month')):
                commit = '有所下降，资产负债结构有所改善。'
            elif (self.db_data('资产负债率', 'year1') == self.db_data('资产负债率','month') == 0):
                commit = '一直为0，处于无负债状态。'
            else:
                pass
        elif self.data_type == 'no_year1':
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
                commit = '在{:.2f}%上下波动，资产负债结构相对稳定。'.format(num)
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
