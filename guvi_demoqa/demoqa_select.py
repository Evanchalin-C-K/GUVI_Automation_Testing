import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://demoqa.com/select-menu")
driver.maximize_window()

dropdown = Select(driver.find_element(By.ID, "oldSelectMenu"))
# dropdown.select_by_visible_text("Blue")
element = dropdown.options
for i in element:
    # text = i.get_attribute('innerText')
    # print(text)
    if i.text == "Yellow":
        dropdown.select_by_visible_text("Yellow")
        break
else:
    dropdown.select_by_visible_text("Blue")
time.sleep(10)

print()

dropdown = Select(driver.find_element(By.ID, "cars"))
dropdown.select_by_index(2)
option = dropdown.options
for i in option:
    if i.text == "Saab":
        dropdown.select_by_visible_text(i.text)
else:
    dropdown.select_by_visible_text("Volvo")

time.sleep(10)
driver.close()