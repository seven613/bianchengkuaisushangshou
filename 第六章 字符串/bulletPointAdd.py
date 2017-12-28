# 行首 添加固定字符*

import pyperclip

text = pyperclip.paste() #从剪贴板获取文本

lines =text.spilt('\n')  #把文本按照换行符分解成一个list
for i in range(len(lines)):#循环列表，每个列表项加*
    lines[i]='*'+lines[i]

text = '/n'.join(lines)#把列表再组合成一段文字

pyperclip.copy(text)#把整理好的文本发到剪贴板
