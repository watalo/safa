#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
# @Time: 2020/3/22 22:59
# @Site    :
# @File    : _analysis_s2d2.py
# @Software: PyCharm

"""
analysis_s2d2 mixin — 短债 / 长债期限结构分析。

混到 dict_ 类里用,只依赖 self.db_data() / self.data_type / self.s2d2。
不改其他 dict。
"""


class AnalysisS2d2Mixin:
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
        elif self.data_type == 'no_year3':
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
        elif self.data_type == 'no_year2':
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
        elif self.data_type == 'no_year1':
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
