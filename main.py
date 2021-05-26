from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import random
import string
import time

PC_HOST = os.environ.get("PC_HOST")
print(PC_HOST)

LAST_NAME="Selenium"

def add_user(driver):
    letters = string.ascii_lowercase
    random_letters = ''.join(random.choice(letters) for i in range(10))

    numbers = string.digits
    random_phone = ''.join(random.choice(numbers) for i in range(7))

    driver.get(f"{PC_HOST}/owners/new")

    elem = driver.find_element_by_name("firstName")
    elem.clear()
    elem.send_keys(random_letters)

    elem = driver.find_element_by_name("lastName")
    elem.clear()
    elem.send_keys(LAST_NAME)

    elem = driver.find_element_by_name("address")
    elem.clear()
    elem.send_keys(f"{random_phone[0:3]} Fake St")

    elem = driver.find_element_by_name("city")
    elem.clear()
    elem.send_keys("Nowhere")

    elem = driver.find_element_by_name("telephone")
    elem.clear()
    elem.send_keys(f"555{random_phone}")

    elem.submit()
    return random_letters

def cause_an_error(driver):
    driver.get(f"{PC_HOST}/404")
    driver.get(f"{PC_HOST}")
    elem = driver.find_element_by_xpath("//a[@href='/oups']")
    print(elem)
    elem.click()
    print(driver.current_url)
    elems = driver.find_elements_by_class_name("container")
    for e in elems:
        print(e.text)

def find_owner(driver, first_name, last_name=LAST_NAME):
    driver.get(f"{PC_HOST}")
    elem = driver.find_element_by_xpath("//a[@href='/owners/find']")
    elem.click()
    elem = driver.find_element_by_id("lastName")
    elem.clear()
    elem.send_keys(last_name)
    elem.submit()

    elems = driver.find_elements_by_tag_name("td")
    for e in elems:
        if e.text == f"{first_name} {last_name}":
            link = e.find_element_by_tag_name("a")
            link.click()
            break
    elems = driver.find_elements_by_tag_name("tr")
    for e in elems:
        print(e.text)

def find_owner_fail(driver):
    driver.get(f"{PC_HOST}")
    elem = driver.find_element_by_xpath("//a[@href='/owners/find']")
    elem.click()
    elem = driver.find_element_by_id("lastName")
    elem.clear()
    elem.send_keys(round(time.time() * 1000))
    elem.submit()
    elem = driver.find_element_by_class_name("help-inline")
    print(elem.text)


def run_tests():
    options = webdriver.chrome.options.Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    cause_an_error(driver)
    for i in range(3):
        first_name = add_user(driver)
        driver.implicitly_wait(2)
        find_owner(driver,first_name)
    find_owner_fail(driver)
    driver.close()

run_tests()