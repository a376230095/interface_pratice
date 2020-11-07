import configparser
class GetConfig():

    def __init__(self):
        # 初始化配置文件的对象
        self.config=configparser.ConfigParser()
        # 读取配置的文件
        self.config.read("config.ini")

    # 获取value，需要传入两个参数，section，option
    def get_value(self,section,option):
        value = self.config.get(section,option)
        return value

if __name__ == "__main__":
    a=GetConfig()
    ip=a.get_value("env","ip")
    print(ip)
