import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                              (id INTEGER PRIMARY KEY AUTOINCREMENT,
                              username TEXT,
                              password TEXT)''')
        self.conn.commit()

    def insert_user(self, username, password):
        self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                            (username, password))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()


def main():
    db_manager = DatabaseManager('userinfo.db')

    username = input("Enter a username: ")
    password = input("Enter a password: ")

    db_manager.insert_user(username, password)

    db_manager.close_connection()
    print("Signup successful!")


if __name__ == '__main__':
    main()
