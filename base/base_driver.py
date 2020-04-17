
from appium import webdriver

def init_driver():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1.1'
    desired_caps['deviceName'] = '127.0.0.1:62001'
    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = '.Settings'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 返回driver对象
    return webdriver.Remote('localhost:4723/wd/hub', desired_caps)