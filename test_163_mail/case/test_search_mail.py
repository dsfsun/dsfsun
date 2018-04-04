from selenium import webdriver
import time,unittest
from test_163_mail.public.login import login
from selenium.webdriver.common.keys import Keys
from test_163_mail.common.logger import Log

class TestSearchMail(unittest.TestCase):
    log = Log()
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.url = "https://mail.163.com/"
        self.verificationErrors = []

    def test_search_mail(self):
        '''搜索邮件'''
        self.log.info("-------搜索邮件成功用例：start-----------")
        driver = self.driver
        driver.get(self.url)
        login(self, "dsfsun", "19900506asd")
        # 输入搜索关键字
        driver.find_element_by_xpath("//input[@class='nui-ipt-input' and @type='text']").send_keys("邓诗芳")
        # 完成搜索动作
        driver.find_element_by_xpath("//input[@class='nui-ipt-input' and @type='text']").send_keys(Keys.ENTER)
        # 断言验证结果
        text = driver.find_element_by_xpath("//div[@class='tb0']/div/h1").text
        # text = driver.find_element_by_xpath("//div[@id='dvMultiTab']/u1/li[7]/div[3]").text
        self.assertEqual(text, "搜索结果")
        self.log.info("-------搜索邮件成功用例：end!-----------")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
