from lxml import html
import chromedriver_binary
import requests


from Support.selenium_utils import Browser
from Support.data_manager import DataManager
from Support.report_generate import ReportTextFile
from Support.database_manager import DBM

if __name__ == "__main__":
    browser = Browser(chromedriver_binary.chromedriver_filename).browser
    new_jobs = list()
    dm = DataManager(browser, new_jobs)
    db = DBM()
    db.create_jobs_table()
    #db.delete_jobs_table()
    db.insert_multi_posting(new_jobs, "Full Stack Developer")
    
    #ReportTextFile(new_jobs)