import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



driver_path = 'C:/circle_ci/chromedriver/chromedriver.exe'

# Create a Chrome driver instance
driver = webdriver.Chrome(executable_path=driver_path)


driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/dropdown")
element = Select(driver.find_element(By.XPATH,"//select[@id='dropdown']"))
element.select_by_index(2)
time.sleep(5)
driver.quit()
