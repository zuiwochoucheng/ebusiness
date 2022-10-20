from selenium.webdriver.common.by import By
from baseDir.base_page import BasePage


# 页面具体操作类
class VhrPage(BasePage):
    un = (By.XPATH, '//*[@id="app"]/div/form/div[1]/div/div/input')
    pw = (By.XPATH, '//*[@id="app"]/div/form/div[2]/div/div/input')
    cd = (By.XPATH, '//*[@id="app"]/div/form/div[3]/div/div/input')
    bt = (By.XPATH, '//*[@id="app"]/div/form/button')
    msg = ((By.CSS_SELECTOR, 'body:nth-child(2) div.el-message.'
                             'el-message--success:nth-child(5) > p.el-message__content'))

    def text_clear(self):
        self.clears(self.un)
        self.clears(self.pw)
        self.clears(self.cd)

    def login_click(self):
        self.click(self.bt)

    def send_text(self, username, passwod, code):
        self.send_key(self.un, username)
        self.send_key(self.pw, passwod)
        self.send_key(self.cd, code)

    def find_msg(self):
        msg = self.find_elementl(self.msg).text
        return msg
