import requests
from get_log import Logs

class TestMember():
    log = Logs().get_logger()


    def setup(self):
        corpid = "f"
        corpsecret = "YC9RRMQcQqGNxapjoeiDIn84mCY7H-aJblz_X9X073U"
        token_url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        token_res = requests.get(url=token_url).json()
        self.log.info(f"获取access_token的响应{token_res}")
        self.access_token = token_res["access_token"]

    def test_get_member(self):
        userid="zhangsan"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.access_token}&userid={userid}"
        res = requests.get(url=url).json()
        self.log.info(f"获取联系人的响应{res}")
        assert res["errcode"] == 0