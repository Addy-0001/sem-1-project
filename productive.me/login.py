from tkinter import * 
#import user data from models.py 
from models import *

#Make a login page 
class Login(Frame):
    def __init__(self, master, productive_db="productive.db"):
        super().__init__(master)
        self.master = master
        self.master.title("Login")
        self.master.geometry("500x500")
        self.master.resizable(False, False)
        self.master.configure(bg="white")
        self.create_widgets()

    def create_widgets(self):
        self.username_label = Label(self.master, text="Username:", bg="white")
        self.username_label.place(x=100, y=100)
        self.username_entry = Entry(self.master, width=30)
        self.username_entry.place(x=200, y=100)
        self.password_label = Label(self.master, text="Password:", bg="white")
        self.password_label.place(x=100, y=150)
        self.password_entry = Entry(self.master, width=30, show="*")
        self.password_entry.place(x=200, y=150)
        self.login_button = Button(self.master, text="Login", width=20, height=2, command=self.login)
        self.login_button.place(x=200, y=200)
        self.register_button = Button(self.master, text="Register", width=20, height=2, command=self.register)
        self.register_button.place(x=200, y=250)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user = User()
        if user.login(username, password):
            self.master.destroy()
            import home
            home.Home(username)
        else:
            self.password_entry.delete(0, END)
            self.password_entry.insert(0, "Incorrect password")

    #Make a register page according to productive.db 
    def register(self):
        self.master.destroy()
        register = Tk()
        Register(register)
        register.mainloop()

class Register(Frame):
    def __init__(self, master, productive_db="productive.db"):
        super().__init__(master)
        self.master = master
        self.master.title("Register")
        self.master.geometry("500x500")
        self.master.resizable(False, False)
        self.master.configure(bg="white")
        self.create_widgets()

    def create_widgets(self):
        self.username_label = Label(self.master, text="Username:", bg="white")
        self.username_label.place(x=100, y=100)
        self.username_entry = Entry(self.master, width=30)
        self.username_entry.place(x=200, y=100)
        self.password_label = Label(self.master, text="Password:", bg="white")
        self.password_label.place(x=100, y=150)
        self.password_entry = Entry(self.master, width=30, show="*")
        self.password_entry.place(x=200, y=150)
        self.email_label = Label(self.master, text="Email:", bg="white")
        self.email_label.place(x=100, y=200)
        self.email_entry = Entry(self.master, width=30)
        self.email_entry.place(x=200, y=200)
        self.first_name_label = Label(self.master, text="First name:", bg="white")
        self.first_name_label.place(x=100, y=250)
        self.first_name_entry = Entry(self.master, width=30)
        self.first_name_entry.place(x=200, y=250)
        self.last_name_label = Label(self.master, text="Last name:", bg="white")
        self.last_name_label.place(x=100, y=300)
        self.last_name_entry = Entry(self.master, width=30)
        self.last_name_entry.place(x=200, y=300)
        self.register_button = Button(self.master, text="Register", width=20, height=2, command=self.register)
        self.register_button.place(x=200, y=350)
        self.back_button = Button(self.master, text="Back", width=20, height=2, command=self.back)
        self.back_button.place(x=200, y=400)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        user = User()
        if user.create_user(username, password, email, first_name, last_name):
            self.master.destroy()
            import home
            home.Home(username)
        else:
            self.username_entry.delete(0, END)
            self.username_entry.insert(0, "Username taken")

def main():
    root = Tk()
    Login(root)
    root.mainloop()

if __name__ == "__main__":
    main()

# Compare this function from productive.me/models.py:
# def login(self, username, password):
#         user = self.select("users", f"username = '{username}'")