from selenium.webdriver.common.by import  By
def login(driver,username,password):
    driver.find_element(By.ID, 'zentao').click()  # 点击开原版
    driver.find_element(By.ID, 'account').send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.ID, 'submit').click()