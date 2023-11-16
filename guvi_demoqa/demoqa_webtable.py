from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/webtables")
tableData = driver.find_elements(By.XPATH, "//div[@class='rt-table']")
for data in tableData:
    print(data.text)

driver.close()
