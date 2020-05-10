import aircv as ac

def img_cheak(imgchk1):
    os.system('adb shell screencap -p /sdcard/cut_img.png')
    os.system(r'adb pull /sdcard/cut_img.png  C:\Users\machunpo\Desktop\myimages')
    imsrc = ac.imread(r'C:\Users\machunpo\Desktop\myimages\cut_img.png') # 原始图像
    rult=ac.find_template(imsrc, imgchk1)
    print(rult)










if __name__ == '__main__':
    img_cheak(r'')
