import requests
import my_def_lib
import time
import win32com.client as win  # pip install pypiwin32

speak = win.Dispatch("SAPI.SpVoice")  #增加语音播报的模块
speak.Rate=-2     #说话速度 -10到10

url='https://3g.dxy.cn/newh5/view/pneumonia'#丁香园关于疫情的实时播报

duibi='新年快乐'
while (1):
    respones = requests.get(url)
    uft_str=respones.text
    uft_str = uft_str.encode("iso-8859-1").decode('utf8')#.encode('utf8')

    list_1=my_def_lib.extract(uft_str,'<p class="topicTitle___2ovVO">','</p>')
    news_feiyang=my_def_lib.quchu_heml(list_1[0])
    print(news_feiyang)
    
    list_2=my_def_lib.extract(uft_str,'<p class="topicContent___1KVfy">','</p>')
    news_feiyang1=my_def_lib.quchu_heml(list_2[0])
    print(news_feiyang1)

    #my_def_lib.speak_and_print(news_feiyang)
    if (duibi != news_feiyang) :

        speak.Speak(news_feiyang)
        speak.Speak(news_feiyang1)
        duibi=news_feiyang
    else:
        time.sleep(300)




#<p class="topicTitle___2ovVO"><i>最新</i>湖北启动突发公共卫生事件二级应急响应</p>
'''
22 日凌晨，湖北发布加强新型肺炎防控通告：根据《中华人民共和国传染病防治法》等有关法律法规的规定，省人民政府决定启动突发公共卫生事件 II 级应急响应。通告包括严格实行属地管理制度、严格实施隔离措施等7部分。</p>

 '''
# 查看响应内容，response.content返回的字节流数据
#print (respones.content)
 
# 查看完整url地址
#print ('地址：',respones.url)
 
# 查看响应头部字符编码
#print (respones.encoding)
 
# 查看响应码
#print (respones.status_code)
