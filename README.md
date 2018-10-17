# Scratch_scraper
# 中文说明 v1.2
Scratch爬虫：获取scratch上某用户发布的所有作品的详细信息并存储为csv文件并根据获取的csv信息下载对应的sb2文件
## 工作流

* 步骤1： 将scratch官网的json数据存储到本地
* 步骤2：将json文件转换为csv文件和存有id的文件id.txt
* 步骤3：根据id.txt下载所有sb2文件到名为变量username的文件夹中


## 用法
在main.py中修改需要查询用户的用户名，执行main.py函数即可
## 输出
csv:
![](http://p4lmrb1gp.bkt.clouddn.com/20181017150811.png)

----------
# English Description v1.0
Get detailed information about all the works published by a user on scratch and store them as csv files
## usage
Modify the username queried in main.py and just execute the main.py function.
## output
csv:
![](http://p4lmrb1gp.bkt.clouddn.com/20181017150811.png)