#coding:utf-8
import time
import os
import unittest
import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from test_163_mail.config import readConfig

# 当前脚本所在文件真实路径
cur_path = os.path.dirname(os.path.realpath(__file__))

# ---------1、加载用例--------------
def add_case(caseName = "case",rule = "test*.py"):
    # 用例所在路径
    case_path = os.path.join(cur_path,caseName)
    # 如果不存在这个case文件夹，就自动创建一个
    if not os.path.exists(case_path):os.mkdir(case_path)
    print("test case path:%s"%case_path)
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(case_path,pattern=rule,top_level_dir=None)
    print(discover)
    return discover

# -----------2、执行所有用例，并把结果写入HTML测试报告------------
def run_case(all_case,reportName = "report"):
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    # 测试报告文件夹
    report_path = os.path.join(cur_path,reportName)
    report_abspath = os.path.join(report_path,now+"result.html")
    print("report_path:%s"%report_abspath)
    fp = open(report_abspath,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="自动化测试报告,测试结果如下：",description="用例执行情况：")
    # 调用add_case函数返回值
    runner.run(all_case)
    fp.close()

# ----------3、获取最新的测试报告--------------
def get_report_file(report_path):
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn:os.path.getmtime(os.path.join(report_path,fn)))
    print("最新生成的测试报告："+lists[-1])
    # 找到最新生成的报告文件
    report_file = os.path.join(report_path,lists[-1])
    return report_file

# -----------4、发送最新的测试报告--------------
def send_mail(sender,psw,receiver,smtpserver,report_file,port):
    with open(report_file,'rb') as f:
        mail_body = f.read()
    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body,_subtype='htlml',_charset='utf-8')
    msg['subject'] = "自动化测试报告"
    msg['from'] = sender
    msg['to'] = receiver
    msg.attach(body)
    # 添加附件
    att = MIMEText(mail_body,"base64","utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment;filename = "report.html"'
    msg.attach(att)
    # 兼容163邮箱和QQ邮箱的发送邮件
    try:
        smtp = smtplib.SMTP_SSL(smtpserver,port)
    except:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver,port)
    smtp.login(sender,psw)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()
    print("邮件已发送，请查收！")

if __name__ == "__main__":
    # 加载用例
    all_case = add_case()
    # 执行用例
    run_case(all_case)
    # 用例文件夹
    report_path = os.path.join(cur_path,"report")
    # 获取最新的测试报告
    report_file = get_report_file(report_path)
    # 邮箱配置
    sender = readConfig.mail_sender
    psw = readConfig.mail_psw
    smtpserver = readConfig.smtp_server
    port = readConfig.mail_port
    receiver = readConfig.mail_receiver
    send_mail(sender,psw,receiver,smtpserver,report_file,port)
