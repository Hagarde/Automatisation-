#!/usr/bin/env python
# -*- coding: utf-8 -*-
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

def newAdvertissement():
    advertissement_button = driver.find_element(By.ID, "navAds")
    advertissement_button.click()
    windowHandleBefore = driver.window_handles[0]
    time.sleep(3)

    getAllAdvertissements = driver.find_elements_by_css_selector('div.cell:not(.c_ad0)')
    i = 0
    for ad in getAllAdvertissements:
        i+=1
        print(i)
        ad.click()
        time.sleep(2)
        getRedDot = driver.find_element(By.ID, 'i' + str(i))
        time.sleep(2)
        getRedDot.click()
        windowHandleAfterAdvertissement = driver.window_handles[1]
        driver.switch_to.window(windowHandleAfterAdvertissement)
        time.sleep(25)
        driver.close()
        time.sleep(4)
        driver.switch_to.window(windowHandleBefore)


def newAdprize():
    advertissement_button = driver.find_element(By.ID, "navAds")
    advertissement_button.click()
    time.sleep(2)
    getMoney = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/span/span').text
    time.sleep(1)
    windowHandleBefore = driver.window_handles[0]
    time.sleep(2)
    adprize_button = driver.find_element(By.ID, "ap_h")
    nbAprize = int(adprize_button.text)
    print(nbAprize)

    for j in range(nbAprize-1):
        j+=1
        print(j)
        adprize_button = driver.find_element(By.ID, "ap_h")
        adprize_button.click()
        time.sleep(3)
        windowHandleAfterAdprize = driver.window_handles[1]
        time.sleep(2)
        driver.switch_to.window(windowHandleAfterAdprize)
        time.sleep(4)
        driver.close()
        time.sleep(4)
        driver.switch_to.window(windowHandleBefore)
    
    return getMoney

def navi (email, password):
    driver.get("https://www.neobux.com/m/v/?vl=53F45EF6C3540938")
    time.sleep(1)

    time.sleep(7)
    champ_email = driver.find_element(By.ID, "Kf1")
    champ_email.send_keys(email + Keys.TAB)
    champ_password = driver.find_element(By.ID, "Kf2")
    champ_password.send_keys(password + Keys.ENTER)

    time.sleep(15)

    newAdvertissement()

    time.sleep(3)

    getMoneyFromNavs = newAdprize()

    time.sleep(2)

    driver.quit()

    return getMoneyFromNavs

options = Options()
# change la partie en dessous pour lancer google comme avec les scripts pour spotify
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome('/Users/aveyronvictor/Documents/AUTO/chromedriver', options=options)
money = navi("Hagardes", "Sakolu-3")

# tu dois pip install smtplib
import smtplib

gmail_user = "victor.neobux.neo@gmail.com"
gmail_password= "Sakolu-3"

sent_from = gmail_user
to = "victor.neobux.neo@gmail.com"
subject = 'Notif Neobux'
body = 'Operation reussi : ' + money

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, to, subject, body)

try:
    server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server_ssl.ehlo()
    server_ssl.login(gmail_user, gmail_password)
    server_ssl.sendmail(sent_from, to, email_text)
    server_ssl.close()
    print('Email sent')
except:
    print ('Something went wrong')

