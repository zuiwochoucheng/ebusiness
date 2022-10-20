import time

from selenium import webdriver

# 测试基类
class TestBase():
    driver = None

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        print("创建驱动")

    def teardown_class(self):
        print("关闭驱动")
        time.sleep(5)
        self.driver.quit()

