from tkinter import *

import os




window = Tk()
window.geometry("1280x800")
window.configure(bg = "#EEEFF3")
window.title("Sign In")
just = os.getcwd().replace("\\","\\\\")
pathset = just+"\\\\imagessignin\\\\"
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
    outline="")

canvas.create_text(
    185.0,
    614.0,
    anchor="nw",
    text="VirtuEdu",
    fill="#3532A7",
    font=("Poppins SemiBold", 64 * -1)
)

canvas.create_text(
    778.0,
    134.0,
    anchor="nw",
    text="Sign In",
    fill="#D8D5E6",
    font=("Poppins SemiBold", 33 * -1)
)

canvas.create_text(
    204.0,
    693.0,
    anchor="nw",
    text="Learn Anywhere, Achieve Everywhere",
    fill="#646ECB",
    font=("Poppins Regular", 15 * -1)
)

canvas.create_text(
    777.0,
    204.0,
    anchor="nw",
    text="Discover a world of limitless learning opportunities with our innovative \neducational app.  Whether you're a student, educator, or lifelong learner,\nwe're here to empower you on your educational journey.",
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
newto.place(x=910.0,y=590.0)



button_1 = Button(
    text="Sign In",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
    font=("lexend deca",20)

)
button_1.place(
    x=909.4287109375,
    y=504.0,
    width=195.0,
    height=45.0,

)

image_image_1 = PhotoImage(
    file=(pathset+"image_1.png"))
image_1 = canvas.create_image(
    834.2857055664062,
    418.0,
    image=image_image_1
)

canvas.create_text(
    861.3333129882812,
    326.0,
    anchor="nw",
    text="Email Address",
    fill="#EAE7ED",
    font=("lexend deca", 14 * -1)
)

canvas.create_text(
    861.3333129882812,
    408.0,
    anchor="nw",
    text="Password",
    fill="#EAE7ED",
    font=("Lexend deca", 14 * -1)
)

entry_image_1 = PhotoImage(
    file=(pathset+"entry_1.png"))
entry_bg_1 = canvas.create_image(
    1004.2619018554688,
    372.0,
    image=entry_image_1
)
def emailfunction(*args):
    email.delete(0, END)
email = Entry(
    bd=0,
    bg="#fff",
    fg="#000716",
    highlightthickness=0,
    font=("lexend deca",14)
    
)
email.place(
    x=823.0,
    y=352.0,
    width=362.5238037109375,
    height=38.0
)
email.insert(0, "Enter Your Email Here")
email.bind("<Button-1>", emailfunction)
canvas.create_text(
    837.8570556640625,
    365.0,
    anchor="nw",
    text="Enter your email address",
    fill="#888888",
    font=("OpenSans Bold", 11 * -1)
)

entry_image_2 = PhotoImage(
    file=(pathset+"entry_2.png"))
entry_bg_2 = canvas.create_image(
    1004.2619018554688,
    451.0,
    image=entry_image_2
)
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
password = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    show="*",
    font=("lexend deca",14)
    
)
password.place(
    x=823.0,
    y=431.0,
    width=362.5238037109375,
    height=38.0
)

canvas.create_text(
    837.8570556640625,
    444.0,
    anchor="nw",
    text="Enter your password",
    fill="#888888",
    font=("OpenSans Bold", 11 * -1)
)


eye = Button(
    image=eyeopen,
    borderwidth=0,
    highlightthickness=0,
    command=toggle_password,
    relief="flat"
)
eye.place(
    x=1137.523681640625,
    y=439.0,
    width=33.142822265625,
    height=24.0
)

image_image_2 = PhotoImage(
    file=(pathset+"image_2.png"))
image_2 = canvas.create_image(
    833.5238037109375,
    337.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=(pathset+"image_3.png"))
image_3 = canvas.create_image(
    331.0,
    317.0,
    image=image_image_3
)

button_image_3 = PhotoImage(
    file=(pathset+"button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=881.0,
    y=724.0,
    width=300.0,
    height=45.0,
    
)

image_image_4 = PhotoImage(
    file=(pathset+"image_4.png"))
image_4 = canvas.create_image(
    1001.0,
    658.0,
    image=image_image_4
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
    fill="#3532A7",
    outline="")

canvas.create_rectangle(
    379.0,
    552.0,
    405.0,
    562.0,
    fill="#3532A7",
    outline="")
window.resizable(False, False)
window.mainloop()
