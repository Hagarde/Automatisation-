#!/usr/bin/env python
# -*- coding: utf-8 -*-
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import Keyboard
import time

def autoGame():
    
    game_button = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/a[2]')
    windowHandleBefore = driver.window_handles[0]
    game_button.click()

    time.sleep(5)
    start_game_button = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div[2]/a/table/tbody/tr/td[2]')
    start_game_button.click()
    time.sleep(5)
    windowHandleAfterGame = driver.window_handles[1]
    time.sleep(5)
    driver.switch_to.window(windowHandleAfterGame)

    # all_games_btn = driver.find_element_by_xpath('/html/body/div[1]/div/div/main/ark-main-block/ark-article/ark-grid/ark-grid[2]/ark-section/ark-nav/ark-div/ark-ul[1]/ark-li[1]/a')
    # all_games_btn.click()
    # time.sleep(5)
    # knife_game_btn = driver.find_element_by_xpath('/html/body/div[1]/div/div/main/ark-main-block/ark-article/ark-grid/ark-grid[6]/ark-all-games-list/ark-allg-list/ark-li[33]')
    # knife_game_btn.click()
    # time.sleep(5)
    time.sleep(5)
    driver.get("https://gameplayneo.com/games/knife-smash/")
    time.sleep(5)
    # les problèmes arrivent ici !!!
    # j'arrive sur la page du jeux --> il faut cliquer sur le bouton Play now

    i = 0
    while i<50:

        condition = driver.find_element_by_xpath('/html/body/div[1]/div/div/main/ark-main-block/ark-article/ark-grid/ark-grid[4]/ark-div/ark-div/ark-div[2]/ark-div[3]/ark-div[5]').get_attribute('style')
        if (condition != "display: none;"):
            play_knife_game_btn = driver.find_element_by_xpath('/html/body/div[1]/div/div/main/ark-main-block/ark-article/ark-grid/ark-grid[4]/ark-div/ark-div/ark-div[2]/ark-div[3]/ark-div[5]/ark-div/ark-div[2]/ark-div[3]')
            play_knife_game_btn.click()
            time.sleep(5)
            play_game_btn = driver.find_element_by_xpath('/html/body/div[1]/div/div/main/ark-main-block/ark-article/ark-grid/ark-grid[4]/ark-div/ark-div/ark-div[2]/ark-div[3]/ark-div[1]/ark-div/div/video-ad-component/ark-ad-div/ark-ad-div/ark-ad-div[2]/ark-ad-div[2]/ark-ad-div[1]')
            play_game_btn.click()
            time.sleep(30)
            canva = driver.find_element_by_xpath('/html/body/div[1]/div/div/main/ark-main-block/ark-article/ark-grid/ark-grid[4]/ark-div/ark-div/ark-div[2]/ark-div[3]/iframe')
            ac = ActionChains(driver)
            ac.move_to_element_with_offset(canva, 320,373)
            ac.click()
            ac.perform()
            time.sleep(59)
            ac.move_to_element_with_offset(canva, 320,373)
            ac.click()
            ac.perform()
            time.sleep(65)
            for j in range(10):
                try:
                    ac.move_to_element_with_offset(canva, 320,373)
                    ac.click()
                    ac.perform() 
                except:
                    pass
            time.sleep(10)
            play_again_btn = driver.find_element_by_xpath('/html/body/div[1]/div/div/main/ark-main-block/ark-article/ark-grid/ark-grid[4]/ark-div/ark-div/ark-div[2]/ark-div[3]/ark-div[6]/ark-div[1]/ark-div[2]/ark-div[1]')
            play_again_btn.click()
            time.sleep(2)
        elif (driver.find_elements_by_xpath('/html/body/div[1]/div/div/main/ark-main-block/ark-article/ark-grid/ark-grid[4]/ark-div/ark-div/ark-div[2]/ark-div[3]/ark-div[1]/ark-div/div/video-ad-component/ark-ad-div/ark-ad-div/ark-ad-div[2]/ark-ad-div[2]/ark-ad-div[1]') != []):
            play_game_btn = driver.find_element_by_xpath('/html/body/div[1]/div/div/main/ark-main-block/ark-article/ark-grid/ark-grid[4]/ark-div/ark-div/ark-div[2]/ark-div[3]/ark-div[1]/ark-div/div/video-ad-component/ark-ad-div/ark-ad-div/ark-ad-div[2]/ark-ad-div[2]/ark-ad-div[1]')
            play_game_btn.click()
            time.sleep(30)
            canva = driver.find_element_by_xpath('/html/body/div[1]/div/div/main/ark-main-block/ark-article/ark-grid/ark-grid[4]/ark-div/ark-div/ark-div[2]/ark-div[3]/iframe')
            ac = ActionChains(driver)
            ac.move_to_element_with_offset(canva, 320,373)
            ac.click()
            ac.perform()
            time.sleep(59)
            ac.move_to_element_with_offset(canva, 320,373)
            ac.click()
            ac.perform()
            time.sleep(65)
            for k in range(10):
                try:
                    ac.move_to_element_with_offset(canva, 320,373)
                    ac.click()
                    ac.perform() 
                except:
                    pass
            time.sleep(10)
            play_again_btn = driver.find_element_by_xpath('/html/body/div[1]/div/div/main/ark-main-block/ark-article/ark-grid/ark-grid[4]/ark-div/ark-div/ark-div[2]/ark-div[3]/ark-div[6]/ark-div[1]/ark-div[2]/ark-div[1]')
            play_again_btn.click()
            time.sleep(2)
        i+=1
        print(i)

    driver.switch_to.window(windowHandleBefore)

# erreur ac.perform
#  peut etre repassé la fonction play_game dans la prémière pour éviter le problème de window
def play_game():

    canva = driver.find_element_by_xpath('/html/body/div[1]/div/div/main/ark-main-block/ark-article/ark-grid/ark-grid[4]/ark-div/ark-div/ark-div[2]/ark-div[3]/iframe')
    ac = ActionChains(driver)
    ac.move_to_element_with_offset(canva, 320,373)
    ac.click()
    ac.perform()
    time.sleep(60)
    ac.move_to_element_with_offset(canva, 320,373)
    ac.click()
    ac.perform()
    time.sleep(65)
    for i in range(10):
        try:
            ac.move_to_element_with_offset(canva, 320,373)
            ac.click()
            ac.perform() 
        except:
            pass
    time.sleep(10)
    play_again_btn = driver.find_element_by_xpath('/html/body/div[1]/div/div/main/ark-main-block/ark-article/ark-grid/ark-grid[4]/ark-div/ark-div/ark-div[2]/ark-div[3]/ark-div[6]/ark-div[1]/ark-div[2]/ark-div[1]')
    play_again_btn.click()
    time.sleep(2)



def navi (email, password):
    driver.get("https://www.neobux.com/m/v/?vl=71E5406D9B2AEE4D8")
    time.sleep(1)

    time.sleep(3)
    champ_email = driver.find_element(By.ID, "Kf1")
    champ_email.send_keys(email + Keys.TAB)
    champ_password = driver.find_element(By.ID, "Kf2")
    champ_password.send_keys(password + Keys.ENTER)

    time.sleep(15)

    time.sleep(2)

    
    autoGame()
    

    driver.quit()

# Change peut être ça pour lancer le driver
options = Options()
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("start-maximized")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


navi("Hagardes", "Sakolu-3")


