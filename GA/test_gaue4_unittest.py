# -*- coding: UTF-8 -*-
from uitrace.api import *
from time import sleep
import unittest


class TestClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        每个测试类运行之前执行一次,初始化类
        """
        # 初始化设备驱动和环境，必填
        init_driver(workspace=os.path.dirname(__file__))
        add_event_handler("(Error|Ok)",'Ok')
        start_event_handler()

    @classmethod
    def tearDownClass(cls):
        """
        每个测试类运行之后执行一次
        """
        # 断开driver
        stop_driver()
        print("test class setup..")

    def setUp(self):
        """
        每个用例开始前初始化
        """
        # 启动应用，需要填写应用包名
        start_app("com.tencent.WebDriverAgentRunner")

    def tearDown(self):
        """
        每个用例结束后执行
        """
        stop_app("com.tencent.WebDriverAgentRunner")


    def test_bt1(self):
        sleep(10)
        bt1 =click(loc="TextBlock_0", by=DriverType.GA_UE, offset=None, timeout=30, duration=0.05, times=1)
        print("点击左边按钮")
        assert bt1 ==True
        sleep(5)

    def test_bt2(self):
        sleep(10)
        bt2 = click(loc="TextBlock_1", by=DriverType.GA_UE, offset=None, timeout=40, duration=0.05, times=1)
        print("点击右边按钮")
        assert bt2 ==True
        sleep(5)

if __name__ == "__main__":
    unittest.main()


