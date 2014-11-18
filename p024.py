# coding:utf-8
'''
Created on 2013-8-9
2783915460
362880    *    2
40320     *    6
5040      *    6
720       *    2
120       *    5
24        *    1
6         *    2
2         *    1
1         *    1
@author: zhaoliang
'''
import copy
import sys

factorial=[1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

list=[0,1,2,3,4,5,6,7,8,9]
# result=[2,6,6,2,5,1,2,1,1]
# 
# s=''
# for x in range(0,9):
#     print 'x:'+str(x)
#     print result
#     print result[x]
#     v=list[result[x]]
#     s+=str(v)
#     print s
#     list.remove(v)
#     print list
#     print '-'*20
#     
# s+=str(list[0])
# 
# print s

count=1
tmp1=copy.copy(list)
for x1 in tmp1:
    tmp2=copy.copy(tmp1)
    tmp2.remove(x1)
    for x2 in tmp2:
        tmp3=copy.copy(tmp2)
        tmp3.remove(x2)
        for x3 in tmp3:
            tmp4=copy.copy(tmp3)
            tmp4.remove(x3)
            for x4 in tmp4:
                tmp5=copy.copy(tmp4)
                tmp5.remove(x4)
                for x5 in tmp5:
                    tmp6=copy.copy(tmp5)
                    tmp6.remove(x5)
                    for x6 in tmp6:
                        tmp7=copy.copy(tmp6)
                        tmp7.remove(x6)
                        for x7 in tmp7:
                            tmp8=copy.copy(tmp7)
                            tmp8.remove(x7)
                            for x8 in tmp8:
                                tmp9=copy.copy(tmp8)
                                tmp9.remove(x8)
                                for x9 in tmp9:
                                    tmp10=copy.copy(tmp9)
                                    tmp10.remove(x9)
                                    for x10 in tmp10:
                                        s=str(x1)+str(x2)+str(x3)+str(x4)+str(x5)+str(x6)+str(x7)+str(x8)+str(x9)+str(x10)
                                        print str(count)+':'+s
                                        count+=1
                                        if count>1000000:
                                            sys.exit(0)
                                        