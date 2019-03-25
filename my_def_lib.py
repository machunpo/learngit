#函数功能：输入一个月份或者日期，如果小于10，则在其前面补齐0，用于月份或者日期的对齐
#输入参数：i 整形变量
#输出参数：l 字符串
def  checkTime(i):
    if (i < 10):
        l = "0" + str(i)  
    else:
        l=str(i)
    return l

if __name__ == '__main__':

    #num=10
    #print('num = ',checkTime(num))
    #print('num-1 = ',checkTime(num-1))
