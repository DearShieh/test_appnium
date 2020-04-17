'''
测试脚本只专注过程  “怎么干”
page “干什么”
'''

import os,sys
sys.path.append(os.getcwd())
from base.base_driver import init_driver
from page.securrty_page import SecurityPage

class TestSecurity:
    def setUp(self):
        self.driver = init_driver()
        self.security_page = SecurityPage(self.driver)
    def test_security_slip(self):
        # 点击显示
        self.security_page.click_display()
        # 点击壁纸
        self.security_page.click_wallpaper()
    def test_hudong(self):
        self.security_page.click_display()
        self.security_page.click_hudong()