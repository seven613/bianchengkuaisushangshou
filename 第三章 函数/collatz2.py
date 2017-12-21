'''
网上的版本，比较好的写法
'''
import sys

def collatz(number):
    print(number)
    if number == 1:
        sys.exit()
    elif number % 2 == 1:
         collatz(3 * number + 1)
    else:
        collatz(number // 2)

if __name__=='__main__':
    n = input('输入一个数字：')
    try:
        num = int(n)
        collatz(num)
    except ValueError:
        print('值错误，输入的不是一个数字。')
