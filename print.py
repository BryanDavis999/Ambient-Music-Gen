#! /usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Firefox()
driver.get("https://www.dcode.fr/music-sheet")
elem = driver.find_element_by_id("convert_from_abc_to_sheet_notes_abc")
print(elem)
elem.clear()

f = open ("notes.txt","r")
notes = f.read()
f.close()
print(notes)
elem.send_keys(notes)
# time.sleep(10)

button = driver.find_element_by_xpath('/html/body/div[2]/div[2]/form[4]/button')
button.location_once_scrolled_into_view
button.click()
time.sleep(5)
button.location_once_scrolled_into_view
button.click()
time.sleep(10)

driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[4]/span[2]/form/button[2]").click()

time.sleep(10)
driver.close()