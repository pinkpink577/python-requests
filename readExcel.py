# @describe:读取Excel的方法

import os
import getpathInfo
from xlrd import open_workbook

path = getpathInfo.get_Path()


class ReadExcel(object):
    def get_xls(self, xls_name, sheet_name): # xls_name填写用例的Excel名称 sheet_name该Excel的sheet名称
        cls = []
        # 获取用例文件路径
        xlsPath = os.path.join(path, "test_file", 'case', xls_name)
        file = open_workbook(xlsPath)  # 打开用例Excel
        sheet = file.sheet_by_name(sheet_name)  # 获取该sheet
        # 获取sheet内容行数
        nrows = sheet.nrows
        for i in range(nrows):
            if sheet.row_values(i)[0] != u'case_name':
                cls.append(sheet.row_values(i))
        return cls


if __name__ == '__main__':
    print(ReadExcel().get_xls('testcase01.xlsx', 'test'))
    print(ReadExcel().get_xls('testcase01.xlsx', 'test')[0][1])
    print(ReadExcel().get_xls('testcase01.xlsx', 'test')[1][2])
