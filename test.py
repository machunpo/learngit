import my_def_lib
import json
import urllib.request
import random

random_number=0
url="https://api.caiyunapp.com/v2/place?token=token&count=1&lang=zh_CN&query=%E6%B5%B7%E5%AE%89%E5%8E%BF&random=2"
response = urllib.request.urlopen(url)
content = response.read().decode('gbk', 'ignore')
new_dict = json.loads(content)
print(new_dict)

