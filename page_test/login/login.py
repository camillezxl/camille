#coding:utf-8
from time import sleep
from lunch import lunch
import unittest

driver = lunch.driver
class login(unittest.TestCase):

    def log_in(self,username,psw):
        u"""登录cos"""
        driver.find_element_by_id("user").send_keys(username)
        driver.find_element_by_id("pass").send_keys(psw)
        driver.find_element_by_id("login").click()
        sleep(2)

    def is_login_sucess(self):
        u"""判断登录是否成功"""
        try:
            login_name = driver.find_element_by_xpath(".//*[@id='header']/div[1]/div/span[1]").text
            print(login_name)
            return True
        except:
            return False

    def test_001_start(self):
        u"""启动浏览器"""
        #使用账号登录
        self.log_in("zybjjg","zy5269")
        #正式环境账号：zybjjg，zy5269
        #测试环境账号：lisajg，密码：111111
        result = self.is_login_sucess()
        self.assertTrue(result)
