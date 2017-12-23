#字典嵌套 每个客人带了多少水果
allGuests={'张磊':{'苹果':2,'梨':5,'香蕉':12},
           '小靳':{'梨':4,'芒果':10,'桃子':10,'苹果':10},
           '任明':{'西瓜':1,'桔子':15}}

def totalBrought(guests,item):
    numBrought = 0
    for k,v in guests.items():
        numBrought = numBrought +v.get(item,0)
    return numBrought

print('苹果是：'+str(totalBrought(allGuests,'苹果')))
print('梨是：'+str(totalBrought(allGuests,'梨')))
print('西瓜是：'+str(totalBrought(allGuests,'西瓜')))