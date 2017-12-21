
'''
网上的版本，函数一样，循环不一致
'''
def collatz(number):
    if number % 2 == 0:
        print(number //2)
        return number //2
    else:
        print(3 * number +1)
        return 3 * number + 1

while True:
    num =int(input())
    result=collatz(num)
    if result == 1:
        break
