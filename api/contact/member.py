import requests

from api.access_token import Access_token
from api.contact.base_api import BaseApi
from common.get_config import GetConfig


class Member(BaseApi):
    config=GetConfig()
    # 获取我们的秘钥
    secret=config.get_value("wework", "contact_secret")
    token=BaseApi().get_token(secret)


    # 增加联系人
    def add_member(self,userid,name,mobile,department):
        # data = {
        #     "userid": "zhangsan",
        #     "name": "张三",
        #     "mobile": "+86 13800000000",
        #     "department": [1, 2],
        # }
        # 通过yml文件获取请求数据
        # data=self.load_yaml("data/contact/member/add_member.yml")
        # # res=self.send_api(data)
        # # token=res["access_token"]
        # # 由于data是一个字典，可以通过找到字典的key值，获取到value
        # token=self.get_token(self.secret)
        # data["params"]=f"access_token={token}"
        # # 要改一下userid，name，mobile，department的值
        # data["json"]["userid"]=userid
        # data["json"]["name"]=name
        # data["json"]["mobile"]=mobile
        # data["json"]["department"]=department
        p_data = {
            # key就是${变量} 这个变量名,value就是我们要替换成为的值
            "token":self.token,
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": [1, 2]
        }
        request_data = self.template("data/contact/member/add_member_demo.yml", p_data)
        # 已经成功获取到了请求数据的字典类型，发送请求了
        res=self.send_api(request_data)
        # 返回响应
        return res

    # 增加联系人
    def get_member(self):
        pass

    # 增加联系人
    def edit_member(self):
        pass

    # 增加联系人
    def delete_member(self,userid):
        p_data = {
            "token": self.token,
            "userid": userid,
        }
        request_data=self.template("data/contact/member/delete_member.yml",p_data)
        res=self.send_api(request_data)
        return res


if __name__=="__main__":
    # a=Member().add_member("tong1234","tong1234","13999661165",[1,2])
    a=Member()
    res=a.delete_member("tong1234")
    print(res)