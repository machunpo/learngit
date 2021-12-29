f = open('study/mcp.txt','w')
f.write('hello\n')
f.write('你好\n')
f.write('今天是个好日子！')
f.close

f = open('study/mcp.txt')
text = f.readline()
print(text)