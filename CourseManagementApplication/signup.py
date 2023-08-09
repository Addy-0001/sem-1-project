from tkinter import *
import os
from pymongo import MongoClient
import subprocess
import sys
import re
window = Tk()
window.geometry("1280x800")
window.configure(bg = "#EEEFF3")
window.title("Sign Up")
just = os.getcwd().replace("\\","\\\\")
pathset = just+"\\\\imagessignup\\\\"
logo = PhotoImage(file=pathset+"logo.png")
window.iconphoto(True, logo)

client = MongoClient('mongodb://localhost:27017/')
db = client['users_data']
collection = db['authenticate']


# Set the initial transparency of the window
window.attributes('-alpha', 1.0)

import bcrypt


from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials

# Client ID and Client Secret from Google API project
CLIENT_ID = '808449259232-ordjm3193u7e2j150k3edu1gj105aqfj.apps.googleusercontent.com'
CLIENT_SECRET = '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'
SCOPES = ['openid', 'email', 'profile']

def authenticate_with_google():
    # Create the authorization flow
    flow = Flow.from_client_secrets_file(
        'client_secret.json',  # Path to your client_secret.json file
        scopes=SCOPES,
        redirect_uri='urn:ietf:wg:oauth:2.0:oob'
    )

    # Generate the authorization URL
    authorization_url, _ = flow.authorization_url(prompt='consent')

    # Open the authorization URL in a browser window
    os.system(f'start {authorization_url}')

    # Prompt the user to enter the authorization code
    authorization_code = input('Enter the authorization code: ')

    # Exchange the authorization code for credentials
    flow.fetch_token(authorization_response=authorization_code)

    # Get the user's profile information
    credentials = flow.credentials
    profile_info = get_profile_info(credentials)

    # Process the profile information or perform further actions
    print('Authentication successful!')
    print('Profile information:')
    print(f'Name: {profile_info["name"]}')
    print(f'Email: {profile_info["email"]}')
    # ...

def get_profile_info(credentials):
    # Use the credentials to get the user's profile information
    client = credentials.authorized_http()
    response = client.get('https://www.googleapis.com/oauth2/v3/userinfo')
    profile_info = response.json()
    return profile_info




def save_data():
    full_name = fullname.get()
    phone_number = phonenumber.get()
    email_address = email.get()
    password_value = password.get()

    # Validate that all fields are filled
    if not (full_name and phone_number and email_address and password_value):
        error_label.config(text='All fields are required')
        return
    
    if not re.match(r'^98\d{8}$', phone_number):
        error_label.config(text='Invalid phone number')
        return

    # Validate the email address format
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email_address):
        error_label.config(text='Invalid email address')
        return
    
    # Hash the password
    hashed_password = bcrypt.hashpw(password_value.encode('utf-8'), bcrypt.gensalt())

    data = {
        'full_name': full_name,
        'phone_number': phone_number,
        'email_address': email_address,
        'password': hashed_password.decode('utf-8')  # Store the hashed password as a string
    }

    collection.insert_one(data) 

    # Clear the entry boxes after saving the data
    fullname.delete(0, 'end')
    phonenumber.delete(0, 'end')
    email.delete(0, 'end')
    password.delete(0, 'end')

    # Destroy the current window
    window.destroy()

    # Open signin.py using subprocess
    subprocess.Popen([sys.executable, 'signin.py'])
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


def fade_out(window, duration):
    # Calculate the number of steps for the fade effect
    steps = int(duration / 10)
    alpha = window.attributes('-alpha')
    alpha_step = alpha / steps

    # Apply the fade effect
    for _ in range(steps):
        alpha -= alpha_step
        window.attributes('-alpha', alpha)
        window.update()
        window.after(10)  # Delay between each step

    # Open the signin.py file
    subprocess.Popen([sys.executable, 'signin.py'])

    # Destroy the current signup.py window
    window.destroy()

newto = Button(
    window,
    anchor="nw",
    text="New to VirtuEdu? Sign Up",
    cursor="hand2",
    font=("lexend deca", 15 * -1),
    command=lambda: fade_out(window, 200) 
    
    
    

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
 
    command=save_data,

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
# Create the error_label widget
error_label = Label(window, text='', fg="red")
error_label.place(x=830, y= 200)
                       

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
    relief="flat",
    cursor="hand2"
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

    command=authenticate_with_google,

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


