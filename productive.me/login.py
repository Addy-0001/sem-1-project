# from .models import * 
from tkinter import *
#create a login form that checks the database and allows login if the user is in the database
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #create a frame
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=0,y=0,height=700,width=1350)
        #create a label
        # self.img=Image.PhotoImage(file="images/login.jpg")
        # img=Label(Frame_login,image=self.img,bd=0).place(x=0,y=0)
        #create a label
        title=Label(Frame_login,text="Login Here",font=("Impact",35,"bold"),fg="#d77337",bg="white").place(x=90,y=100)
        #create a label
        desc=Label(Frame_login,text="Accountant Employee Login Area",font=("Goudy old style",15,"bold"),fg="#d25d17",bg="white").place(x=90,y=160)
        #create a label
        lbl_user=Label(Frame_login,text="Username",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=240)
        #create a entry
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=270,width=350,height=35)
        #create a label
        lbl_pass=Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=320)
        #create a entry
        self.txt_pass=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_pass.place(x=90,y=350,width=350,height=35)
        #create a button
        forget_btn=Button(Frame_login,text="Forget Password?",cursor="hand2",bg="white",fg="#d77337",bd=0,font=("times new roman",12)).place(x=90,y=390)
        #create a button
        login_btn=Button(Frame_login,text="Login",cursor="hand2",command=self.login,fg="white",bg="#d77337",font=("times new roman",20)).place(x=90,y = 430,width=180,height=40)
        #create a button
        register_btn=Button(Frame_login,text="Register New Account",cursor="hand2",command=self.register_window,fg="#d77337",bg="white",bd=0,font=("times new roman",12)).place(x=90,y=480)


#create a function to login
    def login(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txt_pass.get()!="123456" or self.txt_user.get()!="sagar":
            messagebox.showerror("Error","Invalid Username/Password",parent=self.root)
        else:
            messagebox.showinfo("Welcome",f"Welcome {self.txt_user.get()}\nYour Password:{self.txt_pass.get()}",parent=self.root)
    def register_window(self):
        self.root.destroy()
        import register

#create a register form that allows the user to create an account and stores it in the database


root=Tk()
obj=Login(root)
root.mainloop()
