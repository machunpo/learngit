import time

print("########################################################################################################")
arry=[]
f = open('1.txt', 'r')
for line in f:
    print(line.strip())
    arry.append(int(line.strip()))

f.close()

m=arry[-1]+2

while(1):
    for i in arry:
        if (i>(m**0.5)):
            break
        else:
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
    


        
         



