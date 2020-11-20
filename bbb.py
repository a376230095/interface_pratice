from string import Template

# 需要先读取这个yml文件
import yaml

with open("data/contact/member/add_member_demo.yml") as f:
    # f.read()是把文件中的内容读取出来，然后转化成字符串的形式
    p_data={
        # key就是${变量} 这个变量名,value就是我们要替换成为的值
        "token":456,
        "userid":"tong",
        "name":"tong",
        "mobile":"131726116565",
        "department":[1,2]

    }
    request_data=Template(f.read()).substitute(p_data)
    # 由于Tempalte转化的值是一个str类型的，我们需要用dict去传参，需要转化为dict类型
    # yaml.safe_load可以转化为dict类型
    request_data=yaml.safe_load(request_data)
    print(request_data)
    print(type(request_data))