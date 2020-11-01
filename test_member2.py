import requests

class TestMember():

    def setup_class(self):


    def setup(self):
        corpid = "ww630f49269e06f865"
        corpsecret = "YC9RRMQcQqGNxapjoeiDIn84mCY7H-aJblz_X9X073U"
        token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        token_res = requests.get(url=token_url).json()
        print(token_res)
        self.access_token = token_res["access_token"]

    def test_get_member(self):
        userid="zhangsan"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.access_token}&userid={userid}"
        res = requests.get(url=url).json()
        print(res)
        assert res["errcode"] == 0