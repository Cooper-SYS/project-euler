#coding=utf-8
#!/usr/bin/python
#python2.7.8

import datetime
import math
starttime = datetime.datetime.now()
def calc(n):
    nxt=0
    while n>=10:
        nxt += (n%10)**2
        n /= 10
    nxt += n**2
    return nxt

n=max

base89=set()
for n in range(1,568):
    tmp=n
    while tmp!=1 and tmp!=89:
        tmp=calc(tmp)
    if tmp==89:
        base89.add(n)

result=set()
max=9999999
for x in range(1,max+1):
    ts=calc(x)
    if ts in base89:
        result.add(x)

print len(result)
endtime = datetime.datetime.now()
print('All spent '+str((endtime-starttime).seconds)+' seconds')

