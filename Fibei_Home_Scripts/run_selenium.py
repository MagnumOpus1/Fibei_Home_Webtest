"""
# Filename: run_selenium.py
"""

import os.path
from datetime import datetime 
from LoginRegistration_Script import *
from Footer_button_Script import *
from Banners_script import *

##########################   testing navigation bar ################################

def NavBarTest():
    NavBarStrings = ['Home']

    for NavBarString in NavBarStrings:
        browser.find_element(By.LINK_TEXT, NavBarString).click()
        print("\n" + NavBarString + " clicked")
        print("Testing : " + NavBarString)
        CusService()
        KnowMore()
        OrderInfo()
        TermsOFUse()
    
    browser.find_element(By.LINK_TEXT, 'Home').click()
#####################################################################################


LoginRegistration()
NavBarTest()
banner()
banner_2nd()
banner_3rd()
FeaturedCateg()



print("\n...........exiting.............")
browser.quit()


