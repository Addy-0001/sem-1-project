from tkinter import *
from tkinter import ttk
import os,sys,subprocess
window = Tk()
window.geometry("1280x800")
window.configure(bg="#EEEFF3")

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
    relief="flat"
)
button_1.place(
    x=1155.0,
    y=17.0,
    width=56.0,
    height=56.0
)

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
    highlightthickness=0
)
entry_1.place(
    x=717.0,
    y=24.0,
    width=275.0,
    height=32.0
)

button_image_2 = PhotoImage(
    file=("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=976.0,
    y=33.0,
    width=18.333251953125,
    height=18.0
)

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
    relief="flat"
)
button_3.place(
    x=1085.0,
    y=24.0,
    width=28.694091796875,
    height=38.6826171875
)

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
    text="Terms &   Conditions",
    fill="#2A3AD3",
    font=("OpenSans Bold", 60 * -1)
)

canvas.create_rectangle(
    1616.0,
    2701.0,
    1716.0,
    2801.0,
    fill="#000000",
    outline="")

canvas.create_text(
    60.0,
    2852.0,
    anchor="nw",
    text="VirtuEdu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 32 * -1)
)

canvas.create_text(
    504.0,
    2867.0,
    anchor="nw",
    text="Menu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 24 * -1)
)

canvas.create_text(
    738.0,
    2867.0,
    anchor="nw",
    text="Menu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 24 * -1)
)

canvas.create_text(
    1008.0,
    2867.0,
    anchor="nw",
    text="Menu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 24 * -1)
)

canvas.create_text(
    86.0,
    2898.0,
    anchor="nw",
    text="Learn Anywhere, Achieve Everywhere",
    fill="#FFFFFF",
    font=("Poppins Regular", 11 * -1)
)

canvas.create_text(
    88.0,
    2923.0,
    anchor="nw",
    text="Our innovative online learning platform empowers students to pursue their educational goals from anywhere in the world. With flexible schedules and high-quality courses, we provide the tools and resources necessary for you to excel in your studies and succeed in any endeavor. Join our global community of learners and unlock your full potential with Virtu Edu.",
    fill="#FFFFFF",
    font=("Poppins Medium", 12 * -1)
)

button_image_4 = PhotoImage(
    file=("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=516.0,
    y=2910.0,
    width=30.0,
    height=15.0
)

button_image_5 = PhotoImage(
    file=("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=747.0,
    y=2907.0,
    width=112.0,
    height=15.0
)

button_image_6 = PhotoImage(
    file=("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=1021.0,
    y=2907.0,
    width=28.0,
    height=15.0
)

button_image_7 = PhotoImage(
    file=("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=1021.0,
    y=2932.0,
    width=16.0,
    height=15.0
)

button_image_8 = PhotoImage(
    file=("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=1022.0,
    y=2957.0,
    width=13.0,
    height=15.0
)

button_image_9 = PhotoImage(
    file=("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=1022.0,
    y=2982.0,
    width=98.0,
    height=15.0
)

button_image_10 = PhotoImage(
    file=("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=749.0,
    y=2932.0,
    width=69.0,
    height=15.0
)

button_image_11 = PhotoImage(
    file=("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
    relief="flat"
)
button_11.place(
    x=749.0,
    y=2957.0,
    width=41.0,
    height=15.0
)

button_image_12 = PhotoImage(
    file=("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_12 clicked"),
    relief="flat"
)
button_12.place(
    x=749.0,
    y=2982.0,
    width=56.0,
    height=15.0
)

button_image_13 = PhotoImage(
    file=("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_13 clicked"),
    relief="flat"
)
button_13.place(
    x=516.0,
    y=2935.0,
    width=46.0,
    height=15.0
)

button_image_14 = PhotoImage(
    file=("button_14.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_14 clicked"),
    relief="flat"
)
button_14.place(
    x=516.0,
    y=2960.0,
    width=42.0,
    height=15.0
)

button_image_15 = PhotoImage(
    file=("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_15 clicked"),
    relief="flat"
)
button_15.place(
    x=516.0,
    y=2985.0,
    width=33.0,
    height=15.0
)

button_image_16 = PhotoImage(
    file=("button_16.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_16 clicked"),
    relief="flat"
)
button_16.place(
    x=516.0,
    y=3010.0,
    width=39.0,
    height=15.0
)

button_image_17 = PhotoImage(
    file=("button_17.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_17 clicked"),
    relief="flat"
)
button_17.place(
    x=385.0,
    y=31.0,
    width=43.0,
    height=20.0
)

button_image_18 = PhotoImage(
    file=("button_18.png"))
button_18 = Button(
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_18 clicked"),
    relief="flat"
)
button_18.place(
    x=533.0,
    y=32.0,
    width=65.0,
    height=20.0
)

button_image_19 = PhotoImage(
    file=("button_19.png"))
button_19 = Button(
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_19 clicked"),
    relief="flat"
)
button_19.place(
    x=446.0,
    y=32.0,
    width=69.0,
    height=20.0
)

button_image_20 = PhotoImage(
    file=("button_20.png"))
button_20 = Button(
    image=button_image_20,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_20 clicked"),
    relief="flat"
)
button_20.place(
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
    2184.0,
    anchor="nw",
    text="All other terms and conditions as applicable under the Terms and Conditions of Us will be applicable\nto You and will be read along with this Privacy Policy.",
    fill="#000000",
    font=("Poppins Medium", 24 * -1)
)
window.resizable(False, False)
window.mainloop()
