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
from tkinter import messagebox
import webbrowser

    

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
button_1.place(
     x=1160.0,
    y=20.0,
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
    highlightthickness=0,
    font=("lexend deca",12)
)
entry_1.place(
    x=717.0,
    y=16.0,
    width=275.0,
    height=32.0
)




button_image_3 = PhotoImage(
    file=("notification.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=create_gui,
    relief="flat",
    cursor="hand2"
)
button_3.place(
    x=1100.0,
    y=31.615699768066406,
    width=29.694091796875,
    height=29.550003051757812
)
def buildfile():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("thirdmainpage(tutor page)","build"))
        os.chdir(next_folder)

        # Run the gui.py file
        subprocess.Popen([sys.executable, 'gui.py'])

        window.destroy()
button_image_4 = PhotoImage(
    file=("home.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=buildfile,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(388, 31, anchor="nw", window=button_4)



button_image_5 = PhotoImage(
    file=("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat",
    cursor="hand2",
    bg="#83b4ff"
)
canvas.create_window(546, 31, anchor="nw", window=button_5)

button_image_6 = PhotoImage(
    file=("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat",
    cursor="hand2",
    bg="#83b4ff"
)
canvas.create_window(628, 31, anchor="nw", window=button_6)



button_image_7 = PhotoImage(
    file=("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat",
    cursor="hand2",
    bg="#83b4ff"
)
canvas.create_window(459, 31, anchor="nw", window=button_7)



image_image_1 = PhotoImage(
    file=("image_1.png"))
image_1 = canvas.create_image(
    326.0,
    264.640380859375,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=("image_2.png"))
image_2 = canvas.create_image(
    883.0,
    300.259765625,
    image=image_image_2
)

canvas.create_text(
    797.0,
    195.0,
    anchor="nw",
    text="Our Tutors",
    fill="#3E4CCF",
    font=("OpenSans Bold", 60 * -1)
)

canvas.create_text(
    793.0,
    285.0,
    anchor="nw",
    text="Unlock your potential with our transformative courses.",
    fill="#3E4CCF",
    font=("Poppins Regular", 15 * -1)
)

canvas.create_rectangle(
    454.0,
    1747.0,
    914.0,
    1792.0,
    fill="#FFFFFF",
    outline="")

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
canvas.create_window(454, 1747, anchor="nw", window=button_8)



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
canvas.create_window(501, 1747, anchor="nw", window=button_9)



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
canvas.create_window(547, 1747, anchor="nw", window=button_10)


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
canvas.create_window(593, 1747, anchor="nw", window=button_11)



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
canvas.create_window(741, 1747, anchor="nw", window=button_12)


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
canvas.create_window(826, 1747, anchor="nw", window=button_13)



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
canvas.create_window(787, 1747, anchor="nw", window=button_14)


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
canvas.create_window(639, 1747, anchor="nw", window=button_15)


canvas.create_rectangle(
    0.0,
    1813.0,
    1280.0,
    2103.0,
    fill="#3532A7",
    outline="")

canvas.create_rectangle(
    90.0,
    537.0,
    319.0,
    886.0,
    fill="#FFFFFF",
    outline="")

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
canvas.create_window(102, 819, anchor="nw", window=button_16)


canvas.create_text(
    116.719970703125,
    741.888916015625,
    anchor="nw",
    text="SUBAS",
    fill="#000000",
    font=("OpenSans SemiBold", 16 * -1)
)

canvas.create_text(
    116.719970703125,
    771.803466796875,
    anchor="nw",
    text="UI/UX",
    fill="#5E5E5E",
    font=("OpenSans Regular", 12 * -1)
)

canvas.create_text(
    143.239990234375,
    825.649658203125,
    anchor="nw",
    text="1581",
    fill="#468CE7",
    font=("OpenSans SemiBold", 12 * -1)
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
canvas.create_window(248, 817, anchor="nw", window=button_17)



image_image_3 = PhotoImage(
    file=("image_3.png"))
image_3 = canvas.create_image(
    203.0,
    641.0,
    image=image_image_3
)

canvas.create_rectangle(
    90.0,
    944.0,
    319.0,
    1293.0,
    fill="#FFFFFF",
    outline="")

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
canvas.create_window(102, 1226, anchor="nw", window=button_18)


canvas.create_text(
    116.719970703125,
    1148.888916015625,
    anchor="nw",
    text="SUBAS",
    fill="#000000",
    font=("OpenSans SemiBold", 16 * -1)
)

canvas.create_text(
    116.719970703125,
    1178.803466796875,
    anchor="nw",
    text="UI/UX",
    fill="#5E5E5E",
    font=("OpenSans Regular", 12 * -1)
)

canvas.create_text(
    143.239990234375,
    1232.649658203125,
    anchor="nw",
    text="1581",
    fill="#468CE7",
    font=("OpenSans SemiBold", 12 * -1)
)

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
canvas.create_window(248, 1224, anchor="nw", window=button_19)


image_image_4 = PhotoImage(
    file=("image_4.png"))
image_4 = canvas.create_image(
    203.0,
    1048.0,
    image=image_image_4
)

canvas.create_rectangle(
    90.0,
    1340.0,
    319.0,
    1689.0,
    fill="#FFFFFF",
    outline="")

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
canvas.create_window(102, 1662, anchor="nw", window=button_20)



canvas.create_text(
    116.719970703125,
    1544.888671875,
    anchor="nw",
    text="SUBAS",
    fill="#000000",
    font=("OpenSans SemiBold", 16 * -1)
)

canvas.create_text(
    116.719970703125,
    1574.8037109375,
    anchor="nw",
    text="UI/UX",
    fill="#5E5E5E",
    font=("OpenSans Regular", 12 * -1)
)

canvas.create_text(
    143.239990234375,
    1628.6494140625,
    anchor="nw",
    text="1581",
    fill="#468CE7",
    font=("OpenSans SemiBold", 12 * -1)
)

image_image_5 = PhotoImage(
    file=("image_5.png"))
image_5 = canvas.create_image(
    276.0,
    1640.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=("image_6.png"))
image_6 = canvas.create_image(
    203.0,
    1444.0,
    image=image_image_6
)

canvas.create_rectangle(
    394.0,
    537.0,
    623.0,
    886.0,
    fill="#FFFFFF",
    outline="")

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
canvas.create_window(406, 819, anchor="nw", window=button_21)



canvas.create_text(
    420.719970703125,
    741.888916015625,
    anchor="nw",
    text="SUBAS",
    fill="#000000",
    font=("OpenSans SemiBold", 16 * -1)
)

canvas.create_text(
    420.719970703125,
    771.803466796875,
    anchor="nw",
    text="UI/UX",
    fill="#5E5E5E",
    font=("OpenSans Regular", 12 * -1)
)

canvas.create_text(
    447.239990234375,
    825.649658203125,
    anchor="nw",
    text="1581",
    fill="#468CE7",
    font=("OpenSans SemiBold", 12 * -1)
)

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
canvas.create_window(552, 817, anchor="nw", window=button_22)

image_image_7 = PhotoImage(
    file=("image_7.png"))
image_7 = canvas.create_image(
    507.0,
    641.0,
    image=image_image_7
)

canvas.create_rectangle(
    394.0,
    944.0,
    623.0,
    1293.0,
    fill="#FFFFFF",
    outline="")

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
canvas.create_window(406, 1226, anchor="nw", window=button_23)



canvas.create_text(
    420.719970703125,
    1148.888916015625,
    anchor="nw",
    text="SUBAS",
    fill="#000000",
    font=("OpenSans SemiBold", 16 * -1)
)

canvas.create_text(
    420.719970703125,
    1178.803466796875,
    anchor="nw",
    text="UI/UX",
    fill="#5E5E5E",
    font=("OpenSans Regular", 12 * -1)
)

canvas.create_text(
    447.239990234375,
    1232.649658203125,
    anchor="nw",
    text="1581",
    fill="#468CE7",
    font=("OpenSans SemiBold", 12 * -1)
)

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
canvas.create_window(552, 1224, anchor="nw", window=button_24)

button_24.place(
    x=552.0,
    y=1224.0,
    width=57.12000274658203,
    height=41.880340576171875
)

image_image_8 = PhotoImage(
    file=("image_8.png"))
image_8 = canvas.create_image(
    507.0,
    1048.0,
    image=image_image_8
)

canvas.create_rectangle(
    394.0,
    1340.0,
    623.0,
    1689.0,
    fill="#FFFFFF",
    outline="")

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
canvas.create_window(406, 1622, anchor="nw", window= button_25)



canvas.create_text(
    420.719970703125,
    1544.888671875,
    anchor="nw",
    text="SUBAS",
    fill="#000000",
    font=("OpenSans SemiBold", 16 * -1)
)

canvas.create_text(
    420.719970703125,
    1574.8037109375,
    anchor="nw",
    text="UI/UX",
    fill="#5E5E5E",
    font=("OpenSans Regular", 12 * -1)
)

canvas.create_text(
    447.239990234375,
    1628.6494140625,
    anchor="nw",
    text="1581",
    fill="#468CE7",
    font=("OpenSans SemiBold", 12 * -1)
)

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
canvas.create_window(552, 1620, anchor="nw", window=button_26)

image_image_9 = PhotoImage(
    file=("image_9.png"))
image_9 = canvas.create_image(
    507.0,
    1444.0,
    image=image_image_9
)

canvas.create_rectangle(
    674.0,
    531.0,
    903.0,
    880.0,
    fill="#FFFFFF",
    outline="")

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
canvas.create_window(686, 813, anchor="nw", window=button_27)


canvas.create_text(
    700.719970703125,
    735.888916015625,
    anchor="nw",
    text="SUBAS",
    fill="#000000",
    font=("OpenSans SemiBold", 16 * -1)
)

canvas.create_text(
    700.719970703125,
    765.803466796875,
    anchor="nw",
    text="UI/UX",
    fill="#5E5E5E",
    font=("OpenSans Regular", 12 * -1)
)

canvas.create_text(
    727.239990234375,
    819.649658203125,
    anchor="nw",
    text="1581",
    fill="#468CE7",
    font=("OpenSans SemiBold", 12 * -1)
)

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
canvas.create_window(832, 811, anchor="nw", window=button_28)



image_image_10 = PhotoImage(
    file=("image_10.png"))
image_10 = canvas.create_image(
    787.0,
    635.0,
    image=image_image_10
)

canvas.create_rectangle(
    674.0,
    938.0,
    903.0,
    1287.0,
    fill="#FFFFFF",
    outline="")

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
canvas.create_window(686, 1220, anchor="nw", window=button_29)


canvas.create_text(
    700.719970703125,
    1142.888916015625,
    anchor="nw",
    text="SUBAS",
    fill="#000000",
    font=("OpenSans SemiBold", 16 * -1)
)

canvas.create_text(
    700.719970703125,
    1172.803466796875,
    anchor="nw",
    text="UI/UX",
    fill="#5E5E5E",
    font=("OpenSans Regular", 12 * -1)
)

canvas.create_text(
    727.239990234375,
    1226.649658203125,
    anchor="nw",
    text="1581",
    fill="#468CE7",
    font=("OpenSans SemiBold", 12 * -1)
)

image_image_11 = PhotoImage(
    file=("image_11.png"))
image_11 = canvas.create_image(
    860.0,
    1238.0,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=("image_12.png"))
image_12 = canvas.create_image(
    787.0,
    1042.0,
    image=image_image_12
)

canvas.create_rectangle(
    674.0,
    1334.0,
    903.0,
    1683.0,
    fill="#FFFFFF",
    outline="")

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
canvas.create_window(686, 1616, anchor="nw", window=button_30)

button_30.place(
    x=686.43994140625,
    y=1616.6669921875,
    width=48.96000671386719,
    height=35.8974609375
)

canvas.create_text(
    700.719970703125,
    1538.888671875,
    anchor="nw",
    text="SUBAS",
    fill="#000000",
    font=("OpenSans SemiBold", 16 * -1)
)

canvas.create_text(
    700.719970703125,
    1568.8037109375,
    anchor="nw",
    text="UI/UX",
    fill="#5E5E5E",
    font=("OpenSans Regular", 12 * -1)
)

canvas.create_text(
    727.239990234375,
    1622.6494140625,
    anchor="nw",
    text="1581",
    fill="#468CE7",
    font=("OpenSans SemiBold", 12 * -1)
)

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
canvas.create_window(832, 1614, anchor="nw", window=button_31)


image_image_13 = PhotoImage(
    file=("image_13.png"))
image_13 = canvas.create_image(
    787.0,
    1438.0,
    image=image_image_13
)

canvas.create_rectangle(
    960.0,
    531.0,
    1189.0,
    880.0,
    fill="#FFFFFF",
    outline="")

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
canvas.create_window(972, 813, anchor="nw", window=button_32)



canvas.create_text(
    986.719970703125,
    735.888916015625,
    anchor="nw",
    text="SUBAS",
    fill="#000000",
    font=("OpenSans SemiBold", 16 * -1)
)

canvas.create_text(
    986.719970703125,
    765.803466796875,
    anchor="nw",
    text="UI/UX",
    fill="#5E5E5E",
    font=("OpenSans Regular", 12 * -1)
)

canvas.create_text(
    1013.239990234375,
    819.649658203125,
    anchor="nw",
    text="1581",
    fill="#468CE7",
    font=("OpenSans SemiBold", 12 * -1)
)

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
canvas.create_window(1118, 811, anchor="nw", window=button_33)


image_image_14 = PhotoImage(
    file=("image_14.png"))
image_14 = canvas.create_image(
    1073.0,
    635.0,
    image=image_image_14
)

canvas.create_rectangle(
    960.0,
    938.0,
    1189.0,
    1287.0,
    fill="#FFFFFF",
    outline="")

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
canvas.create_window(972, 1220, anchor="nw", window=button_34)

canvas.create_text(
    986.719970703125,
    1142.888916015625,
    anchor="nw",
    text="SUBAS",
    fill="#000000",
    font=("OpenSans SemiBold", 16 * -1)
)

canvas.create_text(
    986.719970703125,
    1172.803466796875,
    anchor="nw",
    text="UI/UX",
    fill="#5E5E5E",
    font=("OpenSans Regular", 12 * -1)
)

canvas.create_text(
    1013.239990234375,
    1226.649658203125,
    anchor="nw",
    text="1581",
    fill="#468CE7",
    font=("OpenSans SemiBold", 12 * -1)
)

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
canvas.create_window(1118, 1218, anchor="nw", window=button_35)


image_image_15 = PhotoImage(
    file=("image_15.png"))
image_15 = canvas.create_image(
    1073.0,
    1042.0,
    image=image_image_15
)

canvas.create_rectangle(
    960.0,
    1334.0,
    1189.0,
    1683.0,
    fill="#FFFFFF",
    outline="")

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
canvas.create_window(972, 1616, anchor="nw", window=button_36)



canvas.create_text(
    986.719970703125,
    1538.888671875,
    anchor="nw",
    text="SUBAS",
    fill="#000000",
    font=("OpenSans SemiBold", 16 * -1)
)

canvas.create_text(
    986.719970703125,
    1568.8037109375,
    anchor="nw",
    text="UI/UX",
    fill="#5E5E5E",
    font=("OpenSans Regular", 12 * -1)
)

canvas.create_text(
    1013.239990234375,
    1622.6494140625,
    anchor="nw",
    text="1581",
    fill="#468CE7",
    font=("OpenSans SemiBold", 12 * -1)
)

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
canvas.create_window(1118, 1614, anchor="nw", window=button_37)



image_image_16 = PhotoImage(
    file=("image_16.png"))
image_16 = canvas.create_image(
    1073.0,
    1438.0,
    image=image_image_16
)

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
canvas.create_window(536, 1895, anchor="nw", window=button_38)



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
canvas.create_window(536, 1874, anchor="nw", window=button_39)


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
canvas.create_window(536, 1916, anchor="nw", window=button_40)


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
canvas.create_window(536, 1937, anchor="nw", window=button_41)

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
canvas.create_window(536, 1958, anchor="nw", window=button_42)



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
canvas.create_window(536, 1958, anchor="nw", window=button_43)


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
canvas.create_window(789, 1874, anchor="nw", window=button_44)



button_image_45 = PhotoImage(
    file=("button_45.png"))
button_45 = Button(
    image=button_image_45,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_45 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(789, 1895, anchor="nw", window=button_45)


button_image_46 = PhotoImage(
    file=("button_46.png"))
button_46 = Button(
    image=button_image_46,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_46 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(796, 1901, anchor="nw", window=button_46)


button_image_47 = PhotoImage(
    file=("button_47.png"))
button_47 = Button(
    image=button_image_47,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_47 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(789, 1916, anchor="nw", window=button_47)


button_image_48 = PhotoImage(
    file=("button_48.png"))
button_48 = Button(
    image=button_image_48,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_48 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(1060, 1874, anchor="nw", window=button_48)



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
canvas.create_window(1060, 1895, anchor="nw", window=button_49)



button_image_50 = PhotoImage(
    file=("button_50.png"))
button_50 = Button(
    image=button_image_50,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_50 clicked"),
    relief="flat",
    cursor="hand2",
    
)
canvas.create_window(1060, 1916, anchor="nw", window=button_50)

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
canvas.create_window(1060, 1937, anchor="nw", window=button_51)



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
canvas.create_window(788, 1937, anchor="nw", window=button_52)


# Footer


canvas.create_text(
    62.0,
    1844.0,
    anchor="nw",
    text="VirtuEdu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 32 * -1)
)

canvas.create_text(
    506.0,
    1874.0,
    anchor="nw",
    text="Menu",
    fill="#fff",
    font=("Poppins SemiBold", 24 * -1)
)

canvas.create_text(
    740.0,
    1874.0,
    anchor="nw",
    text="Menu",
    fill="#fff",
    font=("Poppins SemiBold", 24 * -1)
)

canvas.create_text(
    1010.0,
    1874.0,
    anchor="nw",
    text="Menu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 24 * -1)
)

canvas.create_text(
    88.0,
    1884.0,
    anchor="nw",
    text="Learn Anywhere, Achieve Everywhere",
    fill="#FFFFFF",
    font=("Poppins Regular", 11 * -1)
)

canvas.create_text(
    50.0,
    1924.0,
    anchor="nw",
    text="Our innovative online learning platform empowers students\nto pursue their educational goals from anywhere in the world.\nWith flexible schedules and high-quality courses, we provide the\ntools and resources necessary for you to excel in your studies\nand succeed in any endeavor. Join our global community of\nlearners and unlock your full potential with Virtu Edu.",
    fill="#fff",
    font=("Poppins Medium", 12 * -1)
)


def Homes():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("thirdmainpage(tutor page)","build"))
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
  
    
)
canvas.create_window(506, 1924, anchor="nw", window=button_3)

# button_3.place(
#     x=518.0,
#     y=2615.0,
#     width=30.0,
#     height=15.0
# )

def home():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("thirdmainpage(tutor page)","build"))
        os.chdir(next_folder)

        # Run the gui.py file
        subprocess.Popen([sys.executable, 'gui.py'])

        window.destroy()




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

    

)
canvas.create_window(506, 1954, anchor="nw", window=button_112)

def Courses():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("thirdmainpage(tutor page)","homepage"))
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
canvas.create_window(506, 1984, anchor="nw", window=coursesbtn)


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
canvas.create_window(506, 2016, anchor="nw", window=eventbtn)

def Routines():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("thirdmainpage(tutor page)","routines"))
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
canvas.create_window(506, 2044, anchor="nw", window=routinebtn)

def termsandcondition():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("thirdmainpage(tutor page)","termsandconditions"))
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
canvas.create_window(740, 1924, anchor="nw", window=termsandcon)


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

    

)
canvas.create_window(740, 1954, anchor="nw", window=privacy)

def Support():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("thirdmainpage(tutor page)","support"))
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
canvas.create_window(740, 1984, anchor="nw", window=support)

def Contact():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("thirdmainpage(tutor page)","contact_us"))
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
canvas.create_window(740, 2014, anchor="nw", window=contact)

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
canvas.create_window(1010, 1924, anchor="nw", window=cden)

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
canvas.create_window(1010, 1954, anchor="nw", window=ioe)

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
canvas.create_window(1010, 2025, anchor="nw", window=tu)

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
canvas.create_window(1010, 2014, anchor="nw", window=cu)

# button_image_113 = PhotoImage(
#     file=("button_13.png"))
# button_113 = Button(
#     image=button_image_13,
#     borderwidth=0,
#     highlightthickness=0,
#     command=lambda: print("button_113 clicked"),
#     relief="flat",
    # cursor="hand2"
# )
# canvas.create_window(518, 2665, anchor="nw", window=button_113)

# button_image_114 = PhotoImage(
#     file=("button_14.png"))
# button_114 = Button(
#     image=button_image_114,
#     borderwidth=0,
#     highlightthickness=0,
#     command=lambda: print("button_14 clicked"),
#     relief="flat",
    # cursor="hand2"
# )
# canvas.create_window(518, 2690, anchor="nw", window=button_114)


# button_image_115 = PhotoImage(
#     file=("button_15.png"))
# button_115 = Button(
#     image=button_image_115,
#     borderwidth=0,
#     highlightthickness=0,
#     command=lambda: print("button_15 clicked"),
#     relief="flat",
    # cursor="hand2"
# )
# canvas.create_window(518, 2715, anchor="nw", window=button_115)











window.resizable(False, False)
window.mainloop()
