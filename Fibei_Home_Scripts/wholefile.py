"""
# Filename: run_selenium.py
"""

## Run selenium and chrome driver to scrape data from cloudbytes.dev
import time
import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import traceback
from datetime import datetime 


#timestamp
dt = datetime.now()
waitTime = 2

## Setup chrome options
chrome_options = Options()
#chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--start-maximized") # GUI is On
chrome_options.add_argument("--no-sandbox")

# Set path to chromedriver as per your configuration
homedir = os.path.expanduser("~")
webdriver_service = Service(f"{homedir}/chromedriver/stable/chromedriver")

# Choose Chrome Browser
browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)
#browser.set_window_size(800,600)
# Get page
browser.get("https://fibeigreetings.com/")



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


############################### LOG IN AND REGISTRATION ############################

def LoginRegistration():
    print("Testing Login Page")
    login = browser.find_element(By.CLASS_NAME,"mat-button-wrapper").click()
    print("login button clicked")
    print("***************login test*************")
    time.sleep(waitTime)

    
    print("testing email inputs")
    e_mail = browser.find_element(By.ID, "mat-input-0")
    passWORD = browser.find_element(By.ID, "mat-input-1")
    
    test_emails = ['jeth.fifibuy@gmail.com', 'User2', '12352346534567', 'jeth.fifibuy@gmail.com']
    test_Login_passWords = ['1', '1234', '1234534562435', 'Fibei123']
    browser.find_element(By.CSS_SELECTOR, 'button.mat-ripple.mat-icon-button.cdk-focused.cdk-mouse-focused').click() #password visibility

    for test_mail in test_emails:
        e_mail.clear()
        e_mail.send_keys(test_mail)
        time.sleep(waitTime)

        for test_Login_passWord in test_Login_passWords:
            passWORD.clear()
            passWORD.send_keys(test_Login_passWord)
            print("\ntesting username: "+test_mail)
            print("testing password: "+test_Login_passWord)
            time.sleep(waitTime)
            
            try:
                browser.find_element(By.CSS_SELECTOR,'button.mat-focus-indicator.space-top.ng-tns-c192-1.mat-raised-button.mat-button-base.ng-trigger.ng-trigger-animate.mat-primary.mat-button-disabled').click()
                print("Log in button is NOT clickable")
            except:
                #traceback.print_exc()
                print("Log in button is clickable")
    
    print("***************login test end*************")

    print("\n****************Testing Register***************")
    #REGISTER BUTTONS
    browser.find_element(By.CSS_SELECTOR,"div#mat-tab-label-0-1").click() #clicks the register button
    regName = WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.ID, "mat-input-2"))) #finds the name textbox
    regEmail = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/app-login/div/mat-card-content/ngx-auth-firebaseui/mat-tab-group/div/mat-tab-body[2]/div/mat-card/mat-card-content/form/div/mat-form-field[2]/div/div[1]/div[1]/input")
    regPasswd = browser.find_element(By.NAME, "password")

    #REGISTER TEST LIST
    test_regNames = [' ', 'juan1', 'juan!', ' ']
    test_regEmails = ['jeth.fifibuy@gmail.com', 'User2', 'User3@gmail.com', 'jeth.fifibuy@gmail.com']
    test_regPasswds = ['Fibei123', '1234', '1234534562435', 'Fibei123']
    browser.find_element(By.XPATH, '//*[@id="mat-tab-content-0-1"]/div/mat-card/mat-card-content/form/div/div/mat-form-field/div/div[1]/div[2]/mat-pass-toggle-visibility/button/mat-icon').click()

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
                    browser.find_element(By.CSS_SELECTOR, 'button.mat-focus-indicator.ng-tns-c192-1.mat-raised-button.mat-button-base.ng-trigger.ng-trigger-animate.mat-primary.mat-button-disabled').click()
                    print("Register button is NOT clickable")
                except:
                    #traceback.print_exc()
                    print("Register button is clickable")

    print("****************Testing Register END***************")
    try:
        time.sleep(waitTime)
        WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button.mat-focus-indicator.mat-button.mat-button-base"))).click()
        print("---->exit button clicked")
    except:
        print("Skipping exit button")

    browser.find_element(By.LINK_TEXT, 'Home').click()
####################################################################################

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


###################################   testing banner ################################
def banner():
    print("\n***********Testing 1st banner**************")
    time.sleep(waitTime)
    browser.find_element(By.LINK_TEXT, 'Home').click()
    time.sleep(waitTime)
    browser.find_element(By.XPATH, '//*[@id="tabsSection"]/app-tabs/ion-tabs/div/ion-router-outlet/app-home/ion-content/section/div/div[1]/div[1]/a/img').click()
    print("---->brithday gifts banner clicked")
    time.sleep(waitTime)
    browser.find_element(By.LINK_TEXT, 'Home').click()

    browser.find_element(By.XPATH, '//*[@id="tabsSection"]/app-tabs/ion-tabs/div/ion-router-outlet/app-home/ion-content/section/div/div[1]/div[2]/a/img').click()
    print("---->brithday card banner clicked")
    time.sleep(waitTime)
    browser.find_element(By.LINK_TEXT, 'Home').click()

#####################################################################################


###################################  testing 2nd banner #############################
def banner_2nd():
    print("\n***********Testing 2nd banner**************")
    banner_text = ['ecards', 'cards with poetry', 'postcards', 'sign and send', 'stickers']
    banner_2nd_count = 0
    #//*[@id="tabsSection"]/app-tabs/ion-tabs/div/ion-router-outlet/app-home/ion-content/section/div/div[2]/div/div[{x}]/a/img
    for x in range (1,6,1):
        banner = f'//*[@id="tabsSection"]/app-tabs/ion-tabs/div/ion-router-outlet/app-home/ion-content/section/div/div[2]/div/div[{x}]/a/img'
        try:
            browser.find_element(By.XPATH, banner).click()
            print("---->clicked",banner_text[banner_2nd_count:x])
        except:
            Error(banner_text[banner_2nd_count:x])
        
        banner_2nd_count += 1
        time.sleep(waitTime)
        browser.find_element(By.LINK_TEXT, 'Home').click()
#######################################################################################

def banner_3rd():
    time.sleep(5)
    browser.find_element(By.LINK_TEXT, 'Home').click()
    print("\n***********Testing 3rd banner**************")
    for graduation_nav in range(17):
        browser.find_element(by=By.XPATH, value="//html").send_keys(Keys.TAB)
    
    try:
        browser.find_element(by=By.XPATH, value='//*[@id="tabsSection"]/app-tabs/ion-tabs/div/ion-router-outlet/app-home/ion-content/section/div/div[3]/div/a[1]/img').click()
        print("---->clicked graduation")
        time.sleep(waitTime)
    except:
        print("Graduation banner was not clicked")
        Error('Graduation banner')

    browser.find_element(By.LINK_TEXT, 'Home').click()

    for easter_nav in range(19):
        browser.find_element(by=By.XPATH, value="//html").send_keys(Keys.TAB)
    
    try:
        browser.find_element(By.XPATH, '//*[@id="tabsSection"]/app-tabs/ion-tabs/div/ion-router-outlet/app-home/ion-content/section/div/div[3]/div/a[2]/img').click()
        time.sleep(waitTime)
        print("---->easter cards clicked")
    except:
        print("---->easter cards not clicked")
        Error('easter cards')
    
    time.sleep(5)
    browser.find_element(By.LINK_TEXT, 'Home').click()

    for signSend_nav in range(19):
        browser.find_element(by=By.XPATH, value="//html").send_keys(Keys.TAB)
    
    for signSend_click in range(1,3,1):
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR, 'button.carousel-control-prev').click()
        print("---->Sign and Send carousel next clicked")

#########################################################################################

############################## testing Featured Category ################################
def FeaturedCateg():
    print("\n**************Testing Featured Categ**************")
    time.sleep(5)
    browser.find_element(By.LINK_TEXT, 'Home').click()
    #used to traverse to mother carousel
    '''
    for mother_nav in range(40):
        #time.sleep(1)
        browser.find_element(by=By.XPATH, value="//html").send_keys(Keys.TAB)
    '''

    carousel_lists = ['Mothers day', 'Anniversary day','Sympathy', 'Pet cards']
    carousel_count = 0
    for carousel_num in range(3,7,1):
        carousel_XPATH = f'//*[@id="tabsSection"]/app-tabs/ion-tabs/div/ion-router-outlet/app-home/ion-content/section/div/div[4]/div/div[{carousel_num}]/app-home-featured/div/div[2]/div/div/ngb-carousel/button[1]'
        
        if carousel_num == 3:
            for mother_nav in range(40):
                #time.sleep(1)
                browser.find_element(by=By.XPATH, value="//html").send_keys(Keys.TAB)
        else:
            for mother_nav in range(20):
                #time.sleep(1)
                browser.find_element(by=By.XPATH, value="//html").send_keys(Keys.TAB)

        for click in range(1,3,1):
            try:
                time.sleep(5)
                WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.XPATH, carousel_XPATH))).click()
                print("--->previous carousel button", carousel_lists[carousel_count:carousel_num-2], "clicked")
            except:
                Error(carousel_lists[carousel_count:carousel_num-2])

        carousel_count += 1
        
    """
    print("\nMother's day")

    for mother_click in range(1,3,1):
        time.sleep(5)
        WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="tabsSection"]/app-tabs/ion-tabs/div/ion-router-outlet/app-home/ion-content/section/div/div[4]/div/div[3]/app-home-featured/div/div[2]/div/div/ngb-carousel/button[1]'))).click()
        print("---->Mother's day carousel next clicked")

    #used to traverse to anniversary carousel
    for anniv_nav in range(20):
        #time.sleep(1)
        browser.find_element(by=By.XPATH, value="//html").send_keys(Keys.TAB)

    print("\nAnniversary day")

    for anniv_click in range(1,3,1):
        time.sleep(5)
        WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="tabsSection"]/app-tabs/ion-tabs/div/ion-router-outlet/app-home/ion-content/section/div/div[4]/div/div[4]/app-home-featured/div/div[2]/div/div/ngb-carousel/button[1]'))).click()
        print("---->Anniversary carousel next clicked")

    #used to traverse to sympathy carousel
    for sympathy_nav in range(20):
        #time.sleep(1)
        browser.find_element(by=By.XPATH, value="//html").send_keys(Keys.TAB)
    
    print("\nSympathy")

    for sympathy_click in range(1,3,1):
        time.sleep(5)
        WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="tabsSection"]/app-tabs/ion-tabs/div/ion-router-outlet/app-home/ion-content/section/div/div[4]/div/div[5]/app-home-featured/div/div[2]/div/div/ngb-carousel/button[1]'))).click()
        print("---->Sympathy carousel next clicked")
    
    #used to traverse to pet carousel
    for pet_nav in range(20):
        #time.sleep(1)
        browser.find_element(by=By.XPATH, value="//html").send_keys(Keys.TAB)
    
    print("\npetcards")

    for pet_click in range(1,3,1):
        time.sleep(5)
        WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="tabsSection"]/app-tabs/ion-tabs/div/ion-router-outlet/app-home/ion-content/section/div/div[4]/div/div[6]/app-home-featured/div/div[2]/div/div/ngb-carousel/button[1]'))).click()
        print("---->pet cards carousel next clicked")
    """
#########################################################################################  
    print("\n**************sign and send custom**************")
    for signAndSendCustom_nav in range(15):
        #time.sleep(1)
        browser.find_element(by=By.XPATH, value="//html").send_keys(Keys.TAB)
    try:
        WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="tabsSection"]/app-tabs/ion-tabs/div/ion-router-outlet/app-home/ion-content/section/div/div[5]/div[2]'))).click()
        time.sleep(5)
        print("---->sign and send cards custom clicked")
    except:
        Error('sign and send cards custom')

    browser.back()
    time.sleep(5)
    WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tabsSection"]/app-tabs/ion-tabs/div/ion-router-outlet/app-home/ion-content/section/div/div[5]/div[1]'))).click()

    for signAndSendprocess_nav in range(2):
        time.sleep(1)
        browser.find_element(by=By.XPATH, value="//html").send_keys(Keys.TAB)
    
    try:
        WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tabsSection"]/app-tabs/ion-tabs/div/ion-router-outlet/app-home/ion-content/section/div/div[5]/div[3]'))).click()
        time.sleep(5)
        print("---->sign and send learn more clicked")
    except:
        Error('sign and send learn more')

    browser.back()
    time.sleep(5)

#########################################################################################
    #using this instead of clicking on the html body and sending keys because that doesnt work
    WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tabsSection"]/app-tabs/ion-tabs/div/ion-router-outlet/app-home/ion-content/section/div/div[5]/div[1]'))).click()
   
    #using tabs to traverse through the webpage
    for MostBoughtItems_nav in range(3):
        time.sleep(1)
        browser.find_element(by=By.XPATH, value="//html").send_keys(Keys.TAB)
    
    print("\n************** testing most bought items on the list banner **************")
    for x in range(1,5,1):
        try:
            MostBought_Items = WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="tabsSection"]/app-tabs/ion-tabs/div/ion-router-outlet/app-home/ion-content/section/div/div[7]/app-home-bestseller/div/div[2]/div/div[{x}]/div/div/img')))
            MostBought_Items.click()
            time.sleep(3) #do not remove this, it will be too fast to grab the title of the card for some reason
            MostBought_Items_Title = browser.title #gets the title of the card
            print("----> category: ",MostBought_Items.get_attribute("title")," Card name: ", MostBought_Items_Title," clicked")
            time.sleep(3)
        except:
            Error(MostBought_Items_Title)

        browser.back()
    #clicking image to be able to navigate using tabs
    WebDriverWait(browser, 3).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tabsSection"]/app-tabs/ion-tabs/div/ion-router-outlet/app-home/ion-content/section/div/div[8]'))).click()

    #using tabs to traverse through the webpage
    for Gifts_nav in range(3):
        time.sleep(1)
        browser.find_element(by=By.XPATH, value="//html").send_keys(Keys.TAB)
    
    print("\n************** testing Gift items banner **************")
    for x in range(1,5,1):
        try:
            Gifts_Items = browser.find_element(By.XPATH, f'//*[@id="tabsSection"]/app-tabs/ion-tabs/div/ion-router-outlet/app-home/ion-content/section/div/div[9]/app-home-bestseller/div/div[2]/div/div[{x}]/div/div/img')
            Gifts_Items.click()
            time.sleep(3)
            Gifts_Items_title = browser.title
            print("----> category: ",Gifts_Items.get_attribute("title")," Card name: ", Gifts_Items_title," clicked")
            time.sleep(3)
        except:
            Error(Gifts_Items_title)
        
        browser.back()
########################################################################################

LoginRegistration()
NavBarTest()
banner()
banner_2nd()
banner_3rd()
FeaturedCateg()



print("\n...........exiting.............")
browser.quit()


