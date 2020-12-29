class Posting:

    def __init__(self, company_name, 
                        position, 
                        posting_number, 
                        contact_email,
                        contact_phone,
                        city,
                        province,
                        posting_site,
                        job_url,
                        posting_date):
        self.company_name = company_name
        self.position = position
        self.posting_number = posting_number
        self.contact_email = contact_email
        self.contact_phone = contact_phone
        self.city = city
        self.province = province
        self.posting_site = posting_site
        self.job_url = job_url
        self.posting_date = posting_date

    def __str__(self):
        return f'{self.company_name} - {self.position}'

