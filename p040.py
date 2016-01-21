# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()

'''
Created on 2013-8-14

@author: zhaoliang
'''
import time
start=time.time()
index=1
st=''
while len(st)<1000000:
    st=st+str(index)
    index+=1
ji=int(st[9])*int(st[99])*int(st[999])*int(st[9999])*int(st[99999])*int(st[999999])
print ji
print (edu.time()-ts0)