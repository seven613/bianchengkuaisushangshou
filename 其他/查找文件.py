'''获取指定目录及其子目录下的py文件路径说明：l用于存储找到的py文件路径
get_py函数，递归查找并存储文件路径于l🔝'''

import os
import os.path

l=[]
def get_py(path,l):
    fileList = os.listdir(path)#获取路径下的所有文件包括文件夹

    for filename in fileList:#循环每一个文件，包括文件夹
        pathTmp = os.path.join(path,filename)#添加文件的全部路径

        if os.path.isdir(pathTmp):#判断是否为文件夹
            get_py(pathTmp,l) #确定是文件夹，递归执行该函数
        elif filename[-3:].upper()=='.PY':#确定不是文件夹，是文件，取文件的后缀转为大写，判断是否是.py
            l.append(pathTmp)#如果是文件并且后缀.py添加到列表里

path =input("请输入路径：").strip() #提示输入一个路径
get_py(path,l)#执行函数
print('在%s目录及子目录下找到的%d个py文件\n分别为：\n'%(path,len(l))) #输出
for filepath in l:
    print(filepath+'\n')
