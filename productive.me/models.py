from sqlite3 import * 

class Model:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
        self.conn.commit()

    def insert(self, table_name, columns, values):
        self.cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({values})")
        self.conn.commit()

    def select(self, table_name, columns, condition):
        self.cursor.execute(f"SELECT {columns} FROM {table_name} WHERE {condition}")
        return self.cursor.fetchall()

    def update(self, table_name, columns, condition):
        self.cursor.execute(f"UPDATE {table_name} SET {columns} WHERE {condition}")
        self.conn.commit()

    def delete(self, table_name, condition):
        self.cursor.execute(f"DELETE FROM {table_name} WHERE {condition}")
        self.conn.commit()

    def close(self):
        self.conn.close()

# Make a database table for users that contains the following columns:
# id, username, password, email, first_name, last_name, date_joined
class User(Model):
    def __init__(self, db_name):
        super().__init__(db_name)
        self.create_table("users", "id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, email TEXT, first_name TEXT, last_name TEXT, date_joined TEXT")

    def create_user(self, username, password, email, first_name, last_name, date_joined):
        self.insert("users", "username, password, email, first_name, last_name, date_joined", f"'{username}', '{password}', '{email}', '{first_name}', '{last_name}', '{date_joined}'")

    def get_user(self, username):
        return self.select("users", "*", f"username = '{username}'")

    def update_user(self, username, password, email, first_name, last_name):
        self.update("users", f"password = '{password}', email = '{email}', first_name = '{first_name}', last_name = '{last_name}'", f"username = '{username}'")

    def delete_user(self, username):
        self.delete("users", f"username = '{username}'")

# Make a database table for tasks that contains the following columns:
# id, user_id, title, description, date_created, date_due, date_completed
class Task(Model):
    def __init__(self, db_name):
        super().__init__(db_name)
        self.create_table("tasks", "id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, title TEXT, description TEXT, date_created TEXT, date_due TEXT, date_completed TEXT")

    def create_task(self, user_id, title, description, date_created, date_due):
        self.insert("tasks", "user_id, title, description, date_created, date_due", f"{user_id}, '{title}', '{description}', '{date_created}', '{date_due}'")

    def get_task(self, user_id, title):
        return self.select("tasks", "*", f"user_id = {user_id} AND title = '{title}'")

    def get_tasks(self, user_id):
        return self.select("tasks", "*", f"user_id = {user_id}")

    def update_task(self, user_id, title, description, date_due, date_completed):
        self.update("tasks", f"description = '{description}', date_due = '{date_due}', date_completed = '{date_completed}'", f"user_id = {user_id} AND title = '{title}'")

    def delete_task(self, user_id, title):
        self.delete("tasks", f"user_id = {user_id} AND title = '{title}'")

# Make a database table for notes that contains the following columns:
# id, user_id, title, description, date_created, date_updated
class Note(Model):
    def __init__(self, db_name):
        super().__init__(db_name)
        self.create_table("notes", "id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, title TEXT, description TEXT, date_created TEXT, date_updated TEXT")

    def create_note(self, user_id, title, description, date_created):
        self.insert("notes", "user_id, title, description, date_created", f"{user_id}, '{title}', '{description}', '{date_created}'")

    def get_note_by_title(self, user_id, title):
        return self.select("notes", "*", f"user_id = {user_id} AND title = '{title}'")

    def get_notes(self, user_id):
        return self.select("notes", "*", f"user_id = {user_id}")

    def update_note_by_title(self, user_id, title, description, date_updated):
        self.update("notes", f"description = '{description}', date_updated = '{date_updated}'", f"user_id = {user_id} AND title = '{title}'")

    def delete_note_by_title(self, user_id, title):
        self.delete("notes", f"user_id = {user_id} AND title = '{title}'")

#make a registration model 
class register(Model):
    def __init__(self, db_name):
        super().__init__(db_name)
        self.create_table("registration", "id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, email TEXT, first_name TEXT, last_name TEXT, date_joined TEXT")

    def create_registration(self, username, password, email, first_name, last_name, date_joined):
        self.insert("registration", "username, password, email, first_name, last_name, date_joined", f"'{username}', '{password}', '{email}', '{first_name}', '{last_name}', '{date_joined}'")

    def get_registration(self, username):
        return self.select("registration", "*", f"username = '{username}'")

    def update_registration(self, username, password, email, first_name, last_name):
        self.update("registration", f"password = '{password}', email = '{email}', first_name = '{first_name}', last_name = '{last_name}'", f"username = '{username}'")

    def delete_registration(self, username):
        self.delete("registration", f"username = '{username}'")

