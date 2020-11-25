class IndeedPosting(object):
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
        return f'{self.company} - {self.position} - { self.post_link }'