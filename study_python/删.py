list_1 = [1,2,3,4,5]
del(list_1[1])
print(list_1)
# 1.del函数

list_1.remove(1)
print(list_1)
# 2.remove方法

list_1.pop(0)
print(list_1)

# 3.pop方法

list_1.pop()
print(list_1)
# 4.pop方法没有参数时直接删除最后一个

list_1.pop()
print(list_1)


#tuple 通过重新切片来解决

set_1 = {1,2,3,4,5}
set_1.remove(2)
#remove方法删除元素时，如果元素不存在，会引发KeyError的错误
print(set_1)
set_1.discard(5)
print(set_1)

set_1.pop()
# 随机删除一个元素  没有参数  
print(set_1)
