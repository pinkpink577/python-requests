# python-requests
python+requests+unittest自动化接口搭建尝试

目录结构与用处：
common：

——configDb.py：这个文件主要编写数据库连接池的相关内容，本项目暂未考虑使用数据库来存储读取数据，此文件可忽略，或者不创建。本人是留着以后如果有相关操作时，方便使用。

——configEmail.py：这个文件主要是配置发送邮件的主题、正文等，将测试报告发送并抄送到相关人邮箱的逻辑。

——configHttp.py：这个文件主要来通过get、post、put、delete等方法来进行http请求，并拿到请求响应。

——HTMLTestRunner.py：主要是生成测试报告相关

——Log.py：调用该类的方法，用来打印生成日志

result:

——logs：生成的日志文件

——report.html：生成的测试报告

test_case:

——test01case.py：读取userCase.xlsx中的用例，使用unittest来进行断言校验

test_file:

——testcase01.xlsx：测试用例

caselist.txt：配置将要执行testCase目录下的哪些用例文件，前加#代表不进行执行。当项目过于庞大，用例足够多的时候，我们可以通过这个开关，来确定本次执行哪些接口的哪些用例。

config.ini：数据库、邮箱、接口等的配置项，用于方便的调用读取。

getpathInfo.py：获取项目绝对路径

geturlParams.py：获取接口的URL、参数、method等

readConfig.py：读取配置文件的方法，并返回文件中内容

readExcel.py：读取Excel的方法

runAll.py：开始执行接口自动化，项目工程部署完毕后直接运行该文件即可

test_api.py：自己写的提供本地测试的接口服务

test_sql.py：测试数据库连接池的文件，本次项目未用到数据库，可以忽略

使用方法：
在case文件夹中新增对应excel测试用例，再在入口执行测试框架，生成测试报告查看测试结果。
