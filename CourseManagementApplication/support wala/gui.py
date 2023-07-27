from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("1280x800")
window.configure(bg="#EEEFF3")

# Create a Canvas widget with a scrollbar
canvas = Canvas(window, height=500)
scrollbar = Scrollbar(window, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
canvas.pack(fill="both", expand=True)

def on_mousewheel(event):
    # Get the current scroll position
    current_pos = canvas.canvasy(0)

    # Get the top and bottom coordinates of the content
    top_pos = canvas.bbox("all")[1]
    bottom_pos = canvas.bbox("all")[2]

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
    43.0,
    50.0,
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
    command=lambda: print("profile clicked"),
    relief="flat"
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
    command=lambda: print("notification clicked"),
    relief="flat"
)
canvas.create_window(1157, 22, anchor="nw", window=button_2)

# button_2.place(
#     x=1157.0,
#     y=22.608474731445312,
#     width=17.694091796875,
#     height=20.41619873046875
# )

image_image_1 = PhotoImage(
    file=("image_1.png"))
image_1 = canvas.create_image(
    357.0,
    301.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=("image_2.png"))
image_2 = canvas.create_image(
    974.0,
    128.5842742919922,
    image=image_image_2
)

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
    text="Support",
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
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("home clicked"),
    relief="flat"
)
canvas.create_window(385, 31, anchor="nw", window=button_16)
# button_16.place(
#     x=385.0,
#     y=31.0,
#     width=43.0,
#     height=20.0
# )

button_image_17 = PhotoImage(
    file=("routines.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("routine clicked"),
    relief="flat"
)
canvas.create_window(533, 32, anchor="nw", window=button_17)
# button_17.place(
#     x=533.0,
#     y=32.0,
#     width=65.0,
#     height=20.0
# )

button_image_18 = PhotoImage(
    file=("courses.png"))
button_18 = Button(
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("courses clicked"),
    relief="flat"
)
canvas.create_window(446, 32, anchor="nw", window=button_18)
# button_18.place(
#     x=446.0,
#     y=32.0,
#     width=69.0,
#     height=20.0
# )

button_image_19 = PhotoImage(
    file=("requests.png"))
button_19 = Button(
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("requests clicked"),
    relief="flat"
)
canvas.create_window(610, 32, anchor="nw", window=button_19)
# button_19.place(
#     x=610.0,
#     y=32.0,
#     width=83.0,
#     height=23.0
# )

canvas.create_text(
    429.0,
    492.0,
    anchor="nw",
    text="You can contact us via :\n",
    fill="#3532A7",
    font=("Poppins SemiBold", 34 * -1)
)

image_image_4 = PhotoImage(
    file=("image_4.png"))
image_4 = canvas.create_image(
    230.0,
    644.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=("image_5.png"))
image_5 = canvas.create_image(
    107.0,
    803.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=("image_6.png"))
image_6 = canvas.create_image(
    331.0,
    984.0,
    image=image_image_6
)

canvas.create_rectangle(
    227.5,
    435.0,
    230.5,
    594.0,
    fill="#635EFF",
    outline="")

canvas.create_rectangle(
    106.5,
    440.0,
    109.5,
    753.0,
    fill="#635EFF",
    outline="")

canvas.create_rectangle(
    326.5,
    439.0,
    329.5,
    934.0,
    fill="#635EFF",
    outline="")

canvas.create_rectangle(
    1139.5,
    439.0,
    1142.5,
    1122.0,
    fill="#635EFF",
    outline="")

image_image_7 = PhotoImage(
    file=("image_7.png"))
image_7 = canvas.create_image(
    1142.0,
    1140.0,
    image=image_image_7
)

canvas.create_text(
    340.0,
    614.0,
    anchor="nw",
    text="VirtuEdu Facebook Page",
    fill="#3532A7",
    font=("Poppins SemiBold", 34 * -1)
)

canvas.create_text(
    180.0,
    775.0,
    anchor="nw",
    text="VirtuEdu Instagram page",
    fill="#3532A7",
    font=("Poppins SemiBold", 34 * -1)
)

canvas.create_text(
    380.0,
    954.0,
    anchor="nw",
    text="VirtuEdu Whatsapp Profile",
    fill="#3532A7",
    font=("Poppins SemiBold", 34 * -1)
)

canvas.create_text(
    590.0,
    1113.0,
    anchor="nw",
    text="heypsycho339@gmail.com",
    fill="#3532A7",
    font=("Poppins SemiBold", 34 * -1)
)
# Update the scroll region to include the entire frame
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

window.resizable(False, False)
window.mainloop()
