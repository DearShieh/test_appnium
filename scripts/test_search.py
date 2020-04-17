import os,sys
sys.path.append(os.getcwd())

import pytest
from base.base_driver import init_driver
from page.search_page import SearchPage
from base.base_yml import yml_data_with_file

def data_with_key(key):
    return yml_data_with_file("search_data")[key]

class TestSearch:
    def setup(self):           # setUp  大写了U 报错：E  AttributeError: 'TestSearch' object has no attribute 'display_page'
        self.driver = init_driver()
        self.display_page = SearchPage(self.driver)

    # @pytest.mark.parametrize("text",["设置","123"])
    @pytest.mark.parametrize("text",data_with_key("test_display_search"))
    def test_display_search(self,text):
        # 点击显示
        self.display_page.click_display()
        # 点击搜索
        self.display_page.click_search()
        # 输入文字
        self.display_page.input_search_text(text)
        # 点击返回
        self.display_page.click_back()


# Xpath 精确查找
# //*[contains(@text,'设')]      # 包含
# //*[@text,'设']                # 精确查找
# //*[@text,'设' and @resource-id='xxxxxx']        # 多个条件







