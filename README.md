## Semi-Automatic Financial Analysis(简称safa)
> 本意是想给懒得烧蛇吃的我，节省点写报告的时间，结果自学Python又花了不少时间。

## safa用法
* 在/input/temple.xlsx中填写财务数据
* 运行index.py
* 在/output 中找到生成的以docx格式保存的word文档

## 开发进度
- [x] 项目基本框架
    - [x] 文件夹及基本配置
	- [x] 执行程序：index.py
- [x] 标准报告模板：/far
    - [x] 文本模版：text.py
    - [x] 参数模版：para.py
- [x] 数据处理模块：
    - [x] 数据读取：core.py
- [x] UI界面配置：
    - [ ]  用PyQt做个可视界面
	- [x] 架服务器接受邮件（原始版本已实现）

## 可用版本
处理不了数据缺失的情况，这也是safa项目后面要突破的地方。

![markdown](https://images.cnblogs.com/cnblogs_com/watalo/1685133/o_2003301711373ecd4737c26249da5da94f2a690d8c75.jpg)
