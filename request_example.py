# -*- coding: utf-8 -*-
# @Time    : 2023/3/20 15:10
# @Author  : OKC
import requests

url = "http://127.0.0.1:7401/infer"

payload={'save_img': 'Y'}
files=[
  ('image',('基金版面.JPG',open('img.png','rb'),'application/octet-stream'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)