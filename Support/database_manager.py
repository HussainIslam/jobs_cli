import sqlite3
from datetime import date

class DBM:

    def __init__(self):
        try:
            self.con = sqlite3.connect('myjobs.db')
            print("[ Success ] Database is now connected")
        except Exception as e:
            print(e)

    def get_connection(self):
        return self.con

    def create_jobs_table(self):
        db_cursor = self.con.cursor()
        query_string = '''
        CREATE TABLE jobs(
            job_id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_name text NOT NULL,
            posting_position text NOT NULL,
            posting_number text,
            contact_email text,
            contact_phone text,
            city text NOT NULL,
            province text NOT NULL,
            posting_site text NOT NULL,
            search_position text NOT NULL,
            job_url BLOB NOT NULL,
            posting_date text NOT NULL DEFAULT CURRENT_DATE,
            access_date text NOT NULL
        )
        '''
        try:
            db_cursor.execute(query_string)
            self.con.commit()
            print("[ Success ] Database table 'jobs' was created.")
        except Exception as e:
            print(f"[ Error ] {e}")

    def delete_jobs_table(self):
        db_cursor = self.con.cursor()
        query_string = "DROP TABLE jobs"
        try:
            db_cursor.execute(query_string)
            self.con.commit()
            print("[ Success ] jobs table have been deleted")
        except Exception as e:
            print(f"[ Error ] {e}")

    def remove_all_data(self):
        db_cursor = self.con.cursor()
        query_string = "DELETE FROM jobs"
        try:
            db_cursor.execute(query_string)
            self.con.commit()
            print("[ Success ] Cleared all data from the table 'jobs'")
        except Exception as e:
            print(f"[ Error ] {e}")
    
    def insert_posting(self, posting, search_query):
        db_cursor = self.con.cursor()
        company_name = posting.company_name
        posting_position = posting.position
        posting_number = posting.posting_number
        contact_email = posting.contact_email
        contact_phone = posting.contact_phone
        city = posting.city
        province = posting.province
        posting_site = posting.posting_site
        search_position = search_query
        job_url = posting.job_url
        posting_date = posting.posting_date
        access_date = date.today()
        all_data = (company_name, posting_position, posting_number, 
                    contact_email, contact_phone, city, 
                    province, posting_site, search_position, 
                    job_url, posting_date, access_date)

        query_string = """INSERT INTO jobs 
        (company_name, posting_position, posting_number, contact_email, contact_phone,
        city, province, posting_site, search_position, job_url, posting_date, access_date) 
        values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        try:
            db_cursor.execute(query_string, all_data)
            self.con.commit()
        except Exception as e:
            print(e)

    def insert_multi_posting(self, postings:list, search_query):
        try:
            for posting in postings:
                self.insert_posting(posting, search_query)
            print("[ Success ] All job postings were inserted into database.")
        except Exception as e:
            print(e)