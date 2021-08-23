import os, random, shutil

path_image_old = 'E:/vision/MI/lesions/data/path_old/' # path_old
path_image_new = 'E:/vision/MI/lesions/data/path_new/' # path_new

def moveFile(path_image_old, path_image_new):
    pathDir = os.listdir(path_image_old)  # old path of original files
    NUM_TOTAL = len(pathDir)
    RATE = 0.35
    NUM_NEW = int(RATE * NUM_TOTAL) #   the num of the files that will be moved
    sample = random.sample(pathDir, NUM_NEW)  # files that will be moved
    print(sample)
    for name in sample:
        shutil.move(path_image_old + name, path_image_new + name)
    return

if __name__ == '__main__':
    moveFile(path_image_old, path_image_new)
