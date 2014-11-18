# coding:utf-8
'''
Created on 2013-8-8
对表格从右下角向左上角依次累积
每个点都写上数字
@author: zhaoliang
'''
list=[]
for x in range(0,21):
    list.append([])
    for y in range(0,21):
        list[x].append(1)
#list[20][20]=0

for y in range(19,-1,-1):
    for x in range(19,-1,-1):
        #print str(x)+','+str(y)
        list[x][y]=list[x][y+1]+list[x+1][y]
     
# for x in list:
#     print x
print list[0][0]