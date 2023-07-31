from tkinter import *

import os
import sys
import subprocess
import requests


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
    relief="flat",
    bg="#82B4FF"
)
canvas.create_window(1194, 12, anchor="nw", window=button_1)



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
    file=("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat",
    bg="#fff"
)
canvas.create_window(975, 23, anchor="nw", window=button_2)


button_image_3 = PhotoImage(
    file=("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=create_gui,
    relief="flat",
    bg="#82B4FF"
)
canvas.create_window(1157, 31, anchor="nw", window=button_3)


button_image_4 = PhotoImage(
    file=("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat",
    bg="#82B4FF"
)
canvas.create_window(388, 29, anchor="nw", window=button_4)



button_image_5 = PhotoImage(
    file=("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
    ,bg="#82B4FF"
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
    bg="#82B4FF"
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
    bg="#82B4FF"
)
canvas.create_window(459, 31, anchor="nw", window=button_7)


image_image_1 = PhotoImage(
    file=("image_1.png"))
image_1 = canvas.create_image(
    1206.0,
    269.0,
    image=image_image_1
)

canvas.create_text(
    76.0,
    199.0,
    anchor="nw",
    text="VirtuEdu",
    fill="#2939D2",
    font=("OpenSans Bold", 60 * -1)
)

canvas.create_text(
    80.0,
    273.0,
    anchor="nw",
    text="Learn Anywhere, Achieve Everywhere",
    fill="#414FD2",
    font=("Poppins Regular", 24 * -1)
)

canvas.create_rectangle(
    79.0,
    531.0,
    324.0331115722656,
    783.7969512939453,
    fill="#FFFFFF",
    outline="")

image_image_2 = PhotoImage(
    file=("image_2.png"))
image_2 = canvas.create_image(
    201.0,
    595.0,
    image=image_image_2
)

canvas.create_text(
    92.1629638671875,
    697.5265502929688,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

image_image_3 = PhotoImage(
    file=("image_3.png"))
image_3 = canvas.create_image(
    136.1629638671875,
    671.81689453125,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=("image_4.png"))
image_4 = canvas.create_image(
    201.17559814453125,
    689.1949462890625,
    image=image_image_4
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
canvas.create_window(93, 755, anchor="nw", window=button_8)


canvas.create_text(
    92.1629638671875,
    714.3814086914062,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with our \nIntroduction to User Experience Design course. Dive into the world of\ninteractive design, learn the fundamentals of user-centered thinking\n, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_rectangle(
    81.02508544921875,
    824.2030029296875,
    326.0581970214844,
    1076.9999542236328,
    fill="#FFFFFF",
    outline="")

image_image_5 = PhotoImage(
    file=("image_5.png"))
image_5 = canvas.create_image(
    203.02508544921875,
    888.2030029296875,
    image=image_image_5
)

canvas.create_text(
    94.18804931640625,
    990.7295532226562,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

image_image_6 = PhotoImage(
    file=("image_6.png"))
image_6 = canvas.create_image(
    138.18804931640625,
    965.0198974609375,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=("image_7.png"))
image_7 = canvas.create_image(
    203.2005615234375,
    982.39794921875,
    image=image_image_7
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
canvas.create_window(95, 1048, anchor="nw", window=button_9)


canvas.create_text(
    94.18804931640625,
    1007.5844116210938,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with our \nIntroduction to User Experience Design course. Dive into the world of\ninteractive design, learn the fundamentals of user-centered thinking\n, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_rectangle(
    384.7850646972656,
    531.0,
    629.8181762695312,
    783.7969512939453,
    fill="#FFFFFF",
    outline="")

image_image_8 = PhotoImage(
    file=("image_8.png"))
image_8 = canvas.create_image(
    506.7850646972656,
    595.0,
    image=image_image_8
)

canvas.create_text(
    397.9481506347656,
    697.5265502929688,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

image_image_9 = PhotoImage(
    file=("image_9.png"))
image_9 = canvas.create_image(
    441.9481506347656,
    671.81689453125,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=("image_10.png"))
image_10 = canvas.create_image(
    506.960693359375,
    689.1949462890625,
    image=image_image_10
)



canvas.create_text(
    397.9481506347656,
    714.3814086914062,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with our \nIntroduction to User Experience Design course. Dive into the world of\ninteractive design, learn the fundamentals of user-centered thinking\n, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_rectangle(
    386.8102722167969,
    824.2030029296875,
    631.8433837890625,
    1076.9999542236328,
    fill="#FFFFFF",
    outline="")

image_image_11 = PhotoImage(
    file=("image_11.png"))
image_11 = canvas.create_image(
    508.8102722167969,
    888.2030029296875,
    image=image_image_11
)

canvas.create_text(
    399.9731750488281,
    990.7295532226562,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

image_image_12 = PhotoImage(
    file=("image_12.png"))
image_12 = canvas.create_image(
    443.9731750488281,
    965.0198974609375,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=("image_13.png"))
image_13 = canvas.create_image(
    508.9856872558594,
    982.39794921875,
    image=image_image_13
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
canvas.create_window(400, 1048, anchor="nw", window=button_10)


canvas.create_text(
    399.9731750488281,
    1007.5844116210938,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with our \nIntroduction to User Experience Design course. Dive into the world of\ninteractive design, learn the fundamentals of user-centered thinking\n, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_rectangle(
    670.3195190429688,
    531.0,
    915.3526306152344,
    783.7969512939453,
    fill="#FFFFFF",
    outline="")

image_image_14 = PhotoImage(
    file=("image_14.png"))
image_14 = canvas.create_image(
    792.3195190429688,
    595.0,
    image=image_image_14
)

canvas.create_text(
    683.4825439453125,
    697.5265502929688,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

image_image_15 = PhotoImage(
    file=("image_15.png"))
image_15 = canvas.create_image(
    727.4825439453125,
    671.81689453125,
    image=image_image_15
)

image_image_16 = PhotoImage(
    file=("image_16.png"))
image_16 = canvas.create_image(
    792.4951171875,
    689.1949462890625,
    image=image_image_16
)
button_image_27 = PhotoImage(
    file=("button_11.png"))
button_27 = Button(
    image=button_image_27,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_27 clicked"),
    relief="flat"
)
canvas.create_window(400, 755, anchor="nw", window=button_27)

button_image_11 = PhotoImage(
    file=("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
    relief="flat"
)
canvas.create_window(684, 755, anchor="nw", window=button_11)


canvas.create_text(
    683.4825439453125,
    714.3814086914062,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with our \nIntroduction to User Experience Design course. Dive into the world of\ninteractive design, learn the fundamentals of user-centered thinking\n, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_rectangle(
    672.3446044921875,
    824.2030029296875,
    917.3777160644531,
    1076.9999542236328,
    fill="#FFFFFF",
    outline="")

image_image_17 = PhotoImage(
    file=("image_17.png"))
image_17 = canvas.create_image(
    794.3446044921875,
    888.2030029296875,
    image=image_image_17
)

canvas.create_text(
    685.5076293945312,
    990.7295532226562,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

image_image_18 = PhotoImage(
    file=("image_18.png"))
image_18 = canvas.create_image(
    729.5076293945312,
    965.0198974609375,
    image=image_image_18
)

image_image_19 = PhotoImage(
    file=("image_19.png"))
image_19 = canvas.create_image(
    794.5201416015625,
    982.39794921875,
    image=image_image_19
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
canvas.create_window(686, 1048, anchor="nw", window=button_12)


canvas.create_text(
    685.5076293945312,
    1007.5844116210938,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with our \nIntroduction to User Experience Design course. Dive into the world of\ninteractive design, learn the fundamentals of user-centered thinking\n, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_rectangle(
    962.9417724609375,
    531.0,
    1207.974853515625,
    783.7969512939453,
    fill="#FFFFFF",
    outline="")

image_image_20 = PhotoImage(
    file=("image_20.png"))
image_20 = canvas.create_image(
    1084.9417724609375,
    595.0,
    image=image_image_20
)

canvas.create_text(
    976.1047973632812,
    697.5265502929688,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

image_image_21 = PhotoImage(
    file=("image_21.png"))
image_21 = canvas.create_image(
    1020.1047973632812,
    671.81689453125,
    image=image_image_21
)

image_image_22 = PhotoImage(
    file=("image_22.png"))
image_22 = canvas.create_image(
    1085.1172485351562,
    689.1949462890625,
    image=image_image_22
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
canvas.create_window(977, 755, anchor="nw", window=button_13)


canvas.create_text(
    976.1047973632812,
    714.3814086914062,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with our \nIntroduction to User Experience Design course. Dive into the world of\ninteractive design, learn the fundamentals of user-centered thinking\n, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_rectangle(
    964.9669189453125,
    824.2030029296875,
    1210.0,
    1076.9999542236328,
    fill="#FFFFFF",
    outline="")

image_image_23 = PhotoImage(
    file=("image_23.png"))
image_23 = canvas.create_image(
    1086.9669189453125,
    888.2030029296875,
    image=image_image_23
)

canvas.create_text(
    978.1298217773438,
    990.7295532226562,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

image_image_24 = PhotoImage(
    file=("image_24.png"))
image_24 = canvas.create_image(
    1022.1298217773438,
    965.0198974609375,
    image=image_image_24
)

image_image_25 = PhotoImage(
    file=("image_25.png"))
image_25 = canvas.create_image(
    1087.1423950195312,
    982.39794921875,
    image=image_image_25
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
canvas.create_window(979, 1048, anchor="nw", window=button_14)



canvas.create_text(
    978.1298217773438,
    1007.5844116210938,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with our \nIntroduction to User Experience Design course. Dive into the world of\ninteractive design, learn the fundamentals of user-centered thinking\n, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
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
    text="Our innovative online learning platform empowers students to pursue their educational goals from anywhere in the world. With flexible schedules and high-quality courses, we provide the tools and resources necessary for you to excel in your studies and succeed in any endeavor. Join our global community of learners and unlock your full potential with Virtu Edu.",
    fill="#FFFFFF",
    font=("Poppins Medium", 6 * -1)
)

canvas.create_text(
    464.0,
    1817.0,
    anchor="nw",
    text="Home\nAbout Us\nCourses\nEvents\nRoutine",
    fill="#FFFFFF",
    font=("Poppins Medium", 6 * -1)
)

canvas.create_text(
    756.0,
    1817.0,
    anchor="nw",
    text="Terms and Condition\nPrivacy and Policy\nSupport\nContact Us",
    fill="#FFFFFF",
    font=("Poppins Medium", 6 * -1)
)

canvas.create_text(
    979.0,
    1817.0,
    anchor="nw",
    text="CDEN\nIOE\nTU\nCoventry University",
    fill="#FFFFFF",
    font=("Poppins Medium", 6 * -1)
)

canvas.create_rectangle(
    90.0,
    1169.0,
    94.0,
    1192.0,
    fill="#646ECB",
    outline="")

canvas.create_rectangle(
    80.0,
    490.0,
    84.0,
    513.0,
    fill="#646ECB",
    outline="")

button_image_15 = PhotoImage(
    file=("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_15 clicked"),
    relief="flat"
)
canvas.create_window(507, 1091, anchor="nw", window=button_15)



button_image_16 = PhotoImage(
    file=("button_16.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_16 clicked"),
    relief="flat"
)
canvas.create_window(525, 1616, anchor="nw", window=button_16)


canvas.create_rectangle(
    104.0,
    1234.0,
    333.0,
    1583.0,
    fill="#FFFFFF",
    outline="")

button_image_17 = PhotoImage(
    file=("button_17.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_17 clicked"),
    relief="flat"
)
canvas.create_window(116, 1486, anchor="nw", window=button_17)

canvas.create_text(
    131.0,
    1439.0,
    anchor="nw",
    text="SUBAS KANDEL",
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
    text="2069",
    fill="#468CE7",
    font=("OpenSans SemiBold", 12 * -1)
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
canvas.create_window(262, 1514, anchor="nw", window=button_18)



button_image_19 = PhotoImage(
    file=("button_19.png"))
button_19 = Button(
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_19 clicked"),
    relief="flat"
)
canvas.create_window(262, 1465, anchor="nw", window=button_19)



image_image_26 = PhotoImage(
    file=("image_26.png"))
image_26 = canvas.create_image(
    217.0,
    1338.0,
    image=image_image_26
)

canvas.create_rectangle(
    423.0,
    1228.0,
    652.0,
    1577.0,
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
canvas.create_window(420, 1516, anchor="nw", window=button_20)


button_image_21 = PhotoImage(
    file=("button_21.png"))
button_21 = Button(
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_21 clicked"),
    relief="flat"
)
canvas.create_window(115, 1514, anchor="nw", window=button_21)



canvas.create_text(
    435.0,
    1439.0,
    anchor="nw",
    text="SANGIT POKHREL",
    fill="#000000",
    font=("OpenSans SemiBold", 16 * -1)
)

canvas.create_text(
    435.0,
    1469.0,
    anchor="nw",
    text="FULL STACK WEB DEVELOPER",
    fill="#5E5E5E",
    font=("OpenSans Regular", 12 * -1)
)

canvas.create_text(
    461.239990234375,
    1522.649658203125,
    anchor="nw",
    text="2180",
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
canvas.create_window(566, 1514, anchor="nw", window=button_22)



image_image_27 = PhotoImage(
    file=("image_27.png"))
image_27 = canvas.create_image(
    521.0,
    1338.0,
    image=image_image_27
)

canvas.create_rectangle(
    688.0,
    1228.0,
    917.0,
    1577.0,
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

canvas.create_window(700, 1510, anchor="nw", window=button_23)


canvas.create_text(
    715.0,
    1433.0,
    anchor="nw",
    text="ADAMYA NEUPANE",
    fill="#000000",
    font=("OpenSans SemiBold", 16 * -1)
)

canvas.create_text(
    715.0,
    1463.0,
    anchor="nw",
    text="BACKEND DEVELOPER",
    fill="#5E5E5E",
    font=("OpenSans Regular", 12 * -1)
)

canvas.create_text(
    741.239990234375,
    1516.649658203125,
    anchor="nw",
    text="2130",
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
canvas.create_window(846, 1508, anchor="nw", window=button_24)



image_image_28 = PhotoImage(
    file=("image_28.png"))
image_28 = canvas.create_image(
    801.0,
    1332.0,
    image=image_image_28
)

canvas.create_rectangle(
    974.0,
    1228.0,
    1203.0,
    1577.0,
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
canvas.create_window(986, 1510, anchor="nw", window=button_25)


canvas.create_text(
    1001.0,
    1433.0,
    anchor="nw",
    text="SOME KAAMCHOR",
    fill="#000000",
    font=("OpenSans SemiBold", 16 * -1)
)

canvas.create_text(
    1001.0,
    1463.0,
    anchor="nw",
    text="EATING AND MAKING EXCUSES",
    fill="#5E5E5E",
    font=("OpenSans Regular", 12 * -1)
)

canvas.create_text(
    1027.239990234375,
    1516.649658203125,
    anchor="nw",
    text="-99",
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
canvas.create_window(1132, 1508, anchor="nw", window=button_26)


image_image_29 = PhotoImage(
    file=("image_29.png"))
image_29 = canvas.create_image(
    1087.0,
    1332.0,
    image=image_image_29
)
# Update the scroll region to include the entire frame
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

window.resizable(False, False)
window.mainloop()
