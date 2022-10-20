from pageDir.page_vhr_login import VhrPage
from pageDir.page_vhr_search import SearchPage
from baseDir.test_base import TestBase
import pytest
from baseDir.read_yaml import ReadYaml
from scriptsDir.conftest import Faild


# 测试类 各种测试类

class Test_Vhr(TestBase):

    @pytest.mark.parametrize("un, pw, cd", ReadYaml().read('login_params.yml'))
    def test_login(self, un, pw, cd):
        vhr = VhrPage(self.driver)
        self.driver.get('http://192.168.1.73:9090/index.html')
        vhr.text_clear()
        vhr.send_text(un, pw, cd)  # 可以进行数据驱动实现参数化
        vhr.login_click()
        if '登录成功' not in vhr.find_msg():
            setattr(Faild, "flag", True)
        else:
            setattr(Faild, "flag", False)
            # global co
            # co = self.driver.get_cookies()
            # setattr(Faild, "cookies", co)
        assert '登录成功' in vhr.find_msg()

    @pytest.mark.parametrize("sn", ReadYaml().read('search_params.yml'))
    def test_search(self, sn):
        if getattr(Faild, "flag"):
            pytest.skip("未登入成功")
        else:
            # print(co)
            # s = getattr(Faild, "cookies")
            # print("search1")
            # assert 1 == 1

            sp = SearchPage(self.driver)
            cur = self.driver.current_url
            if cur == 'http://192.168.1.73:9090/index.html#/home':
                self.driver.get('http://192.168.1.73:9090/index.html#/emp/basic')
            sp.sendname(sn)
            sp.search(sp.bt)
            ls = sp.get_names()
            for i in range(1, len(ls) + 1):
                name = sp.find_elementl(sp.get_namepath(i))
                assert sn[0] in name.text, '%s不在搜索的名字中' % sn[0]
