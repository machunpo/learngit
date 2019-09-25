import os
import exifread
import shutil

Source_folder="c:\\Source"
Target_folder="c:\\Target"
pic_type=['jpg','gif','bmp','png','jpeg']

#函数名称：get_file_extension  提取文件名的扩展名
#入口参数：filename  字符串 文件名
#返回参数：filename[-i+1:].lower() 文件的扩展名的小写
def get_file_extension(filename):
    i=0
    j=False
    for character in reversed(filename):
        i=i+1
        if  character == ".":
            j=True
            break
    if j:
        
        return(filename[-i+1:].lower())
        
    else:
        return('这个字符串肯定不是哪个文件的后缀名')

    


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
        year_moon=[['何','马'],['如果商业使用，请遵守相关开源协议','侵权必究']]
    f.close()
    
    return((year_moon[0][0],year_moon[0][1]))


for root, dirs, files  in os.walk(Source_folder):
    for my_file in files:
        
        try:
            houzhuiming_file=get_file_extension(my_file)
            #print(houzhuiming_file)
            length_extension=len(houzhuiming_file)#获取后缀名的长度
            #print(length_extension)
        except :
            print('没有获取到这个文件的扩展名')

        if (houzhuiming_file in pic_type):  #如果文件的后缀名 in pic_type     这里要考虑如果提取不到文件的后缀名ok

            Source_file_path=root+"\\"+my_file

            #print(Source_file_path)   
             
            year,moon=(get_yearmoon_of_pic(Source_file_path))#这里要考虑如果提取不到照片的日期ok
            #print(year,moon)
            
            #name_of_targer_dir=year+'年'+moon+'月'
            Target_dir_path=(Target_folder+'\\'+year+'年'+moon+'月'+'\\')
            Target_file_path=Target_dir_path+my_file
            
            is_target_dir=os.path.exists(Target_dir_path)#目标文件夹是否存在
            is_target_file=os.path.exists(Target_file_path)#目标文件是否存在

            if (is_target_dir):     #目标文件夹如果存在
                
                if is_target_file:
                    m=1
                    while(os.path.exists(Target_file_path)):
                        if m==1 :
                            Target_file_path=Target_file_path[:-length_extension-1]+'('+str(m)+ ')'+Target_file_path[-length_extension-1:]
                         
                        else:
                            Target_file_path=Target_file_path.replace('('+str(m-1)+')','('+str(m)+')')
                            
                            
                        m=m+1
                      
                    shutil.copy(Source_file_path,Target_file_path);print('改名后  {}  文件拷贝到  {}  目录成功！{}'.format(Source_file_path,Target_dir_path,m-1))#改名再拷贝
                else:
                    shutil.copy(Source_file_path,Target_dir_path);print('复制  {}  文件到  {}  目录成功！'.format(Source_file_path,Target_dir_path))#直接拷贝
               
            else:                                            #目标文件夹如果不存在  
                os.mkdir(Target_dir_path)                    #则创建目录
                shutil.copy(Source_file_path,Target_dir_path);print('复制  {}  文件到新建  {}  目录成功！'.format(Source_file_path,Target_dir_path))
                

#input()


#下一步是 把copy改成 move      move(src, dst) 和看看能不能解决何年马月的问题 还有print的重定向问题

#有关英文的插件