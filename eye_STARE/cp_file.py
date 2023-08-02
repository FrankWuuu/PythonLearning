import os
import shutil


path_label = "labels_ah_jpg/"
path_imgs_all = "all_images/"
path_imgs_with_label = "images_with_label/"
os.makedirs(path_imgs_with_label,exist_ok=True)


label_list = open("label_list.txt","r")

# name_lists = []
for name in label_list:
    name = name.strip()
    name = name.split("_")[0]+".jpg"
    # name_lists.append(name)
    shutil.copy(path_imgs_all+name,path_imgs_with_label+name)


