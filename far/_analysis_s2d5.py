#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
# @Time: 2020/3/22 22:59
# @Site    :
# @File    : _analysis_s2d5.py
# @Software: PyCharm

"""
analysis_s2d5 mixin — 资产构成 TOP 5 分析。

混到 dict_ 类里用,依赖 self.db_data() / self.data_type / self.s2d5 / self.sort_asset。
不改其他 dict。
"""


class AnalysisS2d5Mixin:
    def analysis_s2d5(self):
        commit = '%s，在总资产构成中的占比分别为%s'
        text_sorted_asset = ''
        text_sorted_ratio = ''
        if (self.data_type == 'normal' or self.data_type == 'no_year3' or self.data_type == 'no_year2' or
            self.data_type == 'all_years' or self.data_type == 'two_years'):
            text_sorted_asset = '、'.join(self.sort_asset('year1', 'items')[:5])
            sorted_ratio = []
            for value in self.sort_asset('year1', 'year1')[:5]:
                ratio = 100 * value / self.db_data('资产总计', 'year1')
                sorted_ratio.append('%.2f%%' % ratio)
            text_sorted_ratio = '、'.join(sorted_ratio)
        elif self.data_type == 'no_year1':
            text_sorted_asset = '、'.join(self.sort_asset('month', 'items')[:5])
            sorted_ratio = []
            for value in self.sort_asset('month', 'month')[:5]:
                ratio = 100 * value / self.db_data('资产总计', 'month')
                sorted_ratio.append('%.2f%%' % ratio)
            text_sorted_ratio = '、'.join(sorted_ratio)
        else:
            pass
        self.s2d5['分析s2d5'] = commit%(text_sorted_asset,text_sorted_ratio)

    def sort_asset(self, year, output):
        Item = self.table.search((self.Q.type == '流动资产') | (self.Q.type == '非流动资产'))
        list_sorted_dict = sorted(Item, key=lambda Item: Item[year], reverse=True)
        list_item = []
        for sorted_dict in list_sorted_dict:
            list_item.append(sorted_dict[output])
        return list_item
