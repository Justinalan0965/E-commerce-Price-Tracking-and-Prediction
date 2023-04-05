from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

open = driver.get("https://www.youtube.com/")

#print(driver.title)

search = driver.find_element(By.NAME,"search_query")

search.send_keys("Demon slayer")
search.send_keys(Keys.RETURN)
print(driver.page_source)
time.sleep(10)
#print(driver.page_source)

