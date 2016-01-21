# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()

#有一个假定是替换的位数是3位，并且正好是全部替换，觉得不是太合理，但有可能是数学问题就不深究了
import datetime
import math
starttime = datetime.datetime.now()

def isPrime(x):
    for tmp in range(3,int(math.sqrt(x))+1):
        if x%tmp==0:
            return False
    return True


addtion = [
    #一位
    #[10,20,30,40,50,60,70,80,90],
    #[100,200,300,400,500,600,700,800,900],
    #[1000,2000,3000,4000,5000,6000,7000,8000,9000],
    #[10000,20000,30000,40000,50000,60000,70000,80000,90000],
    #二位
    #[110,220,330,440,550,660,770,880,990],
    #[1100,2200,3300,4400,5500,6600,7700,8800,9900],
    #[1010,2020,3030,4040,5050,6060,7070,8080,9090],
    #[10010,20020,30030,40040,50050,60060,70070,80080,90090],
    #[11000,22000,33000,44000,55000,66000,77000,88000,99000],
    #三位
    [1110,2220,3330,4440,5550,6660,7770,8880,9990],
    [10110,20220,30330,40440,50550,60660,70770,80880,90990],
    [11010,22020,33030,44040,55050,66060,77070,88080,99090],
    [101010,202020,303030,404040,505050,606060,707070,808080,909090],
    [11100,22200,33300,44400,55500,66600,77700,88800,99900],
    #四位
    [11110,22220,33330,44440,55550,66660,77770,88880,99990],
    [101110,202220,303330,404440,505550,606660,707770,808880,909990],
    [110110,220220,330330,440440,550550,660660,770770,880880,990990],
    [111010,222020,333030,444040,555050,666060,777070,888080,999090],
    #五位
    [111110,222220,333330,444440,555550,666660,777770,888880,999990],
]

def checkBit(bit,digit):
    init = 0
    bit = (6-len(bit))*'0' + bit
    
    ds = []
    for i in range(0,6):
        if bit[i] == '0':
            continue
        ds.append(int(digit[i])-int(bit[i]))
    if bit.count('1') == 1: 
        return True   
    for x in range(0,len(ds)-1):
        for y in range(x,len(ds)):
            if ds[x] != ds[y]:
                return False
    return True

    
min = 100001  
max = 999999   
primes = [str(x) for x in range(min,max,2) if isPrime(x)]

print('All spent '+str((datetime.datetime.now()-starttime).seconds)+' seconds') 

#这是我自己写的算法
def kepler(primes):
    for start in primes:
        c0 = start[:-1].count('0')
        c1 = start[:-1].count('1')
        c2 = start[:-1].count('2')
        mc = c0
        if c0<c1:mc=c1
        if mc<c2:mc=c2
        for x in addtion:
            x0 = str(x[0])
            if x0.count('1')>mc:continue
            if not checkBit(x0,start):
                continue
            failTimes = 0    
            numbers = [start]
            for y in x:
                fc = int(start)+y
                if str(fc) in primes and checkBit(str(y),start):
                    numbers.append(str(fc))
                else:
                    failTimes = failTimes + 1
                    if failTimes>3:
                        break
            if len(numbers)==8:
                print 'adding bit is ' + str(x[0])
                return numbers
print kepler(primes)
  

print('All spent '+str((datetime.datetime.now()-starttime).seconds)+' seconds')  
#这个算法是从论坛拔下来的  
def P051(primes):
    primeset=set(primes)
    def repd(x):
        if x[:-1].count("0")==3 and x[-1]!="0":  return "0"
        elif x[:-1].count("1")==3 and x[-1]!="1": return "1"
        elif x[:-1].count("2")==3 and x[-1]!="2": return "2"
    
    def eight(x,rd):
        count=0
        numbers = []
        for d in "0123456789":
            y=x.replace(rd,d)
            
            if y in primeset:
                count+=1
                numbers.append(y)
                
        if count==8: 
            print numbers 
            return True
        else: 
            return False
    
    for x in primes:
        if repd(x):
            if eight(x,repd(x)):
                return x
    
print P051(primes)

print (edu.time()-ts0)

