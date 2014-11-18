# coding:utf-8
'''
Created on 2013-8-8

@author: zhaoliang
'''
list=[]
filename='p067_triangle.txt'
file=open(filename,'r')
for line in file.readlines():
    list.append(line.split(" "))

for x in range(0,len(list)):
    for y in range(0,len(list[x])):
        list[x][y]=int(list[x][y])
    
for x in range(len(list)-1,0,-1):
    for y in range(len(list[x])-1,0,-1):
        if list[x][y]>list[x][y-1]:
            list[x-1][y-1]=(list[x-1][y-1])+list[x][y]
        else:
            list[x-1][y-1]=list[x-1][y-1]+list[x][y-1]

print list[0]