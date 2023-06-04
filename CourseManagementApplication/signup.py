from tkinter import *
import os
window = Tk()
window.geometry("1280x800")
window.configure(bg = "#EEEFF3")
window.title("Sign Up")
just = os.getcwd().replace("\\","\\\\")
pathset = just+"\\\\imagessignup\\\\"
logo = PhotoImage(file=pathset+"logo.png")
window.iconphoto(True, logo)


canvas = Canvas(
    window,
    bg = "#EEEFF3",
    height = 832,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    723.0,
    0.0,
    1280.0,
    832.0,
    fill="#3532A7",
    outline="",
)

canvas.create_text(
    774.0,
    52.0,
    anchor="nw",
    text="Create an Account",
    fill="#D8D5E6",
    font=("Poppins SemiBold", 33 * -1)
)

canvas.create_text(
    777.0,
    115.0,
    anchor="nw",
    text="Discover a world of limitless learning opportunities with our innovative \neducational app. Whether you're a student, educator, or lifelong learner,\nwe're here to empower you on your educational journey.",
    fill="#EAE7ED",
    font=("Poppins Regular", 15 * -1)
)
newto = Label(
    window,
    anchor="nw",
    text="New to VirtuEdu? Sign Up",
    cursor="hand2",
    font=("lexend deca", 15 * -1),
    
    
    

)
newto.place(x=930.0,y=615.0)
# canvas.create_text(
#     897.0,
#     611.0,
#     anchor="nw",
#     text="Already Have an Account? Sign In",
#     fill="#EAE7ED",
#     font=("Poppins Regular", 15 * -1)
# )

# button_image_1 = PhotoImage(
#     file=(pathset+"button_1.png"))
button_1 = Button(
    text="Create Your account",
    fg="Black",
    bg="white",
    font=("lexend deca", 16),
 
    command=lambda: print("Create Account button pressed"),

)
button_1.place(
    x=900.4287109375,
    y=550.0,
    width=260.66668701171875,
    height=50.0
)

image_image_1 = PhotoImage(
    file=(pathset+"image_1.png"))
image_1 = canvas.create_image(
    839.2857055664062,
    481.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=(pathset+"image_2.png"))
canvas.create_image(
    822.4287109375,
    228.0,
    image=image_image_2,
    anchor="nw"
)

canvas.create_text(
    866.3333740234375,
    471.0,
    anchor="nw",
    text="Password",
    fill="#EAE7ED",
    font=("OpenSans Bold", 14 * -1)
)

canvas.create_text(
    866.3333129882812,
    389.0,
    anchor="nw",
    text="Email Address",
    fill="#EAE7ED",
    font=("OpenSans Bold", 14 * -1)
)

canvas.create_text(
    866.3333740234375,
    307.0,
    anchor="nw",
    text="Phone Number",
    fill="#EAE7ED",
    font=("OpenSans Bold", 14 * -1)
)

    
canvas.create_text(
    866.3333740234375,
    234.0,
    anchor="nw",
    text="Full Name",
    fill="#EAE7ED",
    font=("OpenSans Bold", 14 * -1)
)

entry_image_1 = PhotoImage(
    file=(pathset+"entry_1.png"))
entry_bg_1 = canvas.create_image(
    1012.0238037109375,
    277.0,
    image=entry_image_1
)





def click(*args):
  fullname.delete(0, 'end')
  




fullname = Entry(
    bd=0,
    bg="#fff",
    fg="#000716",
    highlightthickness=0,
    font=("lexend deca", 14)
)

fullname.insert(0, "Enter Your Full Name")
fullname.bind("<Button-1>", click)


fullname.place(
    x=830.7619018554688,
    y=257.0,
    width=362.5238037109375,
    height=38.0
)

canvas.create_text(
    845.619140625,
    270.0,
    anchor="nw",
    text="Enter your full name",
    fill="#888888",
    font=("OpenSans Bold", 11 * -1)
)

entry_image_2 = PhotoImage(
    file=(pathset+"entry_2.png"))
entry_bg_2 = canvas.create_image(
    1009.2619018554688,
    353.0,
    image=entry_image_2
)

def phonenumberfunction(*args):
    phonenumber.delete(0, END)

phonenumber= Entry(
    bd=0,
    bg="#fff",
    fg="#000716",
    highlightthickness=0,
    font=("lexend deca", 14)
)
phonenumber.place(
    x=828.0,
    y=333.0,
    width=362.5238037109375,
    height=38.0
)
phonenumber.insert(0, "Enter Your Phone Number")
phonenumber.bind("<Button-1>", phonenumberfunction)
canvas.create_text(
    842.8570556640625,
    346.0,
    anchor="nw",
    text="Enter your phone number",
    fill="#888888",
    font=("OpenSans Bold", 11 * -1)
)

entry_image_3 = PhotoImage(
    file=(pathset+"entry_3.png"))
entry_bg_3 = canvas.create_image(
    1009.2619018554688,
    435.0,
    image=entry_image_3
)
def emailfunction(*args):
    email.delete(0, END)
email= Entry(
    bd=0,
    bg="#fff",
    fg="#000716",
    highlightthickness=0,
    font=("lexend deca", 14)
)
email.place(
    x=828.0,
    y=415.0,
    width=362.5238037109375,
    height=38.0
)
email.insert(0, "Enter Your Email Here")
email.bind("<Button-1>", emailfunction)
canvas.create_text(
    842.8570556640625,
    428.0,
    anchor="nw",
    text="Enter your email address",
    fill="#888888",
    font=("OpenSans Bold", 11 * -1)
)

entry_image_4 = PhotoImage(
    file=(pathset+"entry_4.png"))
entry_bg_4 = canvas.create_image(
    1009.2619018554688,
    514.0,
    image=entry_image_4
)
def passwordfunction(*args):
    password.delete(0, END)
eyeclose = PhotoImage(
    file=(pathset+"eyeclose.png"))
eyeopen = PhotoImage(
    file=(pathset+"eyeopen.png"))

def toggle_password():
    
    if password.cget('show') == '':
        password.config(show='*')
        # toggle_btn.config(text='Show Password')
    else:
        password.config(show='')
        eye.config(image=eyeclose,command=eyeopenfunction)
       
def eyeopenfunction():
    password.config(show='')
    eye.config(image=eyeopen, command=toggle_password)    
    password.config(show='*')      
        # toggle_btn.config(text='Hide Password')  
      
canvas.create_text(
    842.8570556640625,
    507.0,
    anchor="nw",
    text="Enter your password",
    fill="#888888",
    font=("OpenSans Bold", 11 * -1)
)    
password = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    show="*",
    font=("lexend deca", 14)
)
password.place(
    x=828.0,
    y=494.0,
    width=362.5238037109375,
    height=38.0
)
# password.insert(0, "Enter Your Password Here")
password.bind("<Button-1>", passwordfunction)


    


eye = Button(
    image=eyeopen,
    borderwidth=0,
    highlightthickness=0,
    command=toggle_password,
    relief="flat"
)

eye.place(
    x=1142.523681640625,
    y=502.0,
    width=33.14288330078125,
    height=24.0
)


image_image_3 = PhotoImage(
    file=(pathset+"image_3.png"))
image_3 = canvas.create_image(
    838.5238037109375,
    400.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=(pathset+"image_4.png"))
image_4 = canvas.create_image(
    839.5238037109375,
    319.0,
    image=image_image_4
)

button_image_3 = PhotoImage(
    file=(pathset+"button_3.png"))

button_3 = Button(
    image=button_image_3,

    command=lambda: print("button_3 clicked"),

)
button_3.place(
    x=890.0,
    y=724.0,
    width=250.0,
    height=50.0
)

image_image_5 = PhotoImage(
    file=(pathset+"image_5.png"))
image_5 = canvas.create_image(
    1001.0,
    679.0,
    image=image_image_5
)

canvas.create_text(
    1001.0,
    664.0,
    anchor="nw",
    text="OR",
    fill="#000000",
    font=("OpenSans Semibold", 22 * -1)
)

canvas.create_text(
    206.0,
    609.0,
    anchor="nw",
    text="VirtuEdu",
    fill="#3532A7",
    font=("Poppins SemiBold", 64 * -1)
)

canvas.create_text(
    225.0,
    688.0,
    anchor="nw",
    text="Learn Anywhere, Achieve Everywhere",
    fill="#646ECB",
    font=("Poppins Regular", 15 * -1)
)

image_image_6 = PhotoImage(
    file=(pathset+"image_6.png"))
image_6 = canvas.create_image(
    352.0,
    312.0,
    image=image_image_6
)

canvas.create_rectangle(
    326.0,
    552.0,
    371.0,
    563.0,
    fill="#3532A7",
    outline="")

canvas.create_rectangle(
    291.0,
    552.0,
    317.0,
    562.0,
    fill="#6E6DBF",
    outline="")

canvas.create_rectangle(
    379.0,
    552.0,
    405.0,
    562.0,
    fill="#6E6DBF",
    outline="")

window.resizable(False, False)
window.mainloop()


