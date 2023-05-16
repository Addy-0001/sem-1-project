import sqlite3
#connect the database to the app
conn = sqlite3.connect('productive.db')
c = conn.cursor()


# Make a user class that stores the name, email and password of a user
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

