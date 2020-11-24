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
        self.browser = webdriver.Chrome(webdriver_location, chrome_options=options)

