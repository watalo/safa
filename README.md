
<h1 align="center">Semi-Automatic Financial Analysis(safa)</h1>


<p align="center">
    <img alt="GitHub" src="https://img.shields.io/github/license/watalo/safa.svg?color=blue&style=flat-square">
    <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/watalo/safa">
    <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/watalo/safa">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/watalo/safa">
</p>

<p align="center">
本项目旨在为被领导PUA太狠的银行加班🐶节省点时间，多摸点鱼，养点生。</p>
<p align="center">
用财务数据.xlsx直接生成报告模板.docx，剩下的留给自己or交给百度（敬请期待）。
</p>

## 使用说明

### 环境依赖
- `python >= 3.8`
- `git clone https://github.com/watalo/safa.git`
- `python -m pip install -r requirements.txt`
  - 一定要这样，因为里面用到的某个包更新变化太大，要用老版本。
  

### 数据准备

- 需要按下表企业财务报表数据完整情况填数据，总共4列(例如:2021|2022|2023|2023M3)
  | 缺失情况 |对应`_text.py`中的模版|填入标记为1的列|备注|
  |:--:|:-:|:-:|-|
  |数据完整| normal|1-1-1-1|成立超3年|
  |缺少第一年数据 | no_year3|0-1-1-1|成立不足3年|
  |缺少第二年数据 | no_year2|0-0-1-1|成立不足2年|
  |缺少第三年数据 | no_year1|0-0-0-1|成立不足1年|
  |当期为年末数据 | all_years|1-1-1-0|报告时间还没出1月报|

- 在`/input/样本1.xlsx`中填写财务数据,<font color="red">如果有缘人懂OCR，可以联系我：</font><link>watalo@163.com</link>
  
> 银行的应该都知道为什么会有这么多奇葩的日期结构吧，如果不知道说明你运气不错，被坑的不多。

### 运行

- 运行`start.py`
- 在`/output`中找到生成的🤗`样本1.docx`，名字与`.xlsx`文件一样。

## ToDo：
- [x] 项目基本框架
    - [x] 文档结构优化
	- [x] 执行程序：start.py
- [x] 标准报告模板：/far
    - [x] 文本模版：_text.py
    - [x] 参数模版：_para.py
- [x] 数据处理模块：
    - [x] 数据读取：_core.py
- [x] UI界面配置：
    - [ ] 制作一个简单的webUI界面
- [ ] 接入大模型：
  - [ ] 🤬正在研究文心、ChatGLM
  - [ ] 优化prompt，完成各版块分析内容生成
## 最后
<br>
<img src="./img/taomi.png" width="300"/>
<br>
如果觉得本项目有点帮助,you can buy me a coffee.