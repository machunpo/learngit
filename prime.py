import time

arry=[2]  #将来更改为从文件中倒入数组
#print(arry[0])
x=0
m=3

while(1):
    for i in arry:
        if (m%i==0):
            break
        else:
            x=1
    if x==1 :
        arry.append(m)
        print(m)
    x=0
    m=m+2

    time.sleep(1)

        
         



