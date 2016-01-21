# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()

import time
start=time.time()
max=1001
list=[]
for x in range(0,max):
    list.append([])
    for y in range(0,max):
        list[x].append(0)

ix=500
iy=500
direc=3   #0向右    1向下    2向左   3向上   
for num in range(1,max*max+1):
    #print str(ix)+':'+str(iy)
    list[ix][iy]=num
    if direc==0 and list[ix+1][iy]==0:  #如果原来向右，则尽量向下
        #print '向下'
        direc=1
    elif direc==1 and list[ix][iy-1]==0:  #如果原来向下，则尽量向左
        #print '向左'
        direc=2
    elif direc==2 and list[ix-1][iy]==0:  #如果原来向左，则尽量向上
        #print '向上'
        direc=3
    elif direc==3 and list[ix][iy+1]==0:  #如果原来向上，则尽量向右
        #print '向右'
        direc=0
    #print 'direction: %d (%d %d)' % (direc,ix,iy)   
    if direc==0:
        iy=iy+1
    if direc==1:
        ix=ix+1
    if direc==2:
        iy=iy-1
    if direc==3:
        ix=ix-1

index=0
number=0
for x in range(0,max) :
    number=number+list[x][index]+list[x][max-index-1]
    if index==max-index-1:
        number=number-list[x][index]
    index+=1
 
print number
print (edu.time()-ts0)