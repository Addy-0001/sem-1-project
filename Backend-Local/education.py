import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS courses
                              (id INTEGER PRIMARY KEY AUTOINCREMENT,
                              name TEXT,
                              description TEXT)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS modules
                              (id INTEGER PRIMARY KEY AUTOINCREMENT,
                              name TEXT,
                              description TEXT)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                              (id INTEGER PRIMARY KEY AUTOINCREMENT,
                              username TEXT,
                              course_id INTEGER,
                              password TEXT,
                              FOREIGN KEY (course_id) REFERENCES courses (id))''')

        self.conn.commit()

    def insert_course(self, name, description):
        self.cursor.execute("INSERT INTO courses (name, description) VALUES (?, ?)",
                            (name, description))
        self.conn.commit()

    def insert_module(self, name, description):
        self.cursor.execute("INSERT INTO modules (name, description) VALUES (?, ?)",
                            (name, description))
        self.conn.commit()

    def insert_user(self, username, course_id, password):
        self.cursor.execute("INSERT INTO users (username, course_id, password) VALUES (?, ?, ?)",
                            (username, course_id, password))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()


def main():
    db_name = 'app.db'
    db_manager = DatabaseManager(db_name)

    # Add Course
    course_name = input("Enter course name: ")
    course_description = input("Enter course description: ")
    db_manager.insert_course(course_name, course_description)
    course_id = db_manager.cursor.lastrowid

    # Add Module
    module_name = input("Enter module name: ")
    module_description = input("Enter module description: ")
    db_manager.insert_module(module_name, module_description)
    module_id = db_manager.cursor.lastrowid

    db_manager.close_connection()
    print("Data added successfully!")


if __name__ == '__main__':
    main()
