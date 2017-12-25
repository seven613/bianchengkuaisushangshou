#字符串左对齐、右对齐、中间对齐
def printPicnic(itemsDict,leftWidth,rightWidth): #定义了函数，包括三个变量，字典，左对齐补齐长度，右对齐补齐长度
    print('PICNIC ITEMS'.center(leftWidth+rightWidth,'-'))#打印表名，表名居中，左对齐+右对齐
    for k,v in itemsDict.items():#循环字典，活动字典的key，value
        print(k.ljust(leftWidth,'.')+str(v))#key的类型是字符，value的类型是数字，输出

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems,12,5)
printPicnic(picnicItems,20,6)