import os
import exifread

Source_folder="c:\\Source"
Target_folder="c:\\Target"
pic_type=['jpg','gif']

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
#返回参数：年和月的元组
def get_yearmoon_of_pic(picpath):
    f = open(picpath, 'rb')
    tags = exifread.process_file(f)
    #print(tags['Image DateTime'])
    try:
        data_arry=tags['Image DateTime'].values.split(" ")
        year_moon=([x.split(":") for x in data_arry])
    except:
        year_moon=[['何','马'],['马','月']]
    f.close()
    
    return((year_moon[0][0],year_moon[0][1]))


for root, dirs, files  in os.walk(Source_folder):
    for my_file in files:

        try:
            pass
        except :
            pass

        if (get_file_extension(my_file) in pic_type):  #如果文件的后缀名 in pic_type     这里要考虑如果提取不到文件的后缀名

            Source_file_path=root+"\\"+my_file

            #print(Source_file_path)   
             
            year,moon=(get_yearmoon_of_pic(Source_file_path))#这里要考虑如果提取不到照片的日期
            #print(year,moon)
            
            #name_of_targer_dir=year+'年'+moon+'月'
            Target_file_path=(Target_folder+'\\'+year+'年'+moon+'月'+'\\')
            
            is_target_dir=os.path.exists(Target_file_path)#目标文件夹是否存在
            is_target_file='备用变量'

            if (is_target_dir):     #目标文件夹如果存在
                #print(Target_file_path,'存在')
                print('目标文件夹存在')
            else:                 #目标文件夹如果不存在  
                os.mkdir(Target_file_path) #则创建目录
                print('创建'  '{}'  '目录'.format(Target_file_path))
                #print(is_target_dir)

   

input()

#下一步是考虑各种情况对文件的拷贝