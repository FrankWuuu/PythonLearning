import os

path_label = "labels_ah_jpg/"
path_imgs_all = "all_images/"
path_imgs_with_label = "images_with_label/"

label_lists = os.listdir(path_label)

# print(len(label_lists))  # 20
# print(len(os.listdir(path_imgs_all)))  # 397

with open("label_list.txt","+w") as f:
    for name in label_lists:
        # print(name)
        f.write(name)
        f.write("\n")
