import time

ctime1 = time.time()
print('test begin')

for i in range(10000000):               #循环1亿次
    a = i**2

ctime2 = time.time()

alltime = ctime2-ctime1

print('程序一共运行了：', alltime, ('秒'))

print(time.localtime().tm_year,"年")
print(time.localtime().tm_mon ,"月")

#  i5:3.8秒
