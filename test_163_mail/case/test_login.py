#coding:utf-8
from selenium import webdriver
import time,unittest
from test_163_mail.public.login import login
from test_163_mail.common.logger import Log

class TestLogin(unittest.TestCase):
    log = Log()
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.url = "https://mail.163.com/"
        self.verificationErrors = []
        self.user_pwd_msg = [["", "", "请输入帐号"], ["dsfsun@163.com", "", "请输入密码"], ["", "19900506asd", "请输入帐号"],
                        ["dsf", "555", "帐号或密码错误"]]

    def test_null(self):
        '''用户名和密码为空'''
        self.log.info("------登录失败用例：start!---------")
        driver = self.driver
        user_pwd_msg = self.user_pwd_msg
        driver.get(self.url)
        username = user_pwd_msg[0][0]
        self.log.info("不输入用户名:%s"%username)
        password = user_pwd_msg[0][1]
        self.log.info("不输入密码:%s"%password)
        msg = user_pwd_msg[0][2]
        login(self,username,password)
        driver.switch_to.frame("x-URS-iframe")
        text = driver.find_element_by_xpath(".//*[@id='nerror']").text
        self.log.info("获取测试结果:%s"%text)
        self.assertEqual(text,msg)
        self.log.info("-------登录失败用例：end!-----------")

    def test_pwd_null(self):
        '''只输入用户名，密码为空'''
        self.log.info("------登录失败用例：start!---------")
        driver = self.driver
        user_pwd_msg = self.user_pwd_msg
        driver.get(self.url)
        username = user_pwd_msg[1][0]
        self.log.info("输入正确的用户名:%s"%username)
        password = user_pwd_msg[1][1]
        self.log.info("不输入密码:%s"%password)
        msg = user_pwd_msg[1][2]
        login(self,username,password)
        driver.switch_to.frame("x-URS-iframe")
        text = driver.find_element_by_xpath(".//*[@id='nerror']").text
        self.log.info("获取测试结果:%s"%text)
        self.assertEqual(text,msg)
        self.log.info("-------登录失败用例：end!-----------")

    def test_user_null(self):
        '''用户名为空，只输入密码'''
        self.log.info("------登录失败用例：start!---------")
        driver = self.driver
        user_pwd_msg = self.user_pwd_msg
        driver.get(self.url)
        username = user_pwd_msg[2][0]
        self.log.info("不输入用户名:%s" % username)
        password = user_pwd_msg[2][1]
        self.log.info("输入正确的密码:%s" % password)
        msg = user_pwd_msg[2][2]
        login(self,username,password)
        driver.switch_to.frame("x-URS-iframe")
        text = driver.find_element_by_xpath(".//*[@id='nerror']").text
        self.log.info("获取测试结果:%s" % text)
        self.assertEqual(text,msg)
        self.log.info("-------登录失败用例：end!-----------")

    # def test_error(self):
    #     '''输入错误的用户名和密码'''
    #     driver = self.driver
    #     user_pwd_msg = self.user_pwd_msg
    #     driver.get(self.url)
    #     username = user_pwd_msg[3][0]
    #     password = user_pwd_msg[3][1]
    #     msg = user_pwd_msg[3][2]
    #     login(self,username,password)
    #     driver.switch_to.frame("x-URS-iframe")
    #     text = driver.find_element_by_xpath(".//*[@id='nerror']").text
    #     self.assertEqual(text,msg)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
