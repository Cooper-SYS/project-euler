#054 poker second try
nums=('0','1','2','3','4','5','6','7','8','9','T','J','Q','K','A')
count=0
scount = []
f=open('p054_poker.txt')
for line in f:
    oldcount = count
    #hand1=line[:14].split()
    #hand2=line[15:].split()
    #split, select numbers, and sort, the result is a string
    numhand1=sorted([nums.index(x) for x in sorted(line[:14:3])])
    numhand2=sorted([nums.index(x) for x in sorted(line[15::3])])
    shapehand1=sorted([x for x in sorted(line[1:14:3])])
    shapehand2=sorted([x for x in sorted(line[16::3])])
    #create dictionary for counting
    hand1dict={x:numhand1.count(x) for x in numhand1}
    hand2dict={x:numhand2.count(x) for x in numhand2}
    hand1sdict={x:shapehand1.count(x) for x in shapehand1}
    hand2sdict={x:shapehand2.count(x) for x in shapehand2}
    #special checks
    max1=max(numhand1)
    max2=max(numhand2)
    flush1=(max(hand1sdict.viewvalues())==5)
    flush2=(max(hand2sdict.viewvalues())==5)
    straight1=((max1-1 in numhand1)and(max1-2 in numhand1)and(max1-3 in numhand1)and(max1-4 in numhand1))
    straight2=((max2-1 in numhand2)and(max2-2 in numhand2)and(max2-3 in numhand2)and(max2-4 in numhand2))
    
    #empty lists
    hand1n=[]
    hand2n=[]
    for x,y in hand1dict.iteritems():
        hand1n.append([y,x])
    for x,y in hand2dict.iteritems():
        hand2n.append([y,x])
    hand1n.sort(reverse=True)
    hand2n.sort(reverse=True)
    hand1na=[row[0] for row in hand1n]
    hand1nb=[row[1] for row in hand1n]
    hand2na=[row[0] for row in hand2n]
    hand2nb=[row[1] for row in hand2n]
    print hand1n, [row[0] for row in hand1n]
    #if there is no flag for flush or straight only need to compare
    #handxna first, if equal, compare handxnb
    if not(flush1 or flush2 or straight1 or straight2):
        if hand1na>hand2na:
            count+=1
        elif(hand1na==hand2na):
            if hand1nb>hand2nb:
                count+=1
    else:
        if flush1 and not flush2:
            if straight1:
                count+=1
            elif not((hand2na[0]==4) or (hand2na[0]==3 and hand2na[1]==2)):
                count+=1
        elif flush2 and not flush1:
            if ((hand1na[0]==4) or (hand1na[0]==3 and hand1na[1]==2)):
                count+=1
        elif flush1 and flush2:
            if (straight1==straight2) and (hand1nb>hand2nb):
                count+=1
            elif straight1 and not straight2:
                count+=1
        else:
            if straight1!=straight2:
                if straight1 and not((hand2na[0]==4) or (hand2na[0]==3 and hand2na[1]==2)):
                    count+=1
                elif straight2 and ((hand1na[0]==4) or (hand1na[0]==3 and hand1na[1]==2)):
                    count+=1
            elif max1>max2:
                count+=1
    if count>oldcount:
        scount.append(1)
    else:
        scount.append(0)
print count
print scount