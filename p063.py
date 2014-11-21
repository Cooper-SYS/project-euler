#coding=utf-8
#!/usr/bin/python
#python2.7.8
'''
len(pow(10,x))=x+1
为了使得len(pow(n,x))=x
x<10，即x in range(1,10)

穷举，当len(pow(n,x)) != x 时 break
'''

import datetime
import math
starttime = datetime.datetime.now()
counting=0

for n in range(1,10):
    x=1 
    while True:
        num=pow(n,x)
        numLen=len(str(num))
        if numLen==x:
            counting+=1
            print str(counting)+'\t: pow( '+str(n)+' , '+str(x)+' )'+'='+str(num)
        else:
            break
        x+=1
            
    n+=1
print '----------------------------'
print counting

endtime = datetime.datetime.now()
print('All spent '+str((endtime-starttime).seconds)+' seconds')