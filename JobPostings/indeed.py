from JobPostings.Posting import Posting

class IndeedPosting(Posting):
    """
    docstring
    """
    def __init__(self, company_name, position, position_number):
        self.company_name = None
        self.position = None
        self.posting_number = None
        self.contact_email = None
        self.contact_phone = None
        self.city = None
        self.province = None
        self.posting_site = None
        self.job_url = None
        self.posting_date = None

    def __str__(self):
        return f'{self.company} - {self.position} - { self.post_link }'