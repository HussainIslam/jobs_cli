from datetime import date
from bs4 import BeautifulSoup
from lxml import html
import requests

from JobPostings.indeed import IndeedPosting
from Support.selenium_utils import Browser



if __name__ == "__main__":
    browser = Browser("/usr/lib/chromium-browser/chromedriver").browser
    new_jobs = list()

    URL = 'https://ca.indeed.com/jobs?q=full+stack+developer&l=Scarborough%2C+ON&fromage=1'
    browser.get(URL)
    page = browser.page_source
    soup = BeautifulSoup(page, 'html.parser')
    results = soup.findAll('div', class_='jobsearch-SerpJobCard')
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
        new_jobs.append(IndeedPosting(job_title, job_company, job_posting_link, job_date, job_location))
    [print(job) for job in new_jobs]