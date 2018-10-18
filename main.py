# 采集项目id
import urllib.request
import json
import saveJSON,JSONToCSV,saveSb2Files,getProjectDetail
from feature_detection import singleprocess_staticData
import time

'''
工作流Workflow
'''
# 全局变量：
##  用户名
username = "atomicmagicnumber"



'''
步骤1： 将scratch官网的json数据存储到本地
'''

# saveJSON.startDownload("user_"+username,username,5)



'''
步骤2：将json文件转换为csv文件和存有id的文件id.txt
'''

# JSONToCSV.startSave("user_"+username)



'''
步骤3：根据id.txt下载所有sb2文件到名为变量username的文件夹中
参数：文件名和存储的sb2文件的前缀
'''

# saveSb2Files.saveSb2s("user_"+username,username)


'''
步骤4：对上述sb2文件夹中的作品进行feature detection
建议启动虚拟环境`source /Users/pailiu/github/902Scratch/902scratch_env/bin/activate`
然后执行：`cd /Users/pailiu/github/Scratch_scraper/feature_detection`
和`python singleprocess_staticData.py`
'''

# begin_time = time.time()
# p = singleprocess_staticData.HandleExcel(foldername=username,username="user_"+username)
# p.run_main_save_to_excel_with_openpyxl()
#
# end_time = time.time()
#
# total_sec = end_time - begin_time
#
# print("总共耗时(s): " + str(total_sec))


'''
步骤5：将excel和csv联表整合获得最后整合后的完整信息
'''
# getProjectDetail.saveProjectDetail("user_"+username)


