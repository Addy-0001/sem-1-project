from tkinter import *
from tkinter import ttk
import os
import sys
import subprocess, webbrowser
window = Tk()
window.geometry("1280x800")
window.configure(bg="#EEEFF3")

# Create a Canvas widget with a scrollbar
canvas = Canvas(window, height=600)
scrollbar = Scrollbar(window, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
canvas.pack(fill="both", expand=True)
from tkinter import messagebox


    

def create_gui():
    
    messagebox.showinfo("Alert", "Feature is not available right now")
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
    outline=""
)

canvas.create_text(
    30.0,
    20.0,
    anchor="nw",
    text="VirtuEdu",
    fill="#3532A7",
    font=("Poppins SemiBold", 25 * -1)
)
canvas.create_text(
    38.0,
    48.0,
    anchor="nw",
    text="Learn Anywhere, Achieve Everywhere",
    fill="#646ECB",
    font=("Poppins Regular", 6 * -1)
)

# canvas.create_window(1160, 31, window=button_1)

# button_image_1 = PhotoImage(
#     file=("profile.png")
# )
# button_1 = Button(
#     canvas,
#     image=button_image_1,
#     borderwidth=0,
#     highlightthickness=0,
#     command=lambda: print("Profile clicked"),
#     relief="flat",
    # cursor="hand2"
# )
# canvas.create_window(1160, 20, anchor="nw", window=button_1)
def routinesfile():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("designing_wala","routines"))
        os.chdir(next_folder)

        # Run the gui.py file
        subprocess.Popen([sys.executable, 'gui.py'])

        window.destroy()

def requestsfile():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("designing_wala","requests_notdone"))
        os.chdir(next_folder)

        # Run the gui.py file
        subprocess.Popen([sys.executable, 'gui.py'])

        window.destroy()

def computingfile():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("designing_wala","computing_wala"))
        os.chdir(next_folder)

        # Run the gui.py file
        subprocess.Popen([sys.executable, 'gui.py'])
      
        window.destroy()

def multimediafile():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("designing_wala","multimedia_wala"))
        os.chdir(next_folder)

        # Run the gui.py file
        subprocess.Popen([sys.executable, 'gui.py'])

        window.destroy()

def marketingfile():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("designing_wala","marketing_wala"))
        os.chdir(next_folder)

        # Run the gui.py file
        subprocess.Popen([sys.executable, 'gui.py'])

        window.destroy()


def languagefile():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("designing_wala","language_wala"))
        os.chdir(next_folder)

        # Run the gui.py file
        subprocess.Popen([sys.executable, 'gui.py'])

        window.destroy() 


def designingfile():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("homepage","designing_wala"))
        os.chdir(next_folder)

        # Run the gui.py file
        subprocess.Popen([sys.executable, 'gui.py'])

        window.destroy() 


def homefile():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("designing_wala", "homepage"))
        print(next_folder)
        os.chdir(next_folder)

        # Run the gui.py file
        subprocess.Popen([sys.executable, 'gui.py'])

        window.destroy() 



entry_image_1 = PhotoImage(
    file=("entry_1.png"))
entry_bg_1 = canvas.create_image(
    854.5,
    41.0,
    image=entry_image_1
)
entry_1 = Entry(
    canvas,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("lexend deca",16)
)
canvas.create_window(717, 16, anchor="nw", window=entry_1)



# entry_image_2 = PhotoImage(
#     file=("entry_2.png"))
# entry_bg_2 = canvas.create_image(
#     858.5,
#     50.0,
#     image=entry_image_2
# )
# entry_2 = Text(
#     bd=0,
#     bg="black",
#     fg="#000716",
#     highlightthickness=0
# )
# entry_2.place(
#     x=723.5,
#     y=30.5,
#     width=270.0,
#     height=19.0
# )

button_image_2 = PhotoImage(
    file=("notification.png"))
button_2 = Button(
    canvas,
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=create_gui,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(1100, 31.615699768066406, anchor="nw", window=button_2)
# button_2.place(
#     x=1100.0,
#     y=31.615699768066406,
#     width=29.694091796875,
#     height=29.550003051757812
# )
def buildfile():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("designing_wala","build"))
        os.chdir(next_folder)

        # Run the gui.py file
        subprocess.Popen([sys.executable, 'gui.py'])

        window.destroy()
button_image_3 = PhotoImage(
    file=("home.png"))
button_3 = Button(
    canvas,
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=buildfile,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(388, 31, anchor="nw", window=button_3)

# button_3.place(
#     x=388.0,
#     y=31.0,
#     width=61.0,
#     height=28.0
# )

button_image_4 = PhotoImage(
    file=("routines.png"))
button_4 = Button(
    canvas,
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=routinesfile,
    relief="flat",
    cursor="hand2",
  
)
canvas.create_window(546, 34, anchor="nw", window=button_4)

# button_4.place(
#     x=546.0,
#     y=34.0,
#     width=65.0,
#     height=20.0
# )

button_image_5 = PhotoImage(
    file=("requests.png"))
button_5 = Button(
    canvas,
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=requestsfile,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(628, 31, anchor="nw", window=button_5)

# button_5.place(
#     x=628.0,
#     y=31.0,
#     width=65.0,
#     height=20.0
# )

button_image_6 = PhotoImage(
    file=("courses.png"))
button_6 = Button(
    canvas,
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Course Button Clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(459, 28, anchor="nw", window=button_6)

# button_6.place(
#     x=459.0,
#     y=28.0,
#     width=69.0,
#     height=30.0
# )

button_image_1 = PhotoImage(
    file=("profile.png"))
button_1 = Button(
    canvas,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=create_gui,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(1160, 20, anchor="nw", window=button_1)
#nav bar ended 
image_image_1 = PhotoImage(
    file=("image_1.png"))
image_1 = canvas.create_image(
    761.0,
    342.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=("image_2.png"))
image_2 = canvas.create_image(
    200.0,
    300.21270751953125,
    image=image_image_2
)

# canvas.create_rectangle(
#     90.0,
#     113.2740478515625,
#     416.9385986328125,
#     326.894775390625,
#     fill="#000000",
#     outline="")

button_image_7 = PhotoImage(
    file=("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=computingfile,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(400, 457, anchor="nw", window=button_7)

# button_7.place(
#     x=400.0,
#     y=457.0,
#     width=114.0,
#     height=35.0
# )

button_image_8 = PhotoImage(
    file=("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=homefile,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(260, 456, anchor="nw", window=button_8)

# button_8.place(
#     x=260.0,
#     y=456.0,
#     width=121.0,
#     height=35.0
# )

button_image_9 = PhotoImage(
    file=("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=multimediafile,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(526, 457, anchor="nw", window=button_9)

# button_9.place(
#     x=526.0,
#     y=457.0,
#     width=115.0,
#     height=35.0
# )

button_image_10 = PhotoImage(
    file=("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(660, 457, anchor="nw", window=button_10)

# button_10.place(
#     x=660.0,
#     y=457.0,
#     width=106.0,
#     height=35.0
# )

button_image_11 = PhotoImage(
    file=("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=languagefile,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(785, 457, anchor="nw", window=button_11)

# button_11.place(
#     x=785.0,
#     y=457.0,
#     width=121.0,
#     height=35.0
# )

button_image_12 = PhotoImage(
    file=("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=marketingfile,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(925, 457, anchor="nw", window=button_12)

# button_12.place(
#     x=925.0,
#     y=457.0,
#     width=121.0,
#     height=35.0
# )

canvas.create_text(
    730.0,
    170.0,
    anchor="nw",
    text="Designing\nCourses",
    fill="#646ECB",
    font=("OpenSans Bold", 60 * -1)
)

canvas.create_text(
    793.0,
    300.0,
    anchor="nw",
    text="Unlock your potential with our transformative courses.",
    fill="#0018FF",
    font=("Poppins Regular", 15 * -1)
)

canvas.create_rectangle(
    94.0,
    531.0,
    336.0,
    775.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    94.0,
    828.0,
    336.0,
    1072.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    388.0,
    531.0,
    630.0,
    775.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    388.0,
    828.0,
    630.0,
    1072.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    691.0,
    531.0,
    933.0,
    775.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    691.0,
    828.0,
    933.0,
    1072.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    987.0,
    533.0,
    1229.0,
    777.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    987.0,
    830.0,
    1229.0,
    1074.0,
    fill="#FFFFFF",
    outline="")

image_image_3 = PhotoImage(
    file=("image_3.png"))
image_3 = canvas.create_image(
    215.0,
    593.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=("image_4.png"))
image_4 = canvas.create_image(
    215.0,
    890.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=("image_5.png"))
image_5 = canvas.create_image(
    509.0,
    593.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=("image_6.png"))
image_6 = canvas.create_image(
    509.0,
    890.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=("image_7.png"))
image_7 = canvas.create_image(
    812.0,
    593.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=("image_8.png"))
image_8 = canvas.create_image(
    812.0,
    890.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=("image_9.png"))
image_9 = canvas.create_image(
    1108.0,
    595.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=("image_10.png"))
image_10 = canvas.create_image(
    1108.0,
    892.0,
    image=image_image_10
)

canvas.create_text(
    107.0,
    691.731689453125,
    anchor="nw",
    text="Graphic Design Specialization ",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    107.0,
    988.731689453125,
    anchor="nw",
    text="UX Design Course",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    401.0,
    691.731689453125,
    anchor="nw",
    text="Web Design for Beginners",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    401.0,
    988.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    704.0,
    691.731689453125,
    anchor="nw",
    text="Interior Design Course",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    704.0,
    988.731689453125,
    anchor="nw",
    text="Fashion Design Course",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    1000.0,
    693.731689453125,
    anchor="nw",
    text="Digital Illustration Course",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    1000.0,
    990.731689453125,
    anchor="nw",
    text="Motion Graphics Course",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

button_image_13 = PhotoImage(
    file=("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_13 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(107, 661, anchor="nw", window=button_13)

# button_13.place(
#     x=107.0,
#     y=661.12548828125,
#     width=87.0,
#     height=11.9024658203125
# )

button_image_14 = PhotoImage(
    file=("button_14.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_14 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(107, 958, anchor="nw", window=button_14)



button_image_15 = PhotoImage(
    file=("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_15 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(401, 661, anchor="nw", window=button_15)



button_image_16 = PhotoImage(
    file=("button_16.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_16 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(401, 958, anchor="nw", window=button_16)



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
canvas.create_window(107, 661, anchor="nw", window=button_17)

 

button_image_18 = PhotoImage(
    file=("button_18.png"))
button_18 = Button(
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_18 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(704, 958, anchor="nw", window=button_18)

 

button_image_19 = PhotoImage(
    file=("button_19.png"))
button_19 = Button(
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_19 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(1000, 663, anchor="nw", window=button_19)

 

button_image_20 = PhotoImage(
    file=("button_20.png"))
button_20 = Button(
    image=button_image_20,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_20 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(1000, 960, anchor="nw", window=button_20)

 

 

image_image_12 = PhotoImage(
    file=("image_12.png"))
image_12 = canvas.create_image(
    215.0,
    980.8292236328125,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=("image_13.png"))
image_13 = canvas.create_image(
    509.0,
    683.8292236328125,
    image=image_image_13
)

image_image_14 = PhotoImage(
    file=("image_14.png"))
image_14 = canvas.create_image(
    509.0,
    980.8292236328125,
    image=image_image_14
)

image_image_15 = PhotoImage(
    file=("image_15.png"))
image_15 = canvas.create_image(
    812.0,
    683.8292236328125,
    image=image_image_15
)

image_image_16 = PhotoImage(
    file=("image_16.png"))
image_16 = canvas.create_image(
    812.0,
    980.8292236328125,
    image=image_image_16
)

image_image_17 = PhotoImage(
    file=("image_17.png"))
image_17 = canvas.create_image(
    1108.0,
    685.8292236328125,
    image=image_image_17
)

image_image_18 = PhotoImage(
    file=("image_18.png"))
image_18 = canvas.create_image(
    1108.0,
    982.8292236328125,
    image=image_image_18
)

button_image_21 = PhotoImage(
    file=("button_21.png"))
button_21 = Button(
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_21 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(108, 747, anchor="nw", window=button_21)

 

button_image_22 = PhotoImage(
    file=("button_22.png"))
button_22 = Button(
    image=button_image_22,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_22 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(108, 1044, anchor="nw", window=button_22)

 

button_image_23 = PhotoImage(
    file=("button_23.png"))
button_23 = Button(
    image=button_image_23,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_23 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(402, 747, anchor="nw", window=button_23)

 

button_image_24 = PhotoImage(
    file=("button_24.png"))
button_24 = Button(
    image=button_image_24,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_24 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(402, 1044, anchor="nw", window=button_24)

 

button_image_25 = PhotoImage(
    file=("button_25.png"))
button_25 = Button(
    image=button_image_25,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_25 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(705, 747, anchor="nw", window=button_25)

 

button_image_26 = PhotoImage(
    file=("button_26.png"))
button_26 = Button(
    image=button_image_26,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_26 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(705, 1044, anchor="nw", window=button_26)

 

button_image_27 = PhotoImage(
    file=("button_27.png"))
button_27 = Button(
    image=button_image_27,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_27 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(1001, 749, anchor="nw", window=button_27)

 

button_image_28 = PhotoImage(
    file=("button_28.png"))
button_28 = Button(
    image=button_image_28,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_28 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(1001, 1046, anchor="nw", window=button_28)

 

canvas.create_text(
    107.0,
    708.0,
    anchor="nw",
    text="Whether you're a budding designer or seeking to enhance your\ndesign skills, this course provides an immersive journey into\nthe world of visual aesthetics, digital tools, and design principles.",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_text(
    107.0,
    1005.0,
    anchor="nw",
    text="Whether you're a budding designer or seeking to enhance your\ndesign skills, this course provides an immersive journey into\nthe world of visual aesthetics, digital tools, and design principles.",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_text(
    401.0,
    708.0,
    anchor="nw",
    text="Whether you're a budding designer or seeking to enhance your\ndesign skills, this course provides an immersive journey into\nthe world of visual aesthetics, digital tools, and design principles.",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_text(
    401.0,
    1005.0,
    anchor="nw",
    text="Whether you're a budding designer or seeking to enhance your\ndesign skills, this course provides an immersive journey into\nthe world of visual aesthetics, digital tools, and design principles.",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_text(
    704.0,
    708.0,
    anchor="nw",
    text="Whether you're a budding designer or seeking to enhance your\ndesign skills, this course provides an immersive journey into\nthe world of visual aesthetics, digital tools, and design principles.",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_text(
    704.0,
    1005.0,
    anchor="nw",
    text="Whether you're a budding designer or seeking to enhance your\ndesign skills, this course provides an immersive journey into\nthe world of visual aesthetics, digital tools, and design principles.",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_text(
    1000.0,
    710.0,
    anchor="nw",
    text="Whether you're a budding designer or seeking to enhance your\ndesign skills, this course provides an immersive journey into\nthe world of visual aesthetics, digital tools, and design principles.",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_text(
    1000.0,
    1007.0,
    anchor="nw",
    text="Whether you're a budding designer or seeking to enhance your\ndesign skills, this course provides an immersive journey into\nthe world of visual aesthetics, digital tools, and design principles.",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_rectangle(
    0.0,
    1189.0,
    1280.0,
    1455.0,
    fill="#3532A7",
    outline="")


#NEw Footer



canvas.create_text(
    31.0,
    1224.0,
    anchor="nw",
    text="VirtuEdu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 32 * -1)
)

canvas.create_text(
   471.0,
    1223.0,
    anchor="nw",
    text="Menu",
    fill="#fff",
    font=("Poppins SemiBold", 24 * -1)
)

canvas.create_text(
    705.0,
    1223.0,
    anchor="nw",
    text="Menu",
    fill="#fff",
    font=("Poppins SemiBold", 24 * -1)
)

canvas.create_text(
    975.0,
    1223.0,
    anchor="nw",
    text="Menu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 24 * -1)
)

canvas.create_text(
    53.0,
    1266.0,
    anchor="nw",
    text="Learn Anywhere, Achieve Everywhere",
    fill="#FFFFFF",
    font=("Poppins Regular", 11 * -1)
)

canvas.create_text(
    53.0,
    1291.0,
    anchor="nw",
    text="Our innovative online learning platform empowers students\nto pursue their educational goals from anywhere in the world.\nWith flexible schedules and high-quality courses, we provide the\ntools and resources necessary for you to excel in your studies\nand succeed in any endeavor. Join our global community of\nlearners and unlock your full potential with Virtu Edu.",
    fill="#fff",
    font=("Poppins Medium", 12 * -1)
)

def alert1():
    messagebox.showinfo("Alert", "You are on Same page now") 

def privacypolicy():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("homepage", "PrivacyPolicy"))
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
    command=alert1,
    relief="flat",
    cursor="hand2",
    text= "Home",
    bg="#3532A7",
    fg="#fff",
    
    
)
canvas.create_window(506, 1830, anchor="nw", window=button_3)

# button_3.place(
#     x=518.0,
#     y=2615.0,
#     width=30.0,
#     height=15.0
# )

def home():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("PrivacyPolicy","homepage"))
        os.chdir(next_folder)

        # Run the gui.py file
        subprocess.Popen([sys.executable, 'gui.py'])

        window.destroy()

button_image_11 = PhotoImage(
    file=("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=home,
    relief="flat",
    cursor="hand2"
)
button_11.place(
    x=751.0,
    y=2687.0,
    width=56.0,
    height=15.0
)



button_image_12 = PhotoImage(
    file=("button_3.png"))
button_12 = Button(
    # image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=create_gui,
    relief="flat",
    cursor="hand2",
    text= "About Us",
    bg="#3532A7",
    fg="#fff",

    

)
canvas.create_window(506, 1860, anchor="nw", window=button_12)

def Courses():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("homepage","secondmainpage(courses_page)"))
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
  
    

)
canvas.create_window(506, 1890, anchor="nw", window=coursesbtn)


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

    

)
canvas.create_window(506, 1920, anchor="nw", window=eventbtn)

def Routines():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("homepage","routines"))
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
 
    

)
canvas.create_window(506, 1950, anchor="nw", window=routinebtn)

def termsandcondition():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("homepage","termsandconditions"))
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


    

)
canvas.create_window(740, 1830, anchor="nw", window=termsandcon)




privacy = Button(
    # image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=privacypolicy,
    relief="flat",
    cursor="hand2",
    text= "Privacy Policy",
    bg="#3532A7",
    fg="#fff",

    

)
canvas.create_window(740, 1860, anchor="nw", window=privacy)

def Support():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("homepage","support"))
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

    

)
canvas.create_window(740, 1890, anchor="nw", window=support)

def Contact():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("homepage","contact_us"))
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
 
    

)
canvas.create_window(740, 1920, anchor="nw", window=contact)

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
  
    

)
canvas.create_window(1010, 1830, anchor="nw", window=cden)

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

    

)
canvas.create_window(1010, 1860, anchor="nw", window=ioe)

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

    

)
canvas.create_window(1010, 1890, anchor="nw", window=tu)

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
   
    

)
canvas.create_window(1010, 1920, anchor="nw", window=cu)


# old footer
# canvas.create_text(
#     31.0,
#     1224.0,
#     anchor="nw",
#     text="VirtuEdu",
#     fill="#FFFFFF",
#     font=("Poppins SemiBold", 32 * -1)
# )

# canvas.create_text(
#     471.0,
#     1223.0,
#     anchor="nw",
#     text="Menu",
#     fill="#FFFFFF",
#     font=("Poppins SemiBold", 24 * -1)
# )

# canvas.create_text(
#     705.0,
#     1223.0,
#     anchor="nw",
#     text="Menu",
#     fill="#FFFFFF",
#     font=("Poppins SemiBold", 24 * -1)
# )

canvas.create_text(
    975.0,
    1223.0,
    anchor="nw",
    text="Menu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 24 * -1)
)

canvas.create_text(
    53.0,
    1266.0,
    anchor="nw",
    text="Learn Anywhere, Achieve Everywhere",
    fill="#FFFFFF",
    font=("Poppins Regular", 11 * -1)
)

canvas.create_text(
    53.0,
    1291.0,
    anchor="nw",
    text="\nour innovative online learning platform empowers students to pursue their educational goals from anywhere in the \nworld. With flexible schedules and high-quality courses, we provide the tools and resources necessary for you to excel \nin your studies and succeed in any endeavor. Join our global community of learners and unlock your full potential with \n Virtu Edu.",
    fill="#FFFFFF",
    font=("Poppins Medium", 12 * -1)
)

button_image_29 = PhotoImage(
    file=("button_29.png"))
button_29 = Button(
    image=button_image_29,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_29 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(483, 1266, anchor="nw", window=button_29)

 

button_image_30 = PhotoImage(
    file=("button_30.png"))
button_30 = Button(
    image=button_image_30,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_30 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(714, 1263, anchor="nw", window=button_30)

 

button_image_31 = PhotoImage(
    file=("button_31.png"))
button_31 = Button(
    image=button_image_31,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_31 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(988, 1263, anchor="nw", window=button_31)

 

button_image_32 = PhotoImage(
    file=("button_32.png"))
button_32 = Button(
    image=button_image_32,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_32 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(988, 1288, anchor="nw", window=button_32)

 

button_image_33 = PhotoImage(
    file=("button_33.png"))
button_33 = Button(
    image=button_image_33,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_33 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(989, 1313, anchor="nw", window=button_33)

 

button_image_34 = PhotoImage(
    file=("button_34.png"))
button_34 = Button(
    image=button_image_34,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_34 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(989, 1338, anchor="nw", window=button_34)

 

button_image_35 = PhotoImage(
    file=("button_35.png"))
button_35 = Button(
    image=button_image_35,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_35 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(716, 1288, anchor="nw", window=button_35)

 

button_image_36 = PhotoImage(
    file=("button_36.png"))
button_36 = Button(
    image=button_image_36,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_36 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(716, 1313, anchor="nw", window=button_36)



button_image_37 = PhotoImage(
    file=("button_37.png"))
button_37 = Button(
    image=button_image_37,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_37 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(716, 1338, anchor="nw", window=button_37)



button_image_38 = PhotoImage(
    file=("button_38.png"))
button_38 = Button(
    image=button_image_38,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_38 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(483, 1291, anchor="nw", window=button_38)

 

button_image_39 = PhotoImage(
    file=("button_39.png"))
button_39 = Button(
    image=button_image_39,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_39 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(483, 1316, anchor="nw", window=button_39)

 

button_image_40 = PhotoImage(
    file=("button_40.png"))
button_40 = Button(
    image=button_image_40,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_40 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(483, 1341, anchor="nw", window=button_40)



button_image_41 = PhotoImage(
    file=("button_41.png"))
button_41 = Button(
    image=button_image_41,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_41 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(483, 1366, anchor="nw", window=button_41)



button_image_42 = PhotoImage(
    file=("button_400.png"))
button_42 = Button(
    image=button_image_42,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_43 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(108, 747, anchor="nw", window=button_42)


button_image_43 = PhotoImage(
    file=("button_400.png"))
button_43 = Button(
    image=button_image_43,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_43 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(108, 1044, anchor="nw", window=button_43)

button_image_44 = PhotoImage(
    file=("button_400.png"))
button_44 = Button(
    image=button_image_44,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_44 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(402, 747, anchor="nw", window=button_44)


button_image_45 = PhotoImage(
    file=("button_400.png"))
button_45 = Button(
    image=button_image_45,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_45 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(402, 1044, anchor="nw", window=button_45)


button_image_46 = PhotoImage(
    file=("button_400.png"))
button_46 = Button(
    image=button_image_46,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_46 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(705, 747, anchor="nw", window=button_46)


button_image_47 = PhotoImage(
    file=("button_400.png"))
button_47 = Button(
    image=button_image_47,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_47 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(705, 1044, anchor="nw", window=button_47)


button_image_48 = PhotoImage(
    file=("button_400.png"))
button_48 = Button(
    image=button_image_48,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_48 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(1001, 749, anchor="nw", window=button_48)


button_image_49 = PhotoImage(
    file=("button_400.png"))
button_49 = Button(
    image=button_image_49,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_49 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(1001, 1046, anchor="nw", window=button_49)

button_image_50 = PhotoImage(
    file=("button_400.png"))
button_50 = Button(
    image=button_image_50,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_50 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(402, 1046, anchor="nw", window=button_50)

button_image_51 = PhotoImage(
    file=("button_400.png"))
button_51 = Button(
    image=button_image_51,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_51 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(108, 1046, anchor="nw", window=button_51)


button_image_52 = PhotoImage(
    file=("button_400.png"))
button_52 = Button(
    image=button_image_52,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_52 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(705, 1046, anchor="nw", window=button_52)

 
window.resizable(False, False)
window.mainloop()
