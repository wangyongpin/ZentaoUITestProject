import time,os
from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
from common import set_driver
from common import login
from selenium.webdriver.support import expected_conditions as EC
import HTMLTestRunner
# current = os.path.dirname(__file__)
# chrome_driver_path = os.path.join(current,'../webdriver/chromedriver.exe')
# firefox_driver_path = os.path.join(current,'../webdriver/geckodriver.exe')

class LoginSuccessCase(unittest.TestCase):
    def setUp(self) -> None: # 把selenium的初始化配置放入
        self.driver = set_driver.set_driver()
    def tearDown(self) -> None: # 测试清理
        time.sleep(2)
        self.driver.quit()

    def test_login(self):
        '这是测试admin Wyp123456 登陆'
        login.login(self.driver, 'admin', 'Wyp123456')
        user_access = self.driver.find_element(By.XPATH,'//*[@id="userNav"]/li/a/span[1]').text
        self.assertEqual(user_access,'admin','test_login测试用例失败')

if __name__ == '__main__':
    unittest.main()
