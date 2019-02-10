import win32com.client as win #pip install pypiwin32
speak = win.Dispatch("SAPI.SpVoice")
speak.Rate=-5
#说话速度 -10到10
speak.Speak("您查询的关键词是：winsapi.voice 以下是该网页在北京时间 2019年01月29日 01:54:09 的快照；如果打开速度慢，可以尝试快速版；如果想更新或删除快照，可以投诉快照。")


#测试获得成功