# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()


import datetime

def isRepeat(x,x2,x3,x4,x5,x6):
    for num in x:
        if x.count(num)>1:
            return False
    for num in x2:
        if x2.count(num)>1:
            return False
    for num in x3:
        if x3.count(num)>1:
            return False
    for num in x4:
        if x4.count(num)>1:
            return False
    for num in x5:
        if x5.count(num)>1:
            return False
    for num in x6:
        if x6.count(num)>1:
            return False
    return True      
                
def isRepeatOK(x,x2,x3,x4,x5,x6):      
    for num in x:
        flag=False
        if x2.find(num)>-1 and x3.find(num)>-1 and x4.find(num)>-1 and x5.find(num)>-1 and x6.find(num)>-1 :
            flag=True
        if not flag:
            return False
    return True

starttime = datetime.datetime.now()

x=123456
while True:
    if isRepeat(str(x),str(2*x),str(3*x),str(4*x),str(5*x),str(6*x)):
        if isRepeatOK(str(x),str(2*x),str(3*x),str(4*x),str(5*x),str(6*x)) :
            print str(x)+' : '+str(2*x)+' : '+str(3*x)+' : '+str(4*x)+' : '+str(5*x)+' : '+str(6*x)
            break
    x+=1
    
print '-----------------'
print (edu.time()-ts0)



