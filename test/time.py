import time

ctime1 = time.time()


print('test begin')


ctime1 = time.time()


for i in range(100000000):  # 循环1亿次
    a = i**2

ctime2 = time.time()

alltime = ctime2-ctime1

print('程序一共运行了：', alltime, ('秒'))

print(time.localtime().tm_year, "年")
print(time.localtime().tm_mon, "月")

#  i5:    34.05399990081787 秒
#  手机： 40.02087473869324 秒

