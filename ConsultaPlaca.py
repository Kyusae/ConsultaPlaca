from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common import exceptions as ex
import time
import os 

Placas = input('Digite as placas a serem consultas (Separe por virgulas): ').split(",")

class ConsultaPlaca:
    def __init__(self, Placas):
        self.Placa = Placas
        self.driver = webdriver.Firefox(executable_path="geckodriver.exe")

    def login(self):
        driver = self.driver
        driver.get("https://placaconsultar.com.br") #URL
        driver.set_window_size(1873,1096)
        time.sleep(3)
        
        try:
            for elemento in Placas:
                
                caminho_arquivo = os.path.expanduser("~/Downloads/" + elemento)

                #Digita a placa no TxtBox
                digitaplaca = driver.find_element(By.ID, "search-placa")
                digitaplaca.click()
                digitaplaca.clear()
                digitaplaca.send_keys(elemento)
    
                ClicaConsultar = driver.find_element(By.ID, "buttonsearch")
                ClicaConsultar.click()
    
                time.sleep(5)
    
                #AbreDados = driver.find_element(By.XPATH, "xpath=//a[@id='accordion1-card-head-elilekqt']/div")
                #AbreDados.click()
    
                #time.sleep(1)
    
                RetornaMarca = driver.find_element(By.ID, "accordion1-card-body-qjuuilju")
                print(RetornaMarca.text)
    
                print('-----------------------------------------------------------------')
                
                with open(caminho_arquivo, "w") as arquivo:
                    for elemento in Placas:
                        arquivo.write(elemento + "\n")
                        
                #"//*[local-name()='img' and @title='BraboCar Logo Dark']"
                VoltaHome = driver.find_element(By.XPATH, "//*[local-name()='img' and @title='BraboCar Logo Dark']")
                VoltaHome.click()
    
                time.sleep(2)
        except ex.NoSuchElementException:
            driver.get("https://buscaplacas.com.br/?ref=pg02")
            time.sleep(3)

            for elemento in Placas:
                caminho_arquivo = os.path.expanduser("~/Downloads/" + elemento)

                #Digita a placa no TxtBox
                digitaplaca = driver.find_element(By.ID, "name-3b55")
                digitaplaca.click() 
                digitaplaca.clear()
                digitaplaca.send_keys(elemento)
                
                ClicaConsultar = driver.find_element(By.XPATH, "/html/body/section/div/div/form/div[2]/a")
                ClicaConsultar.click()
    
                time.sleep(10)
    
                #AbreDados = driver.find_element(By.XPATH, "xpath=//a[@id='accordion1-card-head-elilekqt']/div")
                #AbreDados.click()
    
                #time.sleep(1)
    
                RetornaMarca = driver.find_element(By.ID, "sec-0879")
                print(RetornaMarca.text)

                with open(caminho_arquivo, "w") as arquivo:
                    for elemento in Placas:
                        arquivo.write(RetornaMarca.text + "\n")

                print('-----------------------------------------------------------------')
    
                #"//*[local-name()='img' and @title='BraboCar Logo Dark']"
                VoltaHome = driver.find_element(By.XPATH, "/html/body/header/div/h3/a")
                VoltaHome.click()
    
                time.sleep(2)
        
BotConsultaPlaca = ConsultaPlaca(Placas)
BotConsultaPlaca.login()