import unittest
import requests
from api.login_api import TestLoginApi
from api.employee_api import TestEmployeeApi
from utils import assert_common
import logging
class TestITMLEmployee(unittest.TestCase):

    def setUp(self):
        self.login_api = TestLoginApi()
        self.manage_emp_api = TestEmployeeApi()
        self.session = requests.session()
    def tearDown(self):
        self.session.close()

    # 定义员工管理模块的方法
    def test_01_employee_manage(self):
        # 调用登录的接口
        jsonData = {"mobile": "13800000002", "password": "123456"}
        headers = {"Content_Type": "application/json"}
        login_response = self.session.post(url="http://ihrm-test.itheima.net/api/sys/login", headers=headers,json=jsonData)
        # 打印登录的结果
        logging.info("登录的结果为：{}".format(login_response.json()))
        # 断言
        assert_common(200,True,10000,"操作成功！",login_response,self)
        # 调用添加员工的接口
        add_emp_response = self.manage_emp_api.add_emp(self.session,headers,"大宝贝呱呱呵呵999","15911112222")
        logging.info("新增员工：{}".format(add_emp_response.json()))
        # 断言
        assert_common(200, True, 10000, "操作成功！", login_response, self)
        # 获取响应体中的添加的员工的id
        emp_id = add_emp_response.json().get("data").get("id")
        # 调用查找员工的接口
        find_emp_response = self.manage_emp_api.find_emp(self.session,emp_id,headers)
        logging.info("查询结果：{}".format(find_emp_response.json()))
        # 断言
        assert_common(200, True, 10000, "操作成功！", login_response, self)
        # 调用修改员工的接口
        modify_response = self.manage_emp_api.fix_emp(self.session,emp_id,headers,"减肥的快乐就分开来访")
        logging.info("修改的结果：{}".format(modify_response.json()))
        # 断言
        assert_common(200, True, 10000, "操作成功！", login_response, self)
        # 调用删除员工的接口
        delect_response = self.manage_emp_api.delect_emp(self.session,emp_id,headers=headers)
        logging.info("删除结果：{}".format(delect_response.json()))
        # 断言
        assert_common(200, True, 10000, "操作成功！", login_response, self)
