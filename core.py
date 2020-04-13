#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Administrator
# datetime:2020/2/20 20:21
# software: PyCharm


'''
    读取xlsx表的数据，形成数据库，形成分析报告
    Report类
'''

import os

from tinydb import TinyDB
from tinydb import Query
from openpyxl import load_workbook
from far import _config, _formula, _para, _text
from docx import Document

from docx.oxml.ns import qn
from docx.shared import Inches

class getDB(object):
    '''
        执行顺序：
            g_db= getDB('temple')


    '''

    def __init__(self, name):
        '''
        getDB类的功能：
            1、获取用户发送的数据文件（xlsx文件）
            2、形成和调用过程数据库（json文件）
            3、形成报告，需要导入(text和para模块)
        属性：
            name：企业名称（xlsx文件名称），被index模块调用，index模块获取name传入
        方法：
            xls_db(): 形成初始数据库

        :param name: 企业名称(xlsx文件名称)
        '''
        self.name = name
        self.initPath()
        self.db = self.xlsx_db()
        self.table_without_nodata = self.db.table('without_nodata')
        self.table_for_print = self.db.table('for_print')
        self.initDB()

    def initPath(self):
        # xlsx文件名
        self.xls_file_name = '%s.xlsx' % self.name
        # xlsx文件根目录
        self.root_path = _config.Path.root + '/safa'
        # xlsx文件路径
        self.xls_file_path = ''.join([self.root_path, r"\input\{}".format(self.xls_file_name)])
        # 读取xlsx文件
        self.ws = load_workbook(
            filename=self.xls_file_path,
            data_only=True)["Sheet1"]

    def initDB(self):
        self.__remove_zore_year()

    def xlsx_db(self):
        '''
        数据读取/存储
        :param output: xlsx文件数据形成tinydb数据库对象,并清除数据全部为0的科目
        :return: tinydb数据库对象
        '''
        self.db_path = ''.join([self.root_path, r"\db\{}.json".format(self.name)])
        db = TinyDB(self.db_path)
        # 清洗数据中因复制粘贴带有的‘\u202c’和数字中含有‘，’的问题

        def clear_data(data):
            if isinstance(data, str):
                data = data.replace('\u202c', '').replace(',', '')
                # ['前3年','前2年','前1年','当期']:
                if data in ['前3年', '前2年', '前1年', '当期']:
                    return data
                else:
                    return float(data)
            else:
                return data
        # 写入数据库
        for row in self.ws.iter_rows(min_row=1,
                                     max_col=self.ws.max_column,
                                     max_row=self.ws.max_row
                                     ):
            for cell in row:
                if cell.value is None or cell.value == ' ':
                    cell.value = 0
            db.insert({
                'items': row[0].value.strip(),
                'year3': clear_data(row[1].value),
                'year2': clear_data(row[2].value),
                'year1': clear_data(row[3].value),
                'month': clear_data(row[4].value),
            })
        return db

    def check_complete(self):
        """
        判断原始数据库db中，没有数据的年份或月份
        :param db: 原始数据库，tinydb类
        :return: 无数据年份列表
        """
        def get_data(db, a, b):
            return db.get(Q.items == a)[b]
        self.db.all()
        Q = Query()
        nodata_years_list = []
        for year in ['year3', 'year2', 'year1', 'month']:
            if get_data(self.db, '资产总计', year) == 0 and \
                    get_data(self.db, '负债合计', year) == 0 and \
                    get_data(self.db, '所有者权益合计', year) == 0:
                nodata_years_list.append(year)
            else:
                pass
        return nodata_years_list

    def __remove_zore_year(self):
        '''
        前置步骤:
            cal_f_index() ---> table('without_nodata')
            cal_f_index() ---> table('without_nodata')
        清除无数据年份
        row_dict类型为字典，删除无数据年份对应的键值对
        '''
        table = self.db.table('without_nodata')
        row_dict = self.db.all()
        for row in row_dict:
            for year in self.check_complete():
                del row[year]
            table.insert(row)

    def __remove_zore_item(self, table):
        table.all()
        Q = Query()
        table.remove(
            Q.year3 == 0 and
            Q.year2 == 0 and
            Q.year1 == 0 and
            Q.month == 0
        )
        return table

    def calc_f_index(self, table_name):
        """
            '''纵向扩展 使用insert'''
            1、根据同年数据计算财务指标
            2、存货周转天数、应收账款周转天数 应使用前值与当前值的均值，暂未处理
            3、指标增加需在
                （1）index_list中新增指标名称，
                （2）__formula模块中新增指标计算公式
        :param table:  tinydb.table类实例
        :return: tinydb.table类实例
        """
        table = self.db.table(table_name)
        table_ = table.all()
        Q = Query()
        index_list = [
            '资产负债率', '流动比率', '速动比率', 'EBIT', '利息保障倍数',  # 偿债能力指标
            '营运资产', '营运负债', '营运资金需求', '营运资本', '存货周转天数', '应收账款周转天数',  # 营运能力指标
            '毛利率', '净利润率', '总资产收益率(ROA)', '净资产收益率(ROE)', # 盈利能力指标
            '短债占比', '刚性负债', '刚兑占比', '短期刚兑', '期间费用', '费用收入比', '流动资产占比',  # 报告需要数据
        ]
        years = [
            'year3', 'year2', 'year1', 'month'
        ]
        exsit_data_list = []
        for year in years:
            if year in table_[2].keys():
                exsit_data_list.append(year)

        for index in index_list:
            index_dict = {}
            index_dict.setdefault('items', index)
            for i in exsit_data_list:
                index_dict.setdefault(i, _formula.formula(table, i, index))
            table.insert(index_dict)

        return table

    def calc_m_index(self, table_name):
        """
            '''横向扩展，使用update'''
            1、清除全部为0的科目
            2、增加平均值、求和数、增长率、平均增长率
            3、科目进行分类，更新type标签
        @param table:xlsx转换的tinydb里的table类
        @return: 格式化的数据
        """
        table = self.db.table(table_name)
        table.all()
        Q = Query()

        # 平均值、求和数、增长率、平均增长率
        for row_dict in table.all():
            if row_dict['items'] == '项目':
                pass
            else:
                # 累积值求和
                sum = 0
                exsit_data_list = []
                for year in ['year3', 'year2', 'year1', 'month']:
                    if year in row_dict.keys():
                        sum += row_dict[year]
                        exsit_data_list.append(row_dict[year])
                # 平均值
                averg = sum / len(exsit_data_list)
                # 当期比前值的变化
                if len(exsit_data_list) >= 2:
                    delta = exsit_data_list[-1] - exsit_data_list[-2]
                else:
                    delta = exsit_data_list[-1]
                # 当期比前值的变化幅度
                if exsit_data_list[-2] == 0:
                    ratio = '净新增'
                else:
                    ratio = delta / exsit_data_list[-2]

                table.update(
                    {
                        'averg': averg,
                        'sum': sum,
                        'ratio': ratio,
                        'delta': delta,
                    },
                    Q.items == row_dict['items']
                )
        # 分类标签
        type = [
            '流动资产', '非流动资产', '流动负债', '非流动负债', '权益', '利润表', '现金流量', '财务指标',
        ]  # 数据类型列表
        li_a = [
            '货币资金', '交易性金融资产', '衍生金融资产 ', '应收票据', '应收账款', '应收款项融资 ', '预付账款',
            '其他应收款', '存货', '合同资产', '持有待售资产', '一年到期的非流动资产', '其他流动资产',
        ]  # 流动资产科目
        fi_a = [
            '债权投资', '其他债权投资', '长期应收款', '长期股权投资', '其他权益工具投资', '其他非流动金融资产',
            '投资性房地产', '固定资产', '在建工程', '生产性生物资产', '油气资产', '使用权资产', '无形资产',
            '开发支出', '商誉', '长期待摊费用', '递延所得税资产', '其他非流动资产',
        ]  # 非流动资产科目
        li_d = [
            '短期借款', '交易性金融负债', '衍生金融负债', '应付票据', '应付账款', '预收账款', '合同负债',
            '应付职工薪酬','应交税费', '其他应付款', '持有待售负债', '一年内到期的非流动负债', '其他流动负债',
        ]  # 流动负债科目
        fi_d = [
            '长期借款', '应付债券', '租赁负债', '长期应付款', '预计负债', '递延收益', '递延所得税负债', '其他非流动负债',
        ]  # 非流动负债科目
        equi = [
            '实收资本', '其他权益工具', '资本公积', '其他综合收益', '专项储备', '盈余公积', '未分配利润',
        ]  # 所有者权益科目
        reve = [
            '营业收入', '营业成本', '税金及附加', '销售费用', '管理费用', '研发费用', '财务费用', '投资收益',
            '净敞口套期收益', '公允价值变动收益', '信用减值损失', '资产减值损失', '资产处置收益', '营业利润',
            '营业外收入', '营业外支出', '利润总额', '所得税费用', '净利润',
        ]  # 利润表科目
        csfl = [
            '经营活动现金流入', '销售带来的现金流入', '经营活动现金流出', '经营活动净现金流',
            '投资活动现金流入', '投资活动现金流出', '投资活动现金净流',
            '筹资活动现金流入', '筹资活动现金流出', '筹资活动现金净流入', '现金净流入',
        ]  # 现金流量表科目
        inde = [
            '资产负债率', '流动比率', '速动比率', 'EBIT', '利息保障倍数',
            '营运资产', '营运负债', '营运资金需求', '营运资本', '存货周转天数', '应收账款周转天数',
            '毛利率', '净利润率', '总资产收益率(ROA)', '净资产收益率(ROE)',
        ]  # 财务指标列表

        type_list = [li_a, fi_a, li_d, fi_d, equi, reve, csfl, inde]
        for ty in type_list:
            for it in ty:
                for i in range(len(type_list)):
                    if it in type_list[i]:
                        table.update({'type': type[i]}, Q.items == str(it))
        return table


class getDOCX(object):
    document = Document()

    def __init__(self,name):
        self.name = name
        self.db_path = _config.Path.db
        self.db_file_path = '\\'.join([self.db_path, os.listdir(self.db_path)[0]])
        self.db = TinyDB(self.db_file_path)
        self.table = self.db.table('without_nodata')
        self.table_for_print = self.db.table('for_print')
        # docx类的实例初始化
        self.init_doc()
        # para类的实例初始化
        self.data_type = _para.dict_().data_type
        self.para = _para.dict_()
        self.init_para()
        # text类的实例
        self.normal = _text.normal()
        self.no_year3 = _text.no_year3()
        self.no_year2 = _text.no_year2()
        self.no_year1 = _text.no_year1()
        self.all_years = _text.all_years()
        self.header = _text.header()

    def init_doc(self):
        global document
        document.styles['Normal'].font.name = u'宋体'
        document.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')

    def init_para(self):
        self.para.set()
        self.para.analysis_s2d1()
        self.para.analysis_s2d2()
        self.para.analysis_s2d3()
        self.para.analysis_s2d5()

    def bold(self,text):
        document.add_paragragh().add_run(text).bold = True
        # p.add_run(text).bold = True

    def financial_sheet(self):
        Q = Query()
        item_list = []  # 表头列表
        for item in self.table_for_print.all():
            item_list.append(item['items'])
        data_list = []  # 数据列表
        for data in self.table_for_print.search(Q.items == '项目'):
            for i, it in enumerate(data):
                if type(it) == str:
                    data_list.append(it)
        data_list = data_list[:5]
        xratio = [
            '资产负债率', '流动比率', '速动比率',
            '毛利率', '净利润率',
            '总资产收益率(ROA)', '净资产收益率(ROE)',
        ]  # 百分数形式的财务指标 eg:‘11.11%’
        table = document.add_table(rows=len(self.table_for_print.all()),
                                        cols=5,
                                        style="Medium Grid 1 Accent 1")
        for irows, item in enumerate(item_list):
            for icols, data in enumerate(data_list):
                num = self.table_for_print.get(Q.items == item)[data]
                if isinstance(num, float):
                    if item in xratio:
                        table.cell(irows, icols).text = '{:,.2%}'.format(num)
                    else:
                        table.cell(irows, icols).text = '{:,.0f}'.format(num)
                else:
                    table.cell(irows, icols).text = str(num)

    def big_change_items(self):
        '''
        self.data_type == 'no_year1'时不能是使用本函数
        找出最近一期比上一期变化超过30%的科目
        :return:
        '''
        Q = Query()
        Item = self.table.search((Q.type == '流动资产') | (Q.type == '非流动资产') | (Q.type == '流动负债') | (Q.type == '非流动负债'))
        list1 = []
        list2 = []
        big_change_items = []
        if self.data_type == 'all_years':
            for dict in Item:
                if dict['year1'] == 0 and dict['month'] != 0:
                    list1.append(dict)
                elif dict['year1'] == 0 and dict['month'] == 0:
                    pass
                else:
                    if (dict['month'] - dict['year1']) / dict['year1'] < 0.3 \
                            and (dict['month'] - dict['year1']) / dict['year1'] > -0.3:
                        pass
                    else:
                        list2.append(dict)
            list_sorted_dict = sorted(list2, key=lambda x: x['month'] - x['year1'], reverse=True)
            # 组成当期纯变化和超过30%变化的列表
            for dict in list_sorted_dict:
                list1.append(dict)
            # 形成科目名称列表
            for dict in list1:
                big_change_items.append(dict['items'])
            return big_change_items
        else:
            for dict in Item:
                if dict['year1'] == 0 and dict['year2'] != 0:
                    list1.append(dict)
                elif dict['year1'] == 0 and dict['year2'] == 0:
                    pass
                else:
                    if (dict['year1']-dict['year2'])/dict['year2'] < 0.3 \
                            and (dict['year1']-dict['year2'])/dict['year2'] > -0.3:
                        pass
                    else:
                        list2.append(dict)
            list_sorted_dict = sorted(list2, key=lambda x: x['year1']-x['year2'], reverse=True)
            #组成当期纯变化和超过30%变化的列表
            for dict in list_sorted_dict:
                list1.append(dict)
            # 形成科目名称列表
            for dict in list1:
                big_change_items.append(dict['items'])
            return big_change_items

    def data(self,item, key):
        Q = Query()
        return self.table.get(Q.items == item)[key]

    def big_change_sheet(self):
        table_change_item = ['科目名称', '当期值', '较年初变化', '变化率', '变化情况']
        table_change = document.add_table(rows=len(self.big_change_items()) + 1,
                                               cols=5,
                                               style='Medium Grid 1 Accent 1')
        for i in range(5):
            cell = table_change.cell(0, i)
            cell.text = table_change_item[i]
        if self.data_type == 'all_years':
            for i, item in enumerate(self.big_change_items()):
                table_change.cell(i + 1, 0).text = self.data(item, 'items')  # 科目名称
                table_change.cell(i + 1, 1).text = '{:,.2f}'.format(self.data(item, 'year1'))  # 当期值
                table_change.cell(i + 1, 2).text = '{:,.2f}'.format(
                    self.data(item, 'month') - self.data(item, 'year1'))  # 变化值
                if self.data(item, 'year1') != 0:
                    ratio = self.data(item, 'month') - self.data(item, 'year1') / self.data(item, 'year1')
                    table_change.cell(i + 1, 3).text = '{:.2%}'.format(ratio)  # 变化率
                else:
                    if self.data(item, 'month') > 0:
                        table_change.cell(i + 1, 3).text = '当期净增加'
                    else:
                        table_change.cell(i + 1, 3).text = '当期净减少'
        else:
            for i, item in enumerate(self.big_change_items()):
                table_change.cell(i + 1, 0).text = self.data(item, 'items')  # 科目名称
                table_change.cell(i + 1, 1).text = '{:,.2f}'.format(self.data(item, 'month'))  # 当期值
                table_change.cell(i + 1, 2).text = '{:,.2f}'.format(self.data(item, 'month') - self.data(item, 'year1'))  # 变化值
                if self.data(item, 'year1') != 0:
                    ratio = self.data(item, 'month') - self.data(item, 'year1') / self.data(item, 'year1')
                    table_change.cell(i + 1, 3).text = '{:.2%}'.format(ratio)  # 变化率
                else:
                    if self.data(item, 'month') > 0:
                        table_change.cell(i + 1, 3).text = '当期净增加'
                    else:
                        table_change.cell(i + 1, 3).text = '当期净减少'


    def item_table(self, col1, col2, col3, col4):
        """
        生成固定格式的表格
            1、科目明细
            2、账龄明细
            3、等等
        @param col1: 序号
        @param col2: 名称
        @param col3: 金额
        @param col4: 等等
        @return: 空白表格
        """
        table_regular = [col1, col2, col3, col4]
        b_c_table = document.add_table(rows=7,
                                        cols=4,
                                        style='Medium Shading 1 Accent 1')
        for i in range(4):
            cell = b_c_table.cell(0, i)
            cell.text = table_regular[i]
        for i in range(5):
            cell = b_c_table.cell(i + 1, 0)
            cell.text = str(i + 1)

    def para_add(self, item_para, item):
        if item == "货币资金":
            item_para.add_run("其中现金【】万元，银行存款【】万元、其他货币资金【】万元。")
        elif item == "应收票据":
            item_para.add_run("其中银行承兑汇票【】万元，商业承兑汇票【】万元。")
        elif item == "应收账款":
            item_para.add_run("账面余额【】万元、计提坏账准备【】万元，账龄1年以内占比【】%，3年以上占比【】%。其中，应收账款前五位：")
            self.item_table("序号", "名称", "余额（万元）", "占比")
        elif item == "预付账款":
            item_para.add_run("账龄1年以内占比【】%，3年以上占比【】%。其中，预收账款前五位：")
            self.item_table("序号", "名称", "余额（万元）", "占比")
        elif item == "其他应收款":
            item_para.add_run("账面余额【】万元、计提坏账准备【】万元。其中，其他应付款前五位：")
            self.item_table("序号", "名称", "余额(万元)", "款项性质")
        elif item == "存货":
            item_para.add_run("其中，原材料【】万元、库存商品【】万元、周转材料【】万元、工程施工【】万元、开发成本【】万元。")
        elif item == "其他流动资产":
            item_para.add_run("其中【添加明细】。")
        elif item == "长期股权投资":
            item_para.add_run("系对【n】家企业的投资，本期主要新增【哪家公司】；对外投资前五位如下：")
            self.item_table("序号", "名称", "投资额", "投资性质")
        elif item == "固定资产":
            item_para.add_run("固定资产原值【】万元，累计折旧【】万元，其中房屋及建筑物【】万元、机器设备【】万元、办公设备【】万元、【其他】【】万元。")
        elif item == "在建工程":
            item_para.add_run("主要为【项目1】【】万元、【项目2】【】万元、【项目3】【】万元……")
        elif item == "无形资产":
            item_para.add_run("主要为土地使用权【】万元、采矿权【】万元、专利权【】万元、软件【】万元，其他【】万元。")
        elif item == "短期借款":
            item_para.add_run("主要为【XX银行】【】万元、【XX银行】【】万元、【XX银行】【】万元、【xx银行】【】万元、【xx银行】【】万元。【其他需要说明的内容】")
        elif item == "应付票据":
            item_para.add_run("主要为银行承兑汇票【】万元，商业承兑汇票【】万元。")
        elif item == "应付账款":
            item_para.add_run("其中应付材料款【】万元，应付工程款【】万元。其中前五名如下：")
            self.item_table("序号", "名称", "余额", "性质")
        elif item == "预收账款":
            item_para.add_run("其中前5名如下：")
            self.item_table("序号", "名称", "余额", "账龄")
        elif item == "其他应付款":
            item_para.add_run("应付利息【】万元，往来款【】万元，押金和保证金【】万元，其中前5名如下：")
            self.item_table("序号", "名称", "余额", "账龄")
        elif item == "其他流动负债":
            item_para.add_run("主要为【】")
        elif item == "长期借款":
            item_para.add_run("主要为【XX银行】【】万元、【XX银行】【】万元、【XX银行】【】万元、【xx银行】【】万元、【xx银行】【】万元。【其他需要说明的内容】")
        elif item == "应付债券":
            item_para.add_run("主要为【】")
            self.item_table("序号", "债券名称", "余额", "到期日")
        elif item == "长期应付款":
            item_para.add_run("其中专项应付款【】万元、【】【】万元、其他【】万元。")

    def items_detail(self,date):
        # 形成科目列表
        global type_in_all, total_, item_text
        list_dict = []
        for dict in self.table:
            if dict['type'] in ['流动资产', '非流动资产', '流动负债', '非流动负债']:
                list_dict.append(dict['items'])
            else:
                pass
        # 科目分析
        for item in list_dict:  # 第一行是表头，里面有字符串，必须剔除
            # 设置科目分析的文字模版
            if self.data(item, date) != 0:
                if self.data_type == 'no_1year':
                    item_text = '【{}】：当期余额{:,.2f}万元，在{}中占比{:.2%}。'
                else:
                    item_text = '【{}】：当期余额{:,.2f}万元，在{}中占比{:.2f}，较上年增加{:.2f}万元，{}。'

                if self.data(item, 'type') in ['流动资产', '非流动资产']:
                    type_in_all = '总资产'
                    total_ = self.data('资产总计', date)
                elif self.data(item, 'type') in ['流动负债', '非流动负债']:
                    type_in_all = '总负债'
                    total_ = self.data('负债合计', date)
                else:
                    pass
            else:
                pass
            # “较上年增加后”的文字部分
            if isinstance(self.data(item, 'ratio'), str):
                text_ratio = '为' + self.data(item, 'ratio')
            else:
                text_ratio = '当年增幅为{:.2%}'.format(self.data(item, 'ratio'))
            # 模版的格式化输出
            if self.data_type == 'no_1year':
                item_text.format(self.data(item,'items'),
                                 self.data(item, date),
                                 type_in_all,
                                 self.data(item, date) / total_
                                 )
            else:
                item_text.format(self.data(item, 'items'),
                                 self.data(item, date),
                                 type_in_all,
                                 self.data(item, date) / total_,
                                 self.data(item, 'delta'),
                                 text_ratio
                                 )
            para_ = document.add_paragraph(item_text)
            self.para_add(para_, self.data(item, date)) #根据不同的科目在文字模版后新增文字

    def run(self):
        document.add_heading('{}财务分析报告'.format(self.name))
        # 1.数据
        self.bold(self.header.h1)
        self.financial_sheet()
        document.add_paragragh(':::::::请调整成自己喜欢的表格样式::::::')
        # 2.分析
        if self.data_type == 'normal':
            self.bold(self.header.h2)
            self.bold(self.header.h2s1)
            document.add_paragragh(self.normal.s1d1)
            self.bold(self.header.h2s2)
            document.add_paragragh(self.normal.s2d1.format(**self.para.s2d1))
            document.add_paragragh(self.normal.s2d2.format(**self.para.s2d2))
            self.bold(self.header.h2s3)
            document.add_paragragh(self.normal.s2d3.format(**self.para.s2d3))
            self.bold(self.header.h2s4)
            document.add_paragragh(self.normal.s2d4.format(**self.para.s2d4))
            self.bold(self.header.h2s5)
            document.add_paragragh(self.normal.s2d5.format(**self.para.s2d5))
            self.bold(self.header.h2s6)
            document.add_paragragh(self.normal.s2d6.format(**self.para.s2d6))
            self.bold(self.header.h2s7)
            self.big_change_sheet()
            document.bold(self.header.h3)
            self.items_detail('year1')
        elif self.data_type == 'no_3year':
            self.bold(self.header.h2)
            self.bold(self.header.h2s1)
            document.add_paragragh(self.no_year3.s1d1)
            self.bold(self.header.h2s2)
            document.add_paragragh(self.no_year3.s2d1.format(**self.para.s2d1))
            document.add_paragragh(self.no_year3.s2d2.format(**self.para.s2d2))
            self.bold(self.header.h2s3)
            document.add_paragragh(self.no_year3.s2d3.format(**self.para.s2d3))
            self.bold(self.header.h2s4)
            document.add_paragragh(self.no_year3.s2d4.format(**self.para.s2d4))
            self.bold(self.header.h2s5)
            document.add_paragragh(self.no_year3.s2d5.format(**self.para.s2d5))
            self.bold(self.header.h2s6)
            document.add_paragragh(self.no_year3.s2d6.format(**self.para.s2d6))
            self.bold(self.header.h2s7)
            self.big_change_sheet()
            document.bold(self.header.h3)
            self.items_detail('year1')
        elif self.data_type == 'no_year2':
            self.bold(self.header.h2)
            self.bold(self.header.h2s1)
            document.add_paragragh(self.no_year2.s1d1)
            self.bold(self.header.h2s2)
            document.add_paragragh(self.no_year2.s2d1.format(**self.para.s2d1))
            document.add_paragragh(self.no_year2.s2d2.format(**self.para.s2d2))
            self.bold(self.header.h2s3)
            document.add_paragragh(self.no_year2.s2d3.format(**self.para.s2d3))
            self.bold(self.header.h2s4)
            document.add_paragragh(self.no_year2.s2d4.format(**self.para.s2d4))
            self.bold(self.header.h2s5)
            document.add_paragragh(self.no_year2.s2d5.format(**self.para.s2d5))
            self.bold(self.header.h2s6)
            document.add_paragragh(self.no_year2.s2d6.format(**self.para.s2d6))
            self.bold(self.header.h2s7)
            self.big_change_sheet()
            self.bold(self.header.h3)
            self.items_detail('year1')
        elif self.data_type == 'no_year1':
            self.bold(self.header.h2)
            self.bold(self.header.h2s1)
            document.add_paragragh(self.no_year1.s1d1)
            self.bold(self.header.h2s2)
            document.add_paragragh(self.no_year1.s2d1.format(**self.para.s2d1))
            document.add_paragragh(self.no_year1.s2d2.format(**self.para.s2d2))
            self.bold(self.header.h2s3)
            document.add_paragragh(self.no_year1.s2d3.format(**self.para.s2d3))
            self.bold(self.header.h2s4)
            document.add_paragragh(self.no_year1.s2d4.format(**self.para.s2d4))
            self.bold(self.header.h2s5)
            document.add_paragragh(self.no_year1.s2d5.format(**self.para.s2d5))
            self.bold(self.header.h2s6)
            document.add_paragragh(self.no_year1.s2d6.format(**self.para.s2d6))
            self.bold(self.header.h3)
            self.items_detail('month')
        elif self.data_type == 'all_years':
            self.bold(self.header.h2)
            self.bold(self.header.h2s1)
            document.add_paragragh(self.all_years.s1d1)
            self.bold(self.header.h2s2)
            document.add_paragragh(self.all_years.s2d1.format(**self.para.s2d1))
            document.add_paragragh(self.all_years.s2d2.format(**self.para.s2d2))
            self.bold(self.header.h2s3)
            document.add_paragragh(self.all_years.s2d3.format(**self.para.s2d3))
            self.bold(self.header.h2s4)
            document.add_paragragh(self.all_years.s2d4.format(**self.para.s2d4))
            self.bold(self.header.h2s5)
            document.add_paragragh(self.all_years.s2d5.format(**self.para.s2d5))
            self.bold(self.header.h2s6)
            document.add_paragragh(self.all_years.s2d6.format(**self.para.s2d6))
            self.bold(self.header.h3)
            self.items_detail('year1')
        else:
            pass
        # 3.讨米文案
        document.add_picture('img/taomi.png',width=Inches(2.25))
        p = document.add_paragragh()
        run_1 = p.add_run('后期开发计划是增加各个行业的行业分析，扫码赞赏可以加快开发速度哦，感谢您的支持！').bold = True

    def docx_save(self,output_path):
        document.save(output_path)

if __name__ == '__main__':
    g_db = getDB('temple')



