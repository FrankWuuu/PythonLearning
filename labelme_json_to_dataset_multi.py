import labelme
import os, sys
path="out/" #path to json and img
dirs = os.listdir(path)
i=0
for item in dirs:
   if item.endswith(".json"):
      if os.path.isfile(path+item):
         # print(item)
         file_path = path+item
         my_dest ="out_all/" + str(i)
         print(my_dest)
         os.makedirs(my_dest,exist_ok=True)
         # os.system("mkdir "+my_dest)
         os.system("labelme_json_to_dataset "+file_path+" -o "+my_dest)
         i=i+1
