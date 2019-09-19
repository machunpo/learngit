import os
import exifread

Source_folder="c:\\Source"
Target_folder="c:\\Target"

#函数名称：get_file_extension  提取文件名的扩展名
#入口参数：filename  字符串 文件名
#返回参数：filename[-i+1:] 文件的扩展名
def get_file_extension(filename):
    i=0
    for character in reversed(filename):
        i=i+1
        if  character == ".":
            break
    return(filename[-i+1:])
    #print(i,filename[-i+1:])

#函数名称：get_yearmoon_of_pic  提取图片的拍摄日期中的年和月
#入口参数：picpath              图片的地址路径
#返回参数：形如[['2010', '11', '11'], ['00', '13', '48']]的二维数组
def get_yearmoon_of_pic(picpath):
    f = open(picpath, 'rb')
    tags = exifread.process_file(f)
    data_arry=tags['Image DateTime'].values.split(" ")
    f.close()
    return([x.split(":") for x in data_arry])


for root, dirs, files  in os.walk(Source_folder):
    for my_file in files:
        if (get_file_extension(my_file)=="jpg"):  #如果文件的后缀名为jpg   这里应该用try

            path=root+"\\"+my_file

            print(path)                             #打印出完整的文件路径
            year_moon=get_yearmoon_of_pic(path)
            print(year_moon[0][0],year_moon[0][1])        #打印出照片拍摄的年和月（处理好的）
    #print(root, dirs, files )

#input()

#下一步是剪切文件 和新建文件夹的操作