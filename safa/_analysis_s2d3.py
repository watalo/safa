#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
# @Time: 2020/3/22 22:59
# @Site    :
# @File    : _analysis_s2d3.py
# @Software: PyCharm

"""
analysis_s2d3 mixin — 营业收入 / 净利润 趋势分析。

混到 dict_ 类里用,只依赖 self.db_data() / self.data_type / self.s2d3。
不改其他 dict。
"""


class AnalysisS2d3Mixin:
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

        elif self.data_type == 'no_year3':
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

        elif self.data_type == 'no_year2':
            # com1
            if self.db_data('营业收入', 'year1') > 0:
                com1 = '已实现销售收入'
            else:
                if self.db_data('净利润', 'year1') > 0:
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

        elif self.data_type == 'no_year1':
            com1 = '{:,.2f}'.format(self.db_data('营业收入','month'))
            com2 = '{:,.2f}'.format(self.db_data('净利润','month'))

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
