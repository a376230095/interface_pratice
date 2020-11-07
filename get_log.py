import logging


class Logs():
    # 定义一个生成器
    def __init__(self):
        self.logger=logging.getLogger("通通")
        self.logger.setLevel(logging.DEBUG)
        self.formatter=logging.Formatter("%(asctime)s|%(levelname)-6s|%(filename)s:%(lineno)-3s|%(message)s","%Y-%m-%d-%H:%M")

    # 定义流处理器
    def set_stream_handle(self):
        self.stream_handle=logging.StreamHandler()
        self.stream_handle.setFormatter(self.formatter)
        self.stream_handle.setLevel(logging.DEBUG)
        self.logger.addHandler(self.stream_handle)

    # 定义文件处理器
    def set_file_handle(self):
        self.file_handle=logging.FileHandler(filename="log.log",mode="w")
        self.file_handle.setFormatter(self.formatter)
        self.file_handle.setLevel(logging.DEBUG)
        self.logger.addHandler(self.file_handle)

    # 最终把处理器加入到生成器
    def get_logger(self):
        self.set_stream_handle()
        self.set_file_handle()
        return self.logger


if __name__ == "__main__":
    log=Logs()
    log.get_logger().info("abc")
