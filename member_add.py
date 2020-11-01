import requests

# 增加一个联系人，写一个很粗暴的代码

corpid="ww630f49269e06f865"
corpsecret="YC9RRMQcQqGNxapjoeiDIn84mCY7H-aJblz_X9X073U"
token_url=f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"

# 使用.text或获取到字符串，那么提取我们的access_token是不是很麻烦
token_res=requests.get(url=token_url).text

print(token_res)
print(type(token_res))


# res.json()可以直接获取到响应体，并自动转化成字典格式
token_res=requests.get(url=token_url).json()
assert token_res["errcode"] == 123456
access_token=token_res["access_token"]
print(access_token)

url=f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={access_token}"

data={
    "userid": "zhangsan",
    "name": "张三",
    "mobile": "+86 13800000000",
    "department": [1, 2],
}

res=requests.post(url=url,json=data).json()
assert token_res["errcode"] == 123456
print(res)