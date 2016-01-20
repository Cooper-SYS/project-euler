#coding=utf-8
#!/usr/bin/python
#python2.7.8
#split file
import datetime

name = raw_input("Please input your name(with extension):\n")
lineNumEach=int(input("Please input line number for one file:\n"))
#eachLineByte=int(input("Please input line byte for one line:\n"))
nameArr=name.split('.')
ex=nameArr[-1]
realName=name[:(-1-len(ex))]
inputFile = open(name,'r')
starttime = datetime.datetime.now()
try:
    lineNum=1
    fileNum=1
    newFileName=realName+'_'+str(fileNum)+'.'+ex
    newFile=open(newFileName,'w')
    tempStr=''


    for line in inputFile:
        print(newFileName+':'+str(lineNum))
        
        if lineNum>lineNumEach :
            #需要换新文件，先写缓存
            newFile.writelines(tempStr)
            newFile.close()
            lineNum=1
            fileNum=fileNum+1
            tempStr=line;
            newFileName=realName+'_'+str(fileNum)+'.'+ex
            newFile=open(newFileName,'w')
        else :
            tempStr=tempStr+line
    
        lineNum=lineNum+1
    #当全部结束后将最后的缓存再写入最后一个文件
    if newFile :
        newFile.writelines(tempStr)
        newFile.close()

    newFile.close()
finally:
     inputFile.close()
     
endtime = datetime.datetime.now()
print('All spent '+str((endtime-starttime).seconds)+' seconds')