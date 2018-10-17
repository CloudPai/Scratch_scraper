# 采集项目id
import urllib.request
import json
import saveJSON,JSONToCSV


username = "atomicmagicnumber"

saveJSON.startDownload(username,5)
JSONToCSV.startSave("user_"+username+".csv")