import os
#import exifread

Source_folder="c:\\Source"
Target_folder="c:\\Target"

#print(Source_folder,'\n',Target_folder)
#dan_qian_mu_lu=os.getcwd()
#print(Source_folder)

for root, dirs, files  in os.walk(Source_folder):
    for f in files:
            path=root+"\\"+f
            print(path)
    #print(root, dirs, files )


#下一步是辨别文件的后缀名是什么