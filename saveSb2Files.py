import downloadSb2
import time

#scr.startDownload(171209234)


def saveSb2s(txtName,folderName):
    f = open("cacheFiles/"+txtName+".txt", "r")  #从存放项目id的文件读取要下载的项目id
    lines = f.readlines()#读取全部内容
    f.close
    for  line  in  lines:
        print(int(line))
        time.sleep(0.01)
        try:
            downloadSb2.startDownload(folderName,int(line))
        except ValueError:
            continue
