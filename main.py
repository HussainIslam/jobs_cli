
from lxml import html
import requests


from Support.selenium_utils import Browser
from Support.data_manager import DataManager


if __name__ == "__main__":
    browser = Browser("/usr/lib/chromium-browser/chromedriver").browser
    new_jobs = list()
    dm = DataManager(browser, new_jobs)