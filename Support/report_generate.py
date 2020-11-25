class ReportTextFile(object):
    """
    docstring
    """
    def __init__(self, job_postings):
        """
        docstring
        """
        self.job_postings = job_postings
        output_file = open("Reports/postings.txt", "a+")
        [ output_file.write(str(job) + "\n") for job in self.job_postings ]