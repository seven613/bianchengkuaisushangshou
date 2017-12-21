while True:
    print('Who are you?')
    name =input()
    if name != 'Joe':
        continue  #条件成立，跳出下面代码块
    print('Hello,Joe.What is th password?(It is a fish.)')
    password = input()
    if password =='swordfish':
        break
print('Access granted.')