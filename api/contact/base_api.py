import os

import requests
import yaml

from common.get_config import GetConfig
class BaseApi():
    base_config=GetConfig()
    ip=base_config.get_value("env","ip")
    corpid = base_config.get_value("wework", "corp_id")
    contact_secret = base_config.get_value("wework", "contact_secret")
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    def send_api(self,data:dict):
        """
        封装requests的方法
        :param data: 传入一个api的数据，包含method，url，params，json请求体
        :return: res是我们的响应，保存为json格式
        """
        # 通过对api_data进行解包，获取响应体数据
        res= requests.request(**data).json()
        return res

    # 获取access_token
    def get_token(self,secret):
        api_data = {
            "method": "get",
            "url": f"https://{self.ip}/cgi-bin/gettoken",
            "params": f"corpid={self.corpid}&corpsecret={secret}"
        }
        res = self.send_api(api_data)
        # 获取token
        token = res["access_token"]
        return token

    # 读取yaml文件的,需要传文件，返回字典数据
    # 由于file不能传绝对路径，需要有根路径的支持，变成相对路径
    def load_yaml(self,file_path):
        yaml_path=os.path.join(self.base_path,file_path)
        with open(yaml_path,encoding="utf-8") as f:
            yaml_data=yaml.safe_load(f)
        return yaml_data



if __name__ == "__main__":
    a=BaseApi()
    # print(a.get_token(a.contact_secret))
    data=a.load_yaml("data/contact/member/add_member.yml")
    print(data,type(data))