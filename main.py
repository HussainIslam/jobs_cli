from bs4 import BeautifulSoup
from lxml import html
import requests


URL = 'https://ca.indeed.com/jobs?q=full+stack+developer&l=Scarborough%2C+ON'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.findAll('div', class_='jobsearch-SerpJobCard')
counter = 0
for jobs in results:
    job_header = jobs.find('h2', class_='title').a 
    job_title = job_header['title']
    job_href = 'https://ca.indeed.com' +job_header['href']
    headers={
        "referer": URL,
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
    try:
        posting = requests.get(job_href, headers=headers)
    except Exception as e:
        print(e)
    company_name = jobs.find('div', class_='sjcl').div.find('span', class_='company')
    if company_name.a:
        company_name = company_name.a.getText()[1:]
    else:
        company_name = company_name.getText()[1:]
    print(f'{counter}: {job_title} - {company_name}')
    counter+=1