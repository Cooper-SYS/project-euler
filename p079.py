#coding=utf-8
#!/usr/bin/python
#python2.7.8


#73162890 by hand
import datetime
import math
starttime = datetime.datetime.now()

inputFile = open('p079_keylog.txt','r')
spe=0;
pwdLs=[]
letterLs=set()
for line in inputFile:
    if int(line)>0:
        for le in str(int(line)):
            letterLs.add(int(le))
        pwdLs.append(int(line))

        

print "this shows the minimal width of password : "+str(len(letterLs))

lens=len(letterLs)
flag=False
base=[0,1,2,3,4,5,6,7,8,9]  
nLen=len(pwdLs)
n=0
while n<nLen:
    sD=pwdLs[n]
    s1=int(str(sD)[0:1])
    s2=int(str(sD)[1:2])
    i1=base.index(s1)
    i2=base.index(s2)
    if i1>i2:
        tmp=base[i1]
        base[i1]=base[i2]
        base[i2]=tmp
    i2=base.index(s2)
    s3=int(str(sD)[2:3])
    i3=base.index(s3)
    if i2>i3:
        tmp=base[i2]
        base[i2]=base[i3]
        base[i3]=tmp
    n+=1

pwd=[]    
for x in base:
    if x in letterLs:
        pwd.append(x)
print pwd

    

endtime = datetime.datetime.now()
print('All spent '+str((endtime-starttime).seconds)+' seconds')

