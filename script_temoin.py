#!/usr/bin/env python
# -*- coding: utf-8 -*-
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

import threading
def check_play():
    try:  
        bouton_play = driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[3]/main/div[2]/div[2]/div/div/div[2]/section/div[2]/div[2]/div/button[1]")
        bouton_play_mode = bouton_play.get_attribute("title")
        if (bouton_play_mode == "Lecture"):
            bouton_play.click()
    except Exception:
        pass
def check_repeat():
    try:
        bouton_repeat = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/button[5]')
        if (bouton_repeat.get_attribute("aria-checked") != "true"):
            bouton_repeat.click()
    except Exception:
        pass   
def check_time():
    threading.Timer(2.0,check_time).start()
    check_play()
    check_repeat()

def refresh():
    threading.Timer(3600.0, refresh).start()
    driver.refresh()

def accept_cookies():
    if (driver.find_elements_by_xpath('/html/body/div[12]/div[3]/div/div/div[2]/div/button[1]') != []):
        bouton_cookies = driver.find_element_by_xpath('/html/body/div[12]/div[3]/div/div/div[2]/div/button[1]')
        bouton_cookies.click()

def service_test():
    if (driver.find_elements_by_xpath('/html/body/div[3]/div/div[3]/div/div[2]/button') != []):
        bouton_fermer = driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div[2]/button')
        bouton_fermer.click()
        
# 2 phase de navigation
def navi (email, password):
    # veuillez renseignez votre playlist spotify dans les guillemets
    driver.get("votre playlist spotify")
    time.sleep(1)

    accept_cookies()
    time.sleep(1)
    service_test()
    time.sleep(1)

    bouton_login = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/header/div[5]/button[2]')
    bouton_login.click()
    time.sleep(3)
    champ_email = driver.find_element(By.ID, "login-username")
    champ_email.send_keys(email + Keys.TAB)
    champ_password = driver.find_element(By.ID, "login-password")
    champ_password.send_keys(password + Keys.ENTER)

    time.sleep(5)
    
    check_play()
    check_repeat()

    check_time()
    refresh()

    time.sleep(2)

    bouton_play = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/main/div[2]/div[2]/div/div/div[2]/section/div[2]/div[2]/div/button[1]')
    bouton_play.click()
    
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('useAutomationExtension', False)
# veuillez renseigner votre chemin vers votre chromedriver dans les guillemets
# exemple : 'C:/Votre chemin/chromedriver.exe'
chrome_options.add_argument("--incognito")
chrome_options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome('/Users/aveyronvictor/Documents/GINFO/Automatisation-/chromedriver', options=chrome_options)

#options = Options()
#options.add_experimental_option('useAutomationExtension', False)
# veuillez renseigner votre chemin vers votre chromedriver dans les guillemets
# exemple : 'C:/Votre chemin/chromedriver.exe'
#driver = webdriver.Chrome('path vers chromedriver.exe', options=options)

# où comme cela:
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
# cependant vous devez importer ceci:
# from webdriver_manager.chrome import ChromeDriverManager

# veuillez renseigner votre adresse mail et le mot de passe de votre compte spotify dans les guillemets
navi("adresse mail", "mot de passe")