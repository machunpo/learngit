list_1 = [1,2,3,4,5]
list_1.append(6)
print(list_1)
list_1.append('seven')
print('list_1 =',list_1)
#可修改，有序，可重复

set_1 = {1,2,3,4,5}
set_1.add(6)
print(set_1)
set_1.add('seven')
print(set_1)
set_1.add(8)
print(set_1)
#可修改，无序，不重复

tuple_1 = (1,2,3,4,5,6)
print(tuple_1[2])
tuple_2 = tuple_1 + ('seven',)
print('tuple_2 = ',tuple_2)

#不可修改，有序，可重复
