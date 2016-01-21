# coding:utf-8
# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()


# num1to9=3+3+5+4+4+3+5+6+4
# num11to19=6+6+8+8+7+7+9+8+8
# ten=3
# twenty=6
# thirty=6
# forty=5
# fifty=5
# sixty=5
# seventy=7
# eighty=6
# ninety=6
# num20to90=6+6+5+5+5+7+6+6
# num20to99=num20to90*10+num1to9*8
# hundred=7
# numand=3
# num1to99=num1to9+ten+num11to19+num20to99
# print num1to99
# num100to999=num1to9*100+hundred*900+numand*891+num1to99*9
# print num100to999
# thousand=8
# print num1to99+num100to999+3+8


sum=3+8
for x in range(1,1000):
    ge=x%10
    shi=int((x%100-ge)/10)
    bai=int(x/100)
    number=str(bai*100+shi*10+ge)
    pro=''
    if bai==1:
        pro+='onehundred'
    if bai==2:
        pro+='twohundred'
    if bai==3:
        pro+='threehundred'
    if bai==4:
        pro+='fourhundred'
    if bai==5:
        pro+='fivehundred'
    if bai==6:
        pro+='sixhundred'
    if bai==7:
        pro+='sevenhundred'
    if bai==8:
        pro+='eighthundred'
    if bai==9:
        pro+='ninehundred'
    
    if bai!=0 and (shi!=0 or ge!=0):
        pro+='and'

    if shi==2:
        pro+='twenty'
    if shi==3:
        pro+='thirty'
    if shi==4:
        pro+='forty'
    if shi==5:
        pro+='fifty'
    if shi==6:
        pro+='sixty'
    if shi==7:
        pro+='seventy'
    if shi==8:
        pro+='eighty'
    if shi==9:
        pro+='ninety'
        
    if shi==1:
        if ge==0:
            pro+='ten'
        if ge==1:
            pro+='eleven'
        if ge==2:
            pro+='twelve'
        if ge==3:
            pro+='thirteen'
        if ge==4:
            pro+='fourteen'
        if ge==5:
            pro+='fifteen'
        if ge==6:
            pro+='sixteen'
        if ge==7:
            pro+='seventeen'
        if ge==8:
            pro+='eighteen'
        if ge==9:
            pro+='nineteen'
    else: 
        if ge==1:
            pro+='one'
        if ge==2:
            pro+='two'
        if ge==3:
            pro+='three'
        if ge==4:
            pro+='four'
        if ge==5:
            pro+='five'
        if ge==6:
            pro+='six'
        if ge==7:
            pro+='seven'
        if ge==8:
            pro+='eight'
        if ge==9:
            pro+='nine'
            
    print str(x)+':'+pro+':'+str(len(pro))
    sum+=len(pro)
    
print sum
print (edu.time()-ts0)