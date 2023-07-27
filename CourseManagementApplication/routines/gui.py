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
    command=create_gui,
    relief="flat"
)
canvas.create_window(1194, 12, anchor="nw", window=button_1)

def homefile():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("routines","homepage"))
        os.chdir(next_folder)

        # Run the gui.py file
        subprocess.Popen([sys.executable, 'gui.py'])

        window.destroy()
def requestsfile():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("routines","requests_notdone"))
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

button_image_2 = PhotoImage(
    file=("notification.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=create_gui,
    relief="flat"
)
canvas.create_window(1150, 31.615699768066406, anchor="nw", window=button_2)


image_image_1 = PhotoImage(
    file=("image_1.png"))
image_1 = canvas.create_image(
    328.9998779296875,
    233.9249267578125,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=("image_2.png"))
image_2 = canvas.create_image(
    974.0001220703125,
    170.86285400390625,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=("image_3.png"))
image_3 = canvas.create_image(
    752.0001220703125,
    213.24005126953125,
    image=image_image_3
)

canvas.create_text(
    748.0,
    169.0,
    anchor="nw",
    text="Routines\n",
    fill="#646ECB",
    font=("OpenSans Bold", 60 * -1)
)

canvas.create_rectangle(
    56.0,
    509.0,
    596.0,
    867.0,
    fill="#FFFCFC",
    outline="")

canvas.create_rectangle(
    56.0,
    934.0,
    596.0,
    1292.0,
    fill="#FFFCFC",
    outline="")

canvas.create_rectangle(
    56.0,
    1359.0,
    596.0,
    1717.0,
    fill="#FFFCFC",
    outline="")

canvas.create_rectangle(
    661.0,
    509.0,
    1201.0,
    867.0,
    fill="#FFFCFC",
    outline="")

canvas.create_rectangle(
    661.0,
    934.0,
    1201.0,
    1292.0,
    fill="#FFFCFC",
    outline="")

canvas.create_rectangle(
    661.0,
    1359.0,
    1201.0,
    1717.0,
    fill="#FFFCFC",
    outline="")

canvas.create_text(
    246.0,
    523.0,
    anchor="nw",
    text="Sunday",
    fill="#3532A7",
    font=("Poppins SemiBold", 40 * -1)
)

canvas.create_text(
    237.0,
    948.0,
    anchor="nw",
    text="Tuesday",
    fill="#3532A7",
    font=("Poppins SemiBold", 40 * -1)
)

canvas.create_text(
    228.0,
    1373.0,
    anchor="nw",
    text="Thursday",
    fill="#3532A7",
    font=("Poppins SemiBold", 40 * -1)
)

canvas.create_text(
    846.0,
    523.0,
    anchor="nw",
    text="Monday",
    fill="#3532A7",
    font=("Poppins SemiBold", 40 * -1)
)

canvas.create_text(
    807.0,
    948.0,
    anchor="nw",
    text="Wednesday",
    fill="#3532A7",
    font=("Poppins SemiBold", 40 * -1)
)

canvas.create_text(
    866.0,
    1373.0,
    anchor="nw",
    text="Friday",
    fill="#3532A7",
    font=("Poppins SemiBold", 40 * -1)
)

canvas.create_rectangle(
    56.0,
    604.0,
    596.0,
    605.0,
    fill="#B3AFAF",
    outline="")

canvas.create_rectangle(
    56.0,
    1029.0,
    596.0,
    1030.0,
    fill="#B3AFAF",
    outline="")

canvas.create_rectangle(
    56.0,
    1454.0,
    596.0,
    1455.0,
    fill="#B3AFAF",
    outline="")

canvas.create_rectangle(
    661.0,
    604.0,
    1201.0,
    605.0,
    fill="#B3AFAF",
    outline="")

canvas.create_rectangle(
    661.0,
    1029.0,
    1201.0,
    1030.0,
    fill="#B3AFAF",
    outline="")

canvas.create_rectangle(
    661.0,
    1454.0,
    1201.0,
    1455.0,
    fill="#B3AFAF",
    outline="")

canvas.create_rectangle(
    296.0,
    604.0,
    297.00001525878906,
    867.0,
    fill="#7C7474",
    outline="")

canvas.create_rectangle(
    296.0,
    1029.0,
    297.00001525878906,
    1292.0,
    fill="#7C7474",
    outline="")

canvas.create_rectangle(
    296.0,
    1454.0,
    297.00001525878906,
    1717.0,
    fill="#7C7474",
    outline="")

canvas.create_rectangle(
    901.0,
    604.0,
    902.0,
    867.0,
    fill="#7C7474",
    outline="")

canvas.create_rectangle(
    901.0,
    1029.0,
    902.0,
    1292.0,
    fill="#7C7474",
    outline="")

canvas.create_rectangle(
    901.0,
    1454.0,
    902.0,
    1717.0,
    fill="#7C7474",
    outline="")

canvas.create_rectangle(
    55.0,
    730.0,
    596.0,
    731.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    55.0,
    1155.0,
    596.0,
    1156.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    55.0,
    1580.0,
    596.0,
    1581.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    660.0,
    730.0,
    1201.0,
    731.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    660.0,
    1155.0,
    1201.0,
    1156.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    660.0,
    1580.0,
    1201.0,
    1581.0,
    fill="#000000",
    outline="")

canvas.create_text(
    67.0,
    653.0,
    anchor="nw",
    text="9:00-11:00",
    fill="#000000",
    font=("Poppins Regular", 32 * -1)
)

canvas.create_text(
    67.0,
    1078.0,
    anchor="nw",
    text="9:00-11:00",
    fill="#000000",
    font=("Poppins Regular", 32 * -1)
)

canvas.create_text(
    67.0,
    1503.0,
    anchor="nw",
    text="9:00-11:00",
    fill="#000000",
    font=("Poppins Regular", 32 * -1)
)

canvas.create_text(
    672.0,
    653.0,
    anchor="nw",
    text="9:00-11:00",
    fill="#000000",
    font=("Poppins Regular", 32 * -1)
)

canvas.create_text(
    672.0,
    1078.0,
    anchor="nw",
    text="9:00-11:00",
    fill="#000000",
    font=("Poppins Regular", 32 * -1)
)

canvas.create_text(
    672.0,
    1503.0,
    anchor="nw",
    text="9:00-11:00",
    fill="#000000",
    font=("Poppins Regular", 32 * -1)
)

canvas.create_text(
    67.0,
    779.0,
    anchor="nw",
    text="9:00-11:00",
    fill="#000000",
    font=("Poppins Regular", 32 * -1)
)

canvas.create_text(
    67.0,
    1204.0,
    anchor="nw",
    text="9:00-11:00",
    fill="#000000",
    font=("Poppins Regular", 32 * -1)
)

canvas.create_text(
    67.0,
    1629.0,
    anchor="nw",
    text="9:00-11:00",
    fill="#000000",
    font=("Poppins Regular", 32 * -1)
)

canvas.create_text(
    672.0,
    779.0,
    anchor="nw",
    text="9:00-11:00",
    fill="#000000",
    font=("Poppins Regular", 32 * -1)
)

canvas.create_text(
    672.0,
    1204.0,
    anchor="nw",
    text="9:00-11:00",
    fill="#000000",
    font=("Poppins Regular", 32 * -1)
)

canvas.create_text(
    672.0,
    1629.0,
    anchor="nw",
    text="9:00-11:00",
    fill="#000000",
    font=("Poppins Regular", 32 * -1)
)

canvas.create_text(
    355.0,
    779.0,
    anchor="nw",
    text="Language",
    fill="#000000",
    font=("Poppins Light", 32 * -1)
)

canvas.create_text(
    356.0,
    1204.0,
    anchor="nw",
    text="Designing",
    fill="#000000",
    font=("Poppins Light", 32 * -1)
)

canvas.create_text(
    345.0,
    1629.0,
    anchor="nw",
    text="Computing",
    fill="#000000",
    font=("Poppins Light", 32 * -1)
)

canvas.create_text(
    952.0,
    779.0,
    anchor="nw",
    text="Multimedia",
    fill="#000000",
    font=("Poppins Light", 32 * -1)
)

canvas.create_text(
    960.0,
    1204.0,
    anchor="nw",
    text="Language",
    fill="#000000",
    font=("Poppins Light", 32 * -1)
)

canvas.create_text(
    961.0,
    1629.0,
    anchor="nw",
    text="Designing",
    fill="#000000",
    font=("Poppins Light", 32 * -1)
)

canvas.create_text(
    348.0,
    653.0,
    anchor="nw",
    text="Computing",
    fill="#000000",
    font=("Poppins Light", 32 * -1)
)

canvas.create_text(
    348.0,
    1078.0,
    anchor="nw",
    text="Computing",
    fill="#000000",
    font=("Poppins Light", 32 * -1)
)

canvas.create_text(
    350.0,
    1503.0,
    anchor="nw",
    text="Multimedia",
    fill="#000000",
    font=("Poppins Light", 32 * -1)
)

canvas.create_text(
    965.0,
    653.0,
    anchor="nw",
    text="Marketing",
    fill="#000000",
    font=("Poppins Light", 32 * -1)
)

canvas.create_text(
    965.0,
    1078.0,
    anchor="nw",
    text="Marketing",
    fill="#000000",
    font=("Poppins Light", 32 * -1)
)

canvas.create_text(
    953.0,
    1503.0,
    anchor="nw",
    text="Computing",
    fill="#000000",
    font=("Poppins Light", 32 * -1)
)

canvas.create_text(
    226.0,
    653.0,
    anchor="nw",
    text="Am",
    fill="#000000",
    font=("Poppins Regular", 32 * -1)
)

canvas.create_text(
    226.0,
    1078.0,
    anchor="nw",
    text="Am",
    fill="#000000",
    font=("Poppins Regular", 32 * -1)
)

canvas.create_text(
    226.0,
    1503.0,
    anchor="nw",
    text="Am",
    fill="#000000",
    font=("Poppins Regular", 32 * -1)
)

canvas.create_text(
    831.0,
    653.0,
    anchor="nw",
    text="Am",
    fill="#000000",
    font=("Poppins Regular", 32 * -1)
)

canvas.create_text(
    831.0,
    1078.0,
    anchor="nw",
    text="Am",
    fill="#000000",
    font=("Poppins Regular", 32 * -1)
)

canvas.create_text(
    831.0,
    1503.0,
    anchor="nw",
    text="Am",
    fill="#000000",
    font=("Poppins Regular", 32 * -1)
)

canvas.create_text(
    226.0,
    779.0,
    anchor="nw",
    text="Am",
    fill="#000000",
    font=("Poppins Regular", 32 * -1)
)

canvas.create_text(
    226.0,
    1204.0,
    anchor="nw",
    text="Am",
    fill="#000000",
    font=("Poppins Regular", 32 * -1)
)

canvas.create_text(
    226.0,
    1629.0,
    anchor="nw",
    text="Am",
    fill="#000000",
    font=("Poppins Regular", 32 * -1)
)

canvas.create_text(
    831.0,
    779.0,
    anchor="nw",
    text="Am",
    fill="#000000",
    font=("Poppins Regular", 32 * -1)
)

canvas.create_text(
    831.0,
    1204.0,
    anchor="nw",
    text="Am",
    fill="#000000",
    font=("Poppins Regular", 32 * -1)
)

canvas.create_text(
    831.0,
    1629.0,
    anchor="nw",
    text="Am",
    fill="#000000",
    font=("Poppins Regular", 32 * -1)
)

canvas.create_rectangle(
    0.0,
    1891.0,
    1280.0,
    2157.0,
    fill="#3532A7",
    outline="")

canvas.create_text(
    31.0,
    1926.0,
    anchor="nw",
    text="VirtuEdu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 32 * -1)
)

canvas.create_text(
    471.0,
    1925.0,
    anchor="nw",
    text="Menu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 24 * -1)
)

canvas.create_text(
    705.0,
    1925.0,
    anchor="nw",
    text="Menu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 24 * -1)
)

canvas.create_text(
    975.0,
    1925.0,
    anchor="nw",
    text="Menu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 24 * -1)
)

canvas.create_text(
    53.0,
    1968.0,
    anchor="nw",
    text="Learn Anywhere, Achieve Everywhere",
    fill="#FFFFFF",
    font=("Poppins Regular", 11 * -1)
)

canvas.create_text(
    53.0,
    1993.0,
    anchor="nw",
    text="\nour innovative online learning platform empowers students to pursue their educational goals from anywhere in the \nworld. With flexible schedules and high-quality courses, we provide the tools and resources necessary for you to excel \nin your studies and succeed in any endeavor. Join our global community of learners and unlock your full potential with \n Virtu Edu.",
    fill="#FFFFFF",
    font=("Poppins Medium", 12 * -1)
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
    x=483.0,
    y=1968.0,
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
    relief="flat"
)
button_4.place(
    x=714.0,
    y=1965.0,
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
    relief="flat"
)
button_5.place(
    x=988.0,
    y=1965.0,
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
    relief="flat"
)
button_6.place(
    x=988.0,
    y=1990.0,
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
    relief="flat"
)
button_7.place(
    x=989.0,
    y=2015.0,
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
    relief="flat"
)
button_8.place(
    x=989.0,
    y=2040.0,
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
    relief="flat"
)
button_9.place(
    x=716.0,
    y=1990.0,
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
    relief="flat"
)
button_10.place(
    x=716.0,
    y=2015.0,
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
    relief="flat"
)
button_11.place(
    x=716.0,
    y=2040.0,
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
    relief="flat"
)
button_12.place(
    x=483.0,
    y=1993.0,
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
    relief="flat"
)
button_13.place(
    x=483.0,
    y=2018.0,
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
    relief="flat"
)
button_14.place(
    x=483.0,
    y=2043.0,
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
    relief="flat"
)
button_15.place(
    x=483.0,
    y=2068.0,
    width=39.0,
    height=15.0
)

canvas.create_text(
    31.0,
    1768.0,
    anchor="nw",
    text="Note: Computing class will be on LR 11, Multimedia class will be on LR 15, Designing will be on LR 13, Language class will be on LR 14 and Marketing course will take place on seminar hall.",
    fill="#FF0000",
    font=("Poppins Regular", 24 * -1)
)

button_image_16 = PhotoImage(
    file=("home.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=homefile,
    relief="flat"
)
canvas.create_window(385, 32, anchor="nw", window=button_16)


button_image_17 = PhotoImage(
    file=("button_17_copy.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=requestsfile,
    relief="flat"
)
canvas.create_window(615, 32, anchor="nw", window=button_17)


button_image_18 = PhotoImage(
    file=("button_18_copy.png"))
button_18 = Button(
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=homefile,
    relief="flat"
)
canvas.create_window(446, 32, anchor="nw", window=button_18)


button_image_19 = PhotoImage(
    file=("button_19_copy.png"))
button_19 = Button(
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    state="disabled",
    relief="flat"
)
canvas.create_window(524, 32, anchor="nw", window=button_19)


# Update the scroll region to include the entire frame
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

window.resizable(False, False)
window.mainloop()
