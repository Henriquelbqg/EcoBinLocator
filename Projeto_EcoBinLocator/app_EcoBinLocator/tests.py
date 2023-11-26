from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random
import string
import time
import os
import tempfile

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
browser = webdriver.Chrome(options=chrome_options)


## create a random username
username = ''.join(random.choices(string.ascii_lowercase, k=8))
## create a random password
password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))

class TestSignupLogin(TestCase):
    def test_a_home(self):
        browser.get("http://127.0.0.1:8000/home/")
        time.sleep(3)
        browser.find_element(By.ID, "botao1").click()
        time.sleep(2)
        assert browser.current_url == "http://127.0.0.1:8000/endereco/"
    

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
        time.sleep(5)
        assert browser.current_url == "http://127.0.0.1:8000/home/"
    
    
    # Seus testes anteriores

    def test_d_denuncia(self):
        browser = webdriver.Chrome()
        time.sleep(3)
        try:
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

            # Crie um arquivo temporário aleatório
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(b'Some random content')  # Escreva dados aleatórios no arquivo

            # Localize o campo de upload por ID (ou outro localizador apropriado)
            upload_input = browser.find_element(By.ID, "uploadFile")

            # Envie o caminho do arquivo temporário para o campo de upload
            upload_input.send_keys(temp_file.name)

            # Continue com o teste, por exemplo, clicando no botão de envio
            browser.find_element(By.ID, "enviar").click()
            time.sleep(0.5)
            assert browser.current_url == "http://127.0.0.1:8000/home"
            
        finally:
            # Exclua o arquivo temporário
            os.remove(temp_file.name)

            # Feche o navegador Selenium
            browser.quit()
    
    
    def test_e_suporte(self):
        browser.get("http://127.0.0.1:8000/suporte/")
        time.sleep(4)
        browser.find_element(By.ID, "escreva").send_keys(password)
        time.sleep(3)
        browser.find_element(By.ID, "enviar").click()
        time.sleep(3)
        assert browser.current_url == "http://127.0.0.1:8000/home/"

    def test_f_instrucoes(self):
        browser.get("http://127.0.0.1:8000/instrucoes/")
        time.sleep(5)
        assert browser.current_url == "http://127.0.0.1:8000/home/"


    
    def test_g_checklist(self):
        browser.get
        browser.get("http://127.0.0.1:8000/checklist/")
        time.sleep(3)
        browser.find_element(By.ID, "cbx1").click()
        time.sleep(3)
        browser.find_element(By.ID, "cbx2").click()
        time.sleep(3)
        browser.find_element(By.ID, "cbx3").click()
        time.sleep(3)
        browser.find_element(By.ID, "cbx4").click()
        time.sleep(3)
        browser.find_element(By.ID, "cbx5").click()