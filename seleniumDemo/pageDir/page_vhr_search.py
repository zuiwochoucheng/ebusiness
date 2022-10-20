from selenium.webdriver.common.by import By
from baseDir.base_page import BasePage

class SearchPage(BasePage):
    sn = (By.XPATH, '//*[@id="app"]/div/section/section/main/div[2]/div[1]/div[1]/div[1]/div/input')
    bt = (By.XPATH, '//*[@id="app"]/div/section/section/main/div[2]/div[1]/div[1]/div[1]/button[1]')
    tb = (By.XPATH, '//*[@id="app"]/div/section/section/main/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody')
    nms = (By.TAG_NAME, 'tr')

    def sendname(self, nm):
        self.clears(self.sn)
        self.send_key(self.sn, nm)

    def search(self, nm):
        self.click(nm)
        self.tsleep(2)

    def get_names(self):
        bg = self.find_elementl(self.tb)
        return self.find_elementls(bg, self.nms)

    def get_namepath(self, i: int) -> tuple:
        pt = (By.XPATH, '//*[@id="app"]/div/section/section/main/div[2]/div[2]/div[1]/div[4]/div[2]/table/tbody/tr[' + str(
            i) + ']/td[2]/div')
        return pt

