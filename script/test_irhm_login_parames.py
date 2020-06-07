import unittest

import requests

import app
from api.login_api import TestLoginApi
from utils import assert_common, get_login_data
import logging
from parameterized import parameterized
# 定义登录类
class TestIHMLLogin(unittest.TestCase):

    def setUp(self):
        # 初始化api
        self.login_api = TestLoginApi()

    # 定义方法
    @parameterized.expand(get_login_data(app.BASE_DIR + "/data/login_data.json"))
    def test_01_login_success(self,jsonData,httpcode,success,code,message):
        login_response = self.login_api.login(jsonData, app.headers)
        logging.info("登录的结果：{}".format(login_response.json()))
        # 断言响应体
        assert_common(httpcode,success,code, message, login_response, self)
    #
    # # 断言账号不存在登陆不成功
    # def test_02_login_fail(self):
    #     headers = {"Content_Type": "application/json"}
    #     jsonData = {"mobile": "13000000005", "password": "123456"}
    #     login_response = self.login_api.login(jsonData, headers)
    #     logging.info("登录的结果：{}".format(login_response.json()))
    #     # 断言响应体
    #     assert_common(200, False, 20001, "用户名或密码错误", login_response, self)
    #
    #     # 断言账号不存在登陆不成功
    #
    # def test_03_password_error(self):
    #     headers = {"Content_Type": "application/json"}
    #     jsonData = {"mobile": "13800000002", "password": "1223456"}
    #     login_response = self.login_api.login(jsonData, headers)
    #     logging.info("登录的结果：{}".format(login_response.json()))
    #     # 断言响应体
    #     assert_common(200, False, 20001, "用户名或密码错误", login_response, self)
    #
    # # 手机号为空
    # def test_04_mobile_is_null(self):
    #     headers = {"Content_Type": "application/json"}
    #     jsonData = {"mobile": "", "password": "123456"}
    #     login_response = self.login_api.login(jsonData, headers)
    #     logging.info("登录的结果：{}".format(login_response.json()))
    #     # 断言响应体
    #     assert_common(200, False, 20001, "用户名或密码错误", login_response, self)
    #
    # # 密码为空
    # def test_05_password_is_null(self):
    #     headers = {"Content_Type": "application/json"}
    #     jsonData = {"mobile": "13800000002", "password": ""}
    #     login_response = self.login_api.login(jsonData, headers)
    #     logging.info("登录的结果：{}".format(login_response.json()))
    #     # 断言响应体
    #     assert_common(200, False, 20001, "用户名或密码错误", login_response, self)
    #
    # # 手机号为特殊字符
    # def test_06_mobile_is_error(self):
    #     headers = {"Content_Type": "application/json"}
    #     jsonData = {"mobile": "@#$%^&&&^%$#", "password": ""}
    #     login_response = self.login_api.login(jsonData, headers)
    #     logging.info("登录的结果：{}".format(login_response.json()))
    #     # 断言响应体
    #     assert_common(200, False, 20001, "用户名或密码错误", login_response, self)
    #
    # # 多参
    # def test_07_more_paremes(self):
    #     headers = {"Content_Type": "application/json"}
    #     jsonData = {"mobile": "13800000002", "password": "123456", "verify_code": "8888"}
    #     login_response = self.login_api.login(jsonData, headers)
    #     logging.info("登录的结果：{}".format(login_response.json()))
    #     # 断言响应体
    #     assert_common(200, True, 10000, "操作成功", login_response, self)
    #
    # # 缺少参数password
    # def test_08_litter_paremes(self):
    #     headers = {"Content_Type": "application/json"}
    #     jsonData = {"mobile": "13800000002"}
    #     login_response = self.login_api.login(jsonData, headers)
    #     logging.info("登录的结果：{}".format(login_response.json()))
    #     # 断言响应体
    #     assert_common(200, False, 20001, "用户名或密码错误", login_response, self)
    #
    # #  缺少参数mobile
    # def test_09_litter2_paremes(self):
    #     headers = {"Content_Type": "application/json"}
    #     jsonData = {"password": "123456"}
    #     login_response = self.login_api.login(jsonData, headers)
    #     logging.info("登录的结果：{}".format(login_response.json()))
    #     # 断言响应体
    #     assert_common(200, False, 20001, "用户名或密码错误", login_response, self)
    #
    # # 无参
    # def test_10_no_paremes(self):
    #     headers = {"Content_Type": "application/json"}
    #     jsonData = {}
    #     login_response = self.login_api.login(jsonData, headers)
    #     logging.info("登录的结果：{}".format(login_response.json()))
    #     # 断言响应体
    #     assert_common(200, False, 20001, "用户名或密码错误", login_response, self)
    #
    # # 错误参数
    # def test_11_error_paremes(self):
    #     headers = {"Content_Type": "application/json"}
    #     jsonData = {"mobile": "13800000002", "pass": "123456"}
    #     login_response = self.login_api.login(jsonData, headers)
    #     logging.info("登录的结果：{}".format(login_response.json()))
    #     # 断言响应体
    #     assert_common(200, False, 20001, "用户名或密码错误", login_response, self)
    #
    # # 参数为null
    # def test_12_is_null(self):
    #     headers = {"Content_Type": "application/json"}
    #     jsonData = "null"
    #     login_response = self.login_api.login(jsonData, headers)
    #     logging.info("登录的结果：{}".format(login_response.json()))
    #     # 断言响应体
    #     assert_common(200, False, 99999, "抱歉，系统繁忙，请稍后重试！", login_response, self)
    #
