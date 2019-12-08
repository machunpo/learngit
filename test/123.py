from PIL import Image

def get_pixel_colour(image_path,x,y):
    img=Image.open(image_path)
    img_array=img.load()
    pixel_colour=img_array[x,y]
    img.close()
    return  pixel_colour

if __name__ == '__main__':
    a=get_pixel_colour(r'C:\Users\machunpo\Desktop\images\funtoutiao.png',43,100)  #得到一个元组 (0, 0, 0, 255)
    b=get_pixel_colour(r'C:\Users\machunpo\Desktop\images\funtoutiao.png',570,100)   
    c=get_pixel_colour(r'C:\Users\machunpo\Desktop\images\funtoutiao.png',240,1000)   
    d=get_pixel_colour(r'C:\Users\machunpo\Desktop\images\funtoutiao.png',480,1000)  
    print(a,b,c,d) 
    print((a==(129, 140, 136, 255)) & (b==(243, 247, 246, 255)))
    print((c==(255, 255, 255, 255)) & (d==(255, 255, 255, 255)))
    

