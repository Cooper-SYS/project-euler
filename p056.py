#coding=utf-8
#!/usr/bin/python
#python2.7.8

import datetime
import math
starttime = datetime.datetime.now()

max=1 

for a in range(1,100):
    for b in range(1,100):
        pow=a**b
        dig=0
        for x in str(pow):
            dig+=int(x)
        if dig>max:
            max=dig
print max

print '-----------------'

endtime = datetime.datetime.now()
print('All spent '+str((endtime-starttime).microseconds)+' microseconds')