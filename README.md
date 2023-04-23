# Fibei_Home_Webtest
This is my Project during my Internship
It is a selenium-based website automation for: https://fibeigreetings.com/

system requirements for running Selenium WebDriver and Chrome on WSL2:

Operating System:
* Windows 10 version 1903 or later with WSL2 enabled


Hardware:
* x86_64 architecture
* 4GB RAM (8GB recommended)
* At least 10GB of free disk space


Software:
* Ubuntu 18.04 LTS or later installed in WSL2
* Google Chrome installed in Ubuntu (version 89 or later recommended)
* Latest version of Selenium WebDriver for Python installed in Ubuntu

Optional:
* X server software installed on Windows, such as VcXsrv, for running GUI applications like Chrome


Note: You may need to adjust the system requirements based on the complexity of the web application you are testing.

The installation for the Selenium and Chrome-webdriver kindly run install-selenium.sh

For a more detailed instruction or if any error occured in installing WSL2, Selenium and Chome-webdriver here's the link: https://cloudbytes.dev/snippets/run-selenium-and-chrome-on-wsl2


# Known Errors
This combination will not work as intended and does not enable use of GUI, If GUI is enabled it will crash Chrome
Without GUI it passes Login, but fails during Registration error ( "method": "css selector" value: "mat-input-02" ) but in actuality for that line css selector was not used 

* google-chrome-stable-112.5615.49
* chromedriver-112.0.5615.49
* selenium-4.9.0

installed on the following directories
~/chromedriver/stable/chromedriver
even specifying location of chromedriver binary does not work

# STABLE
* google-chrome-stable-110.0.5481.117
* chromedriver-112.0.5615.49
* selenium-4.8.2
* Python 3.8.10


# Guides
Check your current chrome: https://chromedriver.storage.googleapis.com/LATEST_RELEASE

current implementation status of the WebDriver: https://shorturl.at/ftDR0

Know more about chrome versions: https://shorturl.at/luAQ4

Demo Video on youtube watch here: https://youtu.be/zgb4YGvDkWY

# TroubleShooting

For troubleshooting always throws 'Element is not clickable' error click here: https://chromedriver.chromium.org/help/clicking-issues#h.p_ID_32

ChromeDriver sometimes throws an 'Element is not clickable' error click here: https://chromedriver.chromium.org/help/clicking-issues#h.p_ID_71

ChromeDriver can't click a moving element such as an automatically moving carousel in Fibei website click here: https://chromedriver.chromium.org/help/clicking-issues#h.p_ID_77

