#coding=utf-8
#!/usr/bin/python
#python2.7.8
from __future__ import division
import datetime
import math

starttime = datetime.datetime.now()

inputFile=open('p081_matrix5.txt','r')
matrix=[]

count=0
for line in inputFile:
    matrix.append(map(int,line.split(',')))
    
max=len(matrix)

trace=[]
trace.append([{'x':0,'y':0,'v':matrix[0][0]}])
x=0
y=0

moves=1
while moves<160:
    print str(moves)+' '+str(len(trace))
    for idx in range(0,len(trace)):
        #print 'one trace started'
        pt=trace[idx]   #向右
        #print 'already moved '+str(len(pt))+' moves , '+str(moves)
        
        if len(pt)>moves:
            continue
        
        lastPt=pt[len(pt)-1]
       
        #向右走
        rtx=lastPt['x']+1
        rty=lastPt['y']
        #向下走
        dny=lastPt['y']+1
        dnx=lastPt['x']
        
        if rtx<max and dny<max :
            newPt=pt[:]  
            pt.append({'x':rtx,'y':rty,'v':matrix[rtx][rty]})
            newPt.append({'x':dnx,'y':dny,'v':matrix[dnx][dny]})
            trace[idx]=pt
            trace.append(newPt)
        elif rtx<max:
            pt.append({'x':rtx,'y':rty,'v':matrix[rtx][rty]})
            trace[idx]=pt
        elif dny<max:
            pt.append({'x':dnx,'y':dny,'v':matrix[dnx][dny]})
            trace[idx]=pt
        
    moves+=1

small=1000000    
st=[]
for tt in trace:
    counting=0
    for pt in tt:
        counting+=pt['v']
    
    if counting<small:
        st=tt
        small=counting
print '-----------------'
print 'the smallest path countting is : ' + str(small)
print 'the path is :'
path=[]
for x in st:
    path.append(x['v'])
print path
endtime = datetime.datetime.now()
print('All spent '+str((endtime-starttime).seconds)+' seconds')