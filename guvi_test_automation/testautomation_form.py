from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input").send_keys("Test")
driver.find_element(By.XPATH, "//button[text()='Click Me']").click()
alert = driver.switch_to.alert
alert.accept()
driver.find_element(By.ID, "datepicker").click()
driver.find_element(By.XPATH, "//span[text()='Prev']").click()


driver.find_element(By.LINK_TEXT, "1").click()
driver.find_element(By.XPATH, "//label[text()='Select a speed']").click()
driver.find_element(By.XPATH, "//*[@id='speed']/option[5]").click()
driver.find_element(By.ID, "files").click()
driver.find_element(By.XPATH, "//*[@id='files']/option[2]").click()


driver.find_element(By.ID, "number").click()
driver.find_element(By.XPATH, "//*[@id='number']/option[1]").click()
driver.find_element(By.ID, "products").click()
driver.find_element(By.XPATH, "//*[@id='products']/option[3]").click()
driver.find_element(By.ID, "animals").click()
driver.find_element(By.XPATH, "//*[@id='animals']/option[4]").click()


driver.switch_to.frame('frame-one1434677811')
driver.find_element(By.ID, "RESULT_TextField-1").send_keys("Evanchalin")
driver.find_element(By.ID, 'RESULT_TextField-2').send_keys("C K")
driver.find_element(By.ID, 'RESULT_TextField-3').send_keys("987654321")
driver.find_element(By.ID, 'RESULT_TextField-4').send_keys("India")
driver.find_element(By.ID, 'RESULT_TextField-5').send_keys("Chennai")
driver.find_element(By.ID, 'RESULT_TextField-6').send_keys("abcd@gmail.com")
driver.find_element(By.XPATH, "//label[text()='Female']").click()
driver.find_element(By.XPATH, "//label[text()='Sunday']").click()
driver.find_element(By.CLASS_NAME, "drop_down").click()
driver.find_element(By.XPATH, "//option[text()='Morning']").click()


# upload file
driver.find_element(By.CSS_SELECTOR, "input.file_upload").send_keys("C:\\Users\\glads\\Desktop\\Sample.txt")


# # Drag and drop

driver.switch_to.parent_frame()
actions = ActionChains(driver)
driver.find_element(By.XPATH, "//button[text()='Copy Text']")
actions.double_click().perform()

actions = ActionChains(driver)
source = driver.find_element(By.ID, "draggable")
dest = driver.find_element(By.ID, "droppable")
actions.drag_and_drop(source, dest).perform()


# Slider

actions = ActionChains(driver)
actions.click_and_hold(driver.find_element(By.CSS_SELECTOR, "div#slider>span")).move_by_offset(100, 0).perform()
# actions.click_and_hold(driver.find_element(By.XPATH, "//*[@id='sidebar-right-1']/div[4]/div[2]"))
# /.move_by_offset(100, 0).perform()


actions = ActionChains(driver)
actions.click_and_hold(driver.find_element(By.ID, "resizable")).move_by_offset(100, 50).perform()

driver.close()

