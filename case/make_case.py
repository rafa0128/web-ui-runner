# coding: utf-8
# author: Rafa Chen
# modified by : Rafa Chen
# modification time: 2023-3-21

from public.Decorator import *
from public.Common import Driver
from case import case_baidu,case_upload
from selenium.webdriver.common.by import By
import time
import unittest

d = Driver()

class BaiDu(unittest.TestCase):
    
    @classmethod
    @setupclass(d)
    def setUpClass(cls):
        d.driver.get("http://www.baidu.com")
        d.driver.maximize_window()

    @classmethod
    @teardownclass(d)
    def tearDownClass(cls):
        d.driver.refresh()
        # d.driver.quit()

    @testcase(d)
    def test_01_search(self):
        case_baidu.BaiDu.search(d)
 
class Upload(unittest.TestCase):
        
    @classmethod
    @setupclass(d)
    def setUpClass(cls):
        d.driver.get("https://cli.im/files")
        d.driver.maximize_window()

    @classmethod
    @teardownclass(d)
    def tearDownClass(cls):
        d.driver.quit()

    @testcase(d)
    def test_01_upload(self):
        case_upload.Upload.upload(d)