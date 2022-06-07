import time
import random

ctime1 = time.time()


print('test begin')


ctime1 = time.time()



list1=[random.randint(1,100000) for i in range(100000)] #生成10万个随机数进行排序


for i in range(len(list1)):

    # 内循环将数组元素与外循环迭代元素进行比较
    for j in range(0, len(list1) - i - 1):

      # 比较两个相邻元素
      if list1[j] > list1[j + 1]:

        # 如果元素不是预期顺序则交换元素
        temp = list1[j]
        list1[j] = list1[j+1]
        list1[j+1] = temp





for i in range(10000000):  # 循环1千万次

    a = i**2

ctime2 = time.time()

alltime = ctime2-ctime1

print('程序一共运行了：', alltime, ('秒'))

print(time.localtime().tm_year, "年")
print(time.localtime().tm_mon, "月")

#  i5:      34.05399990081787 秒
#  手机：   40.02087473869324 秒
#  笔记本： 32.953285932540894 秒
#  apple    63.484251260757446 秒
#  老平板   393.6 秒

