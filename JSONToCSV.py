import csv
import json
import os



def startSave(saveName):
    f = open('saveJSON.json',"r",encoding="utf8")
    data = json.load(f)
    f.close()

    path = 'csvFiles/'
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)
    fcsv = csv.writer(open('csvFiles/'+saveName, "w", encoding="utf8"))
    # Write CSV Header, If you dont need that, remove this line
    fcsv.writerow(["No.","id","title","description","instructions","visibility","is_published","author_id","author_username","image","history_created","history_modified","history_shared","stats_views","stats_loves","stats_favorites","stats_comments","stats_remixes","remix_parent","remix_root"])
    i = 1
    for x in data:
        fcsv.writerow(
            [
                i,
                x["id"],
                x["title"],
                x["description"],
                x["instructions"],
                x["visibility"],
                x["is_published"],

                x["author"]["id"],
                x["author"]["username"],

                x["image"],

                x["history"]["created"],
                x["history"]["modified"],
                x["history"]["shared"],

                x["stats"]["views"],
                x["stats"]["loves"],
                x["stats"]["favorites"],
                x["stats"]["comments"],
                x["stats"]["remixes"],

                x["remix"]["parent"],
                x["remix"]["root"]
             ])
        i +=1