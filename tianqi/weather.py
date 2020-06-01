# -*- coding:utf-8 -*-
import urllib.request
import _thread
from my_def_lib import extract

url='https://tianqi.2345.com/haian/70445.htm'

def weather_report():
    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')
    #
    # print(content)



    print(extract(content,'<a class="five-days-item work-bg " href="javascript:void(0)">','<div class="ad-box">'))



if __name__ == '__main__':

    weather_report()
    '''
    try:
        _thread.start_new_thread(weather_report)
    except:
        print ("Error: 无法启动线程")
        '''