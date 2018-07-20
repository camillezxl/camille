#coding:utf-8
import unittest
import os
import HTMLTestRunnerCN
import SendEmail
import time

#用例路径
case_path = os.path.join(os.getcwd(),"")
#报告存放路径
report_path = r"E:\\Python\\python_work\\selenium\\report\\"

def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,pattern="test*.py",top_level_dir=None)
    print(discover)
    return discover

if __name__ == "__main__":
    today = time.strftime('%Y-%m-%d %H-%M-%S',time.localtime())
    test_report = report_path
    filename = test_report + today + 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp,title=u"测试报告",description=u"管理后台")
    runner.run(all_case())
    fp.close()

    new_report = SendEmail.new_report(test_report)
    SendEmail.send_file(new_report)     #发送测试报告