import random

list1=[random.randint(1,100) for i in range(40)] #列表解析
#生成20个100以内随机数进行排序

print(list1)
print('')

for i in range(len(list1)):

  # 内循环将数组元素与外循环迭代元素进行比较
  for j in range(0, len(list1) - i - 1):

    # 比较两个相邻元素
    if list1[j] > list1[j + 1]:

      # 如果元素不是预期顺序则交换元素
      list1[j],list1[j+1] = list1[j+1] ,list1[j] 
  
  print(list1)
#print(list1)