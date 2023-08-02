import gzip
import os
import PIL
from PIL import Image

path_sour = 'labels-ah'
path_dest = 'labels_ah_ppm/'
os.makedirs(path_dest,exist_ok=True)

def ungzip(path_sour, path_dest):
    """
    im0001.ah.ppm.gz to im0001.ah.ppm
    """
    g_file = gzip.GzipFile(path_sour)
    with open(path_dest, '+wb') as f:
        f.write(g_file.read())

def ppm2jpg(path_sour,path_dest):
    img = Image.open(path_sour)
    img.save(path_dest)


name_list = os.listdir(path_sour)
# for name in name_list:
#     name = name.split('.')[0]
#     path_s = path_sour + "/" + name + ".ah.ppm.gz"
#     path_d = path_dest + "/" + name + "_ah.ppm"
#     ungzip(path_s, path_d)
#     # print(name)

path_ppm_sour = "all-images/"
path_ppm_dest = "all_images/"
os.makedirs(path_ppm_dest,exist_ok=True)
name_list = os.listdir(path_ppm_sour)
for name in name_list:
    name = name.split('.')[0]
    path_s = path_ppm_sour + name + ".ppm"
    path_d = path_ppm_dest + name + ".jpg"
    ppm2jpg(path_s, path_d)
    # print(name)

