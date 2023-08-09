from tkinter import *
from tkinter import ttk
import os,sys,subprocess, webbrowser
window = Tk()
window.geometry("1280x800")
window.configure(bg="#EEEFF3")
window.title("Terms & Conditions")
# Create a Canvas widget with a scrollbar
canvas = Canvas(window, height=600)
scrollbar = Scrollbar(window, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
canvas.pack(fill="both", expand=True)

def on_mousewheel(event):
    # Get the current scroll position
    current_pos = canvas.canvasy(0)

    # Get the top and bottom coordinates of the content
    top_pos = canvas.bbox("all")[1]
    bottom_pos = canvas.bbox("all")[3]

    # Calculate the available scroll distance
    scroll_distance = bottom_pos - top_pos - window.winfo_height()

    if event.delta <= 0 and current_pos <= scroll_distance:
        # Scroll down if there is more content to show
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
    elif event.delta >= 0 and current_pos >= 0:
        # Scroll up if not at the top
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

# Bind the mousewheel event to scroll the canvas
canvas.bind_all("<MouseWheel>", on_mousewheel)

# Create a frame inside the canvas to hold your content
frame = Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")
canvas.create_rectangle(
    0.0,
    4.0,
    1282.0,
    450.0,
    fill="#82B4FF",
    outline="")

canvas.create_text(
    40.0,
    20.0,
    anchor="nw",
    text="VirtuEdu",
    fill="#3532A7",
    font=("Poppins SemiBold", 25 * -1)
)

canvas.create_text(
    45.0,
    48.0,
    anchor="nw",
    text="Learn Anywhere, Achieve Everywhere",
    fill="#0018FF",
    font=("Poppins Regular", 10 * -1)
)
from tkinter import messagebox


    

def create_gui():
    
    messagebox.showinfo("Alert", "Feature is not available right now")

button_image_1 = PhotoImage(
    file=("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
    cursor="hand2",
    bg="#82B4FF"
)
canvas.create_window(1155,17,anchor="nw",window=button_1)

entry_image_1 = PhotoImage(
    file=("entry_1.png"))
entry_bg_1 = canvas.create_image(
    854.5,
    41.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    width=23,
    font=("lexend deca",15)
)
canvas.create_window(717,22,anchor="nw",window=entry_1)



button_image_2 = PhotoImage(
    file=("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat",
    cursor="hand2",
    bg="#fff"
)
canvas.create_window(976,24,anchor="nw",window=button_2)



canvas.create_text(
    723.5,
    30.5,
    anchor="nw",
    text="Search Courses",
    fill="#979797",
    font=("Poppins Light", 14 * -1)
)

button_image_3 = PhotoImage(
    file=("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat",
    cursor="hand2",
    bg="#82B4FF"
)
canvas.create_window(1085,24,anchor="nw",window=button_3)


image_image_1 = PhotoImage(
    file=("image_1.png"))
image_1 = canvas.create_image(
    359.0,
    285.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=("image_2.png"))
image_2 = canvas.create_image(
    974.0001220703125,
    244.2086181640625,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=("image_3.png"))
image_3 = canvas.create_image(
    752.0001220703125,
    304.6605224609375,
    image=image_image_3
)

canvas.create_text(
    738.0,
    214.0,
    anchor="nw",
    text="Terms &\n   Conditions",
    fill="#2A3AD3",
    font=("OpenSans Bold", 60 * -1)
)






button_image_17 = PhotoImage(
    file=("button_17.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_17 clicked"),
    relief="flat",
    cursor="hand2"
)
button_17.place(
    x=385.0,
    y=31.0,
    width=43.0,
    height=20.0
)

ioe = Button(
    # image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_18 clicked"),
    relief="flat",
    cursor="hand2"
)
ioe.place(
    x=533.0,
    y=32.0,
    width=65.0,
    height=20.0
)

tu = Button(
    # image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_19 clicked"),
    relief="flat",
    cursor="hand2"
)
tu.place(
    x=446.0,
    y=32.0,
    width=69.0,
    height=20.0
)

cu = Button(
    # image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_20 clicked"),
    relief="flat",
    cursor="hand2"
)
cu.place(
    x=610.0,
    y=32.0,
    width=83.0,
    height=23.0
)

canvas.create_text(
    60.0,
    490.0,
    anchor="nw",
    text="Terms and Conditions for VirtuEdu Effective date: [Insert Date]\n Please read these Terms and Conditions carefully before accessing or using VirtuEdu,\nour web application offering various courses. By accessing or using VirtuEdu, you agree to\nbe bound by these Terms and Conditions.\n1. User Responsibilities:You are responsible for ensuring the accuracy of the information you\nprovide during registration and for maintaining the confidentiality of your login credentials.\nYou agree to use VirtuEdu for lawful purposesand not to engage in any activities that may\ndisrupt the functionality or security of the application.\n2. Intellectual Property:All content provided through VirtuEdu, including course\nmaterials, videos, texts, and graphics, are protected by copyright and other intellectual\nproperty rights. You may access and use the content solely for personal, non-commercial\npurposes. Any unauthorized use, reproduction, or distribution of the content is strictly prohibited.\n3. Course Enrollment and Payments:Enrollment in our courses is subject to availability and\npayment of the required fees. We reserve the right to modify course offerings, fees, and any\nassociated policies without prior notice. All payments made through VirtuEdu are processed\nsecurely, and we do not store any payment information.\n4. Refund Policy:Refunds for course fees are subject to our refund policy, which will be clearly\ncommunicated during the enrollment process. Refunds, if applicable, will be issued according\nto the stated terms.\n5. Third-Party Content and Links.VirtuEdu may contain links to third-party websites or content\nthat are not owned or controlled by us. We do not endorse or assume any responsibility for\nthe content, accuracy, or practices of these third-party websites. Accessing third-party\ncontent is done at your own risk.\n6. Disclaimer of Warranty:VirtuEdu is provided on an as-in basis without any warranties\nexpress or implied. We make no representations or warranties regarding the accuracy,\ncompleteness, or reliability of the content provided. We disclaim any liability for any errors or\nomissions in the content or for any actions taken based on the information provided.\n7. Limitation of Liability:To the maximum extent permitted by law, VirtuEdu and its affiliates shall\nnot be liable for any direct, indirect, incidental, consequential, or punitive damages arising\nout of or in connection with your use of the application or the content provided.\n8. Modification and Termination:We reserve the right to modify, suspend, or terminate VirtuEdu\nor any part thereof, at any time without prior notice. We may also modify these Terms and\nConditions at any time, and the updated version will be effective upon posting.\n9. Governing LawThese Terms and Conditions shall be governed by and construed in\naccordance with the laws of [Insert Jurisdiction]. Any disputes arising out of or in connection\nwith these Terms and Conditions shall be subject to the exclusive jurisdiction of the courts of\n[Insert Jurisdiction].\nBy accessing or using VirtuEdu, you agree to comply with these Terms and Conditions.\nIf you do not agree with any part of these terms, please refrain from using our web application.",
    fill="#000000",
    font=("Poppins Light", 24 * -1)
)

canvas.create_text(
    42.0,
    1945.0,
    anchor="nw",
    text="All other terms and conditions as applicable under the Terms and Conditions of Us will be applicable\nto You and will be read along with this Privacy Policy.",
    fill="#000000",
    font=("Poppins Medium", 24 * -1)
)

# footer



canvas.create_text(
    62.0,
    2029.0,
    anchor="nw",
    text="VirtuEdu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 32 * -1)
)

canvas.create_text(
    506.0,
    2059.0,
    anchor="nw",
    text="Menu",
    fill="#fff",
    font=("Poppins SemiBold", 24 * -1)
)

canvas.create_text(
    740.0,
    2059.0,
    anchor="nw",
    text="Menu",
    fill="#fff",
    font=("Poppins SemiBold", 24 * -1)
)

canvas.create_text(
    1010.0,
    2059.0,
    anchor="nw",
    text="Menu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 24 * -1)
)

canvas.create_text(
    88.0,
    2069.0,
    anchor="nw",
    text="Learn Anywhere, Achieve Everywhere",
    fill="#FFFFFF",
    font=("Poppins Regular", 11 * -1)
)

canvas.create_text(
    50.0,
    2069.0,
    anchor="nw",
    text="Our innovative online learning platform empowers students\nto pursue their educational goals from anywhere in the world.\nWith flexible schedules and high-quality courses, we provide the\ntools and resources necessary for you to excel in your studies\nand succeed in any endeavor. Join our global community of\nlearners and unlock your full potential with Virtu Edu.",
    fill="#fff",
    font=("Poppins Medium", 12 * -1)
)


def Homes():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("PrivacyPolicy","homepage"))
        os.chdir(next_folder)

        # Run the gui.py file
        subprocess.Popen([sys.executable, 'gui.py'])

        window.destroy()

button_image_3 = PhotoImage(
    file=("button_3.png"))
button_3 = Button(
    # image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=Homes,
    relief="flat",
    cursor="hand2",
    text= "Home",
    bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    
)
canvas.create_window(506, 2109, anchor="nw", window=button_3)

# button_3.place(
#     x=518.0,
#     y=2615.0,
#     width=30.0,
#     height=15.0
# )


button_image_112 = PhotoImage(
    file=("button_3.png"))
button_112 = Button(
    # image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=create_gui,
    relief="flat",
    cursor="hand2",
    text= "About Us",
    bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    

)
canvas.create_window(506, 2139, anchor="nw", window=button_112)

def Courses():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("PrivacyPolicy","secondmainpage(courses_page)"))
        os.chdir(next_folder)

        # Run the gui.py file
        subprocess.Popen([sys.executable, 'gui.py'])

        window.destroy()


courses = PhotoImage(
    file=("button_3.png"))
coursesbtn = Button(
    # image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=Courses,
    relief="flat",
    cursor="hand2",
    text= "Courses",
    bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    

)
canvas.create_window(506, 2169, anchor="nw", window=coursesbtn)


events = PhotoImage(
    file=("button_3.png"))
eventbtn = Button(
    # image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=create_gui,
    relief="flat",
    cursor="hand2",
    text= "Events",
    bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    

)
canvas.create_window(506, 2199, anchor="nw", window=eventbtn)

def Routines():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("PrivacyPolicy","routines"))
        os.chdir(next_folder)

        # Run the gui.py file
        subprocess.Popen([sys.executable, 'gui.py'])

        window.destroy()

routinebtn = Button(
    # image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=Routines,
    relief="flat",
    cursor="hand2",
    text= "Routines",    
    bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    

)
canvas.create_window(506, 2229, anchor="nw", window=routinebtn)

def termsandcondition():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("PrivacyPolicy","termsandconditions"))
        os.chdir(next_folder)

        # Run the gui.py file
        subprocess.Popen([sys.executable, 'gui.py'])

        window.destroy()

termsandcon = Button(
    # image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=termsandcondition,
    relief="flat",
    cursor="hand2",
    text= "Terms and Conditions",  
    bg="#3532A7",
    fg="#fff",
    cursor="hand2"

    

)
canvas.create_window(740, 2109, anchor="nw", window=termsandcon)


def alert1():
    messagebox.showinfo("Alert", "You are on Same page now") 

privacy = Button(
    # image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=alert1,
    relief="flat",
    cursor="hand2",
    text= "Privacy Policy",
    bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    

)
canvas.create_window(740, 2139, anchor="nw", window=privacy)

def Support():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("PrivacyPolicy","support"))
        os.chdir(next_folder)

        # Run the gui.py file
        subprocess.Popen([sys.executable, 'gui.py'])

        window.destroy()

support = Button(
    # image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=Support,
    relief="flat",
    cursor="hand2",
    text= "Support",
    bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    

)
canvas.create_window(740, 2169, anchor="nw", window=support)

def Contact():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("PrivacyPolicy","contact_us"))
        os.chdir(next_folder)

        # Run the gui.py file
        subprocess.Popen([sys.executable, 'gui.py'])

        window.destroy()

contact = Button(
    # image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=Contact,
    relief="flat",
    cursor="hand2",
    text= "Contact Us",
    bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    

)
canvas.create_window(740, 2199, anchor="nw", window=contact)

cden = Button(
    # image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: webbrowser.open_new(r"http://www.cden.org.np"),
    relief="flat",
    cursor="hand2",
    text= "CDEN",
       bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    

)
canvas.create_window(1010, 2109, anchor="nw", window=cden)

ioe = Button(
    # image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: webbrowser.open_new(r"http://www.ioe.edu.np"),
    relief="flat",
    cursor="hand2",
    text= "IOE",
       bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    

)
canvas.create_window(1010, 2139, anchor="nw", window=ioe)

tu = Button(
    # image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: webbrowser.open_new(r"http://www.tu.edu.np"),
    relief="flat",
    cursor="hand2",
    text= "TU",
       bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    

)
canvas.create_window(1010, 2169, anchor="nw", window=tu)

cu = Button(
    # image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: webbrowser.open_new(r"http://www.coventry.ac.uk"),
    relief="flat",
    cursor="hand2",
    text= "Coventry University",
    bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    

)
canvas.create_window(1010, 2199, anchor="nw", window=cu)


canvas.create_rectangle(
    0.0,
    2027.0,
    1280.0,
    2266.0,
    fill="#3532A7",
    outline="")



# Update the scroll region to include the entire frame
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))
window.resizable(False, False)
window.mainloop()
