# @describe:测试断言

import json
import unittest
from common.configHttp import RunMain
import paramunittest
import geturlParams
import urllib.parse
import readExcel

url = geturlParams.GeturlParams().get_Url()
query_xls = readExcel.ReadExcel().get_xls('testcase01.xlsx', 'test')


@paramunittest.parametrized(*query_xls)
class TestQuery(unittest.TestCase):
    def setParameters(self, case_name, path, query, method):

        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)

    def description(self):
        self.case_name

    def setup(self):
        print(self.case_name+'测试开始前准备')

    def test01case(self):
        self.checkResult()

    def tearDown(self):
        print('测试结束，输出log完结\n')

    def checkResult(self):  # 断言
        url1 = "http://127.0.0.1:8888/query1?"
        new_url = url1 + self.query
        data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))  #  将一个完整的URL中参数转化为字典
        info = RunMain().run_main(self.method, url, data1)  # 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        ss = json.loads(info)   # 将响应转换为字典格式
        if self.case_name == 'post_city':   # 如果case_name是，说明合法，返回的code应该为200
            self.assertEqual(ss['error_code'], 0)
        if self.case_name == 'post_city_error':  # 同上
            self.assertEqual(ss['error_code'], 1)
        if self.case_name == 'post_city_null':  # 同上
            self.assertEqual(ss['error_code'], 2)


if __name__ =='__main__':
    unittest.main()