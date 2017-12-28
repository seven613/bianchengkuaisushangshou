# ! python3
#密码保管
PASSWORDS={
'支付宝登录':'justone',
'淘宝':'justtwo',
'CSDN':'justthree',
'LinkedIn':'justfour',
'gipsy':'justfive',
'小米':'justsix',
'github':'justseven'}

import sys,pyperclip
if len(sys.argv) <2:
    print("使用方法：python pw.py[账号] 密码会自动复制到剪贴板")
    sys.exit()
account = sys.argv[1] #得到第一个参数是 账号

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("密码已经复制到剪贴板")
else:
    print("没有这个账号")