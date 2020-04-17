import os,sys
sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class SearchPage(BaseAction):

    display_button = By.XPATH,"//*[contains(@text,'显示')]"
    search_button = By.ID,"com.android.settings:id/search"
    input_text_view = By.ID,"android:id/search_src_text"
    back_button = By.CLASS_NAME,"android.widget.ImageButton"

    # 子类从写父类方法(可不写，除需要增加其他操作)
    # def __init__(self,driver):
    #     BaseAction.__init__(self,driver)
    #     self.driver = driver
        # self.click_display()
        # init里面可以写公用功能（如security都要点击进“安全”里面）

    def click_display(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
        # self.driver.find_element(By.XPATH,"//*[contains(@text,'显示')]").click()
        # self.find_element(self.display_button).click()
        self.click(self.display_button)
    def click_search(self):
        # self.driver.find_element_by_id("com.android.settings:id/search").click()
        # self.driver.find_element(By.ID, "com.android.settings:id/search").click()
        # self.find_element(self.search_button).click()
        self.click(self.search_button)
    def input_search_text(self,text):
        # self.driver.find_element_by_id("android:id/search_src_text").send_keys(text)
        # self.driver.find_element(By.ID, "android:id/search_src_text").click()
        # self.find_element(self.input_text_view).click()
        self.input_text(self.input_text_view,text)
    def click_back(self):
        # self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        # self.driver.find_element(By.CLASS_NAME, "android.widget.ImageButton").click()
        # self.find_element(self.back_button).click()
        self.click(self.back_button)
