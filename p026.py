# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()

from math import sqrt
import time
start=time.time()
max=1
number=1
for x in range(1,1000):
    #分母只含有2或5的任意次方的分数都能化成有限小数
    #除此之外的分数都能化成无限循环小数
    if not x in [1, 2, 4, 5, 8, 10, 16, 20, 25, 32, 40, 50, 64, 80, 100, 125, 128, 160, 200, 250, 256, 320, 400, 500, 512, 625, 640, 800, 1000]:
        
        #排除掉所有的非质数，非质数的倒数的循环节不可能太大，因为它可以被分解
        flag=True
        for w in range(2,int(sqrt(x))+1):
            if x%w==0:
                flag=False
                break
        if not flag:
            continue
        
        #将分母化为 999999....... (k个9）则循环节就有k位
        m=9
        while True:
            if m%x==0:
                break
            m=m*10+9
        leng=len(str(m))    
        if leng>max:
            max=leng
            number=x
            
        #print '--------%d--%d--------' % (x,leng)
    
print '********%d**%d********' % (number,max)
print (edu.time()-ts0)