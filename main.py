from datetime import date
from bs4 import BeautifulSoup
from selenium import webdriver
from lxml import html
import requests

class JobPosting(object):
    """
    docstring
    """
    def __init__(self, position, company, post_link, date, location):
        self.position = position
        self.company = company
        self.post_link = post_link
        self.date = date
        self.location = location

    def __str__(self):
        return f'{self.company} - {self.position}'

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


if __name__ == "__main__":
    browser = Browser("/usr/lib/chromium-browser/chromedriver").browser

    URL = 'https://ca.indeed.com/jobs?q=full+stack+developer&l=Scarborough%2C+ON&fromage=1'
    browser.get(URL)
    page = browser.page_source
    soup = BeautifulSoup(page, 'html.parser')
    results = soup.findAll('div', class_='jobsearch-SerpJobCard')
    counter = 0
    for job in results:
        job_header = job.find('h2', class_='title').a 
        job_title = job_header['title']
        job_posting_link = 'https://ca.indeed.com' +job_header['href']
        job_date = date.today().strftime("%d-%m-%Y")
        headers={
            "referer": URL,
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }
        job_company = job.find('div', class_='sjcl').div.find('span', class_='company')
        if job_company.a:
            job_company = job_company.a.getText()[1:]
        else:
            job_company = job_company.getText()[1:]
        
        job_location = job.find('div', class_='sjcl').select_one('.location').getText()
        
        job_posting = JobPosting(job_title, job_company, job_posting_link, job_date, job_location)
            
        print(job_posting)
        # if company_name == 'Procom':
        #     print(job_location)
        counter+=1