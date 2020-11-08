import requests

from api.contact.member import Member
from common.get_log import Logs
from common.get_config import GetConfig


class TestMember():
    # 初始化我们的member的对象
    member=Member()

    log=Logs().get_logger()
    # 生产环境
    # ip="qyapi.weixin.qq.com"
    config=GetConfig()
    ip=config.get_value("env","ip")
    # 测试环境
    # ip ="192.168.0.1"



    def setup(self):
        pass
        # corpid = "ww630f49269e06f865"
        # corpsecret = "YC9RRMQcQqGNxapjoeiDIn84mCY7Hf-ablz_X9X073U"
        # token_url = f"https://{self.ip}/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        # token_res = requests.get(url=token_url).json()
        # self.log.info(f"获取access_token的响应{token_res}")
        # self.access_token = token_res["access_token"]

    def test_add_member(self):
        res = self.member.add_member()
        self.log.info("abcdddddddddddddddddddddddd")
        assert res["errcode"] == 0



