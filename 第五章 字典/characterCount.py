message = 'It was a bright cold day in April,and the clocks were striking thirteen.'
count={} # 初始化字典

for character in message:#循环每个字符
    count.setdefault(character,0) # 如果字符没有，添加到字典，并且默认出现次数为0
    count[character] =  count[character] + 1 # 字符已经存在，出现一次 就加1

print (count)