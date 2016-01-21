# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()

from __future__ import division
import datetime
import math

starttime = datetime.datetime.now()

def getMin(x,y):
    if x<y:
        return x 
    return y
def showMatrix(matrix):
    print '--------------------------------'  
    for line in matrix:
        print line
    print '--------------------------------'    
def calc(ctx,cty,matrix):
    topx=ctx-1
    topy=cty 
    leftx=ctx 
    lefty=cty-1
    if lefty>=0 and topx>=0:
        minV=getMin(matrix[topx][topy],matrix[leftx][lefty])
    elif lefty>=0:
        minV=matrix[leftx][lefty]
    elif topx>=0:
        minV=matrix[topx][topy]
    return minV
        
inputFile=open('p081_matrix80.txt','r')
matrix=[]

count=0
for line in inputFile:
    matrix.append(map(int,line.split(',')))
    
max=len(matrix)

#从左上向右跑,n代表x
for n in range(1,max):
    for move in range(0,n+1):
        ctx=n-move
        cty=move
        matrix[ctx][cty] += calc(ctx,cty,matrix)

#从右下向左跑,n代表y
for n in range(1,max):
    for move in range(n,max):
        ctx=max-move+n-1
        cty=move
        matrix[ctx][cty] += calc(ctx,cty,matrix)

        
print matrix[max-1][max-1]
print '--------------------------------'  
print (edu.time()-ts0)