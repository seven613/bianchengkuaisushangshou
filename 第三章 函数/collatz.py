'''
by 张强 2017.12.21
'''
#collatz函数#参数是偶数 打印number//2,并返回number
#参数是奇数 打印3*number+1,并返回3*number+1
#写一个程序，输入整数，不断的调用collatz，知道返回值=1

#先写函数
def collatz(number):

    if number % 2 == 0:
        print(number//2)
        return number//2
    else:
        print(3 *number + 1)
        return 3 * number + 1

b = True
while b:
    try:
        number = int(input())
        b = False
    except:
        print('请重新输入')


while number != 1:
    number = collatz(number)