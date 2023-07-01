import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def search_user(self, username, password):
        self.cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?",
                            (username, password))
        result = self.cursor.fetchall()
        return result

    def close_connection(self):
        self.conn.close()


def main():
    db_manager = DatabaseManager('userinfo.db')
    count = 0

    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        result = db_manager.search_user(username, password)

        if result:
            print("Login successful!")
            break
        else:
            print("Invalid username or password.")
            count += 1
            if count >= 3:
                print("Too many failed login attempts.")
                break
    db_manager.close_connection()


if __name__ == '__main__':
    main()
