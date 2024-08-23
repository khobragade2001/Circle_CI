import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
# making for 'requirements.txt' , following commond used
# pip freeze > requirements.txt

chrome_driver_path = "C:/circle_ci/chromedriver-win64/chromedriver.exe"
# service = Service(executable_path=chrome_driver_path)
# opt = Options()
# Initialize the WebDriver with the service
driver = webdriver.Chrome(chrome_driver_path)


driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/dropdown")
element = Select(driver.find_element(By.XPATH,"//select[@id='dropdown']"))
element.select_by_index(2)
time.sleep(5)
driver.quit()