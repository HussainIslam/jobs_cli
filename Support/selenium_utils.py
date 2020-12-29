from selenium import webdriver

class Browser(object):
    """
    """
    def __init__(self, webdriver_location):
        self.webdriver_location = webdriver_location
        
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--remote-debugging-port=9222')
        self.browser = webdriver.Chrome(webdriver_location, chrome_options=options)

