# coding:utf-8
'''
Created on 2013-8-7

@author: zhaoliang
'''
def mini(a,b,sta):
    if a%b==0:
        return a
    else: 
        return mini(a+sta,b,sta)

def start(list):
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
        return start(sum)

init=[]
for x in range(20,0,-1):
    init.append(x)

result=start(init)  
print result