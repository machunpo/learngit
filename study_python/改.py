list_1 = [3,2,8,3,4,5]
list_1[3] = 'nihao'
print(list_1)
list_1[3:5]= (11,111)

print(list_1)

list_1[3:5]= ((12345,323),111)
print(list_1)

# 将元组中的 'c' 改为 'd'
tuple_1 = ('a','b','c',4,5,6,7)

lst = list(tuple_1)

lst[2] = 'd'

tuple_1 = tuple(lst)

print(tuple_1)





