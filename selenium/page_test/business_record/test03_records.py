#coding:utf-8
from page_test.login.lunch import lunch
import unittest
from time import sleep
from selenium.webdriver.support.select import Select

driver = lunch.driver
class recordsCharge(unittest.TestCase):

    def setUp(self):
        sleep(1)

    def tearDown(self):
        pass

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
        self.log_in("lisajg","111111")
        #正式环境账号：zybjjg，密码：zy5269
        #测试环境账号：lisajg，密码：111111
        result = self.is_login_sucess()
        self.assertTrue(result)

    def test_002_businessRecords_recharge(self):
        u"""充值记录"""
        #业务记录
        driver.find_element_by_link_text(u"业务记录").click()
        sleep(3)
    #     #充值记录
    #     driver.find_element_by_xpath(".//*[@id='sidebar']/div[4]/dl/dd[1]/div/a").click()
    #     sleep(1)
    #     #按卡号查询
    #     driver.find_element_by_id("cardCode").send_keys("6202006458")
    #     #定义查询按钮
    #     query = driver.find_element_by_xpath(".//*[@id='mainContent']/div[1]/form/div/table/tbody/tr[2]/td[3]/button")
    #     query.click()
    #     sleep(1)
    #     driver.find_element_by_id("cardCode").clear()
    #     query = driver.find_element_by_xpath(".//*[@id='mainContent']/div[1]/form/div/table/tbody/tr[2]/td[3]/button")
    #     query.click()
    #     sleep(1)
    #     #按会员姓名查询
    #     name = driver.find_element_by_xpath(".//*[@id='mainContent']/div[1]/form/div/table/tbody/tr[1]/td[2]/input")
    #     name.send_keys(u"周莹测试001")
    #     sleep(1)
    #     query = driver.find_element_by_xpath(".//*[@id='mainContent']/div[1]/form/div/table/tbody/tr[2]/td[3]/button")
    #     query.click()
    #     sleep(2)
    #     name = driver.find_element_by_xpath(".//*[@id='mainContent']/div[1]/form/div/table/tbody/tr[1]/td[2]/input")
    #     name.clear()
    #     sleep(1)
    #     query = driver.find_element_by_xpath(".//*[@id='mainContent']/div[1]/form/div/table/tbody/tr[2]/td[3]/button")
    #     query.click()
    #     sleep(1)
    #     #按电话号码查询
    #     phone = driver.find_element_by_xpath(".//*[@id='mainContent']/div[1]/form/div/table/tbody/tr[1]/td[3]/input")
    #     phone.send_keys("15313558519")
    #     query = driver.find_element_by_xpath(".//*[@id='mainContent']/div[1]/form/div/table/tbody/tr[2]/td[3]/button")
    #     query.click()
    #     sleep(1)
    #     phone = driver.find_element_by_xpath(".//*[@id='mainContent']/div[1]/form/div/table/tbody/tr[1]/td[3]/input")
    #     phone.clear()
    #     query = driver.find_element_by_xpath(".//*[@id='mainContent']/div[1]/form/div/table/tbody/tr[2]/td[3]/button")
    #     query.click()
    #     sleep(1)
    #     #按证件号查询
    #     ident = driver.find_element_by_xpath(".//*[@id='mainContent']/div[1]/form/div/table/tbody/tr[2]/td[1]/input")
    #     ident.send_keys("120225198809042512")
    #     query = driver.find_element_by_xpath(".//*[@id='mainContent']/div[1]/form/div/table/tbody/tr[2]/td[3]/button")
    #     query.click()
    #     sleep(1)
    #     ident = driver.find_element_by_xpath(".//*[@id='mainContent']/div[1]/form/div/table/tbody/tr[2]/td[1]/input")
    #     ident.clear()
    #     query = driver.find_element_by_xpath(".//*[@id='mainContent']/div[1]/form/div/table/tbody/tr[2]/td[3]/button")
    #     query.click()
    #     sleep(1)
    #     #按时间查询
    #     start_date = ".//*[@id='mainContent']/div[1]/form/div/table/tbody/tr[2]/td[2]/input[1]"
    #     driver.find_element_by_xpath(start_date).send_keys("2016-05-01")
    #     sleep(1)
    #     end_date = ".//*[@id='mainContent']/div[1]/form/div/table/tbody/tr[2]/td[2]/input[2]"
    #     driver.find_element_by_xpath(end_date).send_keys("2016-07-07")
    #     sleep(1)
    #     query = driver.find_element_by_xpath(".//*[@id='mainContent']/div[1]/form/div/table/tbody/tr[2]/td[3]/button")
    #     query.click()
    #     sleep(1)
    #     #清空时间设置
    #     start_date = ".//*[@id='mainContent']/div[1]/form/div/table/tbody/tr[2]/td[2]/input[1]"
    #     driver.find_element_by_xpath(start_date).click()
    #     clear = ".//*[@id='calendar']/div/div[3]/button[1]"
    #     driver.find_element_by_xpath(clear).click()
    #     sleep(1)
    #
    #     end_date = ".//*[@id='mainContent']/div[1]/form/div/table/tbody/tr[2]/td[2]/input[2]"
    #     driver.find_element_by_xpath(end_date).click()
    #     clear = ".//*[@id='calendar']/div/div[3]/button[1]"
    #     driver.find_element_by_xpath(clear).click()
    #     sleep(1)
    #
    #     query = driver.find_element_by_xpath(".//*[@id='mainContent']/div[1]/form/div/table/tbody/tr[2]/td[3]/button")
    #     query.click()
    #     sleep(1)
    #
    #     #下一页
    #     driver.find_element_by_class_name("next").click()
    #     sleep(1)
    #     driver.find_element_by_class_name("next").click()
    #     sleep(3)
    #     #每页显示20条
    #     driver.find_element_by_class_name("select").click()
    #     sleep(0.1)
    #     driver.find_element_by_link_text("20").click()
    #     sleep(2)
    #     #每页显示50条
    #     driver.find_element_by_class_name("select").click()
    #     sleep(0.1)
    #     driver.find_element_by_link_text("50").click()
    #     sleep(2)
    #     #每页显示100条
    #     driver.find_element_by_class_name("select").click()
    #     sleep(0.1)
    #     driver.find_element_by_link_text("100").click()
    #     sleep(2)
    #     driver.find_element_by_link_text("1").click()
    #     sleep(1)
    #     #聚焦元素
    #     target1 = driver.find_element_by_xpath("//div[@class='tableList']/table/tbody/tr[14]/td[1]")
    #     driver.execute_script("arguments[0].scrollIntoView();", target1)
    #     sleep(2)
    #
    #     #申请发票
    #     driver.find_element_by_link_text(u"申请发票").click()
    #     sleep(1)
    #     driver.find_element_by_id("riseText").send_keys(u"北京富电绿能科技股份有限公司")
    #     driver.find_element_by_id("taxpayerIdentificationNumber").send_keys("91110108101437375L")
    #     driver.find_element_by_xpath("html/body/div[14]/div[2]/div/form/div[2]/ul/li[1]/button").click()
    #     sleep(2)
    #     driver.find_element_by_xpath(".//*[@id='alertMsgBox']/div[1]/div/div[2]/ul/li[1]/a/span").click()
    #     sleep(10)
    #
    #     #每页显示100条
    #     driver.find_element_by_class_name("select").click()
    #     sleep(0.1)
    #     driver.find_element_by_link_text("100").click()
    #     sleep(2)
    #
    #     #内嵌滚动条 - 滚动到底部
    #     js1 = "document.getElementsByClassName('tableList')[0].scrollTop=10000"
    #     driver.execute_script(js1)
    #     sleep(2)
    #
    #     #内嵌滚动条 - 滚动到顶部
    #     js2 = "document.getElementsByClassName('tableList')[0].scrollTop=0"
    #     driver.execute_script(js2)
    #     sleep(2)
    #
    #     #内嵌滚动条 - 横向右滑
    #     js2 = "document.getElementsByClassName('tableList')[0].scrollLeft=10000"
    #     driver.execute_script(js2)
    #     sleep(2)
    #
    #     #内嵌滚动条 - 横向左滑
    #     js2 = "document.getElementsByClassName('tableList')[0].scrollLeft=0"
    #     driver.execute_script(js2)
    #     sleep(2)
    #
    # def test_003_record_of_income(self):
    #     u"""收入记录"""
    #     driver.find_element_by_link_text(u"收入记录").click()
    #     sleep(1)
    #     #按卡号查询
    #     driver.find_element_by_id("cardCode").send_keys("200100005501")
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #     driver.find_element_by_id("cardCode").clear()
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #
    #
    #     #横向右侧滑动
    #     js1 = "document.getElementsByClassName('tableList')[0].scrollLeft=10000"
    #     driver.execute_script(js1)
    #     sleep(2)
    #     #按会员姓名查询
    #     driver.find_element_by_id("taxpayerIdentificationNumber").send_keys("91110108101437375L")
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #     #横向右侧滑动
    #     js1 = "document.getElementsByClassName('tableList')[0].scrollLeft=10000"
    #     driver.execute_script(js1)
    #     sleep(2)
    #
    #     #发票入库
    #     driver.find_element_by_link_text(u"发票入库").click()
    #     sleep(2)
    #     driver.find_element_by_id("invoiceCode").send_keys("91110108101437375L")
    #     driver.find_element_by_xpath("html/body/div[14]/div[2]/div/form/div[2]/ul/li[1]/button").click()
    #     sleep(1)
    #     driver.find_element_by_xpath(".//*[@id='alertMsgBox']/div[1]/div/div[2]/ul/li[1]/a/span").click()
    #     sleep(10)
    #
    #     # 按发票状态筛选
    #     #二次定位下拉框 - 未申请
    #     s = driver.find_element_by_id("invoiceYpe")
    #     s.find_element_by_xpath("//option[@value='']").click()
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #     js2 = "document.getElementsByClassName('tableList')[0].scrollLeft=10000"
    #     driver.execute_script(js2)
    #     sleep(2)
    #
    #     #通过xpath(手写)d定位下拉框 - 已申请
    #     driver.find_element_by_xpath(".//*[@id='invoiceYpe']/option[3]").click()
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #     js3 = "document.getElementsByClassName('tableList')[0].scrollLeft=10000"
    #     driver.execute_script(js3)
    #     sleep(2)
    #
    #     # 通过Select模块定位下拉框 - 待领取
    #     s1 = driver.find_element_by_id("invoiceYpe")
    #     Select(s1).select_by_index(3)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #
    #     # 通过Select模块定位下拉框 - 已领取
    #     s1 = driver.find_element_by_id("invoiceYpe")
    #     Select(s1).select_by_value("3")
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #     js4 = "document.getElementsByClassName('tableList')[0].scrollLeft=10000"
    #     driver.execute_script(js4)
    #     sleep(2)
    #
    #     # 通过Select模块定位下拉框 - 作废
    #     s1 = driver.find_element_by_id("invoiceYpe")
    #     Select(s1).select_by_value("4")
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #     js5 = "document.getElementsByClassName('tableList')[0].scrollLeft=10000"
    #     driver.execute_script(js5)
    #     sleep(2)
    #
    #     # 通过Select模块定位下拉框 - 全部
    #     s1 = driver.find_element_by_id("invoiceYpe")
    #     Select(s1).select_by_value("10")
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #     js6 = "document.getElementsByClassName('tableList')[0].scrollLeft=10000"
    #     driver.execute_script(js6)
    #     sleep(2)
    #
    #     #按时间筛选
    #     start_time = ".//*[@id='mainContent']/div[1]/form/div/table/tbody/tr[2]/td/input[1]"
    #     driver.find_element_by_xpath(start_time).send_keys("2016-01-01")
    #     sleep(1)
    #     end_time = ".//*[@id='mainContent']/div[1]/form/div/table/tbody/tr[2]/td/input[2]"
    #     driver.find_element_by_xpath(end_time).send_keys("2016-10-01")
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(1)
    #     start_time = ".//*[@id='mainContent']/div[1]/form/div/table/tbody/tr[2]/td/input[1]"
    #     driver.find_element_by_xpath(start_time).click()
    #     driver.find_element_by_class_name("clearBut").click()
    #     end_time = ".//*[@id='mainContent']/div[1]/form/div/table/tbody/tr[2]/td/input[2]"
    #     driver.find_element_by_xpath(end_time).click()
    #     driver.find_element_by_class_name("clearBut").click()
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(1)
    #
    #     #每页显示 - 20条
    #     js0 = "document.getElementById('mainContent').scrollTop=10000"
    #     driver.execute_script(js0)
    #     sleep(2)
    #     driver.find_element_by_class_name("select").click()
    #     sleep(1)
    #     driver.find_element_by_link_text("20").click()
    #     sleep(2)
    #     js7 = "document.getElementsByClassName('tableList')[0].scrollTop=10000"
    #     driver.execute_script(js7)
    #     sleep(2)
    #     #不同分页
    #     driver.find_element_by_link_text("2").click()
    #     sleep(2)
    #     driver.find_element_by_link_text("3").click()
    #     sleep(2)
    #
    #     #每页显示 - 50条
    #     sleep(2)
    #     driver.find_element_by_class_name("select").click()
    #     sleep(1)
    #     driver.find_element_by_link_text("50").click()
    #     sleep(2)
    #     js8 = "document.getElementById('mainContent').scrollTop=10000"
    #     driver.execute_script(js8)
    #     sleep(2)
    #     #下一页
    #     driver.find_element_by_link_text("1").click()
    #     sleep(2)
    #
    #     #每页显示 - 100条
    #     driver.find_element_by_class_name("select").click()
    #     sleep(1)
    #     driver.find_element_by_link_text("100").click()
    #     sleep(2)
    #     js9 =  "document.getElementsByClassName('tableList')[0].scrollTop=10000"
    #     driver.execute_script(js9)
    #     sleep(2)
    #
    # def test_004_invoice_record(self):
    #     u"""发票记录"""
    #     driver.find_element_by_link_text(u"发票记录").click()
    #     sleep(1)
    #     #按卡号查询
    #     driver.find_element_by_id("cardCode").send_keys("200100005502")
    #     sleep(1)
    #     driver.find_elements_by_css_selector(".button")[1].click()
    #     sleep(1)
    #     # #领取发票
    #     # driver.find_element_by_partial_link_text(u"领取发票").click()
    #     # sleep(1)
    #     # driver.find_element_by_class_name("buttonActive").click()
    #     # sleep(1)
    #     # driver.find_element_by_xpath("//*[@rel='callback']").click()
    #     # sleep(1)
    #     # #作废
    #     # driver.find_element_by_id("cardCode").send_keys("1703774762")
    #     # sleep(1)
    #     # driver.find_elements_by_css_selector(".button")[1].click()
    #     # sleep(1)
    #     # target1 = driver.find_element_by_partial_link_text(u"作废")
    #     # driver.execute_script("arguments[0].scrollIntoView();",target1)
    #     # sleep(1)
    #     # driver.find_element_by_partial_link_text(u"作废").click()
    #     # sleep(1)
    #     # driver.find_element_by_xpath("//*[@class='button' and @rel='callback']").click()
    #     # sleep(10)
    #
    #     #清空卡号
    #     driver.find_element_by_id("cardCode").clear()
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(1)
    #
    #     #按纳税人识别号查询
    #     driver.find_element_by_id("taxpayerIdentificationNumber").send_keys("91110108101437375L")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(1)
    #     #清空纳税人识别号
    #     driver.find_element_by_id("taxpayerIdentificationNumber").clear()
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(1)
    #
    #     #按发票状态查询 - 已申请
    #     s = driver.find_element_by_id("invoiceYpe")
    #     Select(s).select_by_value("1")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(1)
    #
    #
    #     #按发票状态查询 - 待领取
    #     s = driver.find_element_by_id("invoiceYpe")
    #     Select(s).select_by_value("2")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(1)
    #
    #     #按发票状态查询 - 已领取
    #     s = driver.find_element_by_id("invoiceYpe")
    #     Select(s).select_by_value("3")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(1)
    #
    #     #按发票状态查询 - 作废
    #     s = driver.find_element_by_id("invoiceYpe")
    #     Select(s).select_by_value("4")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(1)
    #
    #     #按发票状态查询 - 全部
    #     s = driver.find_element_by_id("invoiceYpe")
    #     Select(s).select_by_value("")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(1)
    #
    #     #按发票代码查询
    #     driver.find_element_by_xpath("//*[@class='textInput' and @name='invoiceCode']").send_keys("11111")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(1)
    #
    #     #清空发票代码
    #     driver.find_element_by_xpath("//*[@class='textInput' and @name='invoiceCode']").clear()
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(1)
    #
    # def test_005_recharge_charge_record(self):
    #     u"""充值变更记录"""
    #     driver.find_element_by_link_text(u"充值变更记录").click()
    #     sleep(1)
    #     #按卡号查询
    #     driver.find_element_by_id("cardCode").send_keys("6202006458")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(1)
    #     #清空卡号
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(1)
    #
    #     #按原流水查询
    #     driver.find_element_by_xpath("//*[@class='textInput' and @name='originalSerialNumber']").send_keys("20160726181247960478214")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(1)
    #     #清空原流水
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(1)
    #
    #     #按时间查询
    #     driver.find_element_by_xpath(".//*[@id='mainContent']/div[1]/form/div/table/tbody/tr/td[3]/input[1]").send_keys("2016-07-06")
    #     sleep(1)
    #     driver.find_element_by_xpath(".//*[@id='mainContent']/div[1]/form/div/table/tbody/tr/td[3]/input[2]").send_keys("2016-07-13")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(1)
    #     #清空时间
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(1)
    #
    #
    # def test_006_records_of_consumption(self):
    #     u"""消费记录"""
    #     driver.find_element_by_link_text(u"消费记录").click()
    #     sleep(3)
    #     #按卡号查询
    #     driver.find_element_by_id("cardCode").send_keys("1703774762")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #     #下一页
    #     for i in range(3):
    #         driver.find_element_by_partial_link_text(u"下一页").click()
    #         sleep(1)
    #     #清空卡号
    #     driver.find_element_by_id("cardCode").clear()
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #
    #     #按会员姓名查询
    #     driver.find_element_by_xpath("//*[@class='textInput' and @name='memberName']").send_keys(u"周莹测试001")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(3)
    #     #清空会员姓名
    #     driver.find_element_by_xpath("//*[@class='textInput' and @name='memberName']").clear()
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #
    #     #按电话查询
    #     driver.find_element_by_xpath("//*[@class='textInput' and @name='phone']").send_keys("15313556575")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(3)
    #     #清空电话
    #     driver.find_element_by_xpath("//*[@class='textInput' and @name='phone']").clear()
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #
    #     #按结算状态查询 - 结算异常
    #     s1 = driver.find_element_by_id("settlementStatus")
    #     Select(s1).select_by_value("0")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #     target1 = driver.find_element_by_xpath(".//*[@id='mainContent']/div[4]/div[2]/table/thead/tr/th[32]")
    #     driver.execute_script("arguments[0].scrollIntoView();",target1)
    #     sleep(2)
    #
    #     #按结算状态查询 - 正常
    #     s1 = driver.find_element_by_id("settlementStatus")
    #     Select(s1).select_by_value("1")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #     target2 = driver.find_element_by_xpath(".//*[@id='mainContent']/div[4]/div[2]/table/thead/tr/th[32]")
    #     driver.execute_script("arguments[0].scrollIntoView();",target2)
    #     sleep(2)
    #
    #     #按结算状态查询 - 忽略
    #     s1 = driver.find_element_by_id("settlementStatus")
    #     Select(s1).select_by_value("2")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #     target3 = driver.find_element_by_xpath(".//*[@id='mainContent']/div[4]/div[2]/table/thead/tr/th[32]")
    #     driver.execute_script("arguments[0].scrollIntoView();",target3)
    #     sleep(2)
    #
    #     #按结算状态查询 - 未完成
    #     s1 = driver.find_element_by_id("settlementStatus")
    #     Select(s1).select_by_value("5")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #     target4 = driver.find_element_by_xpath(".//*[@id='mainContent']/div[4]/div[2]/table/thead/tr/th[32]")
    #     driver.execute_script("arguments[0].scrollIntoView();",target4)
    #     sleep(2)
    #
    #     #按结算状态查询 - 无返回帧
    #     s1 = driver.find_element_by_id("settlementStatus")
    #     Select(s1).select_by_value("6")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #
    #     #按结算状态查询 - 数据异常
    #     s1 = driver.find_element_by_id("settlementStatus")
    #     Select(s1).select_by_value("7")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #     target6 = driver.find_element_by_xpath(".//*[@id='mainContent']/div[4]/div[2]/table/thead/tr/th[32]")
    #     driver.execute_script("arguments[0].scrollIntoView();",target6)
    #     sleep(2)
    #
    #     #按结算状态查询 - 全部
    #     s1 = driver.find_element_by_id("settlementStatus")
    #     Select(s1).select_by_value("")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #     target7 = driver.find_element_by_xpath(".//*[@id='mainContent']/div[4]/div[2]/table/thead/tr/th[32]")
    #     driver.execute_script("arguments[0].scrollIntoView();",target7)
    #     sleep(2)
    #
    #     #按终端机器编码查询
    #     driver.find_element_by_xpath("//*[@class='textInput' and @name='pileNumber']").send_keys("1020150908001064")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #     target8 = driver.find_element_by_xpath(".//*[@id='mainContent']/div[4]/div[2]/table/thead/tr/th[13]")
    #     driver.execute_script("arguments[0].scrollIntoView();",target8)
    #     sleep(2)
    #     #清空终端机器编码
    #     driver.find_element_by_xpath("//*[@class='textInput' and @name='pileNumber']").clear()
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #
    #     #根据机构名称查询
    #     s2 = driver.find_element_by_id("insId")
    #     Select(s2).select_by_value("")
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #
    #     #证件号
    #     driver.find_element_by_xpath("//*[@class='textInput' and @name='identify']").send_keys("17611231273")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #     #清空证件号
    #     driver.find_element_by_xpath("//*[@class='textInput' and @name='identify']").clear()
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #
    #     #按结算方式查询 - 会员卡
    #     s3 = driver.find_element_by_id("jiesuanType")
    #     Select(s3).select_by_value("1")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #
    #     #按结算方式查询 - 微信
    #     s3 = driver.find_element_by_id("jiesuanType")
    #     Select(s3).select_by_value("2")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #
    #     #按结算方式查询 - app
    #     s3 = driver.find_element_by_id("jiesuanType")
    #     Select(s3).select_by_value("3")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #
    #     #按结算方式查询 - 全部
    #     s3 = driver.find_element_by_id("jiesuanType")
    #     Select(s3).select_by_value("")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #
    #     #按结算时间查询   -   fail未时间按时间搜索
    #     #去掉readonly属性
    #     # js = "document.getElementsByClassName('date')[0].removeAttribute('true')"
    #     # driver.execute_script(js)
    #     # driver.find_element_by_xpath(".//*[@id='mainContent']/div[3]/form/div/table/tbody/tr[3]/td[1]/input[1]").send_keys("2018-01-01 00:00:00")
    #     # sleep(1)
    #     # driver.find_element_by_xpath(".//*[@id='mainContent']/div[3]/form/div/table/tbody/tr[3]/td[1]/input[2]").send_keys("2018-06-07 15:18:42")
    #     # sleep(1)
    #     # driver.find_elements_by_class_name("button")[1].click()
    #     # sleep(2)
    #
    #     #按站点名称搜索   -   西站
    #     s1 = driver.find_element_by_id("siteId")
    #     Select(s1).select_by_value("459")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #
    #     #按站点名称搜索   -   saxxxx
    #     s1 = driver.find_element_by_id("siteId")
    #     Select(s1).select_by_value("148")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #
    #     #按站点名称搜索   -   全部
    #     s1 = driver.find_element_by_id("siteId")
    #     Select(s1).select_by_value("")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #
    #     #按签权方式搜索   -  COS刷卡签权
    #     s2 = driver.find_element_by_id("signRightType")
    #     Select(s2).select_by_value("1")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #
    #     #按签权方式搜索   -  微信签权
    #     s2 = driver.find_element_by_id("signRightType")
    #     Select(s2).select_by_value("2")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #
    #     #按签权方式搜索   -  APP签权
    #     s2 = driver.find_element_by_id("signRightType")
    #     Select(s2).select_by_value("4")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #
    #     #按签权方式搜索   -  小程序签权
    #     s2 = driver.find_element_by_id("signRightType")
    #     Select(s2).select_by_value("6")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #
    #     #按签权方式搜索   -  第三方签权
    #     s2 = driver.find_element_by_id("signRightType")
    #     Select(s2).select_by_value("7")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)
    #
    #     #按签权方式搜索   -  全部
    #     s2 = driver.find_element_by_id("signRightType")
    #     Select(s2).select_by_value("")
    #     sleep(1)
    #     driver.find_elements_by_class_name("button")[1].click()
    #     sleep(2)

    def test_007_record_of_consumption_change(self):
        u"""消费变更记录"""
        driver.find_element_by_link_text(u"消费变更记录").click()
        sleep(1)
        #按卡号查询
        driver.find_element_by_id("cardCode").send_keys("200100008302")
        driver.find_elements_by_class_name("button")[1].click()
        sleep(3)
        driver.find_element_by_id("cardCode").clear()
        driver.find_elements_by_class_name("button")[1].click()
        sleep(1)
        #按操作时间查询
        driver.find_element_by_xpath(".//*[@id='mainContent']/div[1]/form/div/table/tbody/tr/td[2]/input[1]").send_keys("2018-06-15")
        driver.find_element_by_xpath(".//*[@id='mainContent']/div[1]/form/div/table/tbody/tr/td[2]/input[2]").send_keys("2018-07-09")
        driver.find_elements_by_class_name("button")[1].click()
        sleep(3)
    # def test_008_card_recording(self):
    #     u"""补卡记录"""
    #     driver.find_element_by_link_text(u"补卡记录").click()
    #     sleep(1)
    #
    # def test_009_backCard_record(self):
    #     u"""退卡记录"""
    #     driver.find_element_by_link_text(u"退卡记录").click()
    #     sleep(1)
    #
    # def test_010_lockingCard_record(self):
    #     u"""解锁卡记录"""
    #     driver.find_element_by_link_text(u"解锁卡记录").click()
    #     sleep(1)
    #
    # def test_011_appConsumption_record(self):
    #     u"""APP消费记录"""
    #     driver.find_element_by_link_text(u"APP消费记录").click()
    #     sleep(1)
    #
    # def test_012_memoryCard_record(self):
    #     u"""不记名卡消费记录"""
    #     driver.find_element_by_link_text(u"不记名卡消费记录").click()
    #     sleep(1)
    #     driver.quit()

if __name__ == '__main__':
    unittest.main()