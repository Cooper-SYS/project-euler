# coding:utf-8
'''
Created on 2013-8-7

@author: zhaoliang
'''
def test():
    ret=0
    for x in range(100,1000):
        for y in range(100,1000):
            sum=x*y
            #print '%dX%d=%d' % (x,y,sum)
            if str(sum)[::-1]==str(sum):
                print '%dX%d=%d' % (x,y,sum)
                if sum>ret:
                    ret=sum
                
    return ret

print test()