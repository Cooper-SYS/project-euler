# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()


import datetime
import math
starttime = datetime.datetime.now()
min = 1000
max = 9999
def three(n):
    numbers = []
    while True:
        n = n + 1
        x = n*(n+1)/2
        if x>=min and x<=max: numbers.append('3'+str(x))
        if x>max: return numbers
            
def four(n):
    numbers = []
    while True:
        n = n + 1
        x = n*n
        if x>=min and x<=max: numbers.append('4'+str(x))
        if x>max: return numbers
        
def five(n):
    numbers = []
    while True:
        n = n + 1
        x = n*(3*n-1)/2
        if x>=min and x<=max: numbers.append('5'+str(x))
        if x>max: return numbers
        
def six(n):
    numbers = []
    while True:
        n = n + 1
        x = n*(2*n-1)
        if x>=min and x<=max: numbers.append('6'+str(x))
        if x>max: return numbers
        
def seven(n):
    numbers = []
    while True:
        n = n + 1
        x = n*(5*n-3)/2
        if x>=min and x<=max: numbers.append('7'+str(x))
        if x>max: return numbers
        
def eight(n):
    numbers = []
    while True:
        n = n + 1
        x = n*(3*n-2)
        if x>=min and x<=max: numbers.append('8'+str(x))
        if x>max: return numbers        
        
        
b0 = []
for x in three(0):b0.append(x)
for x in four(0):b0.append(x)
for x in five(0):b0.append(x)
for x in six(0):b0.append(x)
for x in seven(0):b0.append(x)
for x in eight(0):b0.append(x)
        
def getKey(x,y):
    if int(x[0])<int(y[0]):return x[0]+y[0]
    else: return y[0]+x[0]
    
def get4Keys(x,y):
    key=''
    ok = [x[0],y[0],x[6],y[6]]
    for x in range(3,9):
        if str(x) not in ok:
            key=key+str(x)
    return key    

b1 = {}
b2 = {}
for x in range(3,8):
    for y in range(x+1,9):
        key=str(x)+str(y)
        b1[key]=[]
        b2[key]=[]
        
      
def p061(b0):
    #   12345
    for x in b0:
        for y in b0:
            if x[0]!=y[0]:
                if x[1:3]==y[-2:] : 
                    key = getKey(x,y)
                    b1[key].append(y+':'+x) 
                if y[1:3]==x[-2:] : 
                    key = getKey(x,y)
                    b1[key].append(x+':'+y)
           
    # 12345:24567
    
    for xkey in b1:
        for x in b1[xkey]:
            for ykey in b1:
                if xkey==ykey:continue
                for y in b1[ykey]:
                    if x[0]!=y[0] and x[0]!=y[6] and x[6]!=y[0] and x[6]!=y[6]:
                        if x[1:3]==y[-2:] : 
                            key = get4Keys(x,y)
                            b2[key].append(y+':'+x) 
                        if y[1:3]==x[-2:] : 
                            key = get4Keys(x,y)
                            b2[key].append(x+':'+y)
    
    # 73367:46724:82465:56501
   
    
    for xkey in b1:
        for x in b1[xkey]:
            for y in b2[xkey]:
                if x[1:3]==y[-2:] : 
                    bx = y+':'+x
                    if bx[1:3]==bx[33:35]:return bx
                if y[1:3]==x[-2:] : 
                    bx = x+':'+y
                    if bx[1:3]==bx[33:35]:return bx
            
    return False
    
#72512:81281:68128:52882:38256:45625     
digits = p061(b0)
print digits
if digits:
    print int(digits[1:5])+int(digits[7:11])+int(digits[13:17])+int(digits[19:23])+int(digits[25:29])+int(digits[31:35])
            
            
print (edu.time()-ts0)


