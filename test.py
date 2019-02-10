import win32com.client as win #pip install pypiwin32
speak = win.Dispatch("SAPI.SpVoice")
speak.Speak("come on")
speak.Speak("你好")


#测试获得成功