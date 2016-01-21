# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()

def mini(a,b,sta):
    if a%b==0:
        return a
    else: 
        return mini(a+sta,b,sta)

def p005(list):
    sum=[]
    if len(list)%2==1:
        list.append(1)
    for x in range(0,len(list),2):
        a=list[x]
        b=list[x+1]
        sum.append(mini(a,b,a))    
    if len(sum)==1:
        return sum
    else:
        return p005(sum)

init=[]
for x in range(20,0,-1):
    init.append(x)

result=p005(init)  
print result


print (edu.time()-ts0)