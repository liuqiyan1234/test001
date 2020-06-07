import os
import unittest
import HTMLTestRunner_PY3

import app
from script.test_ihrm_employee1 import TestIHRMEmployee1
from script.test_irhm_login_parames import TestIHMLLogin

suite = unittest.TestSuite()
# suite.addTest(unittest.makeSuite(TestIHMLLogin))
suite.addTest(unittest.makeSuite(TestIHRMEmployee1))
filename = app.BASE_DIR + "/report/ihrm_report.html"
with open(filename,"wb") as f:
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f,verbosity=2,title="测试ihrm的登录和员工管理的接口报告",description="这是人力资源管理系统的测试报告")
    runner.run(suite)