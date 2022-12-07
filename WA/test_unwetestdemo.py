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

    @classmethod
    def tearDownClass(cls):
        """
        每个测试类运行之后执行一次
        """
        # 断开driver
        uninstall_app("com.wetest.demo.db")
        stop_driver()
        

    def setUp(self):
        """
        每个用例开始前初始化
        """
        # 启动应用，需要填写应用包名
        start_app("com.wetest.demo.db")

    def tearDown(self):
        """
        每个用例结束后执行
        """
        stop_app("com.wetest.demo.db")


    def test_login(self):
        click(loc="//Application[1]/Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/TextField[1]", by=DriverType.UI, offset=None, timeout=30, duration=0.05, times=1)
        input_text('123', xpath=None, timeout=30, depth=10)
        sleep(2)
        click(loc="//Application[1]/Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/SecureTextField[1]", by=DriverType.UI, offset=None, timeout=30, duration=0.05, times=1)
        input_text('123', xpath=None, timeout=30, depth=10)
        click(loc="//Button[@name='Sign In' and @label='Sign In']", by=DriverType.UI, offset=None, timeout=30, duration=0.05, times=1)
        sleep(3)
        """登录成功，选择item提交"""
        click(loc="//StaticText[@name='Item1' and @label='Item1']", by=DriverType.UI, offset=None, timeout=30, duration=0.05, times=1)
        click(loc="//StaticText[@name='Item4' and @label='Item4']", by=DriverType.UI, offset=None, timeout=30, duration=0.05, times=1)
        p1 = click(loc="obj_1667982015735.jpg", by=DriverType.CV, offset=None, timeout=30, duration=0.05, times=1)
        assert p1 is not None
        sleep(5)


    def test_fail(self):
        click(loc="//Application[1]/Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/TextField[1]", by=DriverType.UI, offset=None, timeout=30, duration=0.05, times=1)
        input_text('123', xpath=None, timeout=30, depth=10)
        sleep(2)
        click(loc="//Application[1]/Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/SecureTextField[1]", by=DriverType.UI, offset=None, timeout=30, duration=0.05, times=1)
        input_text('123', xpath=None, timeout=30, depth=10)
        click(loc="//Button[@name='Sign In' and @label='Sign In']", by=DriverType.UI, offset=None, timeout=30, duration=0.05, times=1)
        sleep(3)
        """不选择item，直接提交"""
        click(loc="obj_1667982015735.jpg", by=DriverType.CV, offset=None, timeout=30, duration=0.05, times=1)
        add_event_handler("(Error|Ok)",'Ok')
        start_event_handler()
        print("pass")
        sleep(10)


if __name__ == "__main__":
    unittest.main()


