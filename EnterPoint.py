from unittest import TestLoader, TestSuite
import HtmlTestRunner
from TestCase1 import MyTestCase1

def myReportStart():

        runner = HtmlTestRunner.HTMLTestRunner(output='My_dir', report_title='MyTests')
        runner.run(TestSuite((TestLoader().loadTestsFromTestCase(MyTestCase1))))

myReportStart()