from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException

import time, threading

# Setting up Selenium Web Driver
chrome_driver = Service("D:\Development res\Chrome Driver\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

items_to_buy = ["Cursor","Grandma","Factory","Mine","Shipment","Alchemy lab","Portal","Time machine"]

time_to_buy = time.time() + 5
time_to_stop = time.time() + (5*60)

def buy_stuff():
    global driver
    money = int(driver.find_element(By.ID,"money").get_attribute("innerHTML").replace(",",""))
    cost = 0
    item_name = None
    for item in items_to_buy:
        item_cost = int(driver.find_element(By.ID,f"buy{item}").find_element(By.TAG_NAME,"b").get_attribute("innerHTML").split('</moni>')[-1].replace(",",""))
        if (item_cost > cost) and (item_cost < money):
            cost = item_cost
            item_name = item
            print(item_name)
    try:
        buy = driver.find_element(By.ID,f"buy{item_name}")
        buy.click()
    except (ElementNotInteractableException, NoSuchElementException):
        buy_stuff()

while time.time()<time_to_stop:
    if time.time() > time_to_buy:
        # print("5 seconds have passed")
        buy_stuff()
        time_to_buy = time.time() + 5
    cookie_clicker = driver.find_element(By.ID, "cookie")
    cookie_clicker.click()

cps = driver.find_element(By.ID,"cps").text
print(cps)

driver.quit()