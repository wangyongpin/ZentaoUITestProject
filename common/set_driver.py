from selenium import webdriver
import os
def set_driver():
    current = os.path.dirname(__file__)
    chrome_driver_path = os.path.join(current, '../webdriver/chromedriver.exe')
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.implicitly_wait(10)
    # self.driver.maximize_window()
    driver.get('http://127.0.0.1:81/index.php')
    return driver