

from pathlib import Path


from tkinter import *


from tkinter import ttk


window = Tk()

window.geometry("1280x2026")
window.configure(bg = "#EEEFF3")


canvas = Canvas(
    window,
    bg = "#EEEFF3",
    height = 2026,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"

)

canvas.place(x = 0, y = 0)


Yscroll = Scrollbar(window)
Yscroll.pack(side=RIGHT, fill=Y)
canvas.create_rectangle(
    
    0.0,
    4.0,
    1282.0,
    450.0,
    fill="#82B4FF",
    outline="")

canvas.create_text(
  
    54.0,
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
    canvas,
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=717.0,
    y=16.0,
    width=275.0,
    height=32.0
)

button_image_2 = PhotoImage(
    file=("notification.png"))
button_2 = Button(
    canvas,
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
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
    relief="flat"
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
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=459.0,
    y=31.0,
    width=61.0,
    height=28.0
)

image_image_1 = PhotoImage(
    file=("image_1.png"))
image_1 = canvas.create_image(
    1206.0,
    274.433837890625,
    image=image_image_1
)

canvas.create_text(
    76.0,
    199.0,
    anchor="nw",
    text="VirtuEdu",
    fill="#3D4BCF",
    font=("OpenSans Bold", 60 * -1)
)

canvas.create_text(
    80.0,
    273.0,
    anchor="nw",
    text="Learn Anywhere, Achieve Everywhere",
    fill="#3D4BCF",
    font=("Poppins Regular", 24 * -1)
)

canvas.create_rectangle(
    94.0,
    531.0,
    336.0,
    775.0,
    fill="#FFFFFF",
    outline="")

image_image_2 = PhotoImage(
    file=("image_2.png"))
image_2 = canvas.create_image(
    215.0,
    593.0,
    image=image_image_2
)

canvas.create_text(
    107.0,
    691.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

button_image_7 = PhotoImage(
    file=("button_7.png"))
button_7 = Button(
    canvas,
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=107.0,
    y=661.12548828125,
    width=87.0,
    height=11.902435302734375
)

image_image_3 = PhotoImage(
    file=("image_3.png"))
image_3 = canvas.create_image(
    215.0,
    683.8292236328125,
    image=image_image_3
)

button_image_8 = PhotoImage(
    file=("button_8.png"))
button_8 = Button(
    canvas,
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=108.0,
    y=747.79443359375,
    width=66.7545166015625,
    height=18.074081420898438
)

canvas.create_text(
    107.0,
    708.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with our Introduction to User Experience Design course. Dive into the world of interactive design, learn the fundamentals of user-centered thinking, and acquire the skills to create intuitive",
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

image_image_4 = PhotoImage(
    file=("image_4.png"))
image_4 = canvas.create_image(
    217.0,
    876.0,
    image=image_image_4
)

canvas.create_text(
    109.0,
    974.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
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
    x=109.0,
    y=944.12548828125,
    width=87.0,
    height=11.90243911743164
)

image_image_5 = PhotoImage(
    file=("image_5.png"))
image_5 = canvas.create_image(
    217.0,
    966.8292236328125,
    image=image_image_5
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
    x=110.0,
    y=1030.79443359375,
    width=66.7545166015625,
    height=18.074073791503906
)

canvas.create_text(
    109.0,
    991.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with our Introduction to User Experience Design course. Dive into the world of interactive design, learn the fundamentals of user-centered thinking, and acquire the skills to create intuitive,",
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

image_image_6 = PhotoImage(
    file=("image_6.png"))
image_6 = canvas.create_image(
    517.0,
    593.0,
    image=image_image_6
)

canvas.create_text(
    409.0,
    691.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
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
    x=409.0,
    y=661.12548828125,
    width=87.0,
    height=11.902435302734375
)

image_image_7 = PhotoImage(
    file=("image_7.png"))
image_7 = canvas.create_image(
    517.0,
    683.8292236328125,
    image=image_image_7
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
    x=410.0,
    y=747.79443359375,
    width=66.7545166015625,
    height=18.074081420898438
)

canvas.create_text(
    409.0,
    708.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with our Introduction to User Experience Design course. Dive into the world of interactive design, learn the fundamentals of user-centered thinking, and acquire the skills to create intuitive,",
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
    x=411.0,
    y=944.12548828125,
    width=87.0,
    height=11.90243911743164
)

image_image_9 = PhotoImage(
    file=("image_9.png"))
image_9 = canvas.create_image(
    519.0,
    966.8292236328125,
    image=image_image_9
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
    x=412.0,
    y=1030.79443359375,
    width=66.7545166015625,
    height=18.074073791503906
)

canvas.create_text(
    411.0,
    991.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with our Introduction to User Experience Design course. Dive into the world of interactive design, learn the fundamentals of user-centered thinking, and acquire the skills to create intuitive,",
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

image_image_10 = PhotoImage(
    file=("image_10.png"))
image_10 = canvas.create_image(
    799.0,
    593.0,
    image=image_image_10
)

canvas.create_text(
    691.0,
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
    x=691.0,
    y=661.12548828125,
    width=87.0,
    height=11.902435302734375
)

image_image_11 = PhotoImage(
    file=("image_11.png"))
image_11 = canvas.create_image(
    799.0,
    683.8292236328125,
    image=image_image_11
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
    x=692.0,
    y=747.79443359375,
    width=66.7545166015625,
    height=18.074081420898438
)

canvas.create_text(
    691.0,
    708.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with our Introduction to User Experience Design course. Dive into the world of interactive design, learn the fundamentals of user-centered thinking, and acquire the skills to create intuitive,",
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

canvas.create_rectangle(
    680.0,
    814.0,
    922.0,
    938.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    693.0,
    974.731689453125,
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
    x=693.0,
    y=944.12548828125,
    width=87.0,
    height=11.90243911743164
)

image_image_12 = PhotoImage(
    file=("image_12.png"))
image_12 = canvas.create_image(
    801.0,
    966.8292236328125,
    image=image_image_12
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
    x=694.0,
    y=1030.79443359375,
    width=66.7545166015625,
    height=18.074073791503906
)

canvas.create_text(
    693.0,
    991.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with our Introduction to User Experience Design course. Dive into the world of interactive design, learn the fundamentals of user-centered thinking, and acquire the skills to create intuitive,",
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

image_image_13 = PhotoImage(
    file=("image_13.png"))
image_13 = canvas.create_image(
    1088.0,
    593.0,
    image=image_image_13
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
    height=11.902435302734375
)

image_image_14 = PhotoImage(
    file=("image_14.png"))
image_14 = canvas.create_image(
    1088.0,
    683.8292236328125,
    image=image_image_14
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
    height=18.074081420898438
)

canvas.create_text(
    980.0,
    708.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with our Introduction to User Experience Design course. Dive into the world of interactive design, learn the fundamentals of user-centered thinking, and acquire the skills to create intuitive,",
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

image_image_15 = PhotoImage(
    file=("image_15.png"))
image_15 = canvas.create_image(
    1090.0,
    876.0,
    image=image_image_15
)

canvas.create_text(
    982.0,
    974.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

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
    x=982.0,
    y=944.12548828125,
    width=87.0,
    height=11.90243911743164
)

image_image_16 = PhotoImage(
    file=("image_16.png"))
image_16 = canvas.create_image(
    1090.0,
    966.8292236328125,
    image=image_image_16
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
    x=983.0,
    y=1030.79443359375,
    width=66.7545166015625,
    height=18.074073791503906
)

canvas.create_text(
    982.0,
    991.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with our Introduction to User Experience Design course. Dive into the world of interactive design, learn the fundamentals of user-centered thinking, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_rectangle(
    0.0,
    1748.0,
    1280.0,
    2026.0,
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
    97.0,
    1161.0,
    anchor="nw",
    text="RECOMENDED TUTORS",
    fill="#3532A7",
    font=("Poppins SemiBold", 25 * -1)
)

canvas.create_text(
    90.0,
    483.0,
    anchor="nw",
    text="RECOMENDED COURSE",
    fill="#3532A7",
    font=("Poppins SemiBold", 25 * -1)
)

canvas.create_text(
    461.0,
    1785.0,
    anchor="nw",
    text="Menu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 20 * -1)
)

canvas.create_text(
    745.0,
    1787.0,
    anchor="nw",
    text="Menu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 20 * -1)
)

canvas.create_text(
    974.0,
    1787.0,
    anchor="nw",
    text="Menu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 20 * -1)
)

canvas.create_text(
    63.0,
    1824.0,
    anchor="nw",
    text="Our innovative online learning platform empowers students to pursue their educational goals from anywhere in the world. With flexible schedules and high-quality courses, we provide the tools and resources necessary for you to excel in your studies and succeed in any endeavor. Join our global community of learners and unlock your full potential with Virtu Edu.",
    fill="#FFFFFF",
    font=("Poppins Medium", 13 * -1)
)

canvas.create_text(
    464.0,
    1817.0,
    anchor="nw",
    text="Home\nAbout Us\nCourses\nEvents\nRoutine",
    fill="#FFFFFF",
    font=("Poppins Medium", 15 * -1)
)

canvas.create_text(
    756.0,
    1817.0,
    anchor="nw",
    text="Terms and Condition\nPrivacy and Policy\nSupport\nContact Us",
    fill="#FFFFFF",
    font=("Poppins Medium", 15 * -1)
)

canvas.create_text(
    979.0,
    1817.0,
    anchor="nw",
    text="CDEN\nIOE\nTU\nCoventry University",
    fill="#FFFFFF",
    font=("Poppins Medium", 15 * -1)
)

canvas.create_rectangle(
    123.0,
    1169.0,
    127.0,
    1192.0,
    fill="#646ECB",
    outline="")

canvas.create_rectangle(
    116.0,
    490.0,
    120.0,
    513.0,
    fill="#646ECB",
    outline="")

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
    x=507.0,
    y=1091.0,
    width=300.0,
    height=38.0
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
    x=525.0,
    y=1616.0,
    width=300.0,
    height=38.0
)

canvas.create_rectangle(
    104.0,
    1234.0,
    333.0,
    1583.0,
    fill="#FFFFFF",
    outline="")

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
    x=116.43994140625,
    y=1516.666748046875,
    width=48.959991455078125,
    height=35.8974609375
)

canvas.create_text(
    130.719970703125,
    1438.888916015625,
    anchor="nw",
    text="SUBAS",
    fill="#000000",
    font=("OpenSans SemiBold", 16 * -1)
)

canvas.create_text(
    130.719970703125,
    1468.803466796875,
    anchor="nw",
    text="UI/UX",
    fill="#5E5E5E",
    font=("OpenSans Regular", 12 * -1)
)

canvas.create_text(
    157.239990234375,
    1522.649658203125,
    anchor="nw",
    text="1581",
    fill="#468CE7",
    font=("OpenSans SemiBold", 12 * -1)
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
    x=262.0,
    y=1514.0,
    width=57.1199951171875,
    height=41.88037109375
)

image_image_17 = PhotoImage(
    file=("image_17.png"))
image_17 = canvas.create_image(
    217.0,
    1338.0,
    image=image_image_17
)

canvas.create_rectangle(
    408.0,
    1234.0,
    637.0,
    1583.0,
    fill="#FFFFFF",
    outline="")

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
    x=420.43994140625,
    y=1516.666748046875,
    width=48.96000671386719,
    height=35.8974609375
)

canvas.create_text(
    434.719970703125,
    1438.888916015625,
    anchor="nw",
    text="SUBAS",
    fill="#000000",
    font=("OpenSans SemiBold", 16 * -1)
)

canvas.create_text(
    434.719970703125,
    1468.803466796875,
    anchor="nw",
    text="UI/UX",
    fill="#5E5E5E",
    font=("OpenSans Regular", 12 * -1)
)

canvas.create_text(
    461.239990234375,
    1522.649658203125,
    anchor="nw",
    text="1581",
    fill="#468CE7",
    font=("OpenSans SemiBold", 12 * -1)
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
    x=566.0,
    y=1514.0,
    width=57.12000274658203,
    height=41.88037109375
)

image_image_18 = PhotoImage(
    file=("image_18.png"))
image_18 = canvas.create_image(
    521.0,
    1338.0,
    image=image_image_18
)

canvas.create_rectangle(
    688.0,
    1228.0,
    917.0,
    1577.0,
    fill="#FFFFFF",
    outline="")

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
    x=700.43994140625,
    y=1510.666748046875,
    width=48.96000671386719,
    height=35.8974609375
)

canvas.create_text(
    714.719970703125,
    1432.888916015625,
    anchor="nw",
    text="SUBAS",
    fill="#000000",
    font=("OpenSans SemiBold", 16 * -1)
)

canvas.create_text(
    714.719970703125,
    1462.803466796875,
    anchor="nw",
    text="UI/UX",
    fill="#5E5E5E",
    font=("OpenSans Regular", 12 * -1)
)

canvas.create_text(
    741.239990234375,
    1516.649658203125,
    anchor="nw",
    text="1581",
    fill="#468CE7",
    font=("OpenSans SemiBold", 12 * -1)
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
    x=846.0,
    y=1508.0,
    width=57.1199951171875,
    height=41.88037109375
)

image_image_19 = PhotoImage(
    file=("image_19.png"))
image_19 = canvas.create_image(
    801.0,
    1332.0,
    image=image_image_19
)

canvas.create_rectangle(
    974.0,
    1228.0,
    1203.0,
    1577.0,
    fill="#FFFFFF",
    outline="")

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
    x=986.43994140625,
    y=1510.666748046875,
    width=48.959991455078125,
    height=35.8974609375
)

canvas.create_text(
    1000.719970703125,
    1432.888916015625,
    anchor="nw",
    text="SUBAS",
    fill="#000000",
    font=("OpenSans SemiBold", 16 * -1)
)

canvas.create_text(
    1000.719970703125,
    1462.803466796875,
    anchor="nw",
    text="UI/UX",
    fill="#5E5E5E",
    font=("OpenSans Regular", 12 * -1)
)

canvas.create_text(
    1027.0,
    1517.0,
    anchor="nw",
    text="1581",
    fill="#468CE7",
    font=("OpenSans SemiBold", 12 * -1)
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
    x=1132.0,
    y=1508.0,
    width=57.1199951171875,
    height=41.88037109375
)

image_image_20 = PhotoImage(
    file=("image_20.png"))
image_20 = canvas.create_image(
    1087.0,
    1332.0,
    image=image_image_20
)

canvas.create_text(
    63.0,
    1804.0,
    anchor="nw",
    text="Learn Anywhere, Achieve Everywhere",
    fill="#FFFFFF",
    font=("Poppins Regular", 6 * -1)
)

window.resizable(False, False)
window.mainloop()
