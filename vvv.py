import os
import requests
# **b,自动帮我们分解为一个key，value的形式
# 传了key，value，会变成一个字典的形式
def a(**b):
    print(b)

a(a=123,c=456)

# 封装requests，帮我们的请求传入请求方法、请求url、请求体、请求的参数
# res=requests.request(method="get",url="",params="",json="")
ip = "qyapi.weixin.qq.com"
corp_id = "ww630f49269e06f865"
contact_secret= "YC9RRMQcQqGNxapjoeiDIn84mCY7H-aJblz_X9X073U"
data="通过读取yml文件，获取到了api_data"
def send_api(data):
    # 定义一个请求的字典类型，字典存储我们的请求方法、请求url、请求参数、请求体

    # 通过对api_data进行解包，完成了以下的操作
    # res = requests.request(method="get",url="f"https://{ip}/cgi-bin/gettoken"").json()
    res=requests.request**api_dat(a).json()
    return res

print(send_api())


