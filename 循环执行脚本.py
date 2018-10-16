# -*-coding:utf-8-*-
# !/usr/bin/env python
# 循环执行deb文件 author 赵梓渊
import os

def check(filename):
    if os.path.splitext(filename)[1] == ".deb":
        return 1
    else:
        return 0
		
def getfile(diskdir):
    list = os.listdir(diskdir)
    for i in range(0, len(list)):
        path = os.path.join(diskdir, list[i])
        if os.path.isfile(path) & check(path):
            name = os.path.splitext(os.path.basename(path))[0]
            print "|-----",name
            os.system("dpkg -i "+ name +".deb") 

if __name__ == '__main__':
    getfile('/deb')
