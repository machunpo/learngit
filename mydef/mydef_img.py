import aircv as ac


#函数功能：检查一个图片中是否包含另外一个图片
#输入参数：img_arry  需要图片的列表 ['qtoutiao\img\pic1.png','qtoutiao\img\pic2.png']
#img_scr  原始图像
#输出参数：一个列表 [None, {'result': (240.0, 446.0), 'rectangle': ((0, 332), (0, 560), (480, 332), (480, 560)), 'confidence': 1.0}]
#[{'result': (186.5, 917.5), 'rectangle': ((76, 880), (76, 955), (297, 880), (297, 955)), 'confidence': 0.6675431728363037}, {'result': (250.0, 425.0), 'rectangle': ((10, 311), (10, 539), (490, 311), (490, 539)), 'confidence': 0.519646167755127}]

def img_cheak(img_scr,img_arry):

    result_arry=[]
    imgsrc = ac.imread(img_scr) # 原始图像
    for i in img_arry:
            imgtort =ac.imread(i)
            rult=ac.find_template(imgsrc, imgtort)
            result_arry.append(rult)
            #print(ac.find_sift(img_scr,imgtort))
            
    return(result_arry)