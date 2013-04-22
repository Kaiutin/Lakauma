# -*- coding: utf-8 -*-
# @author: Samuel Uusi-Makela
# @version: 
# 
# Webdriver meant to automate searching of the information of available 
# apartments in Jyväskylä from ovv.com website.
#
#
# Requires seleniumHQ, we should all have pip installed so 
# installation is as simple as "[sudo] pip install selenium" (or seleniumHQ,
# can't remember). Try :D
 
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

def runDriver():
    # Create a new instance of the Firefox driver. Could be chrome too.
    driver = webdriver.Firefox()

    # go to the OVV home page
    driver.get("http://www.ovv.com")

    # Open the menu that contains cities, and picks Jyväskylä
    driver.find_element_by_xpath('//*[(@id = "hakuform")]//*[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "jqTransformSelectOpen", " " ))]').click()
    driver.find_element_by_xpath('//li[(((count(preceding-sibling::*) + 1) = 4) and parent::*)]//a').click()

    # Open the menu containing room amounts, chooses "Kaikki"
    driver.find_element_by_xpath('//*[@id="hakuform"]/div[5]/div/div/a').click()
    driver.find_element_by_xpath('//*[@id="hakuform"]/div[5]/div/ul/li/a[@index=4]').click()

    #Klikkaa "Vuokrataan" nappia
    driver.find_element_by_xpath('//*[@id="hakuform"]/div[10]/input[1]').click()
 
    element = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[2]/div/div[5]/div[4]/div[1]'))
    teksti = driver.find_element_by_xpath('//div[@class="resultPage"]/div["resultItem"]/div[@class="itemText"]')
    
    # Save the current HTML to "ovv_sorsa"
    tekstiTied = open('ovv_sorsa', 'w')
    tekstiTied.write(driver.page_source.encode('utf-8'))

if __name__ == "__main__":
    runDriver()


#//div[@class="resultPage"]/div[@class="resultItem"]/div[@class="itemText"]
#driver.find_element_by_xpath('//li[(((count(preceding-sibling::*) + 1) = 5) and parent::*)]//a').click()
#//li[(((count(preceding-sibling::*) + 1) = 5) and parent::*)]//a
#//div[@class="jqTrasformSelectWrapper"]//*[@index="2"]
