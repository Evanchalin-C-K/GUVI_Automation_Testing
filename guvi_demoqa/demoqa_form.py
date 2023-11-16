import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

try:
    driver.find_element(By.XPATH, "//input[@value='Female']").click()
except ElementClickInterceptedException as e:
    driver.execute_script("arguments[0].click()", driver.find_element(By.XPATH, "//input[@value='Female']"))

time.sleep(5)
driver.close()
