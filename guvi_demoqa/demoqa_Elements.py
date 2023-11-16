import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException

# TextBox
driver = webdriver.Chrome()
driver.refresh()
driver.get("https://demoqa.com/text-box")
driver.maximize_window()

OpenJson = open("../Json/Input.json")
readJson = json.load(OpenJson)
OpenJson.close()

driver.find_element(By.XPATH, "//input[@id='userName']").send_keys(readJson["Fullname"])
driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys(readJson["email"])
city = readJson['currentAddress'][0].get('city')
driver.find_element(By.XPATH, "//textarea[@id='currentAddress']").\
    send_keys(readJson['currentAddress'][0].get('city'), "\n", readJson['currentAddress'][0].get('street'))
driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']").\
    send_keys(readJson['permanentAddress'][0].get('city'), "\n", readJson['permanentAddress'][0].get('street'))
time.sleep(5)
# driver.get_screenshot_as_file("text_box.jpeg")
print("TextBox - Done")

#Checkbox

driver.get("https://demoqa.com/checkbox")
driver.find_element(By.XPATH, "//button[@title='Toggle']").click()
driver.find_element(By.XPATH, "//span[text()='Downloads']").click()
time.sleep(3)
# driver.save_screenshot("Checkbox.jpeg")
print("CheckBox - Done")

# RadioButton
driver.get("https://demoqa.com/radio-button")
try:
    driver.find_element(By.XPATH, "//input[@id='yesRadio']").click()
except ElementClickInterceptedException as e:
    driver.execute_script("arguments[0].click()", driver.find_element(By.XPATH, "//input[@id='yesRadio']"))
time.sleep(5)
# driver.get_screenshot_as_png()
print("RadioButton - Done")

# Buttons
driver = webdriver.Chrome()
driver.get("https://demoqa.com/buttons")
driver.maximize_window()
action = ActionChains(driver)
action.double_click(driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")).perform()
time.sleep(3)
action.context_click(driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")).perform()
time.sleep(3)
driver.find_element(By.XPATH, "//button[text()='Click Me']").click()
# driver.execute_script("arguments[0].click()", driver.find_element(By.XPATH, "//button[text()='Click Me']"))
time.sleep(3)
# driver.get_screenshot_as_base64()
print("Buttons - Done")

# Dynamic Properties
driver.get("https://demoqa.com/dynamic-properties")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//button[@id='enableAfter']").click()
driver.find_element(By.XPATH, "//button[@id='colorChange']").click()
click = driver.find_element(By.XPATH, "//button[text()='Visible After 5 Seconds']")
driver.execute_script("arguments[0].click()", click)
# driver.save_screenshot("DynamicProperties.jpeg")
print("Dynamic Properties - Done")

driver.close()
