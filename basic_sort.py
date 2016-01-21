#coding=utf-8
#73162890 by hand
import datetime
import math
import random
starttime = datetime.datetime.now()

oriDigit=[]
max=10000
n=0
while n<max:
    n+=1
    oriDigit.append(random.randint(0, max))

    

#spent 13 seconds  
def sortA(digits):
    length=len(digits)
    for x in range(1,length): 
        y=x-1
        while y>=0:
            preD=digits[y]
            backD=digits[y+1]
            if backD<preD:
                digits[y]=backD
                digits[y+1]=preD
            y-=1

            
            
#spent 2 seconds            
def sortB(digits):
    newDigits=[]
    newDigits.append(digits[0])
    length=len(digits)
    newLen=len(newDigits)
    n=1
    while n<length:
        nowD=digits[n]
        newLen=len(newDigits)
        x=0
        flag=True
        while x<newLen:
            if nowD<newDigits[x]:
                newDigits.insert(x,nowD)
                flag=False
                break
            x+=1
        if flag:
            newDigits.append(nowD)
        n+=1
        newLen=len(newDigits)
    return newDigits
                
print oriDigit[max-1]     
sortA(oriDigit)
print oriDigit[max-1]    
#sortB=sortB(oriDigit)
#print sortB[max-1]              
endtime = datetime.datetime.now()
print('All spent '+str((endtime-starttime).seconds)+' seconds')

