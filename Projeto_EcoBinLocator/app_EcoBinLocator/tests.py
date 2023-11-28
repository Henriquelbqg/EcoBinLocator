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
from selenium.webdriver.support.ui import WebDriverWait


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-dev-shm-usage")
browser = webdriver.Chrome(options=chrome_options)


wait = WebDriverWait(browser, 10)

username = ''.join(random.choices(string.ascii_lowercase, k=8))
password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))

class TestSignupLogin(TestCase):
    def test_b_endereco(self):
        browser.get("http://127.0.0.1:8000/endereco/")
        time.sleep(2)
        browser.find_element(By.ID, "rua").send_keys(password)
        time.sleep(2)
        browser.find_element(By.ID, "numero").send_keys(password)
        time.sleep(2)
        browser.find_element(By.ID, "botao").click()
        time.sleep(2)
        assert browser.current_url == "http://127.0.0.1:8000/home/"

    def test_c_mapa(self):
        browser.get("http://127.0.0.1:8000/mapa/")
        time.sleep(10)
        assert browser.current_url == "http://127.0.0.1:8000/home/"
    
    

    def test_d_denuncia(self):
        browser = webdriver.Chrome()
        time.sleep(3)
        browser.get("http://127.0.0.1:8000/denuncia/")
        time.sleep(3)
        browser.find_element(By.ID, "cidade").send_keys(password)
        time.sleep(3)
        browser.find_element(By.ID, "referencia").send_keys(password)
        time.sleep(3)
        browser.find_element(By.ID, "rua").send_keys(password)
        time.sleep(3)
        browser.find_element(By.ID, "telefone").send_keys(password)
        time.sleep(3)
        browser.find_element(By.ID, "escreva").send_keys(password)
        time.sleep(4)

        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(b'Some random content')

        upload_input = browser.find_element(By.ID, "uploadFile")

        upload_input.send_keys(temp_file.name)

        browser.find_element(By.ID, "enviar").click()
        time.sleep(0.5)
        assert browser.current_url == "http://127.0.0.1:8000/home"
            
        
    
    
    def test_e_suporte(self):
        browser.get("http://127.0.0.1:8000/suporte/")
        time.sleep(5)
        browser.find_element(By.ID, "escreva").send_keys(password)
        time.sleep(3)
        browser.find_element(By.ID, "enviar").click()
        time.sleep(3)
        assert browser.current_url == "http://127.0.0.1:8000/home/"

    def test_f_instrucoes(self):
        browser.get("http://127.0.0.1:8000/instrucoes/")
        time.sleep(10)
        assert browser.current_url == "http://127.0.0.1:8000/home/"
    


    

    def test_h_produtos(self):
        browser.get("http://127.0.0.1:8000/produtos/")
        time.sleep(10)
        assert browser.current_url == "http://127.0.0.1:8000/home/"