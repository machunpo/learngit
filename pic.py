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




for root, dirs, files  in os.walk(Source_folder):
    for my_file in files:
        if (get_file_extension(my_file)=="jpg"):#如果文件的后缀名为jpg

            path=root+"\\"+my_file
            print(path)                             #打印出完整的文件路径
    #print(root, dirs, files )



#下一步是提取文件的拍摄日期是什么时候   也就是exifread的用法