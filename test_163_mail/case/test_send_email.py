from selenium import webdriver
import time,unittest
from test_163_mail.public.login import login,logout
from test_163_mail.common.logger import Log

class TestSendMail(unittest.TestCase):
    log = Log()
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.url = "https://mail.163.com/"
        self.verificationErrors = []

    def test_send_mail1(self):
        '''只填写收件人发送邮件'''
        self.log.info("-------发送邮件成功用例：start!-----------")
        driver = self.driver
        driver.get(self.url)
        # 登录
        login(self,"dsfsun","19900506asd")
        # 写信
        driver.find_element_by_css_selector("#_mail_component_70_70").click()
        # 填写收件人
        driver.find_element_by_xpath(".//*[@class='bz0']/div[2]/div/input").send_keys("1178218917@qq.com")
        # 发送
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/header/div/div/div/span[2]").click()
        # 确认
        driver.find_element_by_xpath("//*[@class='nui-msgbox-ft-btns']/div/span").click()
        # 断言验证发送成功的提示
        text = driver.find_element_by_class_name("tK1").text
        self.assertIn(text,"发送成功")
        self.log.info("-------发送邮件成功用例：end！-----------")

    def test_send_mail2(self):
        '''填写收件人和主题发送邮件'''
        self.log.info("-------发送邮件成功用例：start!-----------")
        driver = self.driver
        driver.get(self.url)
        # 登录
        login(self, "dsfsun", "19900506asd")
        # 写信
        driver.find_element_by_css_selector("#_mail_component_70_70").click()
        # 填写收件人
        driver.find_element_by_xpath(".//*[@class='bz0']/div[2]/div/input").send_keys("1178218917@qq.com")
        # 填写主题
        driver.find_element_by_xpath("//input[@class='nui-ipt-input' and @type='text' and @maxlength='256']").send_keys("给邓诗芳的信")
        # 发送
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/header/div/div/div/span[2]").click()
        # 断言验证发送成功的提示
        text = driver.find_element_by_class_name("tK1").text
        self.assertIn(text, "发送成功")
        self.log.info("-------发送邮件成功用例：end！-----------")

    def test_send_mail3(self):
        '''填写收件人和主题发送邮件'''
        self.log.info("-------发送邮件成功用例：start!-----------")
        driver = self.driver
        driver.get(self.url)
        # 登录
        login(self, "dsfsun", "19900506asd")
        # 写信
        driver.find_element_by_css_selector("#_mail_component_70_70").click()
        # 填写收件人
        driver.find_element_by_xpath(".//*[@class='bz0']/div[2]/div/input").send_keys("1178218917@qq.com")
        # 填写主题
        driver.find_element_by_xpath("//input[@class='nui-ipt-input' and @type='text' and @maxlength='256']").send_keys("给邓诗芳的信")
        # 添加附件
        driver.find_element_by_class_name("O0").send_keys("D:\\testSelenium\\test.txt")
        # 发送
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/header/div/div/div/span[2]").click()
        # 断言验证发送成功的提示
        text = driver.find_element_by_class_name("tK1").text
        self.assertIn("发送成功",text)
        self.log.info("-------发送邮件成功用例：end！-----------")

    def test_send_mail4(self):
        '''只填写收件人、主题、正文发送邮件'''
        self.log.info("-------发送邮件成功用例：start!-----------")
        driver = self.driver
        driver.get(self.url)
        # 登录
        login(self, "dsfsun", "19900506asd")
        # 写信
        driver.find_element_by_css_selector("#_mail_component_70_70").click()
        # 填写收件人
        driver.find_element_by_xpath(".//*[@class='bz0']/div[2]/div/input").send_keys("1178218917@qq.com")
        # 填写主题
        driver.find_element_by_xpath("//input[@class='nui-ipt-input' and @type='text' and @maxlength='256']").send_keys(
            "给邓诗芳的信")
        # 填写正文
        class_name = driver.find_element_by_class_name("APP-editor-iframe")
        driver.switch_to.frame(class_name)
        driver.find_element_by_tag_name("body").send_keys("好久不见")
        # 发送
        driver.switch_to.default_content()
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/header/div/div/div/span[2]").click()
        # 断言验证发送成功的提示
        text = driver.find_element_by_class_name("tK1").text
        self.assertIn("发送成功",text)
        self.log.info("-------发送邮件成功用例：end！-----------")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
