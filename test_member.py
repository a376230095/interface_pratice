import requests

class TestMember():

    def setup(self):
        corpid = "ww630f49269e06f865"
        corpsecret = "YC9RRMQcQqGNxapjoeiDIn84mCY7H-aJblz_X9X073U"
        token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        token_res = requests.get(url=token_url).json()
        self.access_token = token_res["access_token"]

    def test_add_member(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.access_token}"
        data = {
            "userid": "zhangsan",
            "name": "张三",
            "mobile": "+86 13800000000",
            "department": [1, 2],
        }
        res = requests.post(url=url, json=data).json()
        assert res["errcode"] == 0

