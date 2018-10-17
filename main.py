# 采集项目id
import urllib.request
import json
import saveJSON,JSONToCSV,saveSb2Files


## 全局变量：

# 用户名
username = "atomicmagicnumber"

# 保存sb2文件时，文件名的前缀
PrefixString='getUserFiles'


'''
工作流Workflow
'''

# 步骤1： 将scratch官网的json数据存储到本地
saveJSON.startDownload(username,5)

# 步骤2：将json文件转换为csv文件和存有id的文件id.txt

JSONToCSV.startSave("user_"+username+".csv")

# 步骤3：根据id.txt下载所有sb2文件到名为变量username的文件夹中
# 参数：文件名和存储的sb2文件的前缀

saveSb2Files.saveSb2s(username,PrefixString)
