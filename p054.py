#coding=utf-8
#!/usr/bin/python
#python2.7.8
from __future__ import division
import datetime
import math

starttime = datetime.datetime.now()

#just test    
def transPoker(player):
    pld=[]
    plf=False
    for idx in range(0,5):
        dt=player[idx][0:1]
        rt=0
        if dt=='A':
            rt=1
        elif dt=='J':
            rt=11
        elif dt=='Q':
            rt=12
        elif dt=='K':
            rt=13
        elif dt=='T':
            rt='-1'
        else:
            rt=int(dt)
        pld.append(rt)
    if player[0][1:2]==player[1][1:2] and player[0][1:2]==player[2][1:2] and player[0][1:2]==player[3][1:2] and player[0][1:2]==player[4][1:2] :
        plf=True
    
    pld.sort()
    return [pld,plf]


def isRoyalFlush():
    print True   

    
def readPoker(line):
    pk=line.split(' ')
    playA=transPoker([pk[0],pk[1],pk[2],pk[3],pk[4]])
    playB=transPoker([pk[4],pk[5],pk[6],pk[7],pk[8]])
    print line
    
 
inputFile=open('p054_poker.txt','r')
for line in inputFile:
    readPoker(line)


print '--------------------------------'  
endtime = datetime.datetime.now()
print('All spent '+str((endtime-starttime).seconds)+' seconds')
