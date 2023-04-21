"""
# Filename: test_configuration.py
"""

from datetime import datetime 
from browser_config import *
import traceback
import time

#time stamp
dt = datetime.now()

#manual browser wait time
waitTime = 2




"""
# Filename: LoginRegistration_Script.py
"""
#LOGIN test list
test_Login_emails = ['jeth.fifibuy@gmail.com', 'User2', '12352346534567', 'jeth.fifibuy@gmail.com']
test_Login_passWords = ['1', '1234', '1234534562435', 'Fibei123']

#REGISTER TEST LIST
test_regNames = [' ', 'juan1', 'juan!', ' ']
test_regEmails = ['jeth.fifibuy@gmail.com', 'User2', 'User3@gmail.com', 'jeth.fifibuy@gmail.com']
test_regPasswds = ['Fibei123', '1234', '1234534562435', 'Fibei123']

#LOGIN Button 
Login_button = "mat-button-wrapper" #from home page
Login_button1 = 'button.mat-focus-indicator.space-top.ng-tns-c192-1.mat-raised-button.mat-button-base.ng-trigger.ng-trigger-animate.mat-primary.mat-button-disabled' #actual login button

#Password visibility
Login_Passwd_visibility = 'button.mat-ripple.mat-icon-button.cdk-focused.cdk-mouse-focused'

#LOGIN Text Box
e_mail_textbox = 'mat-input-0' #email text box
passWORD_textbox = "mat-input-1" #password text box

#REGISTER Text Box
regName_textbox = "mat-input-2" #finds the name textbox
regEmail_textbox = "/html/body/div[3]/div[2]/div/mat-dialog-container/app-login/div/mat-card-content/ngx-auth-firebaseui/mat-tab-group/div/mat-tab-body[2]/div/mat-card/mat-card-content/form/div/mat-form-field[2]/div/div[1]/div[1]/input"
regPasswd_textbox = "password"

#REGISTER BUTTONS
Register_button = "div#mat-tab-label-0-1"
Register_button1 = 'button.mat-focus-indicator.ng-tns-c192-1.mat-raised-button.mat-button-base.ng-trigger.ng-trigger-animate.mat-primary.mat-button-disabled'
#REGISTER Password visibility
Register_Passwd_visibility = '//*[@id="mat-tab-content-0-1"]/div/mat-card/mat-card-content/form/div/div/mat-form-field/div/div[1]/div[2]/mat-pass-toggle-visibility/button/mat-icon'

#LOGIN REGISTRATION EXIT BUTTON
LogReg_Exit_button = "button.mat-focus-indicator.mat-button.mat-button-base"



"""
# Filename: Banners_script.py
"""
###################################   testing banner ########################
banner_1_XPATH = '//*[@id="tabsSection"]/app-tabs/ion-tabs/div/ion-router-outlet/app-home/ion-content/section/div/div[1]/div[1]/a/img'
banner_2_XPATH = '//*[@id="tabsSection"]/app-tabs/ion-tabs/div/ion-router-outlet/app-home/ion-content/section/div/div[1]/div[2]/a/img'

###################################  2nd banner #############################
banner_2nd_text = ['ecards', 'cards with poetry', 'postcards', 'sign and send', 'stickers']

############################## testing Featured Category ####################
carousel_lists = ['Mothers day', 'Anniversary day','Sympathy', 'Pet cards']
