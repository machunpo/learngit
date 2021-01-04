import time

print("########################################################################################################")
f = open('1.txt', 'r')
print(f.readlines())
for i in f.readlines():
    print(i)
f.close()
print (arry)

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
    x=0
    m=m+2
    #print(arry,m)
    #time.sleep(1)

#改进效率
        
         



