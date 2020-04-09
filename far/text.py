#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__:"watalo"
# @Time: 2020/3/19 0:33
# @Site    : 
# @File    : text.py
# @Software: PyCharm
'''
使用self.normal.s2d1.format(**self.normal.s2d1_dict)给模版传入数据
财务分析的文字模版
    1.数据完整: normal
    2. 缺少第一年数据   no_year3
    3. 缺少第二年数据   no_year2
    4. 缺少第三年数据   no_year1
    5. 当期为年末数据   all_years
'''

# TODO：对目标字符串的格式进行设定

class normal:

    def __init__(self):
        self.table1 = None
        # 1、审计情况分析
        self.s1d1 = \
            "【XXX会计师事务所】对申请人前三年的财务数据出具了编号为【】、【】、【】的审计报告，均出具了无保留意见。" \
            "其中，【年】对【科目】进行了如下调整：【请仔细阅读审计报告后填写】。"
        # 2、资本结构
        self.s2d1 = \
            "申请人近三年及最近一期的" \
            "总资产分别为{总资产3:,.2f}万元、{总资产2:,.2f}万元、{总资产1:,.2f}万元和{总资产m:,.2f}万元；" \
            "总负债分别为{总负债3:,.2f}万元、{总负债2:,.2f}万元、{总负债1:,.2f}万元和{总负债m:,.2f}万元；" \
            "资产负债率分别为{资产负债率3:.2%}、{资产负债率2:.2%}、{资产负债率1:.2%}和{资产负债率m:.2%}。" \
            "整体来看，申请人资产负债率{分析s2d1}"  # 13个变量

        self.s2d2 = \
            '从债务期限结构看，申请人债务{分析s2d2}，' \
            '流动负债分别为{流动负债3:,.2f}万元、{流动负债2:,.2f}万元、{流动负债1:,.2f}万元和{流动负债m:,.2f}万元，' \
            '短期负债占比分别为{短债占比3:.2%}、{短债占比2:.2%}、{短债占比1:.2%}和{短债占比m:.2%}。' \
            '刚性负债(短期借款+一年内到期的长期负债+应付债券+长期借款)分别为{刚性负债3:,.2f}万元、{刚性负债2:,.2f}万元、{刚性负债1:,.2f}万元和{刚性负债m:,.2f}万元。' \
            '刚性负债占比分别为{刚性兑付占比3:.2%}、{刚性兑付占比2:.2%}、{刚性兑付占比1:.2%}和{刚性兑付占比m:.2%}。' \
            '短期内需要刚性兑付的债务为{短期刚兑m:,.2f}万元，主要为短期借款{短期借款m:,.2f}万元，一年内到期的非流动负债{一年内非流m:,.2f}万元。' \
            '总体来看，公司刚性债务带来的偿债压力【较大\在合理范围内\较小，根据实际情况自行评价】。'  # 21个变量

        # 3、盈利能力
        self.s2d3 = \
            "申请人{分析s2d3}，前三年分别实现营业收入{营业收入3:,.2f}万元、{营业收入2:,.2f}万元和{营业收入1:,.2f}万元，" \
            "营业成本{营业成本3:,.2f}万元、{营业成本2:,.2f}万元和{营业成本1:,.2f}万元，毛利率分别为{毛利率3:.2%}、{毛利率2:.2%}和{毛利率1:.2%}，" \
            "期间费用分别为{期间费用3:,.2f}万元、{期间费用2:,.2f}万元和{期间费用1:,.2f}万元，费用收入比分别为{费用收入比3:.2%}、{费用收入比2:.2%}和{费用收入比1:.2%}。" \
            "实现净利润{净利润3:,.2f}万元、{净利润2:,.2f}万元和{净利润1:,.2f}万元，净利润率分别为{净利润率3:.2%}、{净利润率2:.2%}和{净利润率1:.2%}，" \
            "最近一期，申请人实现营业收入{营业收入m:,.2f}万元，营业成本{营业成本m:,.2f}万元，毛利率{毛利率m:.2%}，" \
            "期间费用合计{期间费用m:,.2f}万元，投资收益{投资收益m:,.2f}万元，净利润率{净利润率m:.2%}。" \
            "总体来看，申请人盈利能力【相对较好/稳定/较弱，根据实际情况自行评价】"  # 28个变量

        # 4、现金流量
        self.s2d4 = \
            "申请人前三年分别实现净现金流入{净现金流入3:,.2f}万元、{净现金流入2:,.2f}万元和{净现金流入1:,.2f}万元。其中：" \
            "经营活动现金净流入{经营活动现金净流入3:,.2f}万元、{经营活动现金净流入2:,.2f}万元和{经营活动现金净流入1:,.2f}万元；" \
            "投资活动现金净流入{投资活动现金净流入3:,.2f}万元、{投资活动现金净流入2:,.2f}万元和{投资活动现金净流入1:,.2f}万元；" \
            "筹资活动现金净流入{筹资活动现金净流入3:,.2f}万元、{筹资活动现金净流入2:,.2f}万元和{筹资活动现金净流入1:,.2f}万元。" \
            "总体来看，申请人盈利能力【请根据实际情况自行评价】"  # 16个变量

        # 5、资产质量
        self.s2d5 = \
            "申请人近三年流动资产分别为{流动资产3:,.2f}万元、{流动资产2:,.2f}万元、{流动资产1:,.2f}万元和{流动资产m:,.2f}万元，" \
            "在总资产构成中流动资产占比分别{流动资产占比3:.2%}、{流动资产占比2:.2%}、{流动资产占比1:.2%}和{流动资产占比m:.2%}，【>>>简要分析<<<】。" \
            "上年末，主要资产构成为{分析s2d5}。【请根据实际情况自行评价】。"  # 9个变量

        # 6、流动性分析
        self.s2d6 = \
            "申请人近三年及最近一期流动比率分别为{流动比率3:.2%}、{流动比率2:.2%}、{流动比率1:.2%}和{流动比率m:.2%}，三年平均值为{流动比率av:.2%}，" \
            "较年初变化{流动比率delta}个百分点；" \
            "申请人近三年及最近一期速动比率分别为{速动比率3:.2%}、{速动比率2:.2%}、{速动比率1:.2%}和{速动比率m:.2%}，三年平均值为{速动比率av:.2%}，" \
            "较年初变化{速动比率delta}个百分点。" \
            "【请根据实际情况自行评价】。"  # 12个变量

        # 7、当期科目变化情况（变化超过30%）
        # 直接在core中调用

class no_year3:
    def __init__(self):
        self.table1 =float()
        # 1、审计情况分析
        self.s1d1 = \
            "【XXX会计师事务所】对申请人前三年的财务数据出具了编号为【】、【】的审计报告，均出具了无保留意见。" \
            "其中，【年】对【科目 】进行了如下调整：【请仔细阅读审计报告后填写】。"
        # 2、资本结构
        self.s2d1 = \
            "申请人近两年及最近一期的" \
            "总资产分别为{总资产2:,.2f}万元、{总资产1:,.2f}万元和{总资产m:,.2f}万元；" \
            "总负债分别为{总负债2:,.2f}万元、{总负债1:,.2f}万元和{总负债m:,.2f}万元；" \
            "资产负债率分别为{资产负债率2:.2%}、{资产负债率1:.2%}和{资产负债率m:.2%}。" \
            "整体来看，申请人资产负债率{分析s2d1}"  # 10个变量

        self.s2d2 = \
            "从债务期限结构看，申请人债务{分析s2d2}，" \
            "流动负债分别为{流动负债2:,.2f}万元、{流动负债1:,.2f}万元和{流动负债m:,.2f}万元，" \
            "短期负债占比分别为{短债占比2:.2%}、{短债占比1:.2%}和{短债占比m:.2%}。" \
            "刚性负债(短期借款+一年内到期的长期负债+应付债券+长期借款)分别为{刚性负债2:,.2f}、{刚性负债1:,.2f}和{刚性负债m:,.2f}," \
            "刚性负债占比分别为{刚性兑付占比2:.2%}、{刚性兑付占比1:.2%}和{刚性兑付占比m:.2%}。" \
            "短期内需要刚性兑付的债务为{短期刚兑m:.2f}万元，主要为短期借款{短期借款m:,.2f}万元，一年内到期的非流动负债{一年内非流m:,.2f}万元。" \
            "总体来看，公司刚性债务带来的偿债压力【较大\在合理范围内\较小，根据实际情况自行评价】。"  # 16个变量

        # 3、盈利能力
        self.s2d3 = \
            "申请人前两年分别实现营业收入{营业收入2:,.2f}万元和{营业收入1:,.2f}万元，{分析s2d3}。" \
            "营业成本{营业成本2}万元和{营业成本1:,.2f}万元，毛利率分别为{毛利率3:.2%}、{毛利率2:.2%}和{毛利率1:.2%}，" \
            "期间费用分别为{期间费用2:,.2f}万元和{期间费用1:,.2f}万元，费用收入比分别为{费用收入比2:.2%}和{费用收入比1:.2%}。" \
            "实现净利润{净利润2:,.2f}万元和{净利润1:,.2f}万元，净利润率分别为{净利润率2:.2%}和{净利润率1:.2%}，" \
            "最近一期，申请人实现营业收入{营业收入m:,.2f}万元，营业成本{营业成本m:,.2f}万元，毛利率{毛利率m:.2%}，" \
            "期间费用合计{期间费用m:,.2f}万元，投资收益{投资收益m:,.2f}万元，净利润率{净利润率m:.2%}。" \
            "总体来看，申请人盈利能力【相对较好/稳定/较弱，根据实际情况自行评价】"  # 21个变量

        # 4、现金流量
        self.s2d4 = \
            "申请人前两年分别实现净现金流入{净现金流入2:,.2f}万元和{净现金流入1:,.2f}万元。其中：" \
            "经营活动现金净流入{经营活动现金净流入2:,.2f}万元和{经营活动现金净流入1:,.2f}万元；" \
            "投资活动现金净流入{投资活动现金净流入2:,.2f}万元和{投资活动现金净流入1:,.2f}万元；" \
            "筹资活动现金净流入{筹资活动现金净流入2:,.2f}万元和{筹资活动现金净流入1:,.2f}万元。" \
            "总体来看，申请人盈利能力【请根据实际情况自行评价】"  # 16个变量

        # 5、资产质量
        self.s2d5 = \
            "申请人近两年流动资产分别为{流动资产2:,.2f}万元、{流动资产1:,.2f}万元和{流动资产m:,.2f}万元，" \
            "在总资产构成中流动资产占比分别{流动资产占比2:.2%}、{流动资产占比1:.2%}和{流动资产占比m:.2%}，【>>>简要分析<<<】。" \
            "上年末，主要资产构成为{分析s2d5}。【请根据实际情况自行评价】。"  # 9个变量

        # 6、流动性分析
        self.s2d6 = \
            "申请人近两年及最近一期流动比率分别为{流动比率2:.2%}、{流动比率1:.2%}和{流动比率m:.2%}，平均值为{流动比率av:.2%}，" \
            "较年初变化{流动比率delta}个百分点；" \
            "申请人近两年及最近一期速动比率分别为{速动比率2:.2%}、{速动比率1:.2%}和{速动比率m:.2%}，平均值为{速动比率av:.2%}，" \
            "较年初变化{速动比率delta}个百分点。" \
            "【请根据实际情况自行评价】。"  # 12个变量

        # 7、当期科目变化情况（变化超过30%）
        # 直接在core中调用

class no_year2:
    def __init__(self):
        self.table1 =float()
        # 1、审计情况分析
        self.s1d1 = \
            "【XXX会计师事务所】出具了编号为【】的无保留意见的审计报告。" \
            "其中，【年】对【科目 】进行了如下调整：【请仔细阅读审计报告后填写】。"
        # 2、资本结构
        self.s2d1 = \
            "申请人上一年及最近一期的" \
            "总资产分别为{总资产1:,.2f}万元和{总资产m:,.2f}万元；" \
            "总负债分别为{总负债1:,.2f}万元和{总负债m:,.2f}万元；" \
            "资产负债率分别为{资产负债率1:.2%}和{资产负债率m:.2%}。" \
            "整体来看，申请人资产负债率{分析s2d1}"  # 7个变量

        self.s2d2 = \
            "从债务期限结构看，申请人债务{分析s2d2}，" \
            "流动负债分别为{流动负债1:,.2f}万元和{流动负债m:,.2f}万元，" \
            "短期负债占比分别为{短债占比1:.2%}和{短债占比m:.2%}。" \
            "刚性负债(短期借款+一年内到期的长期负债+应付债券+长期借款)分别为{刚性负债1:,.2f}和{刚性负债m:,.2f}," \
            "刚性负债占比分别为{刚性兑付占比1:.2%}和{刚性兑付占比m:.2%}。" \
            "短期内需要刚性兑付的债务为{短期刚兑m:,.2f}万元，主要为短期借款{短期借款m:,.2f}万元，一年内到期的非流动负债{一年内非流m:,.2f}万元。" \
            "总体来看，公司刚性债务带来的偿债压力【较大\在合理范围内\较小，根据实际情况自行评价】。"  # 12个变量

        # 3、盈利能力
        self.s2d3 = \
            "申请人上一年实现营业收入{营业收入1:,.2f}万元，{营业成本1:,.2f}万元，毛利率{毛利率1:,.2%}，" \
            "期间费用分别为{期间费用1:,.2f}万元，费用收入比分别为{费用收入比1:,.2f}万元。" \
            "实现净利润{净利润1:,.2f}万元，净利润率{净利润率1:.2%}，" \
            "最近一期，申请人实现营业收入{营业收入m:,.2f}万元，营业成本{营业成本m:,.2f}万元，毛利率{毛利率m:.2%}，" \
            "期间费用合计{期间费用m:,.2f}万元，投资收益{投资收益m:,.2f}万元，净利润率{净利润率m:.2%}。" \
            "总体来看，申请人盈利能力【相对较好/稳定/较弱，根据实际情况自行评价】"  # 13个变量

        # 4、现金流量
        self.s2d4 = \
            "申请人上一年实现净现金流入{净现金流入1:,.2f}万元，其中：" \
            "经营活动现金净流入{经营活动现金净流入1:,.2f}万元，" \
            "投资活动现金净流入{投资活动现金净流入1:,.2f}万元，" \
            "筹资活动现金净流入{筹资活动现金净流入1:,.2f}万元，。" \
            "最近一期实现净现金流入{净现金流入m:,.2f}万元，其中：" \
            "经营活动现金净流入{经营活动现金净流入m:,.2f}万元，" \
            "投资活动现金净流入{投资活动现金净流入m:,.2f}万元，" \
            "筹资活动现金净流入{筹资活动现金净流入m:,.2f}万元，。" \
            "总体来看，申请人盈利能力【请根据实际情况自行评价】"  # 8个变量

        # 5、资产质量
        self.s2d5 = \
            "申请人上一年流动资产分别为{流动资产1:,.2f}万元和{流动资产m:,.2f}万元，在总资产中流动资产占比分别{流动资产占比1:.2%}和{流动资产占比m:.2%}，" \
            "【>>>简要分析<<<】。上年末，主要资产构成为{分析s2d5}。【请根据实际情况自行评价】。"  # 5个变量

        # 6、流动性分析
        self.s2d6 = \
            "申请人上一年及最近一期流动比率分别为{流动比率1:.2%}和{流动比率m:.2%}，较年初变化{流动比率delta:.2f}个百分点；" \
            "申请人上一年及最近一期速动比率分别为{速动比率1:.2%}和{速动比率m:.2%}，较年初变化{速动比率delta:.2f}个百分点。" \
            "【请根据实际情况自行评价】。"  # 6个变量

        # 7、当期科目变化情况（变化超过30%）
        # 直接在core中调用

class no_year1:
    def __init__(self):
        self.table1 =float()
        # 1、审计情况分析
        self.s1d1 = \
            "申请人成立不足一年，无审计报告。仅针对现有数据进行分析。"
        # 2、资本结构
        self.s2d1 = \
            "申请人目前总资产为{总资产m:,.2f}万元，总负债为{总负债m:,.2f}万元，资产负债率分别为{资产负债率m:.2%}。" \
            "整体来看，申请人资产负债率{分析s2d1}"  # 13个变量

        self.s2d2 = \
            "从债务期限结构看，申请人债务{分析s2d2}，" \
            "流动负债为{流动负债m:,.2f}万元，" \
            "短期负债占比为{短债占比m:,.2f}。" \
            "刚性负债(短期借款+一年内到期的长期负债+应付债券+长期借款)为{刚性负债m:,.2f}," \
            "刚性负债占比分别为{刚性兑付占比m:,.2f}。" \
            "短期内需要刚性兑付的债务为{短期刚兑m:,.2f}万元，主要为短期借款{短期借款m:,.2f}万元，一年内到期的非流动负债{一年内非流m:,.2f}万元。" \
            "总体来看，公司刚性债务带来的偿债压力【较大\在合理范围内\较小，根据实际情况自行评价】。"  # 21个变量

        # 3、盈利能力
        self.s2d3 = \
            "最近一期，申请人实现营业收入{营业收入m:,.2f}万元，营业成本{营业成本m:,.2f}万元，毛利率{毛利率m:.2%}，" \
            "期间费用合计{期间费用m:,.2f}万元，投资收益{投资收益m:,.2f}万元，净利润率{净利润率m:.2%}。" \
            "总体来看，申请人盈利能力【相对较好/稳定/较弱，根据实际情况自行评价】"  # 28个变量

        # 4、现金流量
        self.s2d4 = \
            "最近一期实现净现金流入{净现金流入m:,.2f}万元，其中：" \
            "经营活动现金净流入{经营活动现金净流入m:,.2f}万元，" \
            "投资活动现金净流入{投资活动现金净流入m:,.2f}万元，" \
            "筹资活动现金净流入{筹资活动现金净流入m:,.2f}万元。" \
            "总体来看，申请人盈利能力【请根据实际情况自行评价】"  # 4个变量

        # 5、资产质量
        self.s2d5 = \
            "申请人流动资产为{流动资产m:,.2f}万元，在总资产中流动资产占比{流动资产占比m:.2%}，【>>>简要分析<<<】。" \
            "主要资产构成为{分析s2d5}。【请根据实际情况自行评价】。"  # 9个变量

        # 6、流动性分析
        self.s2d6 = \
            "申请人最近一期流动比率为{流动比率m:.2%}，较年初变化{流动比率delta}个百分点；" \
            "申请人最近一期速动比率为{速动比率m:.2%}，较年初变化{速动比率delta}个百分点。" \
            "【请根据实际情况自行评价】。"  # 12个变量

        # 7、当期科目变化情况（变化超过30%）
        # 直接在core中调用

class all_years:
    def __init__(self):
        self.table1 =float()
        # 1、审计情况分析
        self.s1d1 = \
            "【XXX会计师事务所】对申请人前三年的财务数据出具了编号为【】、【】、【】的审计报告，均出具了无保留意见。" \
            "其中，【年】对【科目 】进行了如下调整：【请仔细阅读审计报告后填写】。"
        # 2、资本结构
        self.s2d1 = \
            "申请人近三年的" \
            "总资产分别为{总资产3:,.2f}万元、{总资产2:,.2f}万元和{总资产1:,.2f}万元；" \
            "总负债分别为{总负债3:,.2f}万元、{总负债2:,.2f}万元和{总负债1:,.2f}万元；" \
            "资产负债率分别为{资产负债率3:.2%}、{资产负债率2:.2%}和{资产负债率1:.2%}。" \
            "整体来看，申请人资产负债率{分析s2d1}"  # 10个变量

        self.s2d2 = \
            "从债务期限结构看，申请人债务{分析s2d2}，近三年" \
            "流动负债分别为{流动负债3:,.2f}万元、{流动负债2:,.2f}万元和{流动负债1:,.2f}万元，" \
            "短期负债占比分别为{短债占比3:.2%}、{短债占比2:.2%}和{短债占比1:.2%}。" \
            "刚性负债(短期借款+一年内到期的长期负债+应付债券+长期借款)分别为{刚性负债3:,.2f}万元、{刚性负债2:,.2f}万元和{刚性负债1:,.2f}万元," \
            "刚性负债占比分别为{刚性兑付占比3:.2%}、{刚性兑付占比2:.2%}和{刚性兑付占比1:.2%}。" \
            "短期内需要刚性兑付的债务为{短期刚兑1:,.2f}万元，主要为短期借款{短期借款1:,.2f}万元，一年内到期的非流动负债{一年内非流1:,.2f}万元。" \
            "总体来看，公司刚性债务带来的偿债压力【较大\在合理范围内\较小，根据实际情况自行评价】。"  # 21个变量

        # 3、盈利能力
        self.s2d3 = \
            "申请人前三年分别实现营业收入{营业收入3:,.2f}万元、{营业收入2:,.2f}万元和{营业收入1:,.2f}万元，{分析s2d3}。" \
            "营业成本{营业成本3:,.2f}万元、{营业成本2:,.2f}万元和{营业成本1:,.2f}万元，毛利率分别为{毛利率3:.2%}、{毛利率2:.2%}和{毛利率1:.2%}，" \
            "期间费用分别为{期间费用3:,.2f}万元、{期间费用2:,.2f}万元和{期间费用1:,.2f}万元，费用收入比分别为{费用收入比3:.2%}、{费用收入比2:.2%}和{费用收入比1:.2%}。" \
            "实现净利润{净利润3:,.2f}万元、{净利润2:,.2f}万元和{净利润1:,.2f}万元，净利润率分别为{净利润率3:.2%}、{净利润率2:.2%}和{净利润率1:.2%}，" \
            "总体来看，申请人盈利能力【相对较好/稳定/较弱，根据实际情况自行评价】"  # 28个变量

        # 4、现金流量
        self.s2d4 = \
            "申请人前三年分别实现净现金流入{净现金流入3:,.2f}万元、{净现金流入2:,.2f}万元和{净现金流入1:,.2f}万元。其中：" \
            "经营活动现金净流入{经营活动现金净流入3:,.2f}万元、{经营活动现金净流入2:,.2f}万元和{经营活动现金净流入1:,.2f}万元；" \
            "投资活动现金净流入{投资活动现金净流入3:,.2f}万元、{投资活动现金净流入2:,.2f}万元和{投资活动现金净流入1:,.2f}万元；" \
            "筹资活动现金净流入{筹资活动现金净流入3:,.2f}万元、{筹资活动现金净流入2:,.2f}万元和{筹资活动现金净流入1:,.2f}万元。" \
            "总体来看，申请人盈利能力【请根据实际情况自行评价】"  # 16个变量

        # 5、资产质量
        self.s2d5 = \
            "申请人近三年流动资产分别为{流动资产3:,.2f}万元、{流动资产2:,.2f}万元和{流动资产1:,.2f}万元，" \
            "在总资产构成中流动资产占比分别{流动资产占比3:.2%}、{流动资产占比2:.2%}和{流动资产占比1:.2%}，【>>>简要分析<<<】。" \
            "上年末，主要资产构成为{分析s2d5}。【请根据实际情况自行评价】。"  # 9个变量

        # 6、流动性分析
        self.s2d6 = \
            "申请人近三年流动比率分别为{流动比率3:.2%}、{流动比率2:.2%}和{流动比率1:.2%}，三年平均值为{流动比率av:.2%}，" \
            "较年初变化{流动比率delta:.2f}个百分点；" \
            "申请人近三年速动比率分别为{速动比率3:.2%}、{速动比率2:.2%}和{速动比率1:.2%}，三年平均值为{速动比率av:.2%}，" \
            "较年初变化{速动比率delta:.2f}个百分点。" \
            "【请根据实际情况自行评价】。"  # 12个变量

        # 7、当期科目变化情况（变化超过30%）
        # 直接在core中调用

class header:
    def __init__(self):
        self.h1 = "一、财务报表"
        self.h2 = "二、财务分析"
        self.h2s1 = "（一）审计情况分析"
        self.h2s2 = "（二）资本结构分析"
        self.h2s3 = "（三）盈利能力分析"
        self.h2s4 = "（四）现金流量分析"
        self.h2s5 = "（五）资产质量分析"
        self.h2s6 = "（六）流动性分析"
        self.h2s7 = "（七）科目变化情况"
        self.h3 = "三、科目明细分析"


# if __name__ == '__main__':
    # doc = normal()
    # print(doc.s2d1.format(**doc.s2d1_dict))