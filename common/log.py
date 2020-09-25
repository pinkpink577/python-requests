# describe：日志记录

import logging
from datetime import datetime
import threading

class log:
    class Log:
        def __init__(self):
            global logPath, resultPath, proDir
            proDir = readConfig.proDir
            resultPath = os.path.join(proDir, "result")
            # create result file if it doesn't exist
            if not os.path.exists(resultPath):
                os.mkdir(resultPath)
            # defined test result file name by localtime
            logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%M%S")))
            # create test result file if it doesn't exist
            if not os.path.exists(logPath):
                os.mkdir(logPath)
            # defined logger
            self.logger = logging.getLogger()
            # defined log level
            self.logger.setLevel(logging.INFO)

            # defined handler
            handler = logging.FileHandler(os.path.join(logPath, "output.log"))
            # defined formatter
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            # defined formatter
            handler.setFormatter(formatter)
            # add handler
            self.logger.addHandler(handler)