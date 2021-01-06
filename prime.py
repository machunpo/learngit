import time

print("########################################################################################################")
arry=[]
f = open('1.txt', 'r')
for line in f:
    print(line.strip())
    arry.append(int(line.strip()))

f.close()
#print(arry)

#arry=[2,3,5,7,11,13,17,19]  #将来更改为从文件中倒入数组
#x=0
m=arry[-1]+2

while(1):
    for i in arry:
        x=0
        if (m%i==0):
            break
        else:
            x=1


    if x==1 :
        arry.append(m)
        print(m)
        f = open('1.txt', 'a')
        f.write(str(m)+'\n')
        f.close()
        #time.sleep(1)
    x=0
    m=m+2
    #print(arry,m)
    

#改进效率
        
         



