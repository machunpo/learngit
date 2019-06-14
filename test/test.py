# -*- coding: utf-8 -*-

with open('log.txt', 'a+') as f:  #	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
    f.seek(0, 0)
    rember = f.readline()
    print ("文件名: ", f.name)
    print ("是否已关闭 : ", f.closed)
    print ("访问模式 : ", f.mode)
    print ("rember : ", rember)
    position = f.tell()
    print ("当前文件位置 : ", position)




# -*- coding: utf-8 -*-

# 测试文件名为：
# text.txt
# 测试文件内容为：
# abcdefg
# 每次操作后将文件复原

# r
# 以只读方式打开文件，文件不可写
# 要打开的文件不存在时会报错
# 文件的指针将会放在文件的开头
# 这是默认模式
# # file = open('test.txt', 'r')
# # FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'
# file = open('text.txt', 'r')
# print(file.read())
# # abcdefg
# file.write('aaa')
# # io.UnsupportedOperation: not writable
# file.close()

# rb
# 以二进制格式打开一个文件用于只读，文件不可写
# 要打开的文件不存在时会报错
# 文件指针将会放在文件的开头
# 这是默认模式
# # file = open('test.txt', 'rb')
# # FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'
# file = open('text.txt','rb')
# print(file.read())
# b'abcdefg'
# # file.write(b'aaa')
# # io.UnsupportedOperation: not writable
# file.close()

# r+
# 打开一个文件用于读写，写入内容为str
# 文件指针将会放在文件的开头
# 重新写入的内容从头开始替换
# file = open('text.txt', 'r+')
# file.write('aaa')
# file.close()
# file = open('text.txt','r')
# print(file.read())
# # 'abcdefg'
# file.close()

# rb+
# 以二进制格式打开一个文件用于读写，写入内容为bytes
# 文件指针将会放在文件的开头
# 重新写入的内容从头开始替换
# file = open('text.txt','rb+')
# # file.write('aaa')
# # TypeError: a bytes-like object is required, not 'str'
# file.write(b'aaa')
# file.close()
# file = open('text.txt','rb')
# print(file.read())
# # b'aaadefg'
# file.close()

# w
# 打开一个文件只用于写入，写入内容为str
# 文件不可读
# 如果该文件已存在则将其覆盖，原文件内容将清空
# 如果该文件不存在，创建新文件
# file = open('test.txt', 'w')
# 创建一个空文件
# file = open('text.txt', 'w')
# file.write('gfedcba')
# file = open('text.txt', 'r')
# print(file.read())
# file.close()

# wb
# 以二进制格式打开一个文件只用于写入，写入内容为bytes
# 文件不可读
# 如果该文件已存在则将其覆盖，原文件内容将清空
# 如果该文件不存在，创建新文件
# file = open('test.txt', 'wb')
# 创建一个空文件
# file = open('text.txt', 'wb')
# file.write(b'gfedcba')
# file = open('text.txt', 'r')
# print(file.read())
# file.close()

# w+
# 打开一个文件用于读写，写入内容为str
# 如果该文件已存在则将其覆盖，原文件内容将清空
# 如果该文件不存在，创建新文件
# file = open('test.txt', 'w+')
# 创建一个空文件
# file = open('text.txt', 'w+')
# file.write('gfedcba')
# file = open('text.txt', 'r')
# print(file.read())
# file.close()

# wb+
# 以二进制格式打开一个文件用于读写，写入内容为bytes
# 如果该文件已存在则将其覆盖
# 如果该文件不存在，创建新文件
# file = open('text.txt', 'wb+')
# file.write(b'gfedcba')
# file = open('text.txt', 'r')
# print(file.read())
# file.close()

# a
# 打开一个文件用于追加（只写），写入内容为str
# 如果该文件已存在，文件指针将会放在文件的结尾，新的内容将会被写入到已有内容之后
# 如果该文件不存在，创建新文件进行写入
# file = open('test.txt', 'a')
# 创建一个空文件
# file = open('text.txt', 'a')
# file.write('aaa')
# file.close()
# file = open('text.txt')
# print(file.read())
# file.close()

# ab
# 以二进制格式打开一个文件用于追加（只写），写入内容为bytes
# 如果该文件已存在，文件指针将会放在文件的结尾，新的内容将会被写入到已有内容之后
# 如果该文件不存在，创建新文件进行写入
# file = open('test.txt', 'ab')
# 创建一个空文件
# file = open('text.txt', 'ab')
# file.write(b'aaa')
# file.close()
# file = open('text.txt')
# print(file.read())
# file.close()

# a+
# 打开一个文件用于追加（读写），写入内容为str
# 如果该文件已存在，文件指针将会放在文件的结尾，新的内容将会被写入到已有内容之后
# 如果该文件不存在，创建新文件用于读写
# file = open('test.txt', 'a+')
# 创建一个空文件
# file = open('text.txt', 'a+')
# file.write('aaa')
# file.close()
# file = open('text.txt')
# print(file.read())
# file.close()

# ab+
# 以二进制格式打开一个文件用于追加（读写），写入内容为bytes
# 如果该文件已存在，文件指针将会放在文件的结尾，新的内容将会被写入到已有内容之后
# 如果该文件不存在，创建新文件用于读写
# file = open('text.txt', 'ab+')
# file.write(b'aaa')
# file.close()
# file = open('text.txt')
# print(file.read())
# file.close()