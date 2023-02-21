import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj = Service("C:/Users/Alok/drivers/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.wikipedia.org/")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='searchInput']").send_keys("India")
driver.find_element(By.XPATH,"//*[@type='submit']").click()
driver.find_element(By.XPATH,"//*[@id='searchInput']").send_keys("India")
driver.find_element(By.XPATH,"//*[@id='mw-content-text']/div[1]/table[1]/tbody/tr[7]/td/a").click()
print(driver.title)
driver.find_element(By.XPATH,"//*[@id='mw-content-text']/div[1]/table[1]/tbody/tr[8]/td/div/ul/li[1]/a").click()
print(driver.title)



time.sleep(8)