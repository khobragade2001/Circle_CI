import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
# making for 'requirements.txt' , following commond used
# pip freeze > requirements.txt

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/dropdown")
element = Select(driver.find_element(By.XPATH,"//select[@id='dropdown']"))
element.select_by_index(2)
time.sleep(5)
driver.quit()