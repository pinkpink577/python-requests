# @describe:请求响应配置


import os
import smtplib
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SendEmail(object):
    def __init__(self, username, passwd, recv, title, content,
                 file=None, ssl=False,
                 email_host='smtp.163.com', port=25, ssl_port=465):
        self.username = username  # 用户名
        self.passwd = passwd  # 密码
        self.recv = recv  # 收件人，多个要传list ['a@qq.com','b@qq.com]
        self.title = title  # 邮件标题
        self.content = content  # 邮件正文
        self.file = file  # 附件路径，如果不在当前目录下，要写绝对路径
        self.email_host = email_host  # smtp服务器地址
        self.port = port  # 普通端口
        self.ssl = ssl  # 是否安全链接
        self.ssl_port = ssl_port  # 安全链接端口

    def send_email(self):
        msg = MIMEMultipart()
        # 发送内容的对象
        if self.file:  # 处理附件的
            file_name = os.path.split(self.file)[-1]  # 只取文件名，不取路径
            try:
                f = open(self.file, 'rb').read()
            except Exception as e:
                raise Exception('附件打不开！！！！')
            else:
                att = MIMEText(f, "base64", "utf-8")
                att["Content-Type"] = 'application/octet-stream'
                # base64.b64encode(file_name.encode()).decode()
                new_file_name = '=?utf-8?b?' + base64.b64encode(file_name.encode()).decode() + '?='
                # 这里是处理文件名为中文名的，必须这么写
                att["Content-Disposition"] = 'attachment; filename="%s"' % (new_file_name)
                msg.attach(att)
        msg.attach(MIMEText(self.content))  # 邮件正文的内容
        msg['Subject'] = self.title  # 邮件主题
        msg['From'] = self.username  # 发送者账号
        msg['To'] = ','.join(self.recv)  # 接收者账号列表
        if self.ssl:
            self.smtp = smtplib.SMTP_SSL(self.email_host, port=self.ssl_port)
        else:
            self.smtp = smtplib.SMTP(self.email_host, port=self.port)
        # 发送邮件服务器的对象
        self.smtp.login(self.username, self.passwd)
        try:
            self.smtp.sendmail(self.username, self.recv, msg.as_string())
            pass
        except Exception as e:
            print('出错了。。', e)
        else:
            print('发送成功！')
        self.smtp.quit()


if __name__ == '__main__':
    m = SendEmail(
        username='@163.com',
        passwd='',
        recv=[''],
        title='',
        content='测试发送邮件',
        file=r'D:\测试截图\1.png',
        ssl=True,
    )
    m.send_email()

# import os
# import win32com.client as win32
# import datetime
# import readConfig
# import getpathInfo
# from common.Log import logger
#
#
# read_conf = readConfig.ReadConfig()
# subject = read_conf.get_email('subject')#从配置文件中读取，邮件主题
# app = str(read_conf.get_email('app'))#从配置文件中读取，邮件类型
# addressee = read_conf.get_email('addressee')#从配置文件中读取，邮件收件人
# cc = read_conf.get_email('cc')#从配置文件中读取，邮件抄送人
# mail_path = os.path.join(getpathInfo.get_Path(), 'result', 'report.html')#获取测试报告路径
# logger = logger
#
# class send_email():
#     def outlook(self):
#         olook = win32.Dispatch("%s.Application" % app)
#         mail = olook.CreateItem(win32.constants.olMailItem)
#         mail.To = addressee # 收件人
#         mail.CC = cc # 抄送
#         mail.Subject = str(datetime.datetime.now())[0:19]+'%s' %subject#邮件主题
#         mail.Attachments.Add(mail_path, 1, 1, "myFile")
#         content = """
#                     执行测试中……
#                     测试已完成！！
#                     生成报告中……
#                     报告已生成……
#                     报告已邮件发送！！
#                     """
#         mail.Body = content
#         mail.Send()
#         print('send email ok!!!!')
#         logger.info('send email ok!!!!')
#
#
# if __name__ == '__main__':# 运营此文件来验证写的send_email是否正确
#     print(subject)
#     send_email().outlook()
#     print("send email ok!!!!!!!!!!")