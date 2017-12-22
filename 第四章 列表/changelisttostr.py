def change(listparm):

    if type(listparm) != list:
        return '参数不正确 '
    s =''
    for i in range(0,len(listparm) -1):

        s = s+listparm[i]+','

    s = s+'and '+listparm[-1]
    return s


def change2(listparm):
    if type(listparm) != list:
        return "参数不正确"
    return ','.join(listparm[0:-1])+',and '+listparm[-1]


spam = ['apples', 'banana', 'toufu', 'cat']
print(change(spam))
print(change2(spam))