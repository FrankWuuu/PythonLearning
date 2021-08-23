import os
import shutil

path_train_image = 'E:/vision/MI/lesions/data/train_image/'     # 图片原文件路径
path_train_label = 'E:/vision/MI/lesions/data/train_label/'     # 标签原文件路径
path_test_image = 'E:/vision/MI/lesions/data/test_image/'       # 图片目标路径
path_test_label = 'E:/vision/MI/lesions/data/test_label/'       # 标签目标路径
image_name = ['1.png', '81.png', '609.png', '273.png']      # 指定需要移掉的文件名

ls_train_image = os.listdir(path_train_image)
for i in ls_train_image:
    if i in image_name:
        shutil.move(path_train_image + i, path_test_image + i)

ls_train_label = os.listdir(path_train_label)
for i in ls_train_label:
    if i in image_name:
        shutil.move(path_train_label + i, path_test_label + i)
