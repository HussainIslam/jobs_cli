import sqlite3

class DBM:

    def __init__(self):
        self.con = None

    def get_connection(self):
        try:
            self.con = sqlite3.connect('myjobs.db')
            print("[ Success ] Database is now connected")
            return self.con
        except Exception as e:
            print(e)

    
        