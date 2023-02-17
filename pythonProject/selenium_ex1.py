import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/Alok/drivers/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://youtube.com/")
time.sleep(4)
driver.maximize_window()
time.sleep(4)

driver.find_element(By.XPATH,"//input[@id='search']").send_keys("tujhe dekha to ye jana sanam")
time.sleep(4)
driver.find_element(By.XPATH,"//button[@id='search-icon-legacy']").click()
time.sleep(4)
driver.find_element(By.XPATH,"//a[@id='video-title']").click()
time.sleep(140)

