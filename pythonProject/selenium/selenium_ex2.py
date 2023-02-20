import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/Alok/drivers/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://online.qspiders.com/user")
time.sleep(2)
driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH,"//input[@type='email']").send_keys("alokadarsh236166@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@type='tel']").send_keys("8252551890")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[5]/div/div/span/form/div/div[3]/button").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/div/span/form/div/div[1]/div/span/div/div/input").send_keys("5A5l6o1k@661")
time.sleep(2)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div[2]/div/div/div[4]/div/div/span").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='__layout']/div/div[1]/div[2]/div/div/div[4]/ul/div[4]/a/div").click()
k=driver.window_handles
for i in k:
    driver.switch_to.window(i)
    print(driver.title)
    if driver.title=="My Course | Student":
        driver.close()
time.sleep(4)

