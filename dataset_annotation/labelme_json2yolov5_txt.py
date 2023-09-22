import os
import glob
import json
import numpy as np

##labelme_json to yolov5_txt single
def convert(size, box):
    """
    convert [xmin, xmax, ymin, ymax] to [x_centre, y_centre, w, h]
    """
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

class_names = ["cup", "mouse"] #users class name

json_dir = "F:\Auseful\data\yolov5datademo\img_gt"
txt_dir = "txt_out/"
os.makedirs(txt_dir, exist_ok=True)

json_pths = glob.glob(json_dir + "/*.json")

for json_pth in json_pths:
    print(json_pth)
    json_file = open(json_pth, "r")
    json_data = json.load(json_file)

    h, w = json_data["imageHeight"],json_data["imageWidth"]

    json_name = os.path.basename(json_pth)
    out_file = open(os.path.join(txt_dir, json_name.replace("json", "txt")), "w")
    label_infos = json_data["shapes"]
    for label_info in label_infos:
        label = label_info["label"]
        points = label_info["points"]
        if len(points) >= 3:
            points = np.array(points)
            xmin, xmax = max(0, min(np.unique(points[:, 0]))), min(w, max(np.unique(points[:, 0])))
            ymin, ymax = max(0, min(np.unique(points[:, 1]))), min(h, max(np.unique(points[:, 1])))
        elif len(points) == 2:
            x1, y1 = points[0]
            x2, y2 = points[1]
            xmin, xmax = min(x1, x2), max(x1, x2)
            ymin, ymax = min(y1, y2), max(y1, y2)
        else:
            continue
        bbox = [xmin, xmax, ymin, ymax]
        bbox_ = convert((w,h), bbox)
        cls_id = class_names.index(label)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bbox_]) + '\n')
