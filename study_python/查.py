list_1 = [3,4,2,9,0,9]
find = list_1.index(0)
print(find)
count = list_1.count(9)
print('count = ',count)

tuple_1 = (2,4,6,9,3,0,9)
find_tuple = tuple_1.index(9)
print(find_tuple)
count_tuple = tuple_1.count(9)
print(count_tuple)

set_1 = {3,4,5,3,4,5}
print(set_1)
set_1.add(123)
print(set_1)
for i in set_1 :
    print(i)