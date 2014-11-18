# coding:utf-8
'''
Created on 2013-8-13
若n的位全为9，位数则不超过7；
若n的位全为8，为数则不超过6；
由此可得n<=9999999

0！=1，注意(0的阶乘是存在的)

@author: zhaoliang
'''
import time
start=time.time()
list=[1]
result=[]
ini=1
for x in range(1,10):
    ini=ini*x
    list.append(ini)

num=0
for n in range(3,362880*9+1):
    if n==sum( list[int(d)] for d in str(n) ):
        num+=n
    #time.sleep(0.2)
    
    
print num
print time.time()-start

    