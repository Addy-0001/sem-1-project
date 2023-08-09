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
    relief="flat"
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
    relief="flat"
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
    relief="flat"
)
button_4.place(
    x=388.0,
    y=31.0,
    width=61.0,
    height=28.0
)

button_image_5 = PhotoImage(
    file=("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat",
    bg="#83b4ff"
)
button_5.place(
    x=546.0,
    y=31.0,
    width=65.0,
    height=25.0
)

button_image_6 = PhotoImage(
    file=("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat",
    bg="#83b4ff"
)
button_6.place(
    x=628.0,
    y=31.0,
    width=65.0,
    height=30.0
)

button_image_7 = PhotoImage(
    file=("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat",
    bg="#83b4ff"
)
button_7.place(
    x=459.0,
    y=31.0,
    width=69.0,
    height= 25.0
)

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
    relief="flat"
)
button_8.place(
    x=454.0,
    y=1747.0,
    width=47.0,
    height=45.0
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
    x=501.0,
    y=1747.0,
    width=47.0,
    height=45.0
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
    x=547.0,
    y=1747.0,
    width=47.0,
    height=45.0
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
    x=593.0,
    y=1747.0,
    width=47.0,
    height=45.0
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
    x=741.0,
    y=1747.0,
    width=47.0,
    height=45.0
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
    x=826.0,
    y=1747.0,
    width=91.0,
    height=45.0
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
    x=787.0,
    y=1747.0,
    width=47.0,
    height=45.0
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
    x=639.0,
    y=1747.0,
    width=103.0,
    height=45.0
)

canvas.create_rectangle(
    0.0,
    1813.0,
    1280.0,
    2007.0,
    fill="#3532A7",
    outline="")

canvas.create_text(
    131.0,
    1844.0,
    anchor="nw",
    text="VirtuEdu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 25 * -1)
)

canvas.create_text(
    529.0,
    1844.0,
    anchor="nw",
    text="Menu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 20 * -1)
)

canvas.create_text(
    782.0,
    1844.0,
    anchor="nw",
    text="Menu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 20 * -1)
)

canvas.create_text(
    1061.0,
    1844.0,
    anchor="nw",
    text="Menu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 20 * -1)
)

canvas.create_text(
    138.0,
    1872.0,
    anchor="nw",
    text="Learn Anywhere, Achieve Everywhere",
    fill="#FFFFFF",
    font=("Poppins Regular", 6 * -1)
)

canvas.create_text(
    138.0,
    1892.0,
    anchor="nw",
    text="\nour innovative online learning platform empowers students to pursue their educational goals from anywhere in the \nworld. With flexible schedules and high-quality courses, we provide the tools and resources necessary for you to excel \nin your studies and succeed in any endeavor. Join our global community of learners and unlock your full potential with \n Virtu Edu.",
    fill="#FFFFFF",
    font=("Poppins Medium", 10 * -1)
)

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
    relief="flat"
)
button_16.place(
    x=102.43994140625,
    y=819.666748046875,
    width=48.959991455078125,
    height=35.897430419921875
)

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
    relief="flat"
)
button_17.place(
    x=248.0,
    y=817.0,
    width=57.1199951171875,
    height=41.880340576171875
)

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
    relief="flat"
)
button_18.place(
    x=102.43994140625,
    y=1226.666748046875,
    width=48.959991455078125,
    height=35.897430419921875
)

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
    relief="flat"
)
button_19.place(
    x=248.0,
    y=1224.0,
    width=57.1199951171875,
    height=41.880340576171875
)

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
    relief="flat"
)
button_20.place(
    x=102.43994140625,
    y=1622.6669921875,
    width=48.959991455078125,
    height=35.8974609375
)

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
    relief="flat"
)
button_21.place(
    x=406.43994140625,
    y=819.666748046875,
    width=48.96000671386719,
    height=35.897430419921875
)

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
    relief="flat"
)
button_22.place(
    x=552.0,
    y=817.0,
    width=57.12000274658203,
    height=41.880340576171875
)

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
    relief="flat"
)
button_23.place(
    x=406.43994140625,
    y=1226.666748046875,
    width=48.96000671386719,
    height=35.897430419921875
)

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
    relief="flat"
)
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
    relief="flat"
)
button_25.place(
    x=406.43994140625,
    y=1622.6669921875,
    width=48.96000671386719,
    height=35.8974609375
)

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
    relief="flat"
)
button_26.place(
    x=552.0,
    y=1620.0,
    width=57.12000274658203,
    height=41.88037109375
)

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
    relief="flat"
)
button_27.place(
    x=686.43994140625,
    y=813.666748046875,
    width=48.96000671386719,
    height=35.897430419921875
)

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
    relief="flat"
)
button_28.place(
    x=832.0,
    y=811.0,
    width=57.1199951171875,
    height=41.880340576171875
)

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
    relief="flat"
)
button_29.place(
    x=686.43994140625,
    y=1220.666748046875,
    width=48.96000671386719,
    height=35.897430419921875
)

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
    relief="flat"
)
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
    relief="flat"
)
button_31.place(
    x=832.0,
    y=1614.0,
    width=57.1199951171875,
    height=41.88037109375
)

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
    relief="flat"
)
button_32.place(
    x=972.43994140625,
    y=813.666748046875,
    width=48.959991455078125,
    height=35.897430419921875
)

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
    relief="flat"
)
button_33.place(
    x=1118.0,
    y=811.0,
    width=57.1199951171875,
    height=41.880340576171875
)

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
    relief="flat"
)
button_34.place(
    x=972.43994140625,
    y=1220.666748046875,
    width=48.959991455078125,
    height=35.897430419921875
)

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
    relief="flat"
)
button_35.place(
    x=1118.0,
    y=1218.0,
    width=57.1199951171875,
    height=41.880340576171875
)

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
    relief="flat"
)
button_36.place(
    x=972.43994140625,
    y=1616.6669921875,
    width=48.959991455078125,
    height=35.8974609375
)

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
    relief="flat"
)
button_37.place(
    x=1118.0,
    y=1614.0,
    width=57.1199951171875,
    height=41.88037109375
)

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
    relief="flat"
)
button_38.place(
    x=536.0,
    y=1895.0,
    width=88.0,
    height=21.0
)

button_image_39 = PhotoImage(
    file=("button_39.png"))
button_39 = Button(
    image=button_image_39,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_39 clicked"),
    relief="flat"
)
button_39.place(
    x=536.0,
    y=1874.0,
    width=66.0,
    height=21.0
)

button_image_40 = PhotoImage(
    file=("button_40.png"))
button_40 = Button(
    image=button_image_40,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_40 clicked"),
    relief="flat"
)
button_40.place(
    x=536.0,
    y=1916.0,
    width=85.0,
    height=21.0
)

button_image_41 = PhotoImage(
    file=("button_41.png"))
button_41 = Button(
    image=button_image_41,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_41 clicked"),
    relief="flat"
)
button_41.place(
    x=536.0,
    y=1937.0,
    width=66.0,
    height=21.0
)

button_image_42 = PhotoImage(
    file=("button_42.png"))
button_42 = Button(
    image=button_image_42,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_42 clicked"),
    relief="flat"
)
button_42.place(
    x=536.0,
    y=1958.0,
    width=81.0,
    height=21.0
)

button_image_43 = PhotoImage(
    file=("button_43.png"))
button_43 = Button(
    image=button_image_43,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_43 clicked"),
    relief="flat"
)
button_43.place(
    x=536.0,
    y=1958.0,
    width=81.0,
    height=21.0
)

button_image_44 = PhotoImage(
    file=("button_44.png"))
button_44 = Button(
    image=button_image_44,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_44 clicked"),
    relief="flat"
)
button_44.place(
    x=789.0,
    y=1874.0,
    width=179.0,
    height=21.0
)

button_image_45 = PhotoImage(
    file=("button_45.png"))
button_45 = Button(
    image=button_image_45,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_45 clicked"),
    relief="flat"
)
button_45.place(
    x=789.0,
    y=1895.0,
    width=125.0,
    height=21.0
)

button_image_46 = PhotoImage(
    file=("button_46.png"))
button_46 = Button(
    image=button_image_46,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_46 clicked"),
    relief="flat"
)
button_46.place(
    x=796.0,
    y=1901.0,
    width=8.0,
    height=9.0
)

button_image_47 = PhotoImage(
    file=("button_47.png"))
button_47 = Button(
    image=button_image_47,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_47 clicked"),
    relief="flat"
)
button_47.place(
    x=789.0,
    y=1916.0,
    width=81.0,
    height=21.0
)

button_image_48 = PhotoImage(
    file=("button_48.png"))
button_48 = Button(
    image=button_image_48,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_48 clicked"),
    relief="flat"
)
button_48.place(
    x=1060.0,
    y=1874.0,
    width=81.0,
    height=21.0
)

button_image_49 = PhotoImage(
    file=("button_49.png"))
button_49 = Button(
    image=button_image_49,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_49 clicked"),
    relief="flat"
)
button_49.place(
    x=1060.0,
    y=1895.0,
    width=81.0,
    height=21.0
)

button_image_50 = PhotoImage(
    file=("button_50.png"))
button_50 = Button(
    image=button_image_50,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_50 clicked"),
    relief="flat",
    
)
button_50.place(
    x=1060.0,
    y=1916.0,
    width=81.0,
    height=21.0
)

button_image_51 = PhotoImage(
    file=("button_51.png"))
button_51 = Button(
    image=button_image_51,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_51 clicked"),
    relief="flat"
)
button_51.place(
    x=1060.0,
    y=1937.0,
    width=172.0,
    height=21.0
)

button_image_52 = PhotoImage(
    file=("button_52.png"))
button_52 = Button(
    image=button_image_52,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_52 clicked"),
    relief="flat"
)
button_52.place(
    x=788.0,
    y=1937.0,
    width=110.0,
    height=21.0
)













window.resizable(False, False)
window.mainloop()
