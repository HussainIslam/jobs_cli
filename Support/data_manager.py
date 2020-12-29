from bs4 import BeautifulSoup
from datetime import date

from JobPostings.Posting import Posting


class DataManager(object):
    """
    docstring
    """
    def __init__(self, browser, new_jobs):
        """
        docstring
        """
        self.browser = browser
        self.new_jobs = new_jobs
        self.fetch_data()

    def fetch_data(self):
        """
        docstring
        """
        self.scrap_indeed()
    
    def get_data(self):
        """
        docstring
        """
        pass

    def scrap_indeed(self):
        URL = 'https://ca.indeed.com/jobs?q=full+stack+developer&l=Scarborough%2C+ON'
        self.browser.get(URL)
        page = self.browser.page_source
        soup = BeautifulSoup(page, 'html.parser')
        results = soup.findAll('div', class_='jobsearch-SerpJobCard')
        for job in results:
            '''
            company_name, 
            position, 
            position_number, 
            contact_email,
            contact_phone,
            city,
            province,
            posting_site,
            job_url,
            posting_date
            '''
            # scrapping company name
            job_company = job.find('div', class_='sjcl').div.find('span', class_='company')
            if job_company.a:
                job_company = job_company.a.getText()[1:]
            else:
                job_company = job_company.getText()[1:]

            # scrapping job position
            job_header = job.find('h2', class_='title').a 
            position = job_header['title']

            # scrapping position_number
            position_number = None

            # scrapping contact_email
            contact_email = None

            # scrapping contact_phone
            contact_phone = None

            # Scrapping city and province
            job_location = job.find('div', class_='sjcl').select_one('.location').getText()
            city = None
            province = None
            comma_position = job_location.find(",")
            if comma_position > -1:
                city = job_location[:comma_position]
                province = job_location[comma_position+1:].strip()

            # posting_site
            posting_site = "indeed"

            # scrapping job_url
            job_url = 'https://ca.indeed.com' +job_header['href']
            
            # scrapping posting_date
            job_date = date.today().strftime("%d-%m-%Y")

            headers={
                "referer": URL,
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Max-Age': '3600',
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
            }
            
            new_job = Posting(job_company, position, position_number, contact_email, contact_phone, city, province, posting_site, job_url, job_date)
            self.new_jobs.append(new_job)
            

            #self.new_jobs.append(Posting(job_title, job_company, job_posting_link, job_date, job_location))