import os
import glob
import numpy as np

''' 处理.txt文件'''
if __name__ == '__main__':
 # os.chdir('E:/vision/MI/lesions/result/PVTPra/eval/EvaluateResults_PVTPraThreeV1/')
 # for i in glob.glob('*.txt'):
 #  print(i)
 path  = 'E:/vision/MI\lesions/result/PVTPra/eval/EvaluateResults_TransPraP/'
 os.chdir(path)
 name = []
 for file in glob.glob('*.txt'):
  name.append(file)
 # print(name)
 total = []
 for i in range(5):
  fr = open(name[i])
  line = fr.readline()
  items = line.strip().split(')')
  useful = items[1].split(';')
  useful = np.concatenate([useful[:4], useful[6], useful[5]], axis=None)
  # print(useful)
  for  i in range(6):
   useful[i] = useful[i].split(':')[1]
  # print(score)
  total = np.concatenate([total,useful], axis=None)
 tplt_title = "{0:^8}\t{1:^9}\t{2:^7}\t{3:^8}\t{4:^3}\t{5:^6}\t{6:^3}"
 tplt_num= "{0:^11}\t{1:^1}\t{2:^7}\t{3:^1}\t{4:^6}\t{5:^1}"
 # print("CVC300", end=' '),print(tplt.format(total[0:6], chr(12288)))
 temp = total.astype(np.float16) #  先将np转为astype，类型转换float
 title = ['method ', 'meanDice', 'meanIOU', 'wFm', 'Sm', 'maxEm', 'MAE']
 dataset = ["CVC300  ", "ClinicDB", "ColonDB ", "ETIS    ", "Kvasir  "]
 print(tplt_title.format(title[0], title[1],title[2],title[3],title[4],title[5],title[6]))
 # print("CVC300  ", end=' '),print(tplt_num.format("%.3f"%temp[0], "%.3f"%temp[1],"%.3f"%temp[2],"%.3f"%temp[3],"%.3f"%temp[4],"%.3f"%temp[5],chr(12288)))
 # print("ClinicDB", end=' '),print(tplt_num.format("%.3f"%temp[6], "%.3f"%temp[7],"%.3f"%temp[8],"%.3f"%temp[9],"%.3f"%temp[10],"%.3f"%temp[11],chr(12288)))
 # print("ColonDB ", end=' '),print(tplt_num.format("%.3f"%temp[12], "%.3f"%temp[13],"%.3f"%temp[14],"%.3f"%temp[15],"%.3f"%temp[16],"%.3f"%temp[17],chr(12288)))
 # print("ETIS    ", end=' '),print(tplt_num.format("%.3f"%temp[18], "%.3f"%temp[19],"%.3f"%temp[20],"%.3f"%temp[21],"%.3f"%temp[22],"%.3f"%temp[23],chr(12288)))
 # print("Kvasir  ", end=' '),print(tplt_num.format("%.3f"%temp[24], "%.3f"%temp[25],"%.3f"%temp[26],"%.3f"%temp[27],"%.3f"%temp[28],"%.3f"%temp[29],chr(12288)))
 for i in range(5):
  temp_line = []
  for j in range(6):
   temp_line.append(temp[i*6+j])
  print(dataset[i], end=' '), print(tplt_num.format("%.3f"%temp_line[0],"%.3f"%temp_line[1],"%.3f"%temp_line[2],"%.3f"%temp_line[3],"%.3f"%temp_line[4],"%.3f"%temp_line[5]))
 # print("CVC300  ", end=' '),print(temp[0:6])
 # print("ClinicDB", end=' '),print(temp[6:12])
 # print("ColonDB ", end=' '),print(temp[12:18])
 # print("ETIS    ", end=' '),print(temp[18:24])
 # print("Kvasir  ", end=' '),print(temp[24:30])
