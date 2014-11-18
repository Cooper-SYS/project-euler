# coding:utf-8
'''
Created on 2013-8-14
这是别人的程序，我没太看懂
@author: zhaoliang
'''
import math, time
def gcd(a,b):
    while b:
        a, b = b, a%b
    return a

def f(m):
    then = time.time()
    z = [0]*(m+1)
    for u in xrange(1, 1+int((math.sqrt(4*m+1)-3)/4)):
        for v in xrange(u+1, 1+int((math.sqrt(u**2+2*m)-u)/2), 2):
            if gcd(u, v) == 1:
                s = t = 2*v*(u+v)
                while s <= m:
                    z[s] += 1
                    s += t
    t = 0
    for i in xrange(1, m+1):
        if t < z[i]:
            t = z[i]
            s = i
    print s, 'in', time.time()-then, 'seconds'
    
f(1001)