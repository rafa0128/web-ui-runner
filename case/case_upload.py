from selenium.webdriver.common.by import By
import unittest
import time

class Upload(unittest.TestCase):

    @classmethod
    def upload(cls, d):
        d.driver.implicitly_wait(3)
        d.driver.find_element(by=By.ID, value='filedatacode').send_keys(r'D:\code\hyacinth\static\image\404.png')
        d.driver.implicitly_wait(3)
        d.driver.find_element(by=By.ID, value='click-create').click() #生成二维码
        d.driver.implicitly_wait(3)
        d.screenshot('upload')