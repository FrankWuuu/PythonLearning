import os
import shutil

path_sour = 'out_all/'
path_dest = 'out_gt/'

os.makedirs(path_dest,exist_ok=True)

file_name = os.listdir(path_sour)
for file in file_name:
    # print(file)
    shutil.copy(path_sour+file+'/label.png',path_dest+file+'.png')