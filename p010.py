# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()


def p010():
    sum = 2
    min = 3 
    max = 2000000
    i = min
    for i in range(min,max,2):
        if edu.isPrime(i):sum+=i
    return sum


    
print p010()

print (edu.time()-ts0)