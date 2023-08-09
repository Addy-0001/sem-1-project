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

from tkinter import messagebox


    

def create_gui():
    
    messagebox.showinfo("Alert", "Feature is not available right now")


def homefile():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("requests_notdone","homepage"))
        os.chdir(next_folder)

        # Run the gui.py file
        subprocess.Popen([sys.executable, 'gui.py'])

        window.destroy()
def routinesfile():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("requests_notdone","routines"))
        os.chdir(next_folder)

        # Run the gui.py file
        subprocess.Popen([sys.executable, 'gui.py'])

        window.destroy()


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
    46.0,
    48.0,
    anchor="nw",
    text="Learn Anywhere, Achieve Everywhere",
    fill="#0018FF",
    font=("Poppins Regular", 10 * -1)
)

button_image_1 = PhotoImage(
    file=("profile.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=create_gui,
    relief="flat",
    cursor="hand2"
)

canvas.create_window(1194, 12, anchor="nw", window=button_1)

# button_1.place(
#     x=1194.0,
#     y=12.0,
#     width=56.0,
#     height=56.0
# )

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
    font=("lexend deca", 15)
)
canvas.create_window(717, 24, anchor="nw", window=entry_1)

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
canvas.create_window(1130, 26, anchor="nw", window=button_2)


image_image_1 = PhotoImage(
    file=("image_1.png"))
image_1 = canvas.create_image(
    328.9998779296875,
    206.87896728515625,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=("image_2.png"))
image_2 = canvas.create_image(
    974.0,
    151.3076171875,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=("image_3.png"))
image_3 = canvas.create_image(
    752.0001220703125,
    188.75360107421875,
    image=image_image_3
)

canvas.create_text(
    748.0,
    169.0,
    anchor="nw",
    text="Requests",
    fill="#646ECB",
    font=("OpenSans Bold", 60 * -1)
)

canvas.create_rectangle(
    0.0,
    1720.0,
    1280.0,
    1989.0,
    fill="#3532A7",
    outline="")

button_image_3 = PhotoImage(
    file=("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat",
    cursor="hand2"
)
button_3.place(
    x=496.0,
    y=1743.0,
    width=30.0,
    height=15.0
)

button_image_4 = PhotoImage(
    file=("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat",
    cursor="hand2"
)
button_4.place(
    x=727.0,
    y=1740.0,
    width=112.0,
    height=15.0
)

button_image_5 = PhotoImage(
    file=("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat",
    cursor="hand2"
)
button_5.place(
    x=1001.0,
    y=1740.0,
    width=28.0,
    height=15.0
)

button_image_6 = PhotoImage(
    file=("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat",
    cursor="hand2"
)
button_6.place(
    x=1001.0,
    y=1765.0,
    width=16.0,
    height=15.0
)

button_image_7 = PhotoImage(
    file=("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat",
    cursor="hand2"
)
button_7.place(
    x=1002.0,
    y=1790.0,
    width=13.0,
    height=15.0
)

button_image_8 = PhotoImage(
    file=("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat",
    cursor="hand2"
)
button_8.place(
    x=1002.0,
    y=1815.0,
    width=98.0,
    height=15.0
)

button_image_9 = PhotoImage(
    file=("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat",
    cursor="hand2"
)
button_9.place(
    x=729.0,
    y=1765.0,
    width=69.0,
    height=15.0
)

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
button_10.place(
    x=729.0,
    y=1790.0,
    width=41.0,
    height=15.0
)

button_image_11 = PhotoImage(
    file=("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
    relief="flat",
    cursor="hand2"
)
button_11.place(
    x=729.0,
    y=1815.0,
    width=56.0,
    height=15.0
)

button_image_12 = PhotoImage(
    file=("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_12 clicked"),
    relief="flat",
    cursor="hand2"
)
button_12.place(
    x=496.0,
    y=1768.0,
    width=46.0,
    height=15.0
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
button_13.place(
    x=496.0,
    y=1793.0,
    width=42.0,
    height=15.0
)

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
button_14.place(
    x=496.0,
    y=1818.0,
    width=33.0,
    height=15.0
)

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
button_15.place(
    x=496.0,
    y=1843.0,
    width=39.0,
    height=15.0
)
def buildfile():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("requests_notdone","build"))
        os.chdir(next_folder)

        # Run the gui.py file
        subprocess.Popen([sys.executable, 'gui.py'])

        window.destroy()
button_image_16 = PhotoImage(
    file=("home.png"))
button_16 = Button(
    canvas,
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=buildfile,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(385, 31, anchor="nw", window=button_16)


button_image_17 = PhotoImage(
    file=("routines.png"))
button_17 = Button(
    canvas,
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=routinesfile,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(533, 32, anchor="nw", window=button_17)


button_image_18 = PhotoImage(
    file=("courses.png"))
button_18 = Button(
    canvas,
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=homefile,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(446, 32, anchor="nw", window=button_18)


button_image_19 = PhotoImage(
    file=("requests.png"))
button_19 = Button(
    canvas,
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    state=DISABLED,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(628, 31, anchor="nw", window=button_19)
canvas.create_text(
    36.0,
    496.0,
    anchor="nw",
    text="Recommended Books",
    fill="#3532A7",
    font=("Poppins SemiBold", 34 * -1)
)

canvas.create_text(
    51.0,
    1244.0,
    anchor="nw",
    text="Issued Books",
    fill="#3532A7",
    font=("Poppins SemiBold", 34 * -1)
)

canvas.create_rectangle(
    84.0,
    601.0,
    326.0,
    845.0,
    fill="#FFFFFF",
    outline="")



canvas.create_rectangle(
    84.0,
    891.0,
    326.0,
    1135.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    377.0,
    601.0,
    619.0,
    845.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    377.0,
    891.0,
    619.0,
    1135.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    670.0,
    601.0,
    912.0,
    845.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    670.0,
    891.0,
    912.0,
    1135.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    963.0,
    601.0,
    1205.0,
    845.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    963.0,
    891.0,
    1205.0,
    1135.0,
    fill="#FFFFFF",
    outline="")

image_image_4 = PhotoImage(
    file=("image_4.png"))
image_4 = canvas.create_image(
    205.0,
    663.0,
    image=image_image_4
)




image_image_9 = PhotoImage(
    file=("image_9.png"))
image_9 = canvas.create_image(
    205.0,
    953.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=("image_10.png"))
image_10 = canvas.create_image(
    498.0,
    663.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=("image_11.png"))
image_11 = canvas.create_image(
    498.0,
    953.0,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=("image_12.png"))
image_12 = canvas.create_image(
    791.0,
    663.0,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=("image_13.png"))
image_13 = canvas.create_image(
    791.0,
    953.0,
    image=image_image_13
)

image_image_14 = PhotoImage(
    file=("image_14.png"))
image_14 = canvas.create_image(
    1084.0,
    663.0,
    image=image_image_14
)

image_image_15 = PhotoImage(
    file=("image_15.png"))
image_15 = canvas.create_image(
    1084.0,
    953.0,
    image=image_image_15
)

canvas.create_text(
    97.0,
    761.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)


canvas.create_text(
    97.0,
    1051.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    390.0,
    761.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    390.0,
    1051.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    683.0,
    761.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    683.0,
    1051.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    976.0,
    761.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    976.0,
    1051.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

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

canvas.create_window(97, 731, anchor="nw", window=button_20)

# button_20.place(
#     x=97.0,
#     y=731.12548828125,
#     width=87.0,
#     height=11.9024658203125
# )

# button_24.place(
#     x=995.0,
#     y=1462.12548828125,
#     width=87.0,
#     height=11.9024658203125
# )

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

canvas.create_window(97, 1021, anchor="nw", window=button_25)

# button_25.place(
#     x=97.0,
#     y=1021.12548828125,
#     width=87.0,
#     height=11.9024658203125
# )

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
canvas.create_window(390, 731, anchor="nw", window=button_26)

# button_26.place(
#     x=390.0,
#     y=731.12548828125,
#     width=87.0,
#     height=11.9024658203125
# )

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

canvas.create_window(390, 1021, anchor="nw", window=button_27)

# button_27.place(
#     x=390.0,
#     y=1021.12548828125,
#     width=87.0,
#     height=11.9024658203125
# )

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
canvas.create_window(683, 731, anchor="nw", window=button_28)


# button_28.place(
#     x=683.0,
#     y=731.12548828125,
#     width=87.0,
#     height=11.9024658203125
# )

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

canvas.create_window(683, 1021, anchor="nw", window=button_29)

# button_29.place(
#     x=683.0,
#     y=1021.12548828125,
#     width=87.0,
#     height=11.9024658203125
# )

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

canvas.create_window(976, 731, anchor="nw", window=button_30)

# button_30.place(
#     x=976.0,
#     y=731.12548828125,
#     width=87.0,
#     height=11.9024658203125
# )

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
canvas.create_window(976, 1021, anchor="nw", window=button_31)


# button_31.place(
#     x=976.0,
#     y=1021.12548828125,
#     width=87.0,
#     height=11.9024658203125
# )

image_image_16 = PhotoImage(
    file=("image_16.png"))
image_16 = canvas.create_image(
    205.0,
    753.8292236328125,
    image=image_image_16
)



image_image_21 = PhotoImage(
    file=("image_21.png"))
image_21 = canvas.create_image(
    205.0,
    1043.8292236328125,
    image=image_image_21
)

image_image_22 = PhotoImage(
    file=("image_22.png"))
image_22 = canvas.create_image(
    498.0,
    753.8292236328125,
    image=image_image_22
)

image_image_23 = PhotoImage(
    file=("image_23.png"))
image_23 = canvas.create_image(
    498.0,
    1043.8292236328125,
    image=image_image_23
)

image_image_24 = PhotoImage(
    file=("image_24.png"))
image_24 = canvas.create_image(
    791.0,
    753.8292236328125,
    image=image_image_24
)

image_image_25 = PhotoImage(
    file=("image_25.png"))
image_25 = canvas.create_image(
    791.0,
    1043.8292236328125,
    image=image_image_25
)

image_image_26 = PhotoImage(
    file=("image_26.png"))
image_26 = canvas.create_image(
    1084.0,
    753.8292236328125,
    image=image_image_26
)

image_image_27 = PhotoImage(
    file=("image_27.png"))
image_27 = canvas.create_image(
    1084.0,
    1043.8292236328125,
    image=image_image_27
)

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

canvas.create_window(97, 781, anchor="nw", window=button_32)

# button_32.place(
#     x=97.0,
#     y=781.0,
#     width=80.5115966796875,
#     height=18.0740966796875
# )


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

canvas.create_window(97, 1071, anchor="nw", window=button_37)

# button_37.place(
#     x=97.0,
#     y=1071.0,
#     width=80.5115966796875,
#     height=18.0740966796875
# )

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

canvas.create_window(390, 781, anchor="nw", window=button_38)

# button_38.place(
#     x=390.0,
#     y=781.0,
#     width=80.5115966796875,
#     height=18.0740966796875
# )

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

canvas.create_window(390, 1071, anchor="nw", window=button_39)
# button_39.place(
#     x=390.0,
#     y=1071.0,
#     width=80.5115966796875,
#     height=18.0740966796875
# )

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

canvas.create_window(683, 781, anchor="nw", window=button_40)
# button_40.place(
#     x=683.0,
#     y=781.0,
#     width=80.5115966796875,
#     height=18.0740966796875
# )

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

canvas.create_window(683, 1071, anchor="nw", window=button_41)
# button_41.place(
#     x=683.0,
#     y=1071.0,
#     width=80.5115966796875,
#     height=18.0740966796875
# )

button_image_42 = PhotoImage(
    file=("button_42.png"))
button_42 = Button(
    image=button_image_42,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_42 clicked"),
    relief="flat",
    cursor="hand2"
)

canvas.create_window(976, 781, anchor="nw", window=button_42)
# button_42.place(
#     x=976.0,
#     y=781.0,
#     width=80.51171875,
#     height=18.0740966796875
# )

button_image_43 = PhotoImage(
    file=("button_43.png"))
button_43 = Button(
    image=button_image_43,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_43 clicked"),
    relief="flat",
    cursor="hand2"
)

canvas.create_window(976, 1071, anchor="nw", window=button_43)
# button_43.place(
#     x=976.0,
#     y=1071.0,
#     width=80.51171875,
#     height=18.0740966796875
# )

button_image_44 = PhotoImage(
    file=("button_44.png"))
button_44 = Button(
    image=button_image_44,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_44 clicked"),
    relief="flat",
    cursor="hand2"
)

canvas.create_window(133, 805, anchor="nw", window=button_44)
# button_44.place(
#     x=133.0,
#     y=805.0,
#     width=144.0,
#     height=25.0
# )



# button_48.place(
#     x=1031.0,
#     y=1536.0,
#     width=144.0,
#     height=25.0
# )

button_image_49 = PhotoImage(
    file=("button_49.png"))
button_49 = Button(
    image=button_image_49,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_49 clicked"),
    relief="flat",
    cursor="hand2"
)

canvas.create_window(133, 1095, anchor="nw", window=button_49)

# button_49.place(
#     x=133.0,
#     y=1095.0,
#     width=144.0,
#     height=25.0
# )

button_image_50 = PhotoImage(
    file=("button_50.png"))
button_50 = Button(
    image=button_image_50,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_50 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(426, 805, anchor="nw", window=button_50)

# button_50.place(
#     x=426.0,
#     y=805.0,
#     width=144.0,
#     height=25.0
# )

button_image_51 = PhotoImage(
    file=("button_51.png"))
button_51 = Button(
    image=button_image_51,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_51 clicked"),
    relief="flat",
    cursor="hand2"
)

canvas.create_window(426, 1095, anchor="nw", window=button_51)
# button_51.place(
#     x=426.0,
#     y=1095.0,
#     width=144.0,
#     height=25.0
# )

button_image_52 = PhotoImage(
    file=("button_52.png"))
button_52 = Button(
    image=button_image_52,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_52 clicked"),
    relief="flat",
    cursor="hand2"
)

canvas.create_window(719, 805, anchor="nw", window=button_52)

# button_52.place(
#     x=719.0,
#     y=805.0,
#     width=144.0,
#     height=25.0
# )

button_image_53 = PhotoImage(
    file=("button_53.png"))
button_53 = Button(
    image=button_image_53,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_53 clicked"),
    relief="flat",
    cursor="hand2"
)

canvas.create_window(719, 1095, anchor="nw", window=button_53)
# button_53.place(
#     x=719.0,
#     y=1095.0,
#     width=144.0,
#     height=25.0
# )

button_image_54 = PhotoImage(
    file=("button_54.png"))
button_54 = Button(
    image=button_image_54,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_54 clicked"),
    relief="flat",
    cursor="hand2"
)

canvas.create_window(1012, 805, anchor="nw", window=button_54)

# button_54.place(
#     x=1012.0,
#     y=805.0,
#     width=144.0,
#     height=25.0
# )

button_image_55 = PhotoImage(
    file=("button_55.png"))
button_55 = Button(
    image=button_image_55,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_55 clicked"),
    relief="flat",
    cursor="hand2"
)

canvas.create_window(1012, 1095, anchor="nw", window=button_55)

# button_55.place(
#     x=1012.0,
#     y=1095.0,
#     width=144.0,
#     height=25.0
# )

#  footer


canvas.create_text(
    62.0,
    1750.0,
    anchor="nw",
    text="VirtuEdu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 32 * -1)
)

canvas.create_text(
    506.0,
    1780.0,
    anchor="nw",
    text="Menu",
    fill="#fff",
    font=("Poppins SemiBold", 24 * -1)
)

canvas.create_text(
    740.0,
    1780.0,
    anchor="nw",
    text="Menu",
    fill="#fff",
    font=("Poppins SemiBold", 24 * -1)
)

canvas.create_text(
    1010.0,
    1780.0,
    anchor="nw",
    text="Menu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 24 * -1)
)

canvas.create_text(
    88.0,
    1790.0,
    anchor="nw",
    text="Learn Anywhere, Achieve Everywhere",
    fill="#FFFFFF",
    font=("Poppins Regular", 11 * -1)
)

canvas.create_text(
    50.0,
    1830.0,
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
    text= "Home",
    bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    
)
canvas.create_window(506, 1830, anchor="nw", window=button_3)

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
    text= "About Us",
    bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    

)
canvas.create_window(506, 1860, anchor="nw", window=button_112)

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
    text= "Courses",
    bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    

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
    text= "Events",
    bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    

)
canvas.create_window(506, 1920, anchor="nw", window=eventbtn)

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
    text= "Routines",    
    bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    

)
canvas.create_window(506, 1950, anchor="nw", window=routinebtn)

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
    text= "Terms and Conditions",  
    bg="#3532A7",
    fg="#fff",
    cursor="hand2"

    

)
canvas.create_window(740, 1830, anchor="nw", window=termsandcon)


def alert1():
    messagebox.showinfo("Alert", "You are on Same page now") 

privacy = Button(
    # image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=alert1,
    relief="flat",
    text= "Privacy Policy",
    bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    

)
canvas.create_window(740, 1860, anchor="nw", window=privacy)

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
    text= "Support",
    bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    

)
canvas.create_window(740, 1890, anchor="nw", window=support)

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
    text= "Contact Us",
    bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    

)
canvas.create_window(740, 1920, anchor="nw", window=contact)

cden = Button(
    # image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: webbrowser.open_new(r"http://www.cden.org.np"),
    relief="flat",
    text= "CDEN",
       bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    

)
canvas.create_window(1010, 1830, anchor="nw", window=cden)

ioe = Button(
    # image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: webbrowser.open_new(r"http://www.ioe.edu.np"),
    relief="flat",
    text= "IOE",
       bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    

)
canvas.create_window(1010, 1860, anchor="nw", window=ioe)

tu = Button(
    # image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: webbrowser.open_new(r"http://www.tu.edu.np"),
    relief="flat",
    text= "TU",
       bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    

)
canvas.create_window(1010, 1890, anchor="nw", window=tu)

cu = Button(
    # image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: webbrowser.open_new(r"http://www.coventry.ac.uk"),
    relief="flat",
    text= "Coventry University",
    bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    

)
canvas.create_window(1010, 1920, anchor="nw", window=cu)






# Update the scroll region to include the entire frame
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

window.resizable(False, False)
window.mainloop()
