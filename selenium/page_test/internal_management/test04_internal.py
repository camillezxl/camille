#coding:utf-8
from page_test.login.lunch import lunch
import unittest
from time import sleep

driver = lunch.driver
class recordsCharge(unittest.TestCase):

    def setUp(self):
        sleep(1)

    def tearDown(self):
        pass

    # def log_in(self,username,psw):
    #     u"""登录cos"""
    #     driver.find_element_by_id("user").send_keys(username)
    #     driver.find_element_by_id("pass").send_keys(psw)
    #     driver.find_element_by_id("login").click()
    #     sleep(5)
    #
    # def is_login_sucess(self):
    #     u"""判断登录是否成功"""
    #     try:
    #         login_name = driver.find_element_by_xpath(".//*[@id='header']/div[1]/div/span[1]").text
    #         print(login_name)
    #         return True
    #     except:
    #         return False
    #
    # def test_001_start(self):
    #     u"""启动浏览器"""
    #     #使用账号登录
    #     self.log_in("lisajg","111111")
    #     #正式环境账号：zybjjg，zy5269
    #     #测试环境账号：lisajg，密码：111111
    #     result = self.is_login_sucess()
    #     self.assertTrue(result)

    def test_002_recharge(self):
        u"""内部充值"""
        driver.find_element_by_link_text(u"内部管理").click()
        sleep(2)
        driver.find_element_by_link_text(u"内部充值").click()
        sleep(2)
        #卡类型查询 -  实物卡
        s1 = driver.find_element_by_xpath(".//*[@id='mainContent']/div[1]/form/div/table/tbody/tr[1]/td[1]/select")
        s1.click()
        sleep(1)
        driver.quit()

if __name__ == "__main__":
    unittest.main()