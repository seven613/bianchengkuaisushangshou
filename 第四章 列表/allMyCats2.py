cats=[]

while True:
    print('请输入第'+str(len(cats)+1)+'只猫的名字 或者直接退出')
    name =input()
    if name == '':
        break

    cats = cats +[name]

print('这'+str(len(cats))+'只猫是：')
for name in cats:
    print(name)