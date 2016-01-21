# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()

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


print (edu.time()-ts0)