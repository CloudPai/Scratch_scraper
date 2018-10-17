import csv
import json




def startSave(saveName):
    f = open('1.json',"r",encoding="utf8")
    data = json.load(f)
    f.close()
    fcsv = csv.writer(open(saveName, "w", encoding="utf8"))
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