list_1 = [1,2,3,4,5,6,7,8,9,0]
print(list_1)

'''
for i in list_1:
    print(i)

print(list_1[1:-3])
'''

a=[x for x in list_1 if x>5]

print(a)

b=[x**2 for x in list_1 ]

print('b:',b)
c=[x for x in range(0,10) if x>3]

print(c)