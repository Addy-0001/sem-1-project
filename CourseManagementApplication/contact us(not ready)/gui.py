

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage




window = Tk()

window.geometry("1280x1624")
window.configure(bg = "#EEEFF3")


canvas = Canvas(
    window,
    bg = "#EEEFF3",
    height = 1624,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    4.0,
    1282.0,
    450.0,
    fill="#90BCFD",
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
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=1194.0,
    y=12.0,
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
    file=("notification.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=1157.0,
    y=22.608489990234375,
    width=17.694091796875,
    height=20.41619873046875
)

image_image_1 = PhotoImage(
    file=("image_1.png"))
image_1 = canvas.create_image(
    357.0,
    301.0,
    image=image_image_1
)

# image_image_2 = PhotoImage(
#     file=("image_2.png"))
# image_2 = canvas.create_image(
#     974.0,
#     128.58428955078125,
#     image=image_image_2
# )

image_image_3 = PhotoImage(
    file=("image_3.png"))
image_3 = canvas.create_image(
    752.0001220703125,
    160.48995971679688,
    image=image_image_3
)

canvas.create_text(
    748.0,
    169.0,
    anchor="nw",
    text="Contact US",
    fill="#646ECB",
    font=("OpenSans Bold", 60 * -1)
)

canvas.create_rectangle(
    1616.0,
    2701.0,
    1716.0,
    2801.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    0.0,
    1358.0,
    1280.0,
    1624.0,
    fill="#3532A7",
    outline="")

canvas.create_text(
    59.0,
    1387.0,
    anchor="nw",
    text="VirtuEdu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 32 * -1)
)

canvas.create_text(
    503.0,
    1402.0,
    anchor="nw",
    text="Menu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 24 * -1)
)

canvas.create_text(
    737.0,
    1402.0,
    anchor="nw",
    text="Menu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 24 * -1)
)

canvas.create_text(
    1007.0,
    1402.0,
    anchor="nw",
    text="Menu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 24 * -1)
)

canvas.create_text(
    85.0,
    1433.0,
    anchor="nw",
    text="Learn Anywhere, Achieve Everywhere",
    fill="#FFFFFF",
    font=("Poppins Regular", 11 * -1)
)

canvas.create_text(
    87.0,
    1458.0,
    anchor="nw",
    text="Our innovative online learning platform empowers students to pursue their educational goals from anywhere in the world. With flexible schedules and high-quality courses, we provide the tools and resources necessary for you to excel in your studies and succeed in any endeavor. Join our global community of learners and unlock your full potential with Virtu Edu.",
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
    x=515.0,
    y=1445.0,
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
    x=746.0,
    y=1442.0,
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
    x=1020.0,
    y=1442.0,
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
    x=1020.0,
    y=1467.0,
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
    x=1021.0,
    y=1492.0,
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
    x=1021.0,
    y=1517.0,
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
    x=748.0,
    y=1467.0,
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
    x=748.0,
    y=1492.0,
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
    x=748.0,
    y=1517.0,
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
    x=515.0,
    y=1470.0,
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
    x=515.0,
    y=1495.0,
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
    x=515.0,
    y=1520.0,
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
    x=515.0,
    y=1545.0,
    width=39.0,
    height=15.0
)


button_image_16 = PhotoImage(
    file=("home.png"))
button_16 = Button(
    canvas,
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
canvas.create_window(388, 31, anchor="nw", window=button_16)


button_image_17 = PhotoImage(
    file=("routines.png"))
button_17 = Button(
    canvas,
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
canvas.create_window(546, 34, anchor="nw", window=button_17)

button_image_18 = PhotoImage(
    file=("courses.png"))
button_18 = Button(
    canvas,
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Course Button Clicked"),
    relief="flat"
)
canvas.create_window(459, 28, anchor="nw", window=button_18)

button_image_19 = PhotoImage(
    file=("requests.png"))
button_19 = Button(
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_19 clicked"),
    relief="flat"
)
button_19.place(
    x=610.0,
    y=32.0,
    width=83.0,
    height=23.0
)

canvas.create_rectangle(
    42.0,
    476.0,
    1238.0,
    1308.0,
    fill="#FFFCFC",
    outline="")

canvas.create_text(
    297.0,
    490.0,
    anchor="nw",
    text="We Are Always Ready To Help You !!!",
    fill="#3532A7",
    font=("Poppins SemiBold", 34 * -1)
)

canvas.create_text(
    132.0,
    580.0,
    anchor="nw",
    text="Name :",
    fill="#000000",
    font=("Poppins SemiBold", 34 * -1)
)

canvas.create_text(
    134.0,
    687.0,
    anchor="nw",
    text="Email :",
    fill="#000000",
    font=("Poppins SemiBold", 34 * -1)
)

canvas.create_text(
    130.0,
    791.0,
    anchor="nw",
    text="Phone number :",
    fill="#000000",
    font=("Poppins SemiBold", 34 * -1)
)

canvas.create_text(
    135.0,
    876.0,
    anchor="nw",
    text="Message :",
    fill="#000000",
    font=("Poppins SemiBold", 34 * -1)
)

canvas.create_text(
    901.0,
    580.0,
    anchor="nw",
    text="Age :",
    fill="#000000",
    font=("Poppins SemiBold", 34 * -1)
)

entry_image_2 = PhotoImage(
    file=("entry_2.png"))
entry_bg_2 = canvas.create_image(
    657.0,
    1056.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#EFEFEF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=175.0,
    y=927.0,
    width=964.0,
    height=256.0
)

entry_image_3 = PhotoImage(
    file=("entry_3.png"))
entry_bg_3 = canvas.create_image(
    571.0,
    605.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#EFEFEF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=281.0,
    y=567.0,
    width=580.0,
    height=75.0
)

entry_image_4 = PhotoImage(
    file=("entry_4.png"))
entry_bg_4 = canvas.create_image(
    574.0,
    712.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#EFEFEF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=284.0,
    y=674.0,
    width=580.0,
    height=75.0
)

entry_image_5 = PhotoImage(
    file=("entry_5.png"))
entry_bg_5 = canvas.create_image(
    721.0,
    816.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#EFEFEF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=431.0,
    y=778.0,
    width=580.0,
    height=75.0
)

entry_image_6 = PhotoImage(
    file=("entry_6.png"))
entry_bg_6 = canvas.create_image(
    1099.5,
    605.5,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#EFEFEF",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=1027.0,
    y=567.0,
    width=145.0,
    height=75.0
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
    x=498.0,
    y=1224.0,
    width=223.0,
    height=53.0
)
window.resizable(False, False)
window.mainloop()
