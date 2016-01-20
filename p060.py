#coding=utf-8
#!/usr/bin/python
#python2.7.8
#有一个假定是替换的位数是3位，并且正好是全部替换，觉得不是太合理，但有可能是数学问题就不深究了
import datetime
import math
starttime = datetime.datetime.now()

def isPrime(x):
    if x<2: return False
    elif x==2: return True
    elif x==3: return True
    else:
        for tmp in range(3,int(math.sqrt(x))+1):
            if x%tmp==0:
                return False
    return True

def iHateU(ls):
    j = ls[len(ls)-1]
    for i in ls:
        if i==j:continue
        if not isPrime(int(i+j)) or not isPrime(int(j+i)):
            return False
    return True  

    
def p060():    
    min = 3  
    max = 10000   
    primes = [str(x) for x in range(min,max,2) if isPrime(x)]
    sz = len(primes)
    
    for idx0 in range(0,sz-4):
        ls = [primes[idx0]]
        for idx1 in range(idx0+1,sz-3):
            ls = [primes[idx0],primes[idx1]]
            if not iHateU(ls):continue
            for idx2 in range(idx1+1,sz-2):
                ls = [primes[idx0],primes[idx1],primes[idx2]]
                if not iHateU(ls):continue
                for idx3 in range(idx2+1,sz-1):
                    ls = [primes[idx0],primes[idx1],primes[idx2],primes[idx3]]
                    if not iHateU(ls):continue
                    for idx4 in range(idx3+1,sz):
                        ls.append(primes[idx4])
                        ls = [primes[idx0],primes[idx1],primes[idx2],primes[idx3],primes[idx4]]
                        
                        if iHateU(ls):
                            return ls   
ls = p060()
print ls
sum = 0    
for x in ls:
    sum = sum + int(x) 
print sum


print('All spent '+str((datetime.datetime.now()-starttime).seconds)+' seconds') 


