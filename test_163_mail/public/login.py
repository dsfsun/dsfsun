#coding:utf-8
from selenium import webdriver

# 登录
def login(self,username,password):
    driver = self.driver
    # 切换frame
    driver.switch_to.frame("x-URS-iframe")
    driver.find_element_by_name("email").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_id("dologin").click()
    driver.switch_to.default_content()

# 退出
def logout(self):
    driver = self.driver
    driver.find_element_by_link_text("退出").click()