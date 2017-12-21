#collatz函数#参数是偶数 打印number//2,并返回number
#参数是奇数 打印3*number+1,并返回3*number+1
#写一个程序，输入整数，不断的调用collatz，知道返回值=1

#先写函数
def collatz(number):
    if number %2 ==0:
        print(number//2)
        return number
    elif number %2 ==1:
        print(3*number+1)
        return 3*number+1
    else:
        print('输入不是正整数')
        return None

try:
    number =int(input())
except:
    print('输入错误')

while number != 1:
    collatz(number)
