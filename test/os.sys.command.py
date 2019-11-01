import os


#os.system('ping 8.8.8.8')
def cheak_adb_link(order):
    return_txt=os.popen(order).read()
    if 'TTL=' in return_txt:
        return True
    else:
        return False


print(cheak_adb_link('ping 8.8.8.8 -n 1'))
#print (os.popen('ping 8.8.8.8 -n 1').read())

'''
(status, output) = commands.getstatusoutput('ping 8.8.8.8')
print (status, output)
'''