# 采集项目id
import urllib.request
import requests
import json
import csv
#import time
#url="https://api.scratch.mit.edu/explore/projects?limit=16&offset=32&language=zh-cn&mode=trending&q=games"
#html=urllib.request.urlopen(url)
#s = json.loads(html.read())
'''
读取要下载的项目id
url="https://api.scratch.mit.edu/explore/projects?limit=32&offset="+str(x*32)+"&language=zh-cn&mode=popular&q=animations"
'''
f = open("id.txt", 'w')#定义要存放的项目id的文件以及路径
limit = 32
offset = 0
#for x in [x for x in range(0,20000) if x%32 == 0 ]:
# for x in range(0, 3):
    # url="https://api.scratch.mit.edu/explore/projects?limit=32&offset="+str(x*32)+"&language=zh-cn&mode=trending&q=tutorials"
    # url = "https://api.scratch.mit.edu/explore/projects?limit=32&offset=" + str(x) + "&language=zh-cn&mode=popular&q=games"

    # url="https://api.scratch.mit.edu/search/projects?limit=32&offset="+str(x*32)+"&language=zh-cn&q=games"
url="https://api.scratch.mit.edu/users/atomicmagicnumber/projects?limit =2&offset=0"


r=requests.get(url)
# print(type(r.text))
# print(type(r.text))
# print(len(r.text))
# print(r.text)

myJsonString = json.dumps(r.text)
myJsonString = myJsonString # 去除两端的双引号

print("myJsonString:",myJsonString)


f.write(myJsonString)
f.close()
str1 = myJsonString
# j = json.loads(str1)
# print(type(j))
# print(type(myJson))
# s = json.loads(r.text.decode())

print("type(str1):",type(str1))
j = json.loads(str1)
print(j)
print("type(j)",type(j))
print(len(j))