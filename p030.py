# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()

list=[]
for x in range(0,10):
    list.append(x**5)

print list
count=0
'''
9^5=59049，若概数是 n 位的，因为 59049*n > 10^n ; n=7时，59049*7=413343 <10^7;
显然 n 最多为 6 位
'''    
for a in range(0,len(list)):
    for b in range(0,len(list)):
        for c in range(0,len(list)):
            for d in range(0,len(list)):
                for e in range(0,len(list)):
                    for f in range(0,len(list)):
                        if list[a]+list[b]+list[c]+list[d]+list[e]+list[f]==a*100000+b*10000+c*1000+d*100+e*10+f and len(str(list[a]+list[b]+list[c]+list[d]+list[e]))>1:
                            count+=list[a]+list[b]+list[c]+list[d]+list[e]+list[f]
                            print list[a]+list[b]+list[c]+list[d]+list[e]+list[f]
                        
print count

print (edu.time()-ts0)