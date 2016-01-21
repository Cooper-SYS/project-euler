# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()

'''
Created on 2013-8-8
1901年1月1日是星期二
@author: zhaoliang
'''
old=2#这个数字指的是1901年1月1日的星期数，星期一则为1，星期日为7
sumdays=0
times=0
for year in range(1901,2001):
    for month in range(1,13):
        if month in [1,3,5,7,8,10,12]:
            days=31
        if month in [4,6,9,11]:
            days=30
        if month==2:
            days=28
            if year%4==0 and year%400!=0:
                days=29
        week=(sumdays)%7+old
        if week==8:
            week=1
        #print str(month)+':'+str(week)+':'+str(days)
        sumdays+=days
        if week==7:
            times+=1
            
print times
print (edu.time()-ts0)