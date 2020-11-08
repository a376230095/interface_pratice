import requests

from api.contact.base_api import BaseApi
from common.get_config import GetConfig

class Access_token(BaseApi):
    config=GetConfig()
    ip=config.get_value("env","ip")
    corpid = config.get_value("wework","corp_id")
    contact_secret = config.get_value("wework","contact_secret")
    # 获取access_token
    def get_token(self):
        api_data={
            "method":"get",
            "url":f"https://{self.ip}/cgi-bin/gettoken",
            "params":f"corpid={self.corpid}&corpsecret={self.contact_secret}"
        }
        res=self.send_api(api_data)
        # 获取token
        token=res["access_token"]
        return token

if __name__ == "__main__":
    a=Access_token()
    print(a.get_token())
