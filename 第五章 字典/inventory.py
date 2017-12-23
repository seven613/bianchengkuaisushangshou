#课后习题 游戏装备显示
stuff={'rope':1,'torch':6,'gold coin':42,'dragger':1,'arrow':12}



print('自带装备：')
def displayInvertory(invertory):
    total_num = 0
    for k,v in invertory.items():
        print(k+':'+str(v))
        total_num += v
    print('装备总数是：'+str(total_num))

def addToInvertory(invertory,additems):
    for i in range(additems.__len__()):
        invertory.setdefault(additems[i],0)
        invertory[dragonLoot[i]] +=1

inv={'gold coin':42,'rope':1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInvertory(inv,dragonLoot)

displayInvertory(inv)