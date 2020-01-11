import aircv as ac
imsrc = ac.imread(r'd:\1.jpg') # 原始图像
imsch = ac.imread(r'd:\2.jpg') # 带查找的部分

#print(imsch,imsrc)
print(type(imsch))
'''
for j in imsch:
    for i in j:
        print('i=',i)
'''
print(ac.find_template(imsrc, imsch))
#{'result': (165.0, 342.0), 'rectangle': ((5, 222), (5, 462), (325, 222), (325, 462)), 'confidence': 0.8480324745178223}