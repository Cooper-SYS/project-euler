# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()

from __future__ import division
import datetime
import math

starttime = datetime.datetime.now()

matrix=[]
inputFile=open('p081_matrix80.txt','r')
for line in inputFile:
    matrix.append(map(int,line.split(',')))
    
n, m = len(matrix), len(matrix[0]) 
cost = [matrix[i][-1] for i in xrange(n)]

for i in xrange(m-2, -1, -1):
	cost[0] += matrix[0][i]
	for j in xrange(1, n):
		cost[j] = min(cost[j], cost[j-1]) + matrix[j][i]
	for j in xrange(n-2, -1, -1):
		cost[j] = min(cost[j], cost[j+1] + matrix[j][i])

print "Minimum path in", n, "by", m, "matrix =", min(cost)

print '--------------------------------'  
print (edu.time()-ts0)