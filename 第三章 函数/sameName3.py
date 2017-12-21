def spam():
    global eggs
    eggs ='spam' #全局变量

def bacon():
    eggs ='bacon' #局部变量

def ham():
    print(eggs) # 输出全局变量

eggs = 42 #全局变量赋值
spam()
print(eggs)