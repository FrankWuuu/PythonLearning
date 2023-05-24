import os
import json

########### load a json ###########
path_base = 'json_base.json'
with open(path_base,'r') as f:
    data_base = json.load(f)
    data_base["shapes"]=[]
    # print(data_base)
########### load a json ###########

path = '1.json'
with open(path,'r') as f:
    dataj = json.load(f)
    data_base["imageWidth"] = dataj["image"]["width"]
    data_base["imageHeight"] = dataj["image"]["height"]
    data_base["imagePath"] = dataj["image"]["original_filename"]

    lens = len(dataj["annotations"])
    # print(lens)
    for index in range(lens):
        pos = dataj["annotations"][index]["polygon"]["path"]
        points = []
        for i in range(len(pos)):
            points.append([pos[i]['x'],pos[i]['y']])
        # print(len(points))
        # data_base["shapes"]=[{"points":points}]
        data_base["shapes"]=data_base["shapes"]+[{"label": "Tooth","shape_type": "polygon","points":points}]
        # if index==1:
        #     # print(points)
        #     path_base = 'json_base.json'
        #     # data_base["shapes"]=[{"points",points}]
        #     data_base["shapes"]=[{"points":points}]
        #     data_base["shapes"]=data_base["shapes"]+[{"points":points}]
        #     # data_base["shapes"].append([{"points":points}])
        #     # data_base["shapes"]=[]
        #     # print(data_base)

            ########### load a json ###########
            
with open('json_temp.json','w')  as f:
    json.dump(data_base,f,indent=2)
    print(i)


    # ana1 = dataj["annotations"][0]
    # paths = ana1["polygon"]["path"]
# print(path)
# points = []
# print(paths[0]["x"])
# for i in range(len(paths)):
#     points.append([paths[i]['x'],paths[i]['y']])
#     # print(i)
# print(points)


########### load a json ###########


# path = "demojson.json"

# with open(path,'r') as f:
#     data1 = json.load(f)
#     keys = ["duncan_long","adina_norton"]
#     for key in keys:
#         del data1[key]
#     # for key,value in data1.items():
#     #     print(key)
#     #     del value['id']
#     #     data1[key] = value
#         # if key == "kelsea_head" or "phoenix_knox":
#         #     # key.pop()
#         #     # del data1[key]
#         #     data1.pop(key)
#         # value.pop("dataset",None)
#         # del value["id"]
#         # data1[key]=value
#         # f.seek(0)
#         # f.truncate()
#         # json.dump(data1,f,indent=2)


# jj = json.dumps(data1,indent=2)
# with open('demo2.json','w') as f:
#     f.write(jj)

# path = "demojson.json"

# with open(path,'r+') as f:
#     data1 = json.load(f)
#     for key,value in data1.items():
#         print(key)
#         del value['id']
#         data1[key] = value
#         # if key == "kelsea_head" or "phoenix_knox":
#         #     # key.pop()
#         #     # del data1[key]
#         #     data1.pop(key)
#         # value.pop("dataset",None)
#         # del value["id"]
#         # data1[key]=value
#         f.seek(0)
#         f.truncate()
#         json.dump(data1,f,indent=2)


########### write a json ###########
# with open('demojson.json','w') as f:
#     # data_d = json.loads(f)
#     df = {
#         "version":"4.6.0",
#         "flags":{},
#         "shapes":[
#         ]
#     }
#     data = json.dumps(df)
#     f.write(data)
#     print(data)
