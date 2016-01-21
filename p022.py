# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()

list=[]
filename='p022_names.txt'
file=open(filename,'r')
line=file.readline()
list=line.split(',')
list.sort()
count=0
for x in range(0,len(list)):
    sum=0
    for y in range(0,len(list[x])):
        alpha=list[x][y:y+1]
        if alpha!='"':
            sum+=ord(alpha)-64
            
    #print '%s  %d×%d=%d' % (list[x],x+1,sum,sum*(x+1))
    count+=(sum*(x+1))
    
print count
print (edu.time()-ts0)


