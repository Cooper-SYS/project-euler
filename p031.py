# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()

import time
start=time.time()
count=0

for p200 in range(0,2):
    for p100 in range(0,3):
        if p200*200+p100*100>200:break
        for p50 in range(0,5):
            if p200*200+p100*100+p50*50>200:break
            for p20 in range(0,11):
                if p200*200+p100*100+p50*50+p20*20>200:break
                for p10 in range(0,21):
                    if p200*200+p100*100+p50*50+p20*20+p10*10>200:break
                    for p5 in range(0,41):
                        if p200*200+p100*100+p50*50+p20*20+p10*10+p5*5>200:break
                        for p2 in range(0,101):
                            if p200*200+p100*100+p50*50+p20*20+p10*10+p5*5+p2*2>200:break
                            for p1 in range(0,201):
                                if p200*200+p100*100+p50*50+p20*20+p10*10+p5*5+p2*2+p1>200:break
                                if p1+p2*2+p5*5+p10*10+p20*20+p50*50+p100*100+p200*200==200:
                                    count+=1
                                    #print '%d*200 %d*100 %d*50 %d*20 %d*10 %d*5 %d*2 %d' % (p200,p100,p50,p20,p10,p5,p2,p1)




print count           
print (edu.time()-ts0)