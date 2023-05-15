# Tesla Music Player by Sangit Pokhrel
# Tesla Music Player by Sangit Pokhrel




from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Sangit Pokhrel\Videos\New folder\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("605x405")
window.title("Tesla Music player") #window title
photo = PhotoImage(file = './assets/frame0/logo.png')
window.iconphoto(True, photo)
window.configure(bg = "#FFFFFF")



canvas = Canvas(
    window,
    bg = "#4CE1EA",
    height = 405,
    width = 605,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge",
    
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    465.0,
    50.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    382.0,
    120.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    382.0,
    160.0,
    image=image_image_3
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    465.0,
    125.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=366.0,
    y=115.0,
    width=198.0,
    height=18.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    439.0,
    165.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFEFE",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=366.0,
    y=155.0,
    width=146.0,
    height=18.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=523.0,
    y=162.0,
    width=7.0,
    height=6.0
)

canvas.create_text(
    533.0,
    160.0,
    anchor="nw",
    text="Show",
    fill="#000000",
    font=("Inter SemiBold", 6 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=421.0,
    y=182.0,
    width=61.0,
    height=10.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=416.0,
    y=211.0,
    width=73.0,
    height=24.0
)

canvas.create_rectangle(
    392.0,
    266.0,
    533.0,
    267.0,
    fill="#FF0000",
    outline="")

canvas.create_text(
    428.0,
    279.0,
    anchor="nw",
    text="New member?",
    fill="#000000",
    font=("Inter SemiBold", 10 * -1)
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=423.0,
    y=308.0,
    width=92.0,
    height=24.0
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    164.0,
    202.0,
    image=image_image_4
)
window.resizable(False, False)
window.mainloop()
