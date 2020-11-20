import os
from string import Template

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

    # 封装模板技术，改变yml文件的参数（变量）
    def template(self,file,p_data:dict):
        # 让file变成一个相对路径，引用绝对路径来实现这个功能
        yaml_file=os.path.join(self.base_path,file)
        with open(yaml_file) as f:
            # 通过模板技术获取改变后的值
            request_data=Template(f.read()).substitute(p_data)
            # 把模板技术改变的值从字符串变成字典
            request_data=yaml.safe_load(request_data)
        return request_data



if __name__ == "__main__":
    pass
    # a=BaseApi()
    # print(a.get_token(a.contact_secret))
    # data=a.load_yaml("data/contact/member/add_member.yml")
    # print(data,type(data))
    # p_data = {
    #     # key就是${变量} 这个变量名,value就是我们要替换成为的值
    #     "token": 456,
    #     "userid": "tong",
    #     "name": "tong",
    #     "mobile": "131726116565",
    #     "department": [1, 2]
    # }
    # request_data=a.template("data/contact/member/add_member_demo.yml",p_data)
    # print(request_data)