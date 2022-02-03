'''
f = open('study/mcp.txt','w')
f.write('hello\n')
f.write('你好\n')
f.write('今天是个好日子！')
f.write('正是江南好风景')
f.close

f = open('study/mcp.txt')
text = f.read()
print(text)
'''

b=[1,2,4,55,'年']


f = open('study_python/mcp.txt','w')
f.write('你好，这是一个文件操作的复习。\n')
f.write('这是第二句的测试。\n')
f.write('这是第3句的测试。\n')

for i in b :
    f.write(str(i)+'\n')

f.close()

print('文件已经关闭。')

f = open('study_python/mcp.txt')
text = f.read()
print(text)
