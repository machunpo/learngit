



import win32com.client as win #pip install pypiwin32

speak = win.Dispatch("SAPI.SpVoice")  #增加语音播报的模块
speak.Rate=-1 


speak.Speak('本次卫星回收任务圆满成功，请远洋测量人员进行回车定位操作')