
import aircv as ac






if __name__ == '__main__':


    imsrc = ac.imread(r'C:\Users\machunpo\Desktop\funtoutiao.png') # 原始图像
    imsch = ac.imread(r'C:\Users\machunpo\Desktop\f.png')  # 带查找的部分

    #print(imsch,imsrc)

    results=ac.find_template(imsrc, imsch)  
    #{'result': (562.0, 859.0), 'rectangle': ((447, 799), (447, 919), (677, 799), (677, 919)), 'confidence': 0.9999967813491821}

    if(results):
        print(int(results['result'][0]),int(results['result'][1]))
        
    else:
        print("没有找到")    

