import zipfile

zip_file = zipfile.ZipFile('new.zip','w')
# 把zfile整个目录下所有内容，压缩为new.zip文件
zip_file.write('zfile',compress_type=zipfile.ZIP_DEFLATED)
# 把c.txt文件压缩成一个压缩文件
zip_file.write('c.txt',compress_type=zipfile.ZIP_DEFLATED)
zip_file.close()


path_result = '/kaggle/working/result_map/'
zipName_result = 'result_map.zip'#压缩后文件的位置及名称
f = zipfile.ZipFile( zipName_result, 'w', zipfile.ZIP_DEFLATED )
for dirpath, dirnames, filenames in os.walk(path_result):
    for filename in filenames:
#         print(filename)
        f.write(os.path.join(dirpath,filename))
f.close()
