from urllib.request import urlopen
from urllib.parse import quote
import requests
import json

# 获取json数据

# fullurl="https://api.scratch.mit.edu/users/atomicmagicnumber/projects?limit =2&offset=0"
#
# rawtext = urlopen(fullurl, timeout=15).read()
# jsonStr = json.loads(rawtext.decode('utf8'))

str1 = "["
for x in range(0, 5):

    url="https://api.scratch.mit.edu/users/atomicmagicnumber/projects?limit =32&offset="+str(x*32)
    print("x:", x,url)
    r=requests.get(url)
    str2 = str(r.text)[1:-1] # 去掉返回结果两边的中括号
    print("str2",str2)
    if(str2 == ""):
        break
    str1 += str2 + ","

str1 = str1[:-1]+"]"
print("str1",str1)
# 将ltp处理结果保存到文本中

# url="https://api.scratch.mit.edu/users/atomicmagicnumber/projects?limit =32&offset="+str(0*32)
f = open("1.json", "w", encoding="utf8")
f.write(str1)  # 保存前，需要将jsonStr序列化为python相对的数据类型，去掉最后的换行符
f.close()