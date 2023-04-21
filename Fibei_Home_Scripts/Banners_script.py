"""
# Filename: Banners_script.py
"""

import time
from browser_config import *
from test_configuration import *
from miscellanous_script import *



###################################   testing banner ################################
def banner():
    print("\n***********Testing 1st banner**************")
    time.sleep(waitTime)
    browser.find_element(By.LINK_TEXT, 'Home').click()
    time.sleep(waitTime)
    banner_1 = browser.find_element(By.XPATH, banner_1_XPATH)
    banner_1.click()
    banner_1_title = browser.title
    #cant do banner_1.getAttribute("variable") because there is nothing in the html file just an src image
    print("---->brithday gifts banner clicked", "\topened---->", banner_1_title)
    
    time.sleep(waitTime)
    browser.find_element(By.LINK_TEXT, 'Home').click()

    banner_2 = browser.find_element(By.XPATH, banner_2_XPATH)
    banner_2.click()
    banner_2_title = browser.title
    #cant do banner_1.getAttribute("variable") because there is nothing in the html file just an src image
    print("---->brithday gifts banner clicked", "\topened---->", banner_2_title)
    time.sleep(waitTime)
    browser.find_element(By.LINK_TEXT, 'Home').click()

#####################################################################################


###################################  testing 2nd banner #############################
def banner_2nd():
    print("\n***********Testing 2nd banner**************")
    banner_2nd_text = ['ecards', 'cards with poetry', 'postcards', 'sign and send', 'stickers']
    banner_2nd_count = 0
    
    for x in range (1,6,1):
        banner_2nd_XPATH = f'//*[@id="tabsSection"]/app-tabs/ion-tabs/div/ion-router-outlet/app-home/ion-content/section/div/div[2]/div/div[{x}]/a/img'
        try:
            banner_2nd_click = browser.find_element(By.XPATH, banner_2nd_XPATH)
            banner_2nd_click.click()
            banner_2nd_click.get_attribute("title")
            time.sleep(3)
            banner_2nd_title = browser.title
            #print("---->clicked",banner_text[banner_2nd_count:x], "opened---->", banner_2nd_title)
            print("---->clicked",banner_2nd_click.get_attribute("alt"), "\topened---->", banner_2nd_title)
            
        except:
            Error(banner_2nd_text[banner_2nd_count:x])
        
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
    
    carousel_count = 0
    for carousel_num in range(3,7,1):
        carousel_XPATH = f'//*[@id="tabsSection"]/app-tabs/ion-tabs/div/ion-router-outlet/app-home/ion-content/section/div/div[4]/div/div[{carousel_num}]/app-home-featured/div/div[2]/div/div/ngb-carousel/button[1]'
        #used to traverse to mother carousel
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