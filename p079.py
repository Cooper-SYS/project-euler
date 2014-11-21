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
            letterLs.add(le)
        pwdLs.append(int(line))

        

print "this shows the minimal width of password : "+str(len(letterLs))

lens=len(letterLs)
flag=False
base=[]  #存数字的字符格式
#insert(i,x) 把元素x 插入到位置i
#index(x) 返回数组中第一个值为x的位置。如果没有匹配的元素会抛出一个错误
#count(x) 返回x在数组中出现的次数

newPwd=list(pwdLs)
newPwd.sort()            
        
print newPwd

endtime = datetime.datetime.now()
print('All spent '+str((endtime-starttime).seconds)+' seconds')

