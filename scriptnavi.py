#!/usr/bin/env python
# -*- coding: utf-8 -*-
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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
    threading.Timer(10.0,check_time).start()
    check_play()
    check_repeat()
    


# 2 phase de navigation
def navi (emaile, mdpa):
    driver.get("https://open.spotify.com/playlist/5UsnYdUjn9I9uDK4ZzcUZV")
    time.sleep(1)
    #Besoin de se log in ? si oui on le fait sinon on commence la lecture 
    if driver.find_elements(By.CLASS_NAME,"_2221af4e93029bedeab751d04fab4b8b-scss") != [] : 
        connecter = driver.find_elements(By.CLASS_NAME,"_2221af4e93029bedeab751d04fab4b8b-scss") [1]
        connecter.click()
        time.sleep(3)
    #Log in
        if driver.find_elements(By.ID, 'login-button') != [] : # Je teste si je suis déjà connecté ou si il faut se log in
            email =driver.find_element(By.ID, "login-username")
            email.send_keys(emaile + Keys.TAB)
            mdp = driver.find_element(By.ID, "login-password")
            mdp.send_keys(mdpa + Keys.ENTER)
    else : print ("Ca ne marche pas ")web

    time.sleep(2)
    check_play()
    check_repeat()
    

while True :
    with open("email.txt",'r') as f :
        for line in f.readlines() :
            time.sleep(2)
            driver = webdriver.Chrome()
            email = str(line.strip())
            navi(email,"Azerty123")
    time.sleep(3600)


