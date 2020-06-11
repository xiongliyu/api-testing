import unittest
from src.case.demo_test import DemoTest
from src.case.kill_test import SampleTest

def demo_suite():
    demo_suite = unittest.TestSuite()
    demo_suite.addTest(DemoTest('test_index'))
    demo_suite.addTest(DemoTest('test_login'))
    demo_suite.addTest(SampleTest('test_selectEq'))
    demo_suite.addTest(SampleTest('test_kill'))
    return demo_suite






if __name__ == '__main__':
    with open('./report.html', 'wb') as fp:
        # runner = unittest.TextTestRunner()
        str_ = '\n用例执行'
        print(type(str_))
        runner = HtmlTestRunner.HTMLTestRunner(stream=fp,verbosity=2,)
        runner.run(demo_suite())

