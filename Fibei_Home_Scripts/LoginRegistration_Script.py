"""
# Filename: LoginRegistration_Script.py
"""

import os.path
from browser_config import *
from test_configuration import *
############################### LOG IN AND REGISTRATION ############################

def LoginRegistration():
    print("Testing Login Page")
    login = browser.find_element(By.CLASS_NAME,Login_button).click()
    print("login button clicked")
    print("***************login test*************")
    time.sleep(waitTime)

    
    print("testing email inputs")
    e_mail = browser.find_element(By.ID, e_mail_textbox)
    passWORD = browser.find_element(By.ID, passWORD_textbox)
    
    #Login Test List

    browser.find_element(By.CSS_SELECTOR, Login_Passwd_visibility).click() #password visibility
    
    for test_Login_email in test_Login_emails:
        e_mail.clear()
        e_mail.send_keys(test_Login_email)
        time.sleep(waitTime)

        for test_Login_passWord in test_Login_passWords:
            passWORD.clear()
            passWORD.send_keys(test_Login_passWord)
            print("\ntesting username: "+test_Login_email)
            print("testing password: "+test_Login_passWord)
            time.sleep(waitTime)
            
            try:
                browser.find_element(By.CSS_SELECTOR,Login_button1).click() #actual login button
                print("Log in button is NOT clickable")
            except:
                #traceback.print_exc()
                print("Log in button is clickable")
    
    print("***************login test end*************")

    print("\n****************Testing Register***************")
    #REGISTER BUTTONS
    browser.find_element(By.CSS_SELECTOR, Register_button).click() #clicks the register button
    regName = WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.ID, regName_textbox))) #finds the name textbox
    regEmail = browser.find_element(By.XPATH, regEmail_textbox)
    regPasswd = browser.find_element(By.NAME, regPasswd_textbox)

    #REGISTER TEST LIST
    
    browser.find_element(By.XPATH, Register_Passwd_visibility).click()

    for test_regName in test_regNames:
        regName.clear()
        regName.send_keys(test_regName) #enters string in the name textbox
        time.sleep(waitTime)
    
        for test_regEmail in test_regEmails:
            regEmail.clear()
            regEmail.send_keys(test_regEmail)
            time.sleep(waitTime)

            for test_regPasswd in test_regPasswds:
                regPasswd.clear()
                regPasswd.send_keys(test_regPasswd)
                print("\ntesting Name: " + test_regName)
                print("testing Email: " + test_regEmail)
                print("testing Password: " + test_regPasswd)
                time.sleep(waitTime)
                try:
                    browser.find_element(By.CSS_SELECTOR, Register_button1).click()#actual register button
                    print("Register button is NOT clickable")
                except:
                    #traceback.print_exc()
                    print("Register button is clickable")

    print("****************Testing Register END***************")
    try:
        time.sleep(waitTime)
        WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR,LogReg_Exit_button))).click()
        print("---->exit button clicked")
    except:
        print("Skipping exit button")

    browser.find_element(By.LINK_TEXT, 'Home').click()
####################################################################################