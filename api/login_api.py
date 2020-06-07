import requests
# 创建登录类
class TestLoginApi:
    def __init__(self):
        self.login_url = "http://ihrm-test.itheima.net/api/sys/login"
    # 封装登录的方法
    def login(self, jsonData, headers):
        login_response = requests.post(url=self.login_url,json=jsonData, headers=headers )
        return login_response
    # 定义成功登录的方法


if __name__ == "__main__":
    test_login = TestLoginApi()
    response = test_login.login({"mobile":"13800000002","password":"123456"},{"Content_Type":"application/json"})
    print("登录的结果：",response.json())