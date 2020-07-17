from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from pathlib import Path
import sys
import os
from os.path import dirname
from time import sleep

#Get the path of the test file
current_dir_path = str(Path(__file__).parent) + "/test.txt"
print(current_dir_path)



web_driver = webdriver.Chrome()
web_driver.get("https://tus.io/demo.html")

# #choose file locator
file_locator =(By.ID, "js-file-input")
element = WebDriverWait(web_driver, 30).until(EC.visibility_of_element_located(file_locator))
element.send_keys(current_dir_path)

# #start upload
# # start_upload = (By.CSS_SELECTOR, '#toggle-btn')
# # element = WebDriverWait(web_driver, 30).until(EC.visibility_of_element_located(start_upload))
# # element.click()
#
# #verify file upload is successful
sleep(3)
upload_success = (By.XPATH, "//a[@class='button button-primary']")
element = WebDriverWait(web_driver, 30).until(EC.visibility_of_element_located(upload_success))
assert element.is_displayed()
sleep(5)

web_driver.quit()
