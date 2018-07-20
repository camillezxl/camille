#coding:utf-8
from time import sleep
from selenium import webdriver

class lunch():
    #配置文件的地址
    profile_directory = r"C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\zaz66but.default"
    #加载配置
    profile = webdriver.FirefoxProfile(profile_directory)
    #启动浏览器配置
    driver = webdriver.Firefox(profile)
    url = "http://47.93.185.40:8081/auth/home.action"
    #正式环境地址：http://cos.telluspowertech.cn/auth/home.action#
    #测试环境地址：http://47.93.185.40:8081/auth/home.action
    driver.get(url)
    sleep(5)


