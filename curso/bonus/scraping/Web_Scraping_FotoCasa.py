from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

import time
import datetime
import random
import os

url = 'https://www.fotocasa.es/'

driver = webdriver.Chrome()
driver.get(url)

WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'didomi-notice-agree-button'))).click()
buscar = driver.find_element(By.CSS_SELECTOR, 'input.sui-AtomInput-input.sui-AtomInput-input-size-m')
buscar.send_keys('barcelona')
boton_buscar = driver.find_element(By.CSS_SELECTOR, 'button.sui-AtomButton.sui-AtomButton--accent.sui-AtomButton--solid.sui-AtomButton--center').click()
time.sleep(30)

driver.quit()

