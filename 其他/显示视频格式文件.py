#显示当前电脑里的视频文件
import  os

def search_file(start_dir,target): #定义函数，参数：路径；目标文件
    os.chdir(start_dir)# 目标路径变为当前路径

    for each_file in os.listdir(os.curdir):#循环当前路径下的每个文件
        ext = os.path.splitext(each_file)[1]#os.path.splitext(each_file)把文件分为文件名和扩展名两部分的元组，因此取索引1
        if ext in target:#判断扩展名是否在目标里
            vedio_list.append(os.getcwd() + os.sep+ each_file + os.linesep)#列表扩展，补齐当前系统的分隔符和结束符
        if os.path.isdir(each_file):#如果上个if没有执行，有可能是文件夹
            search_file(each_file,target)#递归执行下一级路径   !注意：python的递归是有深度限制的，太多了就不能递归了
            os.chdir(os.pardir)#必须返回上一级目录

start_dir = input('请输入待查找的初始目录：')
program_dir = os.getcwd()

target =['.mp4','.avi','.rmvb']
vedio_list=[]

search_file(start_dir,target)

f= open(program_dir+os.sep+'vedioList.txt','w')
f.writelines(vedio_list)
f.close()
