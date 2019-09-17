import os
#import exifread

Source_folder="c:\\Source"
Target_folder="c:\\Target"


def get_file_extension(filename):
    for i in reversed(filename):
        print(i)




for root, dirs, files  in os.walk(Source_folder):
    for f in files:
            path=root+"\\"+f
            print(path)
    #print(root, dirs, files )

str1="abcdefghijklmnopqrstuvwxyz.txt"
get_file_extension(str1)
print(str1)

#下一步是辨别文件的后缀名是什么