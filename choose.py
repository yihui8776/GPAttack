import os, sys
import random
import shutil
import time


def getJpg(filename: str):
    return filename.endswith("jpg")


def getFile(fileDir, toFileDir, number):
    path = os.path.abspath(fileDir) + "/"
    path.replace("\\", "/")
    if os.path.isdir(fileDir):
        pathList = os.listdir(fileDir)
        jpgList = [i for i in filter(getJpg, pathList)]
        if jpgList:
            try:
                sample = random.sample(jpgList, number)
            except:
                print("某层文件夹图片数量不够")
                return
            for name in sample:
                try:
                    shutil.move(path + name, toFileDir)
                except:
                    filename = str(time.time()).replace('.', '') + ".jpg"
                    path = path.replace("\\", "/")
                    os.rename(path + name, path + filename)
                    shutil.move(path + filename, toFileDir)
        dirList = set(pathList) - set(jpgList)
        if dirList:
            for dir in dirList:
                getFile(path + dir, toFileDir, number)


if __name__ == "__main__":
    # fileDir = input("请输入处理文件夹：")
    # if not os.path.isdir(fileDir):
    #     print("输入错误!")
    #     ss.exit()
    fileDir='E:/data/coco/train2017'
    toFileDir='./image/'
    # toFileDir = input("请输入目标文件夹：")
    # if not os.path.isdir(toFileDir):
    #     print("输入错误!")
    #     sys.exit()
    number = input("请输入随机抽取图片数量：")
    if not number.isdigit() or int(number) <= 0:
        print("输入错误!")
        sys.exit()
    getFile(fileDir, toFileDir, int(number))
