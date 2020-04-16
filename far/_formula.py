#!/usr/bin/python
# -*- coding: utf-8 -*-
#__author__:"watalo"
# @Time: 2020/3/30 22:04
# @Site    : 
# @File    : _formula.py
# @Software: PyCharm

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Administrator
# datetime:2020/2/23 20:19
# software: PyCharm

from tinydb import Query

def formula(db, year, findex):

    db.all()
    Q = Query()

    def divd_(year, a, b):
        '''
        除法计算
        @param year:明确数据是哪年的
        @param a: 浮点数，直接调用db中的数据/ 其他公式的计算结果
        @param b: 浮点数，直接调用db中的数据/ 其他公式的计算结果
        @return: 结果
        '''
        if db.get(Q.items == a) in db.all():
            if db.get(Q.items == b) in db.all():
                return db.get(Q.items == a)[year] / db.get(Q.items == b)[year]
            else:
                return db.get(Q.items == a)[year] / b
        else:
            if db.get(Q.items == b) in db.all():
                return a / db.get(Q.items == b)[year]
            else:
                if b == 0:
                    return 0
                else:
                    return a / b

    def plus_(year, a, b):
        if db.get(Q.items == a) in db.all():
            if db.get(Q.items == b) in db.all():
                return db.get(Q.items == a)[year] + db.get(Q.items == b)[year]
            else:
                return db.get(Q.items == a)[year] + b
        else:
            if db.get(Q.items == b) in db.all():
                return a + db.get(Q.items == b)[year]
            else:
                return a + b

    def minu_(year, a, b):
        if db.get(Q.items == a) in db.all():
            if db.get(Q.items == b) in db.all():
                return db.get(Q.items == a)[year] - db.get(Q.items == b)[year]
            else:
                return db.get(Q.items == a)[year] - b
        else:
            if db.get(Q.items == b) in db.all():
                return a - db.get(Q.items == b)[year]
            else:
                return a - b

    if findex == '资产负债率':
        return divd_(year,
                     '负债合计',
                     '资产总计'
                     )

    elif findex == '流动比率':
        return divd_(year,
                     '流动资产合计',
                     '流动负债合计'
                     )

    elif findex == '速动比率':
        return divd_(year,
                     minu_(year,
                           '流动资产合计',
                           '存货'
                           ),
                     '流动负债合计'
                     )

    elif findex == 'EBIT':
        return plus_(year,
                     plus_(year,
                           '长期待摊费用',
                           '财务费用'
                           ),
                     '利润总额')

    elif findex == '利息保障倍数':
        return divd_(year,
                     plus_(year,
                           plus_(year,
                                 '长期待摊费用',
                                 '财务费用'),
                           '利润总额'
                           ),
                     '财务费用')

    elif findex == '营运资产':
        return plus_(year,
                     plus_(year,
                           '预付账款',
                           '其他应收款'
                           ),
                     '其他流动资产'
                     )

    elif findex == '营运负债':
        return plus_(year,
                     plus_(year, '预收账款', '应付账款'),
                     plus_(year, '应付职工薪酬', '应交税费')
                     )

    elif findex == '营运资金需求':
        return minu_(year,
                     plus_(year,
                           plus_(year, '预付账款', '其他应收款'), '其他流动资产'),
                     plus_(year,
                           plus_(year, '预收账款', '应付账款'),
                           plus_(year, '应付职工薪酬', '应交税费')
                           )
                     )

    elif findex == '营运资本':
        return minu_(year, '流动资产合计', '流动负债合计')

    elif findex == '存货周转天数':
        return 360 * divd_(year,
                           '存货',
                           '营业成本'
                           )

    elif findex == '应收账款周转天数':
        return 360 * divd_(year,
                           '应收账款',
                           '营业收入'
                           )

    elif findex == '毛利率':
        return divd_(year,
                     '营业利润',
                     '营业收入'
                     )

    elif findex == '净利润率':
        return divd_(year,
                     '净利润',
                     '营业收入'
                     )

    elif findex == '总资产收益率(ROA)':
        return divd_(year,
                     '净利润',
                     '资产总计'
                     )

    elif findex == '净资产收益率(ROE)':
        return divd_(year,
                     '净利润',
                     '所有者权益合计'
                     )

    elif findex == '短债占比':
        return divd_(year,
                     '流动负债合计',
                     '负债合计'
                     )

    elif findex == '刚性负债':
        return plus_(year,
                     plus_(year, '短期借款', '一年内到期的非流动负债'),
                     plus_(year, '长期借款', '应付债券',)
                     )

    elif findex == '刚兑占比':
        return divd_(year,
                     plus_(year,
                           plus_(year, '短期借款', '一年内到期的非流动负债'),
                           plus_(year, '长期借款', '应付债券', )
                           ),
                     '负债合计'
                     )

    elif findex == '短期刚兑':
        return plus_(year,
                     '短期借款',
                     '一年内到期的非流动负债'
                     )

    elif findex == '期间费用':
        return plus_(year,
                     plus_(year, '销售费用', '研发费用'),
                     plus_(year, '管理费用', '财务费用',)
                     )

    elif findex == '费用收入比':
        return divd_(year,
                     plus_(year,
                           plus_(year, '销售费用', '研发费用'),
                           plus_(year, '管理费用', '财务费用', )
                           ),
                     '营业收入'
                     )

    elif findex == '流动资产占比':
        return divd_(year,
                     '流动资产合计',
                     '资产总计'
                     )