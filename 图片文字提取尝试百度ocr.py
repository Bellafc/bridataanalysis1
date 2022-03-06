#!/usr/bin/env python
# coding: utf-8

# In[2]:


from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '25715021'
API_KEY = 'SuU9SXax7MOMns4SauG3pFhM'
SECRET_KEY = '6wtahuFmvqk8voUWXbRDOM6OHUq8T4vt'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


# In[4]:


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('图像识别1.png')

""" 调用通用文字识别（高精度版） """
client.basicAccurate(image);

""" 如果有可选参数 """
options = {}
options["detect_direction"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别（高精度版） """
client.basicAccurate(image, options)


# In[ ]:




