import os
from datetime import date

class ReportTextFile(object):
    """
    docstring
    """
    def __init__(self, job_postings):
        """
        docstring
        """
        self.job_postings = job_postings
        location = os.getcwd()
        filename = f'job_postings_{date.today().strftime("%d_%m_%Y")}'
        output_file = open(f'./Reports/{filename}', "a+")
        [ output_file.write(str(job) + "\n") for job in self.job_postings ]