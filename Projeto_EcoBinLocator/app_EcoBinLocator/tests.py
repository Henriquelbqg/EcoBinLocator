from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random
import string
import time
import os
import tempfile
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
browser = webdriver.Chrome(options=chrome_options)


wait = WebDriverWait(browser, 10)

## create a random username
username = ''.join(random.choices(string.ascii_lowercase, k=8))
## create a random password
password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))

class TestSignupLogin(TestCase):
    


    
    def test_g_checklist(self):
        browser.get("http://127.0.0.1:8000/checklist/")
        time.sleep(10)
        browser.find_element(By.ID, "cbx1").click()
        time.sleep(3)
        browser.find_element(By.ID, "cbx2").click()
        time.sleep(3)
        browser.find_element(By.ID, "cbx3").click()
        time.sleep(3)
        browser.find_element(By.ID, "cbx4").click()
        time.sleep(3)
        browser.find_element(By.ID, "cbx5").click()
        assert browser.current_url == "http://127.0.0.1:8000/home/"