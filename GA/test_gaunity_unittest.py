# -*- coding: UTF-8 -*-
from uitrace.api import *
from time import sleep
import unittest


class TestClas(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        每个测试类运行之前执行一次,初始化类
        """
        # 初始化设备驱动和环境，必填
        init_driver(workspace=os.path.dirname(__file__))
        start_event_handler()

    @classmethod
    def tearDownClass(cls):
        """
        每个测试类运行之后执行一次
        """
        # 断开driver
        stop_driver()

    def setUp(self):
        """
        每个用例开始前初始化
        """
        # 启动应用，需要填写应用包名
        start_app("com.tencent.wetest.demo")

    def tearDown(self):
        """
        每个用例结束后执行
        """
        stop_app("com.tencent.wetest.demo")


    def test_findElements(self):
        sleep(2)
        click(loc="/Canvas/Panel/Sample", by=DriverType.GA_UNITY, offset=None, timeout=30, duration=0.05, times=5)
        sleep(2)
        click(loc="/Canvas/Panel/FindElements", by=DriverType.GA_UNITY, offset=None, timeout=30, duration=0.05, times=1)
        sleep(2)
        click(loc="/Canvas/Panel/VerticalPanel/Item(Clone)", by=DriverType.GA_UNITY, offset=None, timeout=30, duration=0.05, times=1)
        click(loc="/Canvas/Panel/Button", by=DriverType.GA_UNITY, offset=None, timeout=30, duration=0.05, times=1)
        sleep(2)
        click(loc="/Canvas/Panel/Button", by=DriverType.GA_UNITY, offset=None, timeout=30, duration=0.05, times=1)
        bt = click(loc="/Canvas/Panel/Button", by=DriverType.GA_UNITY, offset=None, timeout=30, duration=0.05, times=1)
        assert bt is not None
        time.sleep(3)

    def test_interaction(self):
        click(loc="/Canvas/Panel/Interaction", by=DriverType.GA_UNITY, offset=None, timeout=30, duration=0.05, times=1)
        sleep(2)
        click(loc="/Canvas/Panel/Click", by=DriverType.GA_UNITY, offset=None, timeout=30, duration=0.05, times=1)
        sleep(2)
        lc = long_click(loc="/Canvas/Panel/Press", by=DriverType.GA_UNITY, offset=None, timeout=30, duration=4)
        assert lc is not None
        time.sleep(2)


if __name__ == "__main__":
    unittest.main()


