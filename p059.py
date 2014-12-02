#coding=utf-8
#!/usr/bin/python
#python2.7.8
'''
电脑上的每个字符都有一个唯一编码，通用的标准是ASCII (American Standard Code for Information Interchange 美国信息交换标准编码)。
例如大写A = 65， 星号(*) = 42，小写k = 107。

一种现代加密方法是用一个密钥中的给定值，与一个文本文件中字符的ASCII值进行异或。
使用异或方法的好处是对密文使用同样的加密密钥可以得到加密前的内容。
例如，65 XOR 42 = 107, 然后 107 XOR 42 = 65。

对于不可攻破的加密，密钥的长度与明文信息的长度是一样的，而且密钥是由随机的字节组成的。
用户将加密信息和加密密钥保存在不同地方，只有在两部分都得到的情况下，信息才能被解密。

不幸的是，这种方法对于大部分用户来说是不实用的。所以一种修改后的方案是使用一个密码作为密钥。
如果密码比信息短，那么就将其不断循环直到明文的长度。平衡点在于密码要足够长来保证安全性，但是又要足够短使用户能够记得。

你的任务很简单，因为加密密钥是由三个小写字母组成的。
文件 p059_cipher.txt (右键另存为)包含了加密后的ASCII码，并且已知明文是由常用英语单词组成。
使用该文件来解密信息，然后算出明文中字符的ASCII码之和。
'''
import datetime
starttime = datetime.datetime.now()

cipher = map(int, open('p059_cipher.txt','r').read().split(','))
common_words = ['the', 'be', 'to', 'of', 'and', 'in', 'that', 'have', 'it', 'for', 'not', 'with', 'you', 'this', 'but', 'his', 'from', 'they', 'say', 'her', 'she', 'will', 'one', 'all', 'would', 'there', 'their', 'what', 'out', 'about']

ordval = range(ord('a'), ord('z') + 1)
keys = [[i, j, k] for i in ordval for j in ordval for k in ordval]
flag=False
for key in keys:
    #如果密码比信息短，那么就将其不断循环直到明文的长度
    #此处信息的长度为1201，密码长度为3，所以不断循环密码到长度为1201
    #因此密码就成了 ：  key[0]key[1]key[2]key[0]key[1]key[2]key[0]key[1]key[2]...key[0]key[1]key[2]
    decrypt = [cipher[i] ^ key[i%3] for i in range(len(cipher))]
    
    plain_text = ''.join(map(chr, decrypt))
    count = 0
    tmp=[]
    for w in common_words:
        if w in plain_text: 
            count += 1
            tmp.append(w)
    #不断调整这个值，使plain_text看起来像一篇正常的文章
    if count > 18: 
        flag=True
        print map(chr,key)
        print tmp
        break
if flag:
    print '----------------------------'    
    print count
    print plain_text
    print sum(map(ord, plain_text))
else:
    print 'no answer'
    
endtime = datetime.datetime.now()
print('All spent '+str((endtime-starttime).seconds)+' seconds')


