import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/Alok/drivers/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://youtube.com/")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='search']").send_keys("tujhe dekha to ye jana sanam")
time.sleep(4)
time.sleep(40)







