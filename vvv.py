import yaml

# 读取yml文件
# 首先使用with open读取文件
# f是文件数据流
with open("a.yml",encoding="utf-8") as f:
    # 返回列表,通过yaml.safe_load读取yml文件数据流，并返回python的数据类型
    yml_list=yaml.safe_load(f)
    print(yml_list)


