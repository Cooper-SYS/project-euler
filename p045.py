# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()



'''
Tn=n(n+1)/2
Pn=n(3n-1)/2
Hn=n(2n-1)
T285=P165=H143
'''

import datetime

starttime = datetime.datetime.now()

flag = False

n=144
tph=[]
ta=set()
pa=set()
ha=set()
while not flag:
    tn = n*(n+1)/2 
    pn = n*(3*n-1)/2
    hn = n*(2*n-1)
    ha.add(hn)
    
    if pn in ha:
        pa.add(pn)
    
    if tn in pa:
        flag=True
        print str(n)+':'+str(tn)
    
    n+=1
    
    
    
print '-----------------'
print (edu.time()-ts0)



