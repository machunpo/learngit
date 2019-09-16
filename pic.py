import os
#import exifread

Source_folder="c:\\Source"
Target_folder="c:\\Target"

#print(Source_folder,'\n',Target_folder)
#dan_qian_mu_lu=os.getcwd()
#print(Source_folder)

for a,b,c in os.walk(Source_folder):
    print(a,b,c)


#下一步是把所有文件打印出来