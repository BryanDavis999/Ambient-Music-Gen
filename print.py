#! /usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Safari()
driver.get("https://www.dcode.fr/music-sheet")
elem = driver.find_element_by_id("convert_from_abc_to_sheet_notes_abc")
print(elem)
elem.clear()
elem.send_keys("A5, G#5, A5, G#5, F#5, F#5, F#5, F#5, F#5, F#5, F#5, F#5, B5, B5, C#6, B5,")

button = driver.find_element_by_xpath('/html/body/div[2]/div[2]/form[4]/button')
button.location_once_scrolled_into_view
button.click()
time.sleep(5)

driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[4]/span[2]/form/button[2]").click()

time.sleep(10)
driver.close()