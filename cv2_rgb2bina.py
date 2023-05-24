import os
import cv2

path_sour = "out_gt/"
path_dest = "out_bina/"
os.makedirs(path_dest, exist_ok=True)
file_list = os.listdir(path_sour)
for file in file_list:
    # print(file)
    img_gray = cv2.imread(path_sour + file, cv2.IMREAD_GRAYSCALE)
    ret, img_binary = cv2.threshold(img_gray, 1, 255, cv2.THRESH_BINARY)
    cv2.imwrite(path_dest +'gt_'+ file, img_binary)

########## imread single img and transform it 2 gray############
# img_gray = cv2.imread("out_gt/0.png",cv2.IMREAD_GRAYSCALE)
# ret,img_binary = cv2.threshold(img_gray, 1, 255, cv2.THRESH_BINARY)
# cv2.imshow('img',img_binary)
# cv2.waitKey(0)
