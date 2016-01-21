# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()

from __future__ import division
import datetime
import math

starttime = datetime.datetime.now()
LEVEL4 = 14**4
LEVEL3 = 14**3
LEVEL2 = 14**2
LEVEL1 = 14**1
LEVEL0 = 14**0

DEFAULT_LEVEL = [-1,-1]

#同花大顺：同一花色的10、J、Q、K、A。
def level9(poker):
    if poker[0] == 10 and poker[1] == 11 and poker[2] == 12 and poker[3] == 13 and poker[4] == 14 and poker[5]:
        return [9,1]
    return DEFAULT_LEVEL
    
#同花顺：五张牌的牌面是连续的且为同一花色。
def level8(poker):
    if poker[4]-poker[3]==1 and poker[3]-poker[2]==1 and poker[2]-poker[1]==1 and poker[1]-poker[0]==1 and poker[5]:
        return [8,poker[4]]
    return DEFAULT_LEVEL
    
#四条：四张牌面一样的牌。
def level7(poker):
    if poker[0]==poker[1] and poker[0]==poker[2] and poker[0]==poker[3]:
        return [7,LEVEL1*poker[0]+poker[4]]
    if poker[1]==poker[2] and poker[1]==poker[3] and poker[1]==poker[4]:
        return [7,LEVEL1*poker[1]+poker[0]]
    if poker[2]==poker[3] and poker[2]==poker[4] and poker[2]==poker[0]:
        return [7,LEVEL1*poker[2]+poker[1]]
    if poker[3]==poker[4] and poker[3]==poker[0] and poker[3]==poker[1]:
        return [7,LEVEL1*poker[3]+poker[2]]
    if poker[4]==poker[0] and poker[4]==poker[1] and poker[4]==poker[2]:
        return [7,LEVEL1*poker[4]+poker[3]]
    return DEFAULT_LEVEL
    
#葫芦：三条带一个对子。
def level6(poker):
    if poker[0] == poker[1]  and poker[3] == poker[4] :
        if poker[2] == poker[1] or poker[2] == poker[3]:
            if(poker[2] == poker[1]):
                return [6,LEVEL1*poker[2] + poker[3]]
            else:
                return [6,LEVEL1*poker[3] + poker[2]]
    return DEFAULT_LEVEL

#同花：五张牌是同一花色。
def level5(poker):
    if poker[5]:
        return [5,LEVEL4*poker[4]+LEVEL3*poker[3]+LEVEL2*poker[2]+LEVEL1*poker[1]+LEVEL0*poker[0]]
    return DEFAULT_LEVEL
    
    
#顺子：五张牌的牌面是连续的。
def level4(poker):
    if poker[4]-poker[3]==1 and poker[3]-poker[2]==1 and poker[2]-poker[1]==1 and poker[1]-poker[0]==1:
        return [4,poker[4]]
    return DEFAULT_LEVEL

#三条：三张牌面一样的牌。
def level3(poker):
    if (poker[0] == poker[1] and poker[0] == poker[2]) or (poker[1] == poker[2] and poker[1] == poker[3]) or (poker[2] == poker[3] and poker[2] == poker[4]):
        if poker[0] == poker[1] and poker[0] == poker[2]:
            return [3,LEVEL3*poker[2] + LEVEL2*poker[4] + LEVEL1*poker[3]]
        if poker[1] == poker[2] and poker[1] == poker[3]:
            return [3,LEVEL3*poker[2] + LEVEL2*poker[4] + LEVEL1*poker[0]]
        if poker[2] == poker[3] and poker[2] == poker[4]:
            return [3,LEVEL3*poker[2] + LEVEL2*poker[1] + LEVEL1*poker[0]]
    return DEFAULT_LEVEL
    
    
#两对：两个不同的对子。
def level2(poker):
    if (poker[0] == poker[1] and poker[2] == poker[3]) or (poker[0] == poker[1] and poker[3] == poker[4]) or (poker[1] == poker[2] and poker[3] == poker[4]):
        if poker[0] == poker[1] and poker[2] == poker[3]:
            return [2,LEVEL3*poker[3]+LEVEL2*poker[1]+LEVEL1*poker[4]]
        if poker[0] == poker[1] and poker[3] == poker[4]:
            return [2,LEVEL3*poker[4]+LEVEL2*poker[1]+LEVEL1*poker[2]]
        if poker[1] == poker[2] and poker[3] == poker[4]:
            return [2,LEVEL3*poker[4]+LEVEL2*poker[2]+LEVEL1*poker[0]]
    return DEFAULT_LEVEL

#对子：两张牌面一样的牌。
def level1(poker):
    if poker[0] == poker[1] or poker[1] == poker[2] or poker[2] == poker[3] or poker[3] == poker[4]:
        if poker[0] == poker[1]:
            return [1,LEVEL3*poker[0]+LEVEL2*poker[4]+LEVEL1*poker[3]+LEVEL0*poker[2]]
        
        if poker[1] == poker[2]:
            return [1,LEVEL3*poker[1]+LEVEL2*poker[4]+LEVEL1*poker[3]+LEVEL0*poker[0]]
        
        if poker[2] == poker[3]:
            return [1,LEVEL3*poker[2]+LEVEL2*poker[4]+LEVEL1*poker[1]+LEVEL0*poker[0]]
        
        if poker[3] == poker[4]:
            return [1,LEVEL3*poker[3]+LEVEL2*poker[2]+LEVEL1*poker[1]+LEVEL0*poker[0]]
    return DEFAULT_LEVEL
    
#单牌：牌面最大的一张牌。
def level0(poker):
    return [0,LEVEL4*poker[4]+LEVEL3*poker[3]+LEVEL2*poker[2]+LEVEL1*poker[1]+LEVEL0*poker[0]]
    
player1 = []
player2 = []

lineNumber = 0
inputFile=open('p054_poker.txt','r')
for line in inputFile:
    if line is not None:
        lineNumber = lineNumber + 1
        pk = line.split(' ')
        number = []
        for p in pk:
            if p[0] < 'A':
                num = int(p[0])
            else:
                if p[0] == 'T':
                    num = 10
                elif p[0] == 'J':
                    num = 11
                elif p[0] == 'Q':
                    num = 12
                elif p[0] == 'K':
                    num = 13
                elif p[0] == 'A':
                    num = 14
            number.append(num)
            
        p1 = [number[0],number[1],number[2],number[3],number[4]]
        p2 = [number[5],number[6],number[7],number[8],number[9]]
        p1.sort()
        p2.sort()
        if pk[0][1] == pk[1][1] and pk[0][1] == pk[2][1] and pk[0][1] == pk[3][1] and pk[0][1] == pk[4][1]:
            p1.append(True)
        else:
            p1.append(False)
        
        if pk[5][1] == pk[6][1] and pk[5][1] == pk[7][1] and pk[5][1] == pk[8][1] and pk[5][1] == pk[9][1]:
            p2.append(True)
        else:
            p2.append(False)
        player1.append(p1)
        player2.append(p2)

        
answer = []        
inputFile=open('p054_answer.txt','r')
for line in inputFile:
    if line is not None:
        answer.append(int(line))
       
score = []
for idx in range(0,lineNumber):

    grades1 = [level9(player1[idx]) , level8(player1[idx]), level7(player1[idx]), level6(player1[idx]), level5(player1[idx]), level4(player1[idx]), level3(player1[idx]), level2(player1[idx]), level1(player1[idx]), level0(player1[idx])]
    
    grades2 = [level9(player2[idx]) , level8(player2[idx]), level7(player2[idx]), level6(player2[idx]), level5(player2[idx]), level4(player2[idx]), level3(player2[idx]), level2(player2[idx]), level1(player2[idx]), level0(player2[idx])]
    
    
    pe = -1
    for i in range(0,10):
        if grades1[i][0]==-1 and grades2[i][0] == -1:
            continue
            
        if grades1[i][0]>grades2[i][0]:
            pe = 1 
            
        if grades1[i][0]<grades2[i][0]:
            pe = 0    
            
        
        if grades1[i][0]==grades2[i][0] and grades1[i][0]>-1:
            
            if grades1[i][1]>grades2[i][1]:
                pe = 1        
                
            if grades1[i][1]<grades2[i][1]:
                pe = 0
        
        if pe == 1:
            lvl = 9-i
            if lvl==0 :
                lvl_desc = '单牌'
            elif lvl==1 :
                lvl_desc = '对子'
            elif lvl==2 :
                lvl_desc = '两对'
            elif lvl==3 :
                lvl_desc = '三条'
            elif lvl==4 :
                lvl_desc = '顺子'
            elif lvl==5 :
                lvl_desc = '同花'
            elif lvl==6 :
                lvl_desc = '葫芦'
            elif lvl==7 :
                lvl_desc = '四条'
            elif lvl==8 :
                lvl_desc = '同花顺'
            elif lvl==9 :
                lvl_desc = '同花大顺'
            score.append(pe)
            
            break
        if pe == 0:
            score.append(pe)
            break
    if pe != answer[idx]:
        print idx
        print pe 
        print answer[idx]
        print player1[idx]
        print grades1
        print player2[idx]
        print grades2
        print '----------------------------------'
        
        
        
        
print lineNumber
player1Wons = 0     
player2Wons = 0
for i in range(0,len(score)):
    #print score[i]
    if score[i] == 1:
        player1Wons = player1Wons + 1 
    if score[i] == 0:
        player2Wons = player2Wons + 1
        
print player1Wons
print player2Wons
  
print (edu.time()-ts0)