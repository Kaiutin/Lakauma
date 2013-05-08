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
from __future__ import print_function 
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from ovv_parser import parse_ovv
import time

def run_driver():
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


    driver.find_element_by_xpath('//*[@id="hakuform"]/div[10]/input[1]').click()
    
    time.sleep(10)
    tekstiTied = open('ovv_json.json', 'r+w')
    elem = driver.find_element_by_xpath("//*")
    source_code = elem.get_attribute("outerHTML")
    
    tekstiTied.write(parse_ovv(source_code))
    tekstiTied.close()
    driver.quit()

if __name__ == "__main__":
    run_driver()


