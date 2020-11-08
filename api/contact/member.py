import requests

from api.access_token import Access_token
from api.contact.base_api import BaseApi


class Member(BaseApi):
    a=Access_token()
    access_token=a.get_token()

    # 增加联系人
    def add_member(self):
        data = {
            "userid": "zhangsan",
            "name": "张三",
            "mobile": "+86 13800000000",
            "department": [1, 2],
        }
        res=self.send_api(data)
        token=res["access_token"]
        return token



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