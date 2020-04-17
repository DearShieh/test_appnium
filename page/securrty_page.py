import os,sys
sys.path.append(os.getcwd())
from base.base_action import BaseAction
from selenium.webdriver.common.by import By


class SecurityPage(BaseAction):

    display_button = By.XPATH,"//*[contains(@text,'显示')]"
    wallpaper_button = By.XPATH,"//*[contains(@text,'壁纸')]"
    hudong_button = By.XPATH,"//*[contains(@text,'互动屏幕')]"

    def __init__(self,driver):
        BaseAction.__init__(self, driver)
        self.driver = driver
        self.click_display()
    def click_display(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
        # self.driver.find_element(By.XPATH,"//*[contains(@text,'显示')]").click()
        # self.find_element(self.display_button).click()
        self.click(self.display_button)
    def click_wallpaper(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'壁纸')]").click()
        # self.driver.find_element(By.XPATH,"//*[contains(@text,'壁纸')]").click()
        # self.find_element(self.wallpaper_button).click()
        self.click(self.wallpaper_button)
    def click_hudong(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'互动屏幕')]").click()
        # self.driver.find_element(By.XPATH,"//*[contains(@text,'互动屏幕')]").click()
        # self.find_element(self.hudong_button).click()
        self.click(self.hudong_button)