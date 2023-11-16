import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/browser-windows")
driver.maximize_window()

newtab = driver.find_element(By.XPATH, "//button[@id='tabButton']")
newtab.click()
driver.switch_to.window(driver.window_handles[1])
print("new tab opened")
driver.switch_to.window((driver.window_handles[0]))
driver.find_element(By.XPATH, "//button[@id='windowButton']").click()
driver.switch_to.window(driver.window_handles[2])
driver.quit()
print("new window closed")
driver.find_element(By.XPATH, "//button[@id='messageWindowButton']")
time.sleep(5)
driver.switch_to.window(driver.window_handles[1])
driver.quit()
print("new window closed")

driver.close()
