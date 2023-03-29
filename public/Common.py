import os
import re
import time
import unittest
from logzero import logger
from selenium import webdriver
from public.HTMLTestReport import HTMLTestRunner    

report_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

class Driver():

    def __init__(self, browser='chrome'):
        match(browser):
            case 'chrome':
                # 无界面模式
                # chrome_options = webdriver.ChromeOptions()
                # chrome_options.add_argument('--headless')
                # chrome_options.add_argument('--disable-gpu')
                # self.driver = webdriver.Chrome(chrome_options=chrome_options)
                self.driver = webdriver.Chrome()
            case 'firefox':
                self.driver = webdriver.Firefox()
            case 'edge':
                self.driver = webdriver.Edge()        
            case _:
                 raise('{} is undefined'.format(browser))   
        
        self.reportRoot = Method.make_path(os.path.join(os.getcwd(), 'report'))
        self.reportPath = Method.make_path(os.path.join(self.reportRoot, report_time))

    def screenshot(self, name):
        date_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screenshot = '{}-{}.PNG'.format(name, date_time)
        path = os.path.join(self.reportPath, screenshot)
        self.driver.save_screenshot(path)
        print('IMAGE:{}'.format(screenshot))
        return screenshot

class Method:

    @classmethod
    def make_path(cls, path):
         if not os.path.exists(path):
             os.mkdir(path)
         return path
    
class CaseStrategy:
    def __init__(self,case_path,case_pattern):
        self.case_path = case_path
        self.case_pattern = case_pattern

    def _collect_cases(self, cases, top_dir=None):
        suites = unittest.defaultTestLoader.discover(self.case_path,
                                                     pattern=self.case_pattern, top_level_dir=top_dir)
        for suite in suites:
            for case in suite:
                cases.addTest(case)

    def collect_cases(self):
        """collect cases

        collect cases from the giving path by case_path via the giving pattern by case_pattern

        return: all cases that collected by the giving path and pattern, it is a unittest.TestSuite()

        """
        cases = unittest.TestSuite()
        self._collect_cases(cases, top_dir=None)
        return cases
    
class RunCases:

    def __init__(self):
        self.reportRoot = Method.make_path(os.path.join(os.getcwd(), 'report'))
        self.reportPath = Method.make_path(os.path.join(self.reportRoot, report_time))
        self.file_name = os.path.join(self.reportPath, 'report.html')

    def run(self, cases):
        with open(self.file_name, 'wb') as file:
            runner = HTMLTestRunner(stream=file, title='WEB-UI自动化测试报告', description='用例执行情况：')
            runner.run(cases)
            file.close()
        result = self.get_report_info()
        logger.info(result)
        return result    

    def get_report_info(self):
        report = self.file_name
        result = {}
        with open(report, 'r', encoding='utf-8') as f:
            res_str = re.findall("测试结果(.+%)", f.read())
            if res_str:
                res = re.findall(r"\d+", res_str[0])
                result["sum"] = res[0]
                result["pass"] = res[1]
                result['fail'] = res[2]
                result['error'] = res[3]
                result['passrate'] = re.findall('通过率 = (.+%)', res_str[0])[0]
            else:
                raise Exception("解析报告异常")
            f.close()
        with open(report, 'r', encoding='utf-8') as f:
            result['duration'] = re.findall("合计耗时 : </strong> (.+)</p>", f.read())[0].split('.')[0]
            f.close()
        return result        