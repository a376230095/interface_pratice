import logging


# 定义一个生成器,名字为tong
logger=logging.getLogger("tong")

# 定义这个tong的生成器的level
# DEBUG,INFO,ERROR
level=logger.setLevel(logging.DEBUG)

# 定义处理器（流处理器，文件处理器）
stream=logging.StreamHandler()

# 传文件名，模式是怎么样，w，a
file=logging.FileHandler("a.txt","w")

# 定义一个格式
format=logging.Formatter("%(asctime)s|%(levelname)-6s|%(filename)s:%(lineno)-3s|%(message)s","%Y-%m-%d-%H:%M")

#
stream.setLevel(logging.DEBUG)

# 把格式弄到生成器里面去
stream.setFormatter(format)

# 把这个流处理器放入到生成器中
# logger.addHandler(stream)

file.setLevel(logging.DEBUG)
file.setFormatter(format)
# 把文件处理器加入到生成器中
logger.addHandler(file)

logger.error("abc")





# def set_stream(self):
#     # 生成处理器流处理器
#     consolehandle = logging.StreamHandler()
#     # 默认等级为DEBUG
#     consolehandle.setLevel(logging.DEBUG)
#     # 处理器添加格式，这里都添加同一个
#     consolehandle.setFormatter(self.formatter)
#     # 记录器添加处理器，就拥有了屏幕输出的和文件输出的日志了
#     self.logger.addHandler(consolehandle)