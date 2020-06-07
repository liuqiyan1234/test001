# 创建测试类
import logging
import unittest

import requests
from parameterized import parameterized
from api.employee_api import TestEmployeeApi
from api.login_api import TestLoginApi
from utils import assert_common, get_login_data, get_emp_data
import app

class TestIHRMEmployee1(unittest.TestCase):

    def setUp(self):
        self.login_api = TestLoginApi()
        self.manage_emp_api = TestEmployeeApi()
        self.session = requests.session()


    def tearDown(self):
        self.session.close()

    # 编写测试函数
    def test01_login(self):
        # 调用登录的接口
        jsonData = {"mobile": "13800000002", "password": "123456"}
        app.headers = {"Content_Type": "application/json"}
        login_response = self.session.post(url="http://ihrm-test.itheima.net/api/sys/login", headers=app.headers,
                                           json=jsonData)
        token ="Bearer " + str(login_response.json().get("data"))
        app.headers.update({"Authorization":token})
        # 打印登录的结果
        logging.info("登录的结果为：{}".format(login_response.json()))
        # 断言
        assert_common(200, True, 10000, "操作成功！", login_response, self)

    # 添加员工
    filename = app.BASE_DIR+"/data/emp_data.json"
    @parameterized.expand(get_emp_data(filename,'add_emp'))
    def test02_add_emp(self,username,mobile,httpcode,success,code,message):
        # 调用添加员工的接口
        add_emp_response = self.manage_emp_api.add_emp(self.session, app.headers,username,mobile)
        logging.info("新增员工：{}".format(add_emp_response.json()))
        # 断言
        assert_common(httpcode, success, code, message, add_emp_response, self)
        # 获取响应体中的添加的员工的id
        app.emp_id = add_emp_response.json().get("data").get("id")
    # 查询员工
    @parameterized.expand(get_emp_data(filename,'query_emp'))
    def test03_query_emp(self,httpcode,success,code,message):
        print(app.emp_id)
        # 调用查找员工的接口
        find_emp_response = self.manage_emp_api.find_emp(self.session, app.emp_id, app.headers)
        logging.info("查询结果：{}".format(find_emp_response.json()))
        # 断言
        assert_common(httpcode, success, code, message, find_emp_response, self)

    # 修改员工
    @parameterized.expand(get_emp_data(filename, 'modify_emp'))
    def test04_modify_emp(self,username,httpcode,success,code,message):
        # 调用修改员工的接口
        modify_response = self.manage_emp_api.fix_emp(self.session, app.emp_id, app.headers, username)
        logging.info("修改的结果：{}".format(modify_response.json()))
        # 断言
        assert_common(httpcode, success, code, message, modify_response, self)
    # 删除员工
    @parameterized.expand(get_emp_data(filename, 'delete_emp'))
    def test05_delete_emp(self,httpcode,success,code,message):
        # 调用删除员工的接口
        delect_response = self.manage_emp_api.delect_emp(self.session, app.emp_id, app.headers)
        logging.info("删除结果：{}".format(delect_response.json()))
        # 断言
        assert_common(httpcode, success, code, message, delect_response, self)
