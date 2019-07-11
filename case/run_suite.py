# 导包
import unittest
from tool.HTMLTestRunner import HTMLTestRunner

# 定义测试套件
discover = unittest.defaultTestLoader.discover("./", pattern="test*.py")

# 获取报告文件流，实例化调用run方法
with open("../report/api_report.html", "wb") as f:
    runner = HTMLTestRunner(stream=f, verbosity=2,
                            title="接口测试报告",
                            description="Windows/Chrome")
    runner.run(discover)
