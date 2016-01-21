# coding:utf-8
import datetime
import time
import math


class Euler:
    def isPrime(self,x):
        for tmp in range(3,int(math.sqrt(x))+1):
            if x%tmp==0:
                return False
        return True
        
    def time(self):
        return int(time.time())
        #return datetime.datetime.now()