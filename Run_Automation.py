# encoding = utf-8
from Util import HTMLTestRunner
import unittest
import time
import os

class StartTest(object):

    def __init__(self):
        print("generate test reports...")

    @staticmethod
    def start_test():
        # 获取当前文件所在目录的父目录的绝对路劲
        parent_directory_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print(parent_directory_path)

        test_suite = unittest.defaultTestLoader.discover('src/case', pattern='*_test.py')
        current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

        # 定义报告文件名
        filename = parent_directory_path + "\\api-testing\\TestResult\\Results-" + current_time + "result.html"
        print(filename)

        # 打开报告文件
        fp = open(filename, 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Result', description='Test_Report')

        # 执行测试
        runner.run(test_suite)
        print('Test reports generate finished')


if __name__ == '__main__':
    StartTest.start_test()