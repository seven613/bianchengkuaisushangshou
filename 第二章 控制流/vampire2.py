
#if elif 按顺序执行，如果条件达成就运行代码块
name = input()

if name =='Alice':
    print('Hi,Alice.')
elif age <12:
    print('You are not Alice,kiddo.')
elif age>100:
    print('You are not Alice,grannie.')
elif age > 2000: #永远不会执行
    print('Unlike you, Alice is not an undead,immortal vampire.')