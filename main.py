from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

PC_HOST = os.environ.get("PC_HOST")
print(PC_HOST)
options = webdriver.chrome.options.Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)
driver.get(f"{PC_HOST}/owners/new")

elem = driver.find_element_by_name("firstName")
elem.clear()
elem.send_keys("pycon")

elem = driver.find_element_by_name("lastName")
elem.clear()
elem.send_keys("pycon")

elem = driver.find_element_by_name("address")
elem.clear()
elem.send_keys("123 Fake St")

elem = driver.find_element_by_name("city")
elem.clear()
elem.send_keys("Nowhere")

elem = driver.find_element_by_name("telephone")
elem.clear()
elem.send_keys("5551234567")

elem.submit()

driver.close()