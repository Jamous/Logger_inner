#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime

#Code
username = ""
password = ""

driver = webdriver.Chrome()

driver.get("https://www.lumen.com/login")

time.sleep(3)
driver.find_element(By.XPATH, '//button[normalize-space()="Continue"]').click()

time.sleep(3)
driver.find_element(By.ID, "signInName").send_keys(username)
driver.find_element(By.ID, "next").click()

time.sleep(3)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.ID, "next").click()

time.sleep(60)
driver.quit()

logFile = open("log.txt", 'a')
logFile.write("Script as completed. " + str(datetime.datetime.now()) + "\n")