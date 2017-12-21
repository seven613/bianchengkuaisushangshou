'''
网上的版本，代码有毒
'''
def collatz(number):
    if number % 2 == 0:
        print('number // 2 = '+str(number//2))
        return number // 2
    elif number % 2 == 1:
        print('3 * number + 1 = '+str(3 * number + 1))
        return 3 * number + 1


# 下面这段代码有毒 网上的版本
print('这是一个collatz项目，请输入exit退出程序')
quitFlag ='' #判断用户是否开始计算
conExit = '' #退出程序的阀门

while conExit != 'Exit':
    print('你是否想继续，Yes or No')
    if quitFlag == 'Yes':
        try:
            print('请输入一个数字')
            useInput = int(input())
            while True:
                userInput=collatz(userInput)
                print(userInput)
                if userInput == 1:
                    break
        except ValueError:
            print('请输入一个正整数')
    elif quitFlag == 'No':
        print('程序退出')
        conExit = 'Exit'
