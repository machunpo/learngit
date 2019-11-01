import os


#os.system('ping 8.8.8.8')
def cheak_adb_link(order):
    return_txt=os.popen(order).read()
    print('1',return_txt)
    if 'TTL=' in return_txt:
        return True
    else:
        return False


print('2',cheak_adb_link('adb shell input swipe 320 410 320 1000 500'))
#print (os.popen('ping 8.8.8.8 -n 1').read())
ccv=os.popen('adb shell input swipe 320 410 320 1000 500').read()
print('3',ccv)
'''
(status, output) = os.getstatusoutput('adb shell input swipe 320 410 320 1000 500')
print ('4',status, output)
'''

ccv=os.system('adb shell input swipe 320 410 320 1000 500')
print('4',ccv)

#0成功 1 失败