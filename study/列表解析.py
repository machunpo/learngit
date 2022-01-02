list_1 = [1,2,3,4,5,6,7,8,9,0]
print('list_1=',list_1)

'''
for i in list_1:
    print(i)

print(list_1[1:-3])
'''
def haha(nn):
    return nn+nn


a=[haha(x) for x in list_1 ]

print('a = ',a)



print('b = ',[x**3 for x in list_1 ])
c=[x for x in range(0,10) if x>3]

<<<<<<< HEAD
print(c)

d = {x for x in range(10)}

print(d)
=======
print('c =',c)
>>>>>>> 39391bb7823fc618590f773de7b2f8d0dbc470c7
