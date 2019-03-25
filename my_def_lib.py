def  checkTime(i):
    i=int(i)
    if (i < 10):
        l = "0" + str(i)  
    else:
        l=str(i)
    return str(l)

m=input()
#m=int(m)
checkTime(m)
print(m)