# @describe：日志记录

import logging, os
import readConfig
from datetime import datetime
import threading


class Log:
    def __init__(self):

        global logPath, resultPath, proDir
        proDir = readConfig.proDir
        resultPath = os.path.join(proDir, "result")
        # 判断result文件是否存在
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        # 按照本地时间定义测试结果文件名
        logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))
        # 判断测试结果文件是否存在
        if not os.path.exists(logPath):
            os.mkdir(logPath)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        # 定义FileHandler
        handler = logging.FileHandler(os.path.join(logPath, "output.log"))
        # 定义日志格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # 定义对象日志格式
        handler.setFormatter(formatter)
        # 日志加载至FileHandler，通过log日志文件进行日志记录
        self.logger.addHandler(handler)


class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():

        if MyLog is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()

        return MyLog.log
