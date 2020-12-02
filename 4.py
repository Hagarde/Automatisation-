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
        if driver.find_elements_by_css_selector("button[class='control-button spoticon-pause-16 control-button--circled']") == [] :
            bouton_play = driver.find_element_by_css_selector("button[class='control-button spoticon-play-16 control-button--circled']")
            bouton_play.click()
    except Exception:
        pass
def check_repeat():
    try:
        if driver.find_elements_by_css_selector("button[class='control-button spoticon-repeat-16']") != [] :
            etat_no_repeat = driver.find_element_by_css_selector("button[class='control-button spoticon-repeat-16']")
            etat_no_repeat.click()
    except Exception:
        pass   
def check_time():
    threading.Timer(2.0,check_time).start()
    check_play()
    check_repeat()

def refresh():
    threading.Timer(3600.0, refresh).start()
    driver.refresh()

# 2 phase de navigation
def navi (email, password):
    driver.get("https://open.spotify.com/playlist/7MQ2ATqqdDTnlx3UUDHe5d?si=d3bJe6odSe-b2Ww8obRR_A")
    time.sleep(3)

    bouton_login = driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/header/div[5]/button[2]')
    bouton_login.click()
    time.sleep(6)
    champ_email = driver.find_element(By.ID, "login-username")
    champ_email.send_keys(email + Keys.TAB)
    champ_password = driver.find_element(By.ID, "login-password")
    champ_password.send_keys(password + Keys.ENTER)

    time.sleep(8)

    bouton_play = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[4]/main/div/div[2]/div/div/div[2]/section/div[3]/div/button[1]')
    bouton_play.click()


    # mettre la boucle on click jsuque'à ce qu'on soit en mode repeat simple
    time.sleep(2)
        
    check_play()
    check_repeat()

    check_time()
    refresh()
    
options = Options()
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome('/Users/aveyronvictor/Documents/AUTO/chromedriver', options=options)
navi("hdxznbbe@gmail.com", "azerty123")