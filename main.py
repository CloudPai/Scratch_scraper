# 采集项目id
import urllib.request
import json
#import time
#url="https://api.scratch.mit.edu/explore/projects?limit=16&offset=32&language=zh-cn&mode=trending&q=games"
#html=urllib.request.urlopen(url)
#s = json.loads(html.read())
'''
读取要下载的项目id
url="https://api.scratch.mit.edu/explore/projects?limit=32&offset="+str(x*32)+"&language=zh-cn&mode=popular&q=animations"
'''
f = open("/Users/pailiu/github/作品爬虫/id.txt", 'w')#定义要存放的项目id的文件以及路径
limit = 32
offset = 0
#for x in [x for x in range(0,20000) if x%32 == 0 ]:
for x in [x for x in range(0, 20000)]:
    # url="https://api.scratch.mit.edu/explore/projects?limit=32&offset="+str(x*32)+"&language=zh-cn&mode=trending&q=tutorials"
    url = "https://api.scratch.mit.edu/explore/projects?limit=32&offset=" + str(x) + "&language=zh-cn&mode=popular&q=games"
    # url="https://api.scratch.mit.edu/search/projects?limit=32&offset="+str(x*32)+"&language=zh-cn&q=games"
    html=urllib.request.urlopen(url)
    s = json.loads(html.read().decode())
    print(s)
    for y in [y for y in range(0, 32)]:
        f.write(str(s[y]["id"])+'\n')
f.close()