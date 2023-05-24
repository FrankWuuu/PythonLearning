import os
import cv2

# img_ = cv2.imread('cv2/9.jpg')
# img_mm = cv2.imread('cv2/9_mm.jpg')
# img_gt = cv2.imread('cv2/9_gt.jpg')
# # img_out = img_ * img_mm
# # img_out = cv2.subtract(img_mm,img_)
# img_out = cv2.bitwise_and(img_mm,img_)
# cv2.imshow('img',img_out)
# cv2.imwrite('cv2/9_out.png',img_out)
# # cv2.resizeWindow('img',400,400)
# cv2.namedWindow('img',cv2.WINDOW_AUTOSIZE)
# cv2.waitKey(0)

path_img = 'E:/vision/teeth/data/Tufts_Dental_Database/Radiographs/'
path_mm  = 'E:/vision/teeth/data/Tufts_Dental_Database/Segmentation/maxillomandibular/'
path_out ='output/'
os.makedirs(path_out,exist_ok=True)
img_list = os.listdir(path_img)
print(len(img_list))
for name in img_list:
    img_img = cv2.imread(path_img+name)
    img_mm = cv2.imread(path_mm+name)
    print(name)
    img_out = cv2.bitwise_and(img_mm,img_img)
    cv2.imwrite(path_out+name,img_out)

