"""
# Filename: Footer_button_Script.py
"""

from browser_config import *
from miscellanous_script import *

###############################  Customer Service  #################################
def CusService():
    '''
    CusService_lists = ['Contact Us', 'Chat Now','Review Product']

    for CusService_list in CusService_lists:
        try:
            EndPage()
            WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,f"{CusService_list}"))).click()
            print(f"---->{CusService_list} button clicked")
        except: 
            print("Skipping {CusService_list} button")
            print(browser.get_screenshot_as_file(f"{CusService_list}_{dt}.png"))
            traceback.print_exc()
    '''
    try:
        EndPage()
        WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,"Contact Us"))).click()
        print("---->Contact Us button clicked")
    except: 
        print("Skipping contact us button")
        Error('Contact Us button')
    try:
        EndPage()
        WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.LINK_TEXT,"Chat Now"))).click()
        print("---->Chat Now button clicked")
    except:
        print("Skipping Chat Now button")
        Error('Chat Now button')
    try:
        EndPage()
        WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.LINK_TEXT,'Review Product'))).click()
        print("---->Review Product button clicked")
    except:
        print("Skipping Review Product button")
        Error('Review Product button')
####################################################################################


##############################  KNOW MORE PAGE  ####################################
def KnowMore():
    try:
        EndPage()
        WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,"About FibeiGreetings"))).click()
        print("---->About FibeiGreetings button clicked")
    except: 
        print("Skipping About FibeiGreetings button")
        Error('About FibeiGreetings button')
        

    try:
        EndPage()
        WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.LINK_TEXT,'Press Page'))).click()
        print("---->Press Page button clicked")
    except: 
        print("Skipping Press Page button")
        Error('Press Page button')

    try:
        EndPage()
        WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,"Sign And Send"))).click()
        print("---->Sign And Send button clicked")
    except: 
        print("Skipping Sign And Send button")
        Error('Sign And Send button')
####################################################################################

##########################  ORDER INFORMATION PAGE  ################################
def OrderInfo():
    try:
        EndPage()
        WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,"Shipping and Delivery"))).click()
        print("---->Shipping and Delivery button clicked")
    except: 
        print("Skipping Shipping and Delivery button")
        Error('Delivery button')
#####################################################################################

##########################  TERMS OF USE  ###########################################
def TermsOFUse():
    try:
        EndPage()
        WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,"Terms and Conditions"))).click()
        print("---->Terms and Conditions button clicked")
    except: 
        print("Skipping Terms and Conditions button")
        Error('Terms and Conditions button')

    try:
        EndPage()
        WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,"Privacy Policy"))).click()
        print("---->Privacy Policy button clicked")
    except: 
        print("Skipping Privacy Policy button")
        Error('Privacy Policy button')
        
####################################################################################