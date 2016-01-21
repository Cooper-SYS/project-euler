# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()


import datetime

starttime = datetime.datetime.now()
def checkRepeat(lst):
    lst2=lst[:]
    lst2.sort()
    for x in range(1,len(lst2)):
        if lst2[x-1]==lst2[x]:
            return True
    return False
def checkPartRepeat(x,y):
    if x[1]!=y[0] or x[2]!=y[1]:
        return True
    return False
def lst2int(lst):
    rtStr=''
    for x in lst:
        rtStr=rtStr+str(x)
    return int(rtStr)
rtNum=0
    
def check(lst):
    #print lst
    for x in range(0,10):
        if lst.count(x)==0:
            lst.insert(0,x) 
    
    global rtNum
    print lst2int(lst)
    rtNum=rtNum+lst2int(lst)
    return True
    

    
f=[0,1,2,3,4,5,6,7,8,9]
tmpLst1=[]
tmpLst2=[]
tmpLst3=[]
tmpLst4=[]
tmpLst5=[]
tmpLst6=[]
tmpLst7=[]
for x1 in f:
    for x2 in f:
        for x3 in f:
            if x1==x2 or x1==x3 or x2==x3:
                continue
            num=x1*100+x2*10+x3
            tmpLst=[x1,x2,x3]
            if num%2==0:
                tmpLst1.append(tmpLst)
            if num%3==0:
                tmpLst2.append(tmpLst)
            if num%5==0:
                tmpLst3.append(tmpLst)
            if num%7==0:
                tmpLst4.append(tmpLst)
            if num%11==0:
                tmpLst5.append(tmpLst)
            if num%13==0:
                tmpLst6.append(tmpLst)
            if num%17==0:
                tmpLst7.append(tmpLst)



for y1 in tmpLst1:
    for y2 in tmpLst2: 
        if checkPartRepeat(y1,y2):
            continue
        for y3 in tmpLst3: 
            if checkPartRepeat(y2,y3):
                continue
            for y4 in tmpLst4: 
                if checkPartRepeat(y3,y4) or checkRepeat(y1+y4):
                    continue
                for y5 in tmpLst5:
                    if checkPartRepeat(y4,y5):
                        continue
                    for y6 in tmpLst6:
                        if checkPartRepeat(y5,y6):
                            continue
                        for y7 in tmpLst7:
                            if checkPartRepeat(y6,y7) or checkRepeat(y1+y4+y7):
                                continue
                            tmpNew=y1+y4+y7
                            check(tmpNew)
print '-------------'
print rtNum
print (edu.time()-ts0)



