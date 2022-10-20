import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 页面基类
class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_elementl(self, loc):
        try:
            # return WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*loc))
            el = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(loc))
            return el
        except:
            return None

    def find_elementls(self, el, loc):
        try:
            return WebDriverWait(self.driver, 5).until(lambda x: el.find_elements(*loc))
            # el = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(loc))
            # return el
        except:
            return None

    def click(self, loc):
        self.find_elementl(loc).click()

    def send_key(self, loc, strs):
        self.find_elementl(loc).send_keys(strs)

    def clears(self, loc):
        self.find_elementl(loc).clear()

    def tsleep(self, se):
        time.sleep(se)

