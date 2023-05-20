import os
import json

########### load a file list ###########
path_total = "json_demo"
file_list = os.listdir(path_total)
for i in file_list:
    # print(i)
    path_base = 'json_base.json'
    with open(path_base,'r') as f:
        data_base = json.load(f)
        data_base["shapes"]=[]
    with open(path_total+'/'+i,'r') as f:
        data_d = json.load(f)
        print(data_d["image"]["filename"])
        data_base["imageWidth"] = data_d["image"]["width"]
        data_base["imageHeight"] = data_d["image"]["height"]
        data_base["imagePath"] = data_d["image"]["original_filename"]

    lens = len(data_d["annotations"])
    # print(lens)
    for index in range(lens):
        pos = data_d["annotations"][index]["polygon"]["path"]
        points = []
        for j in range(len(pos)):
            points.append([pos[j]['x'],pos[j]['y']])
        # print(len(points))
        # data_base["shapes"]=[{"points":points}]
        data_base["shapes"]=data_base["shapes"]+[{"label": "Tooth","shape_type": "polygon","points":points}]
    file_name = data_d["image"]["filename"].split('.')[0]
    with open('out/'+file_name+'.json','w')  as f:
        json.dump(data_base,f,indent=2)
