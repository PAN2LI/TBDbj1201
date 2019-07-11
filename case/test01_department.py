import unittest
import requests
from parameterized import parameterized
from api.api_department import ApiDep
from tool.read_json import read_json


def get_json_data(filename):
    data_list = list()
    data_list.append(tuple(read_json("{}".format(filename)).values()))
    return data_list


class TestLogin(unittest.TestCase):
    session = None

    def setUp(self):
        # 获取session对象
        self.session = requests.session()
        # 获取对象
        self.part = ApiDep(self.session)

    def tearDown(self):
        # 结束
        self.session.close()

    @parameterized.expand(get_json_data("post_data.json"))
    def test01_post(self, data, code, exp):
        # 调用新增方法
        result = self.part.api_post_dep(data)
        print("响应的状态码：", result.status_code)
        print("响应的数据：", result.json())
        # 断言
        ret = result.json().get("create_success").get("count")
        self.assertEqual(code, result.status_code)
        self.assertEqual(exp, ret)

    @parameterized.expand(get_json_data("put_data.json"))
    def test02_put(self, dep_id, data, code, expect):
        # 调用更新方法
        result = self.part.api_put_dep(dep_id, data)
        print("响应的状态码：", result.status_code)
        print("响应的数据：", result.json())
        # 断言
        self.assertEqual(code, result.status_code)
        self.assertEqual(expect, result.json().get("dep_name"))

    @parameterized.expand(get_json_data("get_one_data.json"))
    def test03_get_one(self, dep_id, code, expect):
        # 调用查询指定方法
        result = self.part.api_get_one_dep(dep_id)
        print("响应的状态码：", result.status_code)
        print("响应的数据：", result.json())
        # 断言
        self.assertEqual(code, result.status_code)
        self.assertEqual(expect, result.json().get("dep_id"))

    def test04_get_all(self):
        # 调用查询所有方法

        result = self.part.api_get_all_dep()
        print("响应的状态码：", result.status_code)
        print("响应的数据：", result.json())
        # 断言
        arr = list()
        for i in result.json().get("results"):
            arr.append(i.get("dep_id"))
        self.assertIn("T01", arr)

    @parameterized.expand(get_json_data("delete_data.json"))
    def test05_delete(self, dep_id, code):
        # 调用删除方法
        result = self.part.api_delete_dep(dep_id)
        print("响应的状态码：", result.status_code)
        # 断言
        self.assertEqual(code, result.status_code)
