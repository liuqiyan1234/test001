import requests
class TestEmployeeApi:
    def __init__(self):
        self.add_employee_url = "http://ihrm-test.itheima.net/api/sys/user"


    def add_emp(self,session,headers,username,mobile):
        add_employee_response = session.post(url=self.add_employee_url, headers=headers, json={"username": username,
                                                                                                "mobile": mobile,
                                                                                                "workNumbe": "00123657",
                                                                                                "timeOfEntry": "2018-03-09",
                                                                                                "departmentid": "2463829",
                                                                                                "departmentName": "人事部2部门",
                                                                                                "correctionTime": "2020-01-03"
                                                                                                })

        return add_employee_response


    # 定义查找员工的方法
    def find_emp(self,session,emp_id,headers):
        return session.get(url=self.add_employee_url+"/"+ str(emp_id),headers=headers)


    # 定义修改员工的方法
    def fix_emp(self,session,emp_id,headers,username):
        return session.put(url=self.add_employee_url+"/"+ str(emp_id),headers=headers,json={"username":username})

        # 定义删除员工的方法
    def delect_emp(self, session,emp_id, headers):
        return session.delete(url=self.add_employee_url + "/" + str(emp_id), headers=headers)