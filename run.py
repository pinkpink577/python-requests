import unittest
from common import HTMLTestRunner
from common.log import *
from common.configHttp import *


def set_case_list(self):
    fb = open(self.caseListFile)
    for value in fb.readlines():
        data = str(value)
        if data != '' and not data.startswith("#"):
            self.caseList.append(data.replace("\n", ""))
    fb.close()


def set_case_suite(self):
    self.set_case_list()
    test_suite = unittest.TestSuite()
    suite_model = []

    for case in self.caseList:
        case_file = os.path.join(readConfig.proDir, "test_case")
        print(case_file)
        case_name = case.split("/")[-1]
        print(case_name+".py")
        discover = unittest.defaultTestLoader.discover(case_file, pattern=case_name + '.py', top_level_dir=None)
        suite_model.append(discover)

    if len(suite_model) > 0:
        for suite in suite_model:
            for test_name in suite:
                test_suite.addTest(test_name)
    else:
        return None
    return test_suite


def run(self):
    try:
        suit = self.set_case_suite()
        log_ = Log()
        if suit is not None:
            log_.logger.info("********TEST START********")
            fp = open(self.resultPath, 'wb')
            runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
            runner.run(suit)
        else:
            log_.logger.info("Have no case to test.")
    except Exception as ex:
        log_.logger.error(str(ex))
    finally:
        log_.logger.info("*********TEST END*********")
        # send test report by email
        # if int(on_off) == 0:
        #     self.email.send_email()
        # elif int(on_off) == 1:
        #     logger.info("Doesn't send report email to developer.")
        # else:
        #     logger.info("Unknow state.")
