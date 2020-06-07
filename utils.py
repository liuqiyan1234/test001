

# 定义断言的方法
import json


def assert_common(httpcode,success,code,message,response,self):
    self.assertIn(message, response.json().get("message"))
    self.assertEqual(code, response.json().get("code"))
    self.assertEqual(success,response.json().get("success"))
    self.assertEqual(httpcode, response.status_code)


# 定义获取json数据的方法
def get_login_data(jsonData_path):
    test_login_data = []
    with open(jsonData_path,mode="r",encoding="utf-8")as f:
        test_data = json.load(f)
        for data in test_data:
            test_login_data.append(tuple(data.values()))
        print(test_login_data)
        return test_login_data


# 定义获取员工模块数据的方法
def get_emp_data(path,key_name):
    emp_data = []
    with open(path,"r",encoding="utf-8")as f:
        test_data = json.load(f)
        data = test_data.get(key_name)
        emp_data.append(list(data.values()))
        print(emp_data)
    return emp_data



if __name__ == "__main__":
    import app
    filename = app.BASE_DIR + "/data/login_data.json"
    get_login_data(filename)
    filename1 = app.BASE_DIR + "/data/emp_data.json"
    get_emp_data(filename1,"add_emp")