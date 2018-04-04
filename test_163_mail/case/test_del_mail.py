#coding:utf-8
from selenium import webdriver
import time,unittest
from test_163_mail.public.login import login
from test_163_mail.common.logger import Log

class TestDeleteMail(unittest.TestCase):
    log = Log()
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.url = "https://mail.163.com/"
        self.verificationErrors = []

    # 删除邮件
    def test_del_mail(self):
        '''删除邮件'''
        self.log.info("-------删除邮件成功用例：start！-----------")
        driver = self.driver
        driver.get(self.url)
        login(self,"dsfsun","19900506asd")
        # 查看收件箱
        driver.find_element_by_id("_mail_component_78_78").click()
        time.sleep(3)
        driver.find_elements_by_xpath("//span[@class='nui-chk-symbol']/b").pop(1).click()

        try:
            spans = driver.find_elements_by_class_name("nui-btn-text")
            for s in spans:
                if s.text == "删 除":
                    s.click()
        except:
            pass


        # 断言判断是否已被删除
        # text = driver.find_element_by_css_selector("span.nui-tips-text>a").text
        # self.assertEqual(text,"已删除")
        self.log.info("-------删除邮件成功用例：end！-----------")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

if __name__ == "__main__":
    unittest.main()



