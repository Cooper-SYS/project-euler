# coding:utf-8
'''
Created on 2013-8-14
N>=2
最大的数位987654321，有9位，因此乘数最多4位
@author: zhaoliang
'''
import time
start=time.time()
ini=1
max=123456789
while ini<9876:
    s=''
    x=1
    flag=True
    while len(s)<10:
        if len(s)+len(str(ini*x))<10:
            s=s+str(ini*x)
            x+=1
            for m in range(0,len(s)):
                for n in range(m+1,len(s)):
                    if s[m:m+1]==s[n:n+1]:
                        flag=False
                        break
            if '0' in s:
                flag=False
                break
        else:
            break
    if x>2 and flag and int(s)>max:
        max=int(s)
    ini+=1

print max
print time.time()-start
