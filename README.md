
<h1 align="center">Semi-Automatic Financial Analysis(safa)</h1>


<p align="center">
    <img alt="GitHub" src="https://img.shields.io/github/license/watalo/safa.svg?color=blue&style=flat-square">
    <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/watalo/safa">
    <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/watalo/safa">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/watalo/safa">
</p>

<p align="center">
只用填好财务数据表格，就可以直接生成报告
</p><p align="center">
财务报表.xlsx ➡️ 分析报告.docx
</p>

## 使用环境

### 安装

语言：python >= 3.8

1. 打开Win系统中的终端:    <kbd>Win</kbd> + <kbd>R</kbd> ,输入 `cmd`，按下<kbd>ENTER</kbd>
2. 进入准备保存项目的目录，比如：`cd E:\`
3. 下载项目文件，输入： `git clone https://github.com/watalo/safa.git`，等待下载完成。
4. 进入项目目录，输入： `cd safa`
5. 创建虚拟环境，输入： `python -m venv .venv`
6. 激活虚拟环境，输入： `.venv\Scripts\activate`
7. 安装依赖，输入： `pip install -r requirements.txt`

> 最好别用本地的ChatGLM-6B，因为配置麻烦，速度太慢。

如果非要用：[参阅THUDM/ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B)
- 可在[wenda](https://github.com/l15y/wenda)下载网盘的懒人包


### 数据准备

- 按下表企业财务报表数据完整情况填写数据

  | 缺失情况 |对应`_text.py`中的模版|填入标记为1的列|备注|
  |:--:|:-:|:-:|-|
  |数据完整| normal|1-1-1-1|成立超3年|
  |缺少第1年数据 | no_year3|0-1-1-1|成立不足3年|
  |缺少第2年数据 | no_year2|0-0-1-1|成立不足2年|
  |缺少第3年数据 | no_year1|0-0-0-1|成立不足1年|
  |当期为年末数据 | all_years|1-1-1-0|报告时间还没出1月报|

- 在input文件夹中找到`***.xlsx`，填写财务数据
  - 总共4列(例如:2021 | 2022 | 2023 | 2023M3 )

### 使用

#### 普通版

- 运行py文件
  - 运行`start.py`
  - 在`\output`中找到生成的`***.docx`，名字与`***.xlsx`文件一样。


#### 网页版
  - 运行`webapp.py`启动本地网页后台
  - 浏览器访问：http://127.0.0.1:5000

#### ChatGLM版（不建议使用）
  - 运行`start_aigc.py`
  - 在`\output`中找到生成的`***.docx`，名字与`***.xlsx`文件一样。


<br>
<img src="./img/taomi.png" width="300"/>
<br>
