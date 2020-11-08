import configparser
import os


class GetConfig():
    # 弄一个根路径
    base_path=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    def __init__(self):
        # 初始化配置文件的对象
        self.config=configparser.ConfigParser()
        # 读取配置的文件,读取根目录+config.ini
        file_path=os.path.join(self.base_path,"config.ini")
        self.config.read(file_path)

    # 获取value，需要传入两个参数，section，option
    def get_value(self,section,option):
        value = self.config.get(section,option)
        return value

if __name__ == "__main__":
    a=GetConfig()
    print(a.base_path)
    ip=a.get_value("env","ip")
    print(ip)
