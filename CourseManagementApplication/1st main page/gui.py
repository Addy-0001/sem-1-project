from pathlib import Path
from tkinter import *
from PIL import *
from tkinter import ttk
window = Tk()
window.geometry("1280x1987")
window.configure(bg = "#EEEFF3")

canvas = Canvas(
    window,
    bg = "#EEEFF3",
    height = 1987,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x=0,y=0)

label = LabelFrame(canvas)




def on_mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta/120)), "units")



# Create a Canvas widget with a scrollbar
canvas = Canvas(window, height=290)
scrollbar = Scrollbar(window, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
canvas.pack(fill="both", expand=True)

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
    canvas,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
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
    command=lambda: print("notification clicked"),
    relief="flat"
)
button_2.place(
    x=1100.0,
    y=31.615699768066406,
    width=29.694091796875,
    height=29.550003051757812
)

button_image_3 = PhotoImage(
    file=("home.png"))
button_3 = Button(
    canvas,
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=388.0,
    y=31.0,
    width=61.0,
    height=28.0
)

button_image_4 = PhotoImage(
    file=("routines.png"))
button_4 = Button(
    canvas,
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat",
  
)
button_4.place(
    x=546.0,
    y=34.0,
    width=65.0,
    height=20.0
)

button_image_5 = PhotoImage(
    file=("requests.png"))
button_5 = Button(
    canvas,
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=628.0,
    y=31.0,
    width=65.0,
    height=20.0
)

button_image_6 = PhotoImage(
    file=("courses.png"))
button_6 = Button(
    canvas,
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Course Button Clicked"),
    relief="flat"
)
button_6.place(
    x=459.0,
    y=28.0,
    width=69.0,
    height=30.0
)

image_image_1 = PhotoImage(
    file=("image_1.png"))
image_1 = canvas.create_image(
    326.0,
    299.6911163330078,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=("image_2.png"))
image_2 = canvas.create_image(
    883.0,
    339.415283203125,
    image=image_image_2
)

button_image_7 = PhotoImage(
    file=("computing.png"))
button_7 = Button(
    canvas,
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=400.0,
    y=457.0,
    width=114.0,
    height=35.0
)

button_image_8 = PhotoImage(
    file=("all.png"))
button_8 = Button(
    canvas,
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=260.0,
    y=456.0,
    width=121.0,
    height=35.0
)

button_image_9 = PhotoImage(
    file=("button_9.png"))
button_9 = Button(
    canvas,
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=526.0,
    y=457.0,
    width=115.0,
    height=35.0
)

button_image_10 = PhotoImage(
    file=("button_10.png"))
button_10 = Button(
    canvas,
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=660.0,
    y=457.0,
    width=106.0,
    height=35.0
)

button_image_11 = PhotoImage(
    file=("button_11.png"))
button_11 = Button(
    canvas,
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
    relief="flat"
)
button_11.place(
    x=785.0,
    y=457.0,
    width=121.0,
    height=35.0
)

button_image_12 = PhotoImage(
    file=("button_12.png"))
button_12 = Button(
    canvas,
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_12 clicked"),
    relief="flat"
)
button_12.place(
    x=925.0,
    y=457.0,
    width=121.0,
    height=35.0
)

canvas.create_text(
    797.0,
    195.0,
    anchor="nw",
    text="\nour Courses",
    fill="#3D4AC0",
    font=("OpenSans Bold", 60 * -1)
)

canvas.create_text(
    794.0,
    285.0,
    anchor="nw",
    text="Unlock your potential with \nour transformative courses.",
    fill="#646ECB",
    font=("Poppins Regular", 15 * -1)
)

canvas.create_rectangle(
    94.0,
    531.0,
    336.0,
    775.0,
    fill="#FFFFFF",
    outline="")

image_image_3 = PhotoImage(
    file=("image_3.png"))
image_3 = canvas.create_image(
    215.0,
    593.0,
    image=image_image_3
)

canvas.create_text(
    107.0,
    691.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

button_image_13 = PhotoImage(
    file=("button_13.png"))
button_13 = Button(
    canvas,
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_13 clicked"),
    relief="flat"
)
button_13.place(
    x=107.0,
    y=661.12548828125,
    width=87.0,
    height=11.9024658203125
)

entry_image_3 = PhotoImage(
    file=("entry_3.png"))
entry_bg_3 = canvas.create_image(
    215.01956176757812,
    684.5987854003906,
    image=entry_image_3
)
entry_3 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=108.0,
    y=679.8292236328125,
    width=214.03912353515625,
    height=7.53912353515625
)

button_image_14 = PhotoImage(
    file=("button_14.png"))
button_14 = Button(
    canvas,
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_14 clicked"),
    relief="flat"
)
button_14.place(
    x=108.0,
    y=747.79443359375,
    width=66.7545166015625,
    height=18.0740966796875
)

canvas.create_text(
    107.0,
    708.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with \nour Introduction to User Experience Design course. Dive into the \nworld of interactive design, learn the fundamentals of user-centered \nthinking, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_rectangle(
    396.0,
    531.0,
    638.0,
    775.0,
    fill="#FFFFFF",
    outline="")

image_image_4 = PhotoImage(
    file=("image_4.png"))
image_4 = canvas.create_image(
    517.0,
    593.0,
    image=image_image_4
)

canvas.create_text(
    409.0,
    691.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

button_image_15 = PhotoImage(
    file=("button_15.png"))
button_15 = Button(
    canvas,
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_15 clicked"),
    relief="flat"
)
button_15.place(
    x=409.0,
    y=661.12548828125,
    width=87.0,
    height=11.9024658203125
)

entry_image_4 = PhotoImage(
    file=("entry_4.png"))
entry_bg_4 = canvas.create_image(
    517.0195617675781,
    684.5987854003906,
    image=entry_image_4
)
entry_4 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=410.0,
    y=679.8292236328125,
    width=214.03912353515625,
    height=7.53912353515625
)

button_image_16 = PhotoImage(
    file=("button_16.png"))
button_16 = Button(
    canvas,
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_16 clicked"),
    relief="flat"
)
button_16.place(
    x=410.0,
    y=747.79443359375,
    width=66.7545166015625,
    height=18.0740966796875
)

canvas.create_text(
    409.0,
    708.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with \nour Introduction to User Experience Design course. Dive into the \nworld of interactive design, learn the fundamentals of user-centered \nthinking, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_rectangle(
    678.0,
    531.0,
    920.0,
    775.0,
    fill="#FFFFFF",
    outline="")

image_image_5 = PhotoImage(
    file=("image_5.png"))
image_5 = canvas.create_image(
    799.0,
    593.0,
    image=image_image_5
)

canvas.create_text(
    691.0,
    691.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

button_image_17 = PhotoImage(
    file=("button_17.png"))
button_17 = Button(
    canvas,
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_17 clicked"),
    relief="flat"
)
button_17.place(
    x=691.0,
    y=661.12548828125,
    width=87.0,
    height=11.9024658203125
)

entry_image_5 = PhotoImage(
    file=("entry_5.png"))
entry_bg_5 = canvas.create_image(
    799.0195617675781,
    684.5987854003906,
    image=entry_image_5
)
entry_5 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=692.0,
    y=679.8292236328125,
    width=214.03912353515625,
    height=7.53912353515625
)

button_image_18 = PhotoImage(
    file=("button_18.png"))
button_18 = Button(
    canvas,
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_18 clicked"),
    relief="flat"
)
button_18.place(
    x=692.0,
    y=747.79443359375,
    width=66.7545166015625,
    height=18.0740966796875
)

canvas.create_text(
    691.0,
    708.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with \nour Introduction to User Experience Design course. Dive into the \nworld of interactive design, learn the fundamentals of user-centered \nthinking, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_rectangle(
    967.0,
    531.0,
    1209.0,
    775.0,
    fill="#FFFFFF",
    outline="")

image_image_6 = PhotoImage(
    file=("image_6.png"))
image_6 = canvas.create_image(
    1088.0,
    593.0,
    image=image_image_6
)

canvas.create_text(
    980.0,
    691.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

button_image_19 = PhotoImage(
    file=("button_19.png"))
button_19 = Button(
    canvas,
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_19 clicked"),
    relief="flat"
)
button_19.place(
    x=980.0,
    y=661.12548828125,
    width=87.0,
    height=11.9024658203125
)

entry_image_6 = PhotoImage(
    file=("entry_6.png"))
entry_bg_6 = canvas.create_image(
    1088.01953125,
    684.5987854003906,
    image=entry_image_6
)
entry_6 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=981.0,
    y=679.8292236328125,
    width=214.0390625,
    height=7.53912353515625
)

button_image_20 = PhotoImage(
    file=("button_20.png"))
button_20 = Button(
    canvas,
    image=button_image_20,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_20 clicked"),
    relief="flat"
)
button_20.place(
    x=981.0,
    y=747.79443359375,
    width=66.7545166015625,
    height=18.0740966796875
)

canvas.create_text(
    980.0,
    708.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with \nour Introduction to User Experience Design course. Dive into the \nworld of interactive design, learn the fundamentals of user-centered \nthinking, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_rectangle(
    96.0,
    814.0,
    338.0,
    1058.0,
    fill="#FFFFFF",
    outline="")

image_image_7 = PhotoImage(
    file=("image_7.png"))
image_7 = canvas.create_image(
    217.0,
    876.0,
    image=image_image_7
)

canvas.create_text(
    109.0,
    974.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)
#overflow part
button_image_21 = PhotoImage(
    file=("button_21.png"))
button_21 = Button(
    canvas,
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_21 clicked"),
    relief="flat"
)
button_21.place(
    x=109.0,
    y=944.12548828125,
    width=87.0,
    height=11.9024658203125
)

entry_image_7 = PhotoImage(
    file=("entry_7.png"))
entry_bg_7 = canvas.create_image(
    217.01956176757812,
    967.5987854003906,
    image=entry_image_7
)
entry_7 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=110.0,
    y=962.8292236328125,
    width=214.03912353515625,
    height=7.53912353515625
)

button_image_22 = PhotoImage(
    file=("button_22.png"))
button_22 = Button(
    canvas,
    image=button_image_22,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_22 clicked"),
    relief="flat"
)
button_22.place(
    x=110.0,
    y=1030.79443359375,
    width=66.7545166015625,
    height=18.0740966796875
)

canvas.create_text(
    109.0,
    991.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with \nour Introduction to User Experience Design course. Dive into the \nworld of interactive design, learn the fundamentals of user-centered \nthinking, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_rectangle(
    398.0,
    814.0,
    640.0,
    1058.0,
    fill="#FFFFFF",
    outline="")

image_image_8 = PhotoImage(
    file=("image_8.png"))
image_8 = canvas.create_image(
    519.0,
    876.0,
    image=image_image_8
)

canvas.create_text(
    411.0,
    974.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

button_image_23 = PhotoImage(
    file=("button_23.png"))
button_23 = Button(
    canvas,
    image=button_image_23,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_23 clicked"),
    relief="flat"
)
button_23.place(
    x=411.0,
    y=944.12548828125,
    width=87.0,
    height=11.9024658203125
)

entry_image_8 = PhotoImage(
    file=("entry_8.png"))
entry_bg_8 = canvas.create_image(
    519.0195617675781,
    967.5987854003906,
    image=entry_image_8
)
entry_8 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=412.0,
    y=962.8292236328125,
    width=214.03912353515625,
    height=7.53912353515625
)

button_image_24 = PhotoImage(
    file=("button_24.png"))
button_24 = Button(
    canvas,
    image=button_image_24,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_24 clicked"),
    relief="flat"
)
button_24.place(
    x=412.0,
    y=1030.79443359375,
    width=66.7545166015625,
    height=18.0740966796875
)

canvas.create_text(
    411.0,
    991.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with \nour Introduction to User Experience Design course. Dive into the \nworld of interactive design, learn the fundamentals of user-centered \nthinking, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_rectangle(
    680.0,
    814.0,
    922.0,
    1058.0,
    fill="#FFFFFF",
    outline="")

image_image_9 = PhotoImage(
    file=("image_9.png"))
image_9 = canvas.create_image(
    801.0,
    876.0,
    image=image_image_9
)

canvas.create_text(
    693.0,
    974.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

button_image_25 = PhotoImage(
    file=("button_25.png"))
button_25 = Button(
    canvas,
    image=button_image_25,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_25 clicked"),
    relief="flat"
)
button_25.place(
    x=693.0,
    y=944.12548828125,
    width=87.0,
    height=11.9024658203125
)

entry_image_9 = PhotoImage(
    file=("entry_9.png"))
entry_bg_9 = canvas.create_image(
    801.0195617675781,
    967.5987854003906,
    image=entry_image_9
)
entry_9 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_9.place(
    x=694.0,
    y=962.8292236328125,
    width=214.03912353515625,
    height=7.53912353515625
)

button_image_26 = PhotoImage(
    file=("button_26.png"))
button_26 = Button(
    canvas,
    image=button_image_26,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_26 clicked"),
    relief="flat"
)
button_26.place(
    x=694.0,
    y=1030.79443359375,
    width=66.7545166015625,
    height=18.0740966796875
)

canvas.create_text(
    693.0,
    991.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with \nour Introduction to User Experience Design course. Dive into the \nworld of interactive design, learn the fundamentals of user-centered \nthinking, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_rectangle(
    969.0,
    814.0,
    1211.0,
    1058.0,
    fill="#FFFFFF",
    outline="")

image_image_10 = PhotoImage(
    file=("image_10.png"))
image_10 = canvas.create_image(
    1090.0,
    876.0,
    image=image_image_10
)

canvas.create_text(
    982.0,
    974.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

button_image_27 = PhotoImage(
    file=("button_27.png"))
button_27 = Button(
    canvas,
    image=button_image_27,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_27 clicked"),
    relief="flat"
)
button_27.place(
    x=982.0,
    y=944.12548828125,
    width=87.0,
    height=11.9024658203125
)

entry_image_10 = PhotoImage(
    file=("entry_10.png"))
entry_bg_10 = canvas.create_image(
    1090.01953125,
    967.5987854003906,
    image=entry_image_10
)
entry_10 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_10.place(
    x=983.0,
    y=962.8292236328125,
    width=214.0390625,
    height=7.53912353515625
)

button_image_28 = PhotoImage(
    file=("button_28.png"))
button_28 = Button(
    canvas,
    image=button_image_28,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_28 clicked"),
    relief="flat"
)
button_28.place(
    x=983.0,
    y=1030.79443359375,
    width=66.7545166015625,
    height=18.0740966796875
)

canvas.create_text(
    982.0,
    991.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with \nour Introduction to User Experience Design course. Dive into the \nworld of interactive design, learn the fundamentals of user-centered \nthinking, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_rectangle(
    96.0,
    1094.0,
    338.0,
    1338.0,
    fill="#FFFFFF",
    outline="")

image_image_11 = PhotoImage(
    file=("image_11.png"))
image_11 = canvas.create_image(
    217.0,
    1156.0,
    image=image_image_11
)

canvas.create_text(
    109.0,
    1254.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

button_image_29 = PhotoImage(
    file=("button_29.png"))
button_29 = Button(
    canvas,
    image=button_image_29,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_29 clicked"),
    relief="flat"
)
button_29.place(
    x=109.0,
    y=1224.12548828125,
    width=87.0,
    height=11.9024658203125
)

entry_image_11 = PhotoImage(
    file=("entry_11.png"))
entry_bg_11 = canvas.create_image(
    217.01956176757812,
    1247.5987548828125,
    image=entry_image_11
)
entry_11 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_11.place(
    x=110.0,
    y=1242.8292236328125,
    width=214.03912353515625,
    height=7.5390625
)

button_image_30 = PhotoImage(
    file=("button_30.png"))
button_30 = Button(
    canvas,
    image=button_image_30,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_30 clicked"),
    relief="flat"
)
button_30.place(
    x=110.0,
    y=1310.79443359375,
    width=66.7545166015625,
    height=18.0740966796875
)

canvas.create_text(
    109.0,
    1271.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with \nour Introduction to User Experience Design course. Dive into the \nworld of interactive design, learn the fundamentals of user-centered \nthinking, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_rectangle(
    398.0,
    1094.0,
    640.0,
    1338.0,
    fill="#FFFFFF",
    outline="")

image_image_12 = PhotoImage(
    file=("image_12.png"))
image_12 = canvas.create_image(
    519.0,
    1156.0,
    image=image_image_12
)

canvas.create_text(
    411.0,
    1254.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

button_image_31 = PhotoImage(
    file=("button_31.png"))
button_31 = Button(
    canvas,
    image=button_image_31,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_31 clicked"),
    relief="flat"
)
button_31.place(
    x=411.0,
    y=1224.12548828125,
    width=87.0,
    height=11.9024658203125
)

entry_image_12 = PhotoImage(
    file=("entry_12.png"))
entry_bg_12 = canvas.create_image(
    519.0195617675781,
    1247.5987548828125,
    image=entry_image_12
)
entry_12 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_12.place(
    x=412.0,
    y=1242.8292236328125,
    width=214.03912353515625,
    height=7.5390625
)

button_image_32 = PhotoImage(
    file=("button_32.png"))
button_32 = Button(
    canvas,
    image=button_image_32,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_32 clicked"),
    relief="flat"
)
button_32.place(
    x=412.0,
    y=1310.79443359375,
    width=66.7545166015625,
    height=18.0740966796875
)

canvas.create_text(
    411.0,
    1271.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with \nour Introduction to User Experience Design course. Dive into the \nworld of interactive design, learn the fundamentals of user-centered \nthinking, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_rectangle(
    680.0,
    1094.0,
    922.0,
    1338.0,
    fill="#FFFFFF",
    outline="")

image_image_13 = PhotoImage(
    file=("image_13.png"))
image_13 = canvas.create_image(
    801.0,
    1156.0,
    image=image_image_13
)

canvas.create_text(
    693.0,
    1254.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

button_image_33 = PhotoImage(
    file=("button_33.png"))
button_33 = Button(
    canvas,
    image=button_image_33,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_33 clicked"),
    relief="flat"
)
button_33.place(
    x=693.0,
    y=1224.12548828125,
    width=87.0,
    height=11.9024658203125
)

entry_image_13 = PhotoImage(
    file=("entry_13.png"))
entry_bg_13 = canvas.create_image(
    801.0195617675781,
    1247.5987548828125,
    image=entry_image_13
)
entry_13 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_13.place(
    x=694.0,
    y=1242.8292236328125,
    width=214.03912353515625,
    height=7.5390625
)

button_image_34 = PhotoImage(
    file=("button_34.png"))
button_34 = Button(
    canvas,
    image=button_image_34,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_34 clicked"),
    relief="flat"
)
button_34.place(
    x=694.0,
    y=1310.79443359375,
    width=66.7545166015625,
    height=18.0740966796875
)

canvas.create_text(
    693.0,
    1271.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with \nour Introduction to User Experience Design course. Dive into the \nworld of interactive design, learn the fundamentals of user-centered \nthinking, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_rectangle(
    969.0,
    1094.0,
    1211.0,
    1338.0,
    fill="#FFFFFF",
    outline="")

image_image_14 = PhotoImage(
    file=("image_14.png"))
image_14 = canvas.create_image(
    1090.0,
    1156.0,
    image=image_image_14
)

canvas.create_text(
    982.0,
    1254.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

button_image_35 = PhotoImage(
    file=("button_35.png"))
button_35 = Button(
    canvas,
    image=button_image_35,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_35 clicked"),
    relief="flat"
)
button_35.place(
    x=982.0,
    y=1224.12548828125,
    width=87.0,
    height=11.9024658203125
)

entry_image_14 = PhotoImage(
    file=("entry_14.png"))
entry_bg_14 = canvas.create_image(
    1090.01953125,
    1247.5987548828125,
    image=entry_image_14
)
entry_14 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_14.place(
    x=983.0,
    y=1242.8292236328125,
    width=214.0390625,
    height=7.5390625
)

image_image_15 = PhotoImage(
    file=("image_15.png"))
image_15 = canvas.create_image(
    1016.0,
    1319.79443359375,
    image=image_image_15
)

canvas.create_text(
    982.0,
    1271.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with \nour Introduction to User Experience Design course. Dive into the \nworld of interactive design, learn the fundamentals of user-centered \nthinking, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_rectangle(
    98.0,
    1377.0,
    340.0,
    1621.0,
    fill="#FFFFFF",
    outline="")

image_image_16 = PhotoImage(
    file=("image_16.png"))
image_16 = canvas.create_image(
    219.0,
    1439.0,
    image=image_image_16
)

canvas.create_text(
    111.0,
    1537.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

button_image_36 = PhotoImage(
    file=("button_36.png"))
button_36 = Button(
    canvas,
    image=button_image_36,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_36 clicked"),
    relief="flat"
)
button_36.place(
    x=111.0,
    y=1507.12548828125,
    width=87.0,
    height=11.9024658203125
)

entry_image_15 = PhotoImage(
    file=("entry_15.png"))
entry_bg_15 = canvas.create_image(
    219.01956176757812,
    1530.5987548828125,
    image=entry_image_15
)
entry_15 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_15.place(
    x=112.0,
    y=1525.8292236328125,
    width=214.03912353515625,
    height=7.5390625
)

button_image_37 = PhotoImage(
    file=("button_37.png"))
button_37 = Button(
    canvas,
    image=button_image_37,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_37 clicked"),
    relief="flat"
)
button_37.place(
    x=112.0,
    y=1593.79443359375,
    width=66.7545166015625,
    height=18.0740966796875
)

canvas.create_text(
    111.0,
    1554.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with \nour Introduction to User Experience Design course. Dive into the \nworld of interactive design, learn the fundamentals of user-centered \nthinking, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_rectangle(
    400.0,
    1377.0,
    642.0,
    1621.0,
    fill="#FFFFFF",
    outline="")

image_image_17 = PhotoImage(
    file=("image_17.png"))
image_17 = canvas.create_image(
    521.0,
    1439.0,
    image=image_image_17
)

canvas.create_text(
    413.0,
    1537.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

button_image_38 = PhotoImage(
    file=("button_38.png"))
button_38 = Button(
    canvas,
    image=button_image_38,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_38 clicked"),
    relief="flat"
)
button_38.place(
    x=413.0,
    y=1507.12548828125,
    width=87.0,
    height=11.9024658203125
)

entry_image_16 = PhotoImage(
    file=("entry_16.png"))
entry_bg_16 = canvas.create_image(
    521.0195617675781,
    1530.5987548828125,
    image=entry_image_16
)
entry_16 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_16.place(
    x=414.0,
    y=1525.8292236328125,
    width=214.03912353515625,
    height=7.5390625
)

button_image_39 = PhotoImage(
    file=("button_39.png"))
button_39 = Button(
    canvas,
    image=button_image_39,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_39 clicked"),
    relief="flat"
)
button_39.place(
    x=414.0,
    y=1593.79443359375,
    width=66.7545166015625,
    height=18.0740966796875
)

canvas.create_text(
    413.0,
    1554.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with \nour Introduction to User Experience Design course. Dive into the \nworld of interactive design, learn the fundamentals of user-centered \nthinking, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_rectangle(
    682.0,
    1377.0,
    924.0,
    1621.0,
    fill="#FFFFFF",
    outline="")

image_image_18 = PhotoImage(
    file=("image_18.png"))
image_18 = canvas.create_image(
    803.0,
    1439.0,
    image=image_image_18
)

canvas.create_text(
    695.0,
    1537.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

button_image_40 = PhotoImage(
    file=("button_40.png"))
button_40 = Button(
    canvas,
    image=button_image_40,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_40 clicked"),
    relief="flat"
)
button_40.place(
    x=695.0,
    y=1507.12548828125,
    width=87.0,
    height=11.9024658203125
)

entry_image_17 = PhotoImage(
    file=("entry_17.png"))
entry_bg_17 = canvas.create_image(
    803.0195617675781,
    1530.5987548828125,
    image=entry_image_17
)
entry_17 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_17.place(
    x=696.0,
    y=1525.8292236328125,
    width=214.03912353515625,
    height=7.5390625
)

button_image_41 = PhotoImage(
    file=("button_41.png"))
button_41 = Button(
    canvas,
    image=button_image_41,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_41 clicked"),
    relief="flat"
)
button_41.place(
    x=696.0,
    y=1593.79443359375,
    width=66.7545166015625,
    height=18.0740966796875
)

canvas.create_text(
    695.0,
    1554.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with \nour Introduction to User Experience Design course. Dive into the \nworld of interactive design, learn the fundamentals of user-centered \nthinking, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_rectangle(
    971.0,
    1377.0,
    1213.0,
    1621.0,
    fill="#FFFFFF",
    outline="")

image_image_19 = PhotoImage(
    file=("image_19.png"))
image_19 = canvas.create_image(
    1092.0,
    1439.0,
    image=image_image_19
)

canvas.create_text(
    984.0,
    1537.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

button_image_42 = PhotoImage(
    file=("button_42.png"))
button_42 = Button(
    canvas,
    image=button_image_42,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_42 clicked"),
    relief="flat"
)
button_42.place(
    x=984.0,
    y=1507.12548828125,
    width=87.0,
    height=11.9024658203125
)

entry_image_18 = PhotoImage(
    file=("entry_18.png"))
entry_bg_18 = canvas.create_image(
    1092.01953125,
    1530.5987548828125,
    image=entry_image_18
)
entry_18 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_18.place(
    x=985.0,
    y=1525.8292236328125,
    width=214.0390625,
    height=7.5390625
)

button_image_43 = PhotoImage(
    file=("button_43.png"))
button_43 = Button(
    canvas,
    image=button_image_43,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_43 clicked"),
    relief="flat"
)
button_43.place(
    x=985.0,
    y=1593.79443359375,
    width=66.7545166015625,
    height=18.0740966796875
)

canvas.create_text(
    984.0,
    1554.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with \nour Introduction to User Experience Design course. Dive into the \nworld of interactive design, learn the fundamentals of user-centered \nthinking, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_rectangle(
    457.0,
    1644.0,
    917.0,
    1689.0,
    fill="#FFFFFF",
    outline="")

button_image_44 = PhotoImage(
    file=("button_44.png"))
button_44 = Button(
    canvas,
    image=button_image_44,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_44 clicked"),
    relief="flat"
)
button_44.place(
    x=457.0,
    y=1644.0,
    width=47.0,
    height=45.0
)

button_image_45 = PhotoImage(
    file=("button_45.png"))
button_45 = Button(
    canvas,
    image=button_image_45,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_45 clicked"),
    relief="flat"
)
button_45.place(
    x=504.0,
    y=1644.0,
    width=47.0,
    height=45.0
)

button_image_46 = PhotoImage(
    file=("button_46.png"))
button_46 = Button(
    canvas,
    image=button_image_46,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_46 clicked"),
    relief="flat"
)
button_46.place(
    x=550.0,
    y=1644.0,
    width=47.0,
    height=45.0
)

button_image_47 = PhotoImage(
    file=("button_47.png"))
button_47 = Button(
    canvas,
    image=button_image_47,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_47 clicked"),
    relief="flat"
)
button_47.place(
    x=596.0,
    y=1644.0,
    width=47.0,
    height=45.0
)

button_image_48 = PhotoImage(
    file=("button_48.png"))
button_48 = Button(
    canvas,
    image=button_image_48,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_48 clicked"),
    relief="flat"
)
button_48.place(
    x=744.0,
    y=1644.0,
    width=47.0,
    height=45.0
)

button_image_49 = PhotoImage(
    file=("button_49.png"))
button_49 = Button(
    canvas,
    image=button_image_49,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_49 clicked"),
    relief="flat"
)
button_49.place(
    x=828.0,
    y=1644.0,
    width=92.0,
    height=45.0
)

button_image_50 = PhotoImage(
    file=("button_50.png"))
button_50 = Button(
    canvas,
    image=button_image_50,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_50 clicked"),
    relief="flat"
)
button_50.place(
    x=790.0,
    y=1644.0,
    width=47.0,
    height=45.0
)

button_image_51 = PhotoImage(
    file=("button_51.png"))
button_51 = Button(
    canvas,
    image=button_image_51,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_51 clicked"),
    relief="flat"
)
button_51.place(
    x=642.0,
    y=1644.0,
    width=103.0,
    height=45.0
)

canvas.create_rectangle(
    0.0,
    1748.0,
    1280.0,
    1987.0,
    fill="#3532A7",
    outline="")

canvas.create_text(
    56.0,
    1776.0,
    anchor="nw",
    text="VirtuEdu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 25 * -1)
)

canvas.create_text(
    461.0,
    1785.0,
    anchor="nw",
    text="Menu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 17 * -1)
)

canvas.create_text(
    745.0,
    1787.0,
    anchor="nw",
    text="Menu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 17 * -1)
)

canvas.create_text(
    974.0,
    1787.0,
    anchor="nw",
    text="Menu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 17 * -1)
)

canvas.create_text(
    63.0,
    1804.0,
    anchor="nw",
    text="Learn Anywhere, Achieve Everywhere",
    fill="#FFFFFF",
    font=("Poppins Regular", 6 * -1)
)

canvas.create_text(
    63.0,
    1824.0,
    anchor="nw",
    text="\nour innovative online learning platform empowers students to pursue their educational goals from anywhere in the \nworld. With flexible schedules and high-quality courses, we provide the tools and resources necessary for you to excel in your studies and succeed in any endeavor. Join \nour global community of learners and unlock your full potential with Virtu Edu.",
    fill="#FFFFFF",
    font=("Poppins Medium", 6 * -1)
)

button_image_52 = PhotoImage(
    file=("button_52.png"))
button_52 = Button(
    canvas,
    image=button_image_52,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_52 clicked"),
    relief="flat"
)
button_52.place(
    x=464.0,
    y=1817.0,
    width=41.0,
    height=18.0
)

button_image_53 = PhotoImage(
    file=("button_53.png"))
button_53 = Button(
    canvas,
    image=button_image_53,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_53 clicked"),
    relief="flat"
)
button_53.place(
    x=464.0,
    y=1835.0,
    width=41.0,
    height=18.0
)

button_image_54 = PhotoImage(
    file=("button_54.png"))
button_54 = Button(
    canvas,
    image=button_image_54,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_54 clicked"),
    relief="flat"
)
button_54.place(
    x=464.0,
    y=1853.0,
    width=41.0,
    height=18.0
)

button_image_55 = PhotoImage(
    file=("button_55.png"))
button_55 = Button(
    canvas,
    image=button_image_55,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_55 clicked"),
    relief="flat"
)
button_55.place(
    x=464.0,
    y=1871.0,
    width=41.0,
    height=18.0
)

button_image_56 = PhotoImage(
    file=("button_56.png"))
button_56 = Button(
    canvas,
    image=button_image_56,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_56 clicked"),
    relief="flat"
)
button_56.place(
    x=464.0,
    y=1889.0,
    width=41.0,
    height=18.0
)

button_image_57 = PhotoImage(
    file=("button_57.png"))
button_57 = Button(
    canvas,
    image=button_image_57,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_57 clicked"),
    relief="flat"
)
button_57.place(
    x=756.0,
    y=1817.0,
    width=75.0,
    height=15.0
)

button_image_58 = PhotoImage(
    file=("button_58.png"))
button_58 = Button(
    canvas,
    image=button_image_58,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_58 clicked"),
    relief="flat"
)
button_58.place(
    x=756.0,
    y=1832.0,
    width=75.0,
    height=15.0
)

button_image_59 = PhotoImage(
    file=("button_59.png"))
button_59 = Button(
    canvas,
    image=button_image_59,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_59 clicked"),
    relief="flat"
)
button_59.place(
    x=756.0,
    y=1847.0,
    width=75.0,
    height=15.0
)

button_image_60 = PhotoImage(
    file=("button_60.png"))
button_60 = Button(
    canvas,
    image=button_image_60,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_60 clicked"),
    relief="flat"
)
button_60.place(
    x=756.0,
    y=1862.0,
    width=75.0,
    height=15.0
)

button_image_61 = PhotoImage(
    file=("button_61.png"))
button_61 = Button(
    canvas,
    image=button_image_61,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_61 clicked"),
    relief="flat"
)
button_61.place(
    x=979.0,
    y=1817.0,
    width=40.0,
    height=13.0
)

button_image_62 = PhotoImage(
    file=("button_62.png"))
button_62 = Button(
    canvas,
    image=button_image_62,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_62 clicked"),
    relief="flat"
)
button_62.place(
    x=979.0,
    y=1830.0,
    width=40.0,
    height=13.0
)

button_image_63 = PhotoImage(
    file=("button_63.png"))
button_63 = Button(
    canvas,
    image=button_image_63,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_63 clicked"),
    relief="flat"
)
button_63.place(
    x=979.0,
    y=1843.0,
    width=40.0,
    height=13.0
)

button_image_64 = PhotoImage(
    file=("button_64.png"))
button_64 = Button(
    canvas,
    image=button_image_64,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_64 clicked"),
    relief="flat"
)
button_64.place(
    x=979.0,
    y=1856.0,
    width=75.0,
    height=13.0
)

window.resizable(False, False)
window.mainloop()
