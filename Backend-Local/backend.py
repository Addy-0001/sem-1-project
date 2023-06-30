import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                              (id INTEGER PRIMARY KEY AUTOINCREMENT,
                              name TEXT,
                              age INTEGER,
                              email TEXT)''')
        self.conn.commit()

    def insert_user(self, name, age, email):
        self.cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)",
                            (name, age, email))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()


def main():
    db_manager = DatabaseManager('data.db')

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    email = input("Enter your email: ")

    db_manager.insert_user(name, age, email)

    db_manager.close_connection()
    print("Data stored successfully!")


if __name__ == '__main__':
    main()
