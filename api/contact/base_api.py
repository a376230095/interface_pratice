import requests

from common.get_config import GetConfig
class BaseApi():
    base_config=GetConfig()
    ip=base_config.get_value("env","ip")
    def send_api(self,data:dict):
        """
        封装requests的方法
        :param data: 传入一个api的数据，包含method，url，params，json请求体
        :return: res是我们的响应，保存为json格式
        """
        # 通过对api_data进行解包，获取响应体数据
        res= requests.request(**data).json()
        return res
