#coding=utf-8
#!/usr/bin/python
#python2.7.8

import datetime

def getNum(n,r):
    top=1
    botLeft=1 
    botRight=1
    
    for x in range(2,n+1):
        top *= x 
    for x in range(2,r+1):
        botLeft *= x
    for x in range(2,n-r+1):
        botRight *= x
    return int(top/botLeft/botRight)      
                
starttime = datetime.datetime.now()

x=123456
n=1
ctArr=[]
while True:
    for r in range(1,n+1):
        numb=getNum(n,r)
        if numb>1000000:
            print str(n)+':'+str(r)+":"+str(numb)
            ctArr.append(numb)
    n+=1
    if n>100:
        break

print '-----------------'
print len(ctArr)        
print '-----------------'
endtime = datetime.datetime.now()
print('All spent '+str((endtime-starttime).microseconds)+' microseconds')



