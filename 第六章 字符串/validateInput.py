#年龄验证
while True:
    print('请输入年龄：')
    age = input()
    if age.isdecimal(): #如果是数字就执行退出循环
        break
    print("请输入一个数字")
#密码验证
while True:
    print("请输入一个密码，只能包括数字和字母")
    password = input()
    if password.isalnum():#如果是数字和字母就退出循环
        break
    print("请输入只有字母和数字的密码")