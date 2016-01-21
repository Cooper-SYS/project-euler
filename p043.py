# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()

import datetime

starttime = datetime.datetime.now()

def remvoeValue(lst,lst2):
    rtLst=lst[:]
    for x in lst2:
        rtLst.remove(x)
    return rtLst

num=0;    

def isOk(tmp,x):
    global num
    num=num+1
    #print num
    if tmp.count(x)>0:
        return True
    else:
        tmp.append(x)
        tmpLen=len(tmp)
        if tmpLen>=4:
            tmpNum234=tmp[1]*100+tmp[2]*10+tmp[3]
            if tmpNum234%2!=0:
                return True
        if tmpLen>=5:
            tmpNum345=tmp[2]*100+tmp[3]*10+tmp[4]
            if tmpNum345%3!=0:
                return True
        if tmpLen>=6:
            tmpNum456=tmp[3]*100+tmp[4]*10+tmp[5]
            if tmpNum456%5!=0:
                return True
        if tmpLen>=7:
            tmpNum567=tmp[4]*100+tmp[5]*10+tmp[6]
            if tmpNum567%7!=0:
                return True
        if tmpLen>=8:
            tmpNum678=tmp[5]*100+tmp[6]*10+tmp[7]
            if tmpNum678%11!=0:
                return True
        if tmpLen>=9:
            tmpNum789=tmp[6]*100+tmp[7]*10+tmp[8]
            if tmpNum789%13!=0:
                return True
        if tmpLen>=10:
            tmpNum890=tmp[7]*100+tmp[8]*10+tmp[9]
            if tmpNum890%17!=0:
                return True
        return False
rtList=[]
def lst2str(lst):
    rtStr=''
    for x in lst:
        rtStr=rtStr+str(x)
    return rtStr
    
f=[0,1,2,3,4,5,6,7,8,9]
for x1 in range(1,10):
    tmp1=[]
    if isOk(tmp1,x1):
        continue
    f2=remvoeValue(f,tmp1)
    for x2 in f2:
        tmp2=tmp1[:]
        if isOk(tmp2,x2):
            continue
        f3=remvoeValue(f,tmp2)
        for x3 in f3:
            tmp3=tmp2[:]
            if isOk(tmp3,x3):
                continue
            f4=remvoeValue(f,tmp3)
            for x4 in f4:
                tmp4=tmp3[:]
                if isOk(tmp4,x4):
                    continue
                f5=remvoeValue(f,tmp4)
                for x5 in f5:
                    tmp5=tmp4[:]
                    if isOk(tmp5,x5):
                        continue
                    f6=remvoeValue(f,tmp5)
                    for x6 in f6:
                        tmp6=tmp5[:]
                        if isOk(tmp6,x6):
                            continue
                        f7=remvoeValue(f,tmp6)
                        for x7 in f7:
                            tmp7=tmp6[:]
                            if isOk(tmp7,x7):
                                continue
                            f8=remvoeValue(f,tmp7)
                            for x8 in f8:
                                tmp8=tmp7[:]
                                if isOk(tmp8,x8):
                                    continue
                                f9=remvoeValue(f,tmp8)
                                for x9 in f9:
                                    tmp9=tmp8[:]
                                    if isOk(tmp9,x9):
                                        continue
                                    f10=remvoeValue(f,tmp9)
                                    for x10 in f10:
                                        tmp10=tmp9[:]
                                        if isOk(tmp10,x10):
                                            continue
                                        rtList.append(lst2str(tmp10))
                                        


rtNum=0
for x in rtList:
    print x
    rtNum=rtNum+int(x)
print '-------------'
print rtNum
print (edu.time()-ts0)

