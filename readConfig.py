import os
import codecs
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]  # 1.获得当前执行脚本的绝对路径 2.按照路径将文件名和路径分隔开，取路径名
configPath = os.path.join(proDir, "config.ini")     # 将proDir目录与config.ini文件名合成一条路径


class ReadConfig:
    def __init__(self):
        fd = open(configPath)
        data = fd.read()

        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:  # 判断是否带有BOM(ByteOrderMark)文件，如果有则直接改写文件内容，删除BOM
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()   # 初始化
        self.cf.read(configPath)    # 读取configPath路径

    # 获取邮箱地址
    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    # 获取接口地址
    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    # 获取数据库地址
    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value
