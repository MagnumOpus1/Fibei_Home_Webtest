"""
# Filename: miscellanous_script.py
"""

from browser_config import *
from test_configuration import *


################################# EndPage Function ################################
def EndPage():
    time.sleep(waitTime)
    browser.find_element(by=By.CSS_SELECTOR, value="html").click()
    browser.find_element(by=By.XPATH, value="/html/body").send_keys(Keys.END)
    browser.find_element(by=By.XPATH, value="/html/body").send_keys(Keys.END)
    #print("page down")

####################################################################################

################################# PageDown Function ################################
def PageDown():
    time.sleep(waitTime)
    #browser.find_element(by=By.CSS_SELECTOR, value="body").click()
    #body12.send_keys(Keys.TAB)
    browser.find_element(by=By.XPATH, value="//html").send_keys(Keys.PAGE_DOWN)
    browser.find_element(by=By.XPATH, value="//html").send_keys(Keys.PAGE_DOWN)
    #try1 = browser.find_element(By.LINK_TEXT, 'Home').click()
    #try1.send_keys(Keys.PAGE_DOWN)

####################################################################################

################################# Error function ###################################
def Error(error_name):
    get_url = browser.current_url
    try:
        error_name_underscore = error_name.replace(" ", "_")
        error_SS = browser.get_screenshot_as_file(f"{error_name_underscore}_{dt}.png")
        print("Error occured at: ", error_name_underscore, "\nAt URL: ",get_url, "\nScreentshot saved: ", error_SS)
        
    except:
        error_SS = browser.get_screenshot_as_file(f"{error_name}_{dt}.png")
        print("Error occured at: ", error_name, "\nAt URL: ",get_url, "\nScreentshot saved: ", error_SS)
    
    traceback.print_exc()
####################################################################################  