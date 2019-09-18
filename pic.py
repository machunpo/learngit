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
#返回参数：
def get_yearmoon_of_pic(picpath):
    f = open(picpath, 'rb')
    tags = exifread.process_file(f)
    f.close()
    return(str(tags['Image DateTime']))


for root, dirs, files  in os.walk(Source_folder):
    for my_file in files:
        if (get_file_extension(my_file)=="jpg"):#如果文件的后缀名为jpg

            path=root+"\\"+my_file
            print(path)                             #打印出完整的文件路径

            print(get_yearmoon_of_pic(path))
    #print(root, dirs, files )

input()

#下一步是分割字符串 把年月的信息提取出来