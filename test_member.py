import requests

import logging
from get_log import Logs
from get_config import GetConfig


class TestMember():
    log=Logs().get_logger()
    # 生产环境
    # ip="qyapi.weixin.qq.com"
    config=GetConfig()
    ip=config.get_value("env","ip")
    # 测试环境
    # ip ="192.168.0.1"



    def setup(self):
        corpid = "ww630f49269e06f865"
        corpsecret = "YC9RRMQcQqGNxapjoeiDIn84mCY7H-aJblz_X9X073U"
        token_url = f"https://{self.ip}/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        token_res = requests.get(url=token_url).json()
        self.log.info(f"获取access_token的响应{token_res}")
        self.access_token = token_res["access_token"]

    def test_add_member(self):
        url = f"https://{self.ip}/cgi-bin/user/create?access_token={self.access_token}"
        data = {
            "userid": "zhangsan",
            "name": "张三",
            "mobile": "+86 13800000000",
            "department": [1, 2],
        }
        res = requests.post(url=url, json=data).json()
        self.log.info(f"增加联系人的响应{res}")
        assert res["errcode"] == 0

