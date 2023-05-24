import os
import cv2

# path_sour = "out_gt/"
# path_dest = "out_bina/"
# os.makedirs(path_dest, exist_ok=True)
# file_list = os.listdir(path_sour)
# for file in file_list:
#     # print(file)
#     img_gray = cv2.imread(path_sour + file, cv2.IMREAD_GRAYSCALE)
#     ret, img_binary = cv2.threshold(img_gray, 1, 255, cv2.THRESH_BINARY)
#     cv2.imwrite(path_dest +'gt_'+ file, img_binary)

img_ = cv2.imread('cv2/9.jpg')
img_mm = cv2.imread('cv2/9_mm.jpg')
img_gt = cv2.imread('cv2/9_gt.jpg')
# img_out = img_ * img_mm
# img_out = cv2.subtract(img_mm,img_)
img_out = cv2.bitwise_and(img_mm,img_)
cv2.imshow('img',img_out)
cv2.imwrite('cv2/9_out.png',img_out)
# cv2.resizeWindow('img',400,400)
cv2.namedWindow('img',cv2.WINDOW_AUTOSIZE)
cv2.waitKey(0)
