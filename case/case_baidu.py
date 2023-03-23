from selenium.webdriver.common.by import By
import unittest
import time
class BaiDu(unittest.TestCase):

    @classmethod
    def search(cls, d):
         d.driver.implicitly_wait(3)
         d.driver.find_element(by=By.ID, value='kw').send_keys('123') #输入框输入123
         d.driver.find_element(by=By.ID, value='su').click() #点击查询
         d.driver.implicitly_wait(5)
         cls.assertTrue(cls, expr=d.driver.find_element(by=By.ID, value='content_left').is_displayed()) #断言是否存在某个元素
        #  d.driver.implicitly_wait(3)
         time.sleep(5)
         d.screenshot('baidu')