birthdays={'Alcie':'3月12日','Bob':'5月17日','carol':'10月1日'}

while True:
    print('请输入人名或者退出')
    name =input()
    if name =='':
        break
    if name in birthdays:
        print(name +'的生日是'+birthdays[name])
    else:
        print(name+'的生日还没有，请添加')
        bday =input()
        birthdays[name]=bday
        print(name+'的生日已更新')
