# import os
# import shutil

# path_train_image = 'E:/vision/MI/lesions/data/train_image/'     # 图片原文件路径
# path_train_label = 'E:/vision/MI/lesions/data/train_label/'     # 标签原文件路径
# path_test_image = 'E:/vision/MI/lesions/data/test_image/'       # 图片目标路径
# path_test_label = 'E:/vision/MI/lesions/data/test_label/'       # 标签目标路径
# image_name = ['1.png', '81.png', '609.png', '273.png']      # 指定需要移掉的文件名

# ls_train_image = os.listdir(path_train_image)
# for i in ls_train_image:
#     if i in image_name:
#         shutil.move(path_train_image + i, path_test_image + i)

# ls_train_label = os.listdir(path_train_label)
# for i in ls_train_label:
#     if i in image_name:
#         shutil.move(path_train_label + i, path_test_label + i)

import os, shutil, random

path_origin_image = 'E:/vision/MI/lesions/data/archive/PNG/Original/'  #原图片位置
path_origin_label = 'E:/vision/MI/lesions/data/archive/PNG/Ground Truth/'  #原标签路径
path_same = 'E:/vision/MI/lesions/data/archive_new/'
path_train_image = path_same + 'train_image/'     # 训练图片路径
path_train_label = path_same + 'train_label/'     # 训练标签路径
path_test_image = path_same + 'test_image/'       # 测试图片路径
path_test_label = path_same + 'test_label/'       # 测试标签路径
path_whole = [path_same, path_train_image, path_train_label, path_test_image, path_test_label]
for i in path_whole:
    if not os.path.exists(i):
        os.mkdir(i)

# 随机将图片分成训练集和测试机
RATE = 0.3
name_origin_image = os.listdir(path_origin_image)   # os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。
name_origin_label = os.listdir(path_origin_label)
num_origin_image = len(name_origin_image)
num_test_image = int(RATE * num_origin_image)
num_train_image = num_origin_image - num_test_image

name_train_image_index = random.sample(list(range(1, num_origin_image+1)), num_train_image)
name_test_image_index = [x for x in list(range(1, num_origin_image+1)) if x not in name_train_image_index]

name_train_image_list = []  # 指定训练集的图片名称列表
name_test_image_list = []   # 指定测试集的图片名称列表
name_train_label_list = name_train_image_list
name_test_label_list = name_test_image_list

for i in name_train_image_index:
    name_train_image_list.append(str(i) + '.png')
for i in name_test_image_index:
    name_test_image_list.append(str(i) + '.png')

def movefile(nameold, namenew, pathold, pathnew):
    for i in nameold:
        if i in namenew:
            shutil.copy(pathold+i, pathnew)     # shutil.copy(),文件的copy，参数为新旧路径

movefile(name_origin_image, name_train_image_list, path_origin_image, path_train_image)
movefile(name_origin_image, name_test_image_list, path_origin_image, path_test_image)
movefile(name_origin_label, name_train_label_list, path_origin_label, path_train_label)
movefile(name_origin_label, name_test_label_list, path_origin_label, path_test_label)

# for i in name_origin_image:
#     if i in name_train_image_list:
#         shutil.copy(path_origin_image + i, path_train_image + i)
#
# for i in name_origin_image:
#     if i in name_test_image_list:
#         shutil.copy(path_origin_image + i, path_test_image + i)
#
# for i in name_origin_label:
#     if i in name_train_label_list:
#         shutil.copy(path_origin_label + i, path_train_label + i)
#
# for i in name_origin_label:
#     if i in name_test_label_list:
#         shutil.copy(path_origin_label + i, path_test_label + i)

