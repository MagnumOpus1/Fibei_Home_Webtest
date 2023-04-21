from selenium.webdriver.chrome.options import Options as ChromeOptions

options = ChromeOptions()
options.platform_name = "Windows 11"
options.browser_version = "latest"
sauce_options = {}
caps = {}
caps['sauce:options']['build'] = 'selenium-build-TRR4J'
caps['sauce:options']['name'] = '<your test name>'
options.set_capability('sauce:options', sauce_options)


url = "https://oauth-jethoyt-8d27d:2ba4f64e-793f-4ecd-8e19-dda2f221ffe2@ondemand.eu-central-1.saucelabs.com:443/wd/hub"
driver = webdriver.Remote(command_executor=url, options=options)