#coding=utf-8
#!/usr/bin/python
#python2.7.8
from __future__ import division
import datetime

                
starttime = datetime.datetime.now()
fenzi=[3,7]
fenmu=[2,5]

counting=0
for lens in range(2,1000):
    #通过公式推导得出分子分母的算法
    newFenzi=2*fenmu[lens-1]+fenzi[lens-1]
    newFenmu=fenmu[lens-1]+fenzi[lens-1]
    #print newFenzi/newFenmu
    fenzi.append(newFenzi)
    fenmu.append(newFenmu)
    if len(str(newFenzi))>len(str(newFenmu)):
        counting+=1
        
        
print counting
endtime = datetime.datetime.now()
print('All spent '+str((endtime-starttime).seconds)+' seconds')



