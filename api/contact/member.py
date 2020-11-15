import requests

from api.access_token import Access_token
from api.contact.base_api import BaseApi
from common.get_config import GetConfig


class Member(BaseApi):
    config=GetConfig()
    # 获取我们的秘钥
    secret=config.get_value("wework", "contact_secret")


    # 增加联系人
    def add_member(self):
        # data = {
        #     "userid": "zhangsan",
        #     "name": "张三",
        #     "mobile": "+86 13800000000",
        #     "department": [1, 2],
        # }
        # 通过yml文件获取请求数据
        data=self.load_yaml("data/contact/member/add_member.yml")
        # res=self.send_api(data)
        # token=res["access_token"]
        # 由于data是一个字典，可以通过找到字典的key值，获取到value
        token=self.get_token(self.secret)
        data["params"]=f"access_token={token}"
        # 已经成功获取到了请求数据的字典类型，发送请求了
        res=self.send_api(data)
        # 返回响应
        return res

    # 增加联系人
    def get_member(self):
        pass

    # 增加联系人
    def edit_member(self):
        pass

    # 增加联系人
    def delete_member(self):
        pass

if __name__=="__main__":
    a=Member().add_member()
    print(a)