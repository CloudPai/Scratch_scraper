import scr
import time

#scr.startDownload(171209234)
f = open("/Users/pailiu/github/作品爬虫/id.txt", "r")  #从存放项目id的文件读取要下载的项目id
lines = f.readlines()#读取全部内容  
f.close
for  line  in  lines:
    print(int(line))
    time.sleep(0.01)
    try:
        scr.startDownload(int(line))
    except ValueError:
        continue
