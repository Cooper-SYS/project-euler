# coding:utf-8
from Euler import Euler
edu = Euler()

ts0 = edu.time()


import datetime

starttime = datetime.datetime.now()
number=100
xRay=[0]*number
xRay[0]=1
xRay[1]=3
print('calculate the triangle numbers array...')
for x in range(3,number+1):
    xRay[x-1]=x*(x+1)*0.5
print('the triangle numbers array bellow:')    
print(xRay)
print('calculate the words and its number...')
inputFile = open('p042_words.txt','r')
spe=0;
for line in inputFile:
    #word_arr=line.split('')
    num=0
    tmp_str=''
    for letter in line:
        letter_num=ord(letter)
        if letter_num>90 or letter_num<65: 
            continue
        tmp_str=tmp_str+'+'+str(ord(letter)-64)
        num=num+ord(letter)-64
    #print(str(line)+':'+str(num)+':'+tmp_str)
    if num in xRay:
        spe+=1 
    if num>xRay[number-1]:
        print('the triangle array is too small...')
print('the  triangle words number is : '+str(spe))    

print (edu.time()-ts0)

