# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 09:45:07 2021

@author: EGBUNA
"""

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException
import time

path = 'C:/Program Files (x86)/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(path)
driver.set_window_size(1120, 1000)
    
url = 'C:/Users/EGBUNA/Desktop/myscript.html?'
driver.get(url)
num_1 = driver.find_element_by_id('firstnum')
num_1.send_keys(input('input first number: '))
time.sleep(3)
num_2 = driver.find_element_by_id('secondnum')
num_2.send_keys(input('input second number: '))
time.sleep(3)
submit = driver.find_element_by_css_selector('body > form:nth-child(1) > input:nth-child(3)')
submit.click()
time.sleep(2)
try:
    driver.close()
except UnexpectedAlertPresentException:
    driver.close()