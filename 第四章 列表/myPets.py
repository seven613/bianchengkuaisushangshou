myPets = ['老大','老二' ,'小三']

name = input('输入宠物的名字')
if name not in myPets:
    print('这不是我的宠物')
else:
    print('哈哈，'+name+'是我的宠物')