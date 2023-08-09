


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *
import sqlite3
import os
import requests




window = Tk()

window.geometry("1280x832")
window.configure(bg = "#EEEFF3")

def post_data():
    # Get data from entry fields
    name = entry_1.get()
    email = entry_2.get()
    message = entry_3.get()

    # Create the data payload
    payload = {
        'contact_name': name,
        'email': email,
        'message': message
    }

    # Make the POST request to the API
    try:
        response = requests.post('https://virtuedu.com/api_virtuedu/contact/', json=payload)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        # Handle the response (e.g., display a success message)
        error_label.config(text="Data successfully sent to the API!", fg="green")
     # Clear the entry fields
        entry_1.delete(0, END)
        entry_2.delete(0, END)
        entry_3.delete(0, END)
    except requests.exceptions.RequestException as e:
        # Handle the exception (e.g., display an error message)
        error_label.config(text="Error: Failed to send data to the API.", fg="red")
        print(f"Error: {e}")
   

canvas = Canvas(
    window,
    bg = "#EEEFF3",
    height = 832,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    723.0,
    0.0,
    1280.0,
    832.0,
    fill="#3532A7",
    outline="")

canvas.create_text(
    185.0,
    614.0,
    anchor="nw",
    text="VirtuEdu",
    fill="#3532A7",
    font=("Poppins SemiBold", 64 * -1)
)

canvas.create_text(
    909.0,
    57.0,
    anchor="nw",
    text="Contact  us",
    fill="#D8D5E6",
    font=("Poppins SemiBold", 40 * -1)
)

canvas.create_text(
    204.0,
    693.0,
    anchor="nw",
    text="Learn Anywhere, Achieve Everywhere",
    fill="#646ECB",
    font=("Poppins Regular", 15 * -1)
)

canvas.create_text(
    816.0,
    125.0,
    anchor="nw",
    text="We are always there for you to Help you when You face any issues.",
    fill="#EAE7ED",
    font=("Poppins Regular", 15 * -1)
)

button_image_1 = PhotoImage(
    file=("button_1.png"))
button_1 = Button(
    canvas,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=post_data,
    relief="flat"
)
canvas.create_window(912, 684, anchor="nw", window=button_1)

# button_1.place(
#     x=912.0,
#     y=684.0,
#     width=196.0,
#     height=34.0
# )

# Create a label for error messages
error_label = Label(window, text="", fg="red")
error_label.place(x=816.0, y=160.0)
image_image_1 = PhotoImage(
    file=("image_1.png"))
image_1 = canvas.create_image(
    837.2857055664062,
    285.0,
    image=image_image_1
)

canvas.create_text(
    864.3333129882812,
    193.0,
    anchor="nw",
    text="Full name",
    fill="#EAE7ED",
    font=("OpenSans Bold", 14 * -1)
)

canvas.create_text(
    864.3333129882812,
    275.0,
    anchor="nw",
    text="Email",
    fill="#EAE7ED",
    font=("OpenSans Bold", 14 * -1)
)

canvas.create_text(
    864.3333129882812,
    366.0,
    anchor="nw",
    text="Message",
    fill="#EAE7ED",
    font=("OpenSans Bold", 14 * -1)
)

entry_image_1 = PhotoImage(
    file=("entry_1.png"))
entry_bg_1 = canvas.create_image(
    1007.2619018554688,
    239.0,
    image=entry_image_1
)


entry_1 = Entry(
    bd=0,
    
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("lexend deca", 15)
    
)
entry_1.place(
    x=826.0,
    y=219.0,
    width=362.5238037109375,
    height=38.0
)

entry_image_2 = PhotoImage(
    file=("entry_2.png"))
entry_bg_2 = canvas.create_image(
    1010.0,
    318.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("lexend deca", 13)
)
entry_2.place(
    x=826.0,
    y=298.0,
    width=368.0,
    height=38.0
)

entry_image_3 = PhotoImage(
    file=("entry_3.png"))
entry_bg_3 = canvas.create_image(
    1010.0,
    518.5,
    image=entry_image_3
    
)
entry_3 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    width=80
)
entry_3.place(
    x=826.0,
    y=389.0,
    width=368.0,
    height=257.0
)

image_image_2 = PhotoImage(
    file=("image_2.png"))
image_2 = canvas.create_image(
    836.5238037109375,
    204.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=("image_3.png"))
image_3 = canvas.create_image(
    836.5238037109375,
    374.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=("image_4.png"))
image_4 = canvas.create_image(
    331.0,
    317.0,
    image=image_image_4
)

canvas.create_rectangle(
    305.0,
    557.0,
    350.0,
    568.0,
    fill="#3532A7",
    outline="")

canvas.create_rectangle(
    270.0,
    557.0,
    296.0,
    567.0,
    fill="#3532A7",
    outline="")

canvas.create_rectangle(
    358.0,
    557.0,
    384.0,
    567.0,
    fill="#3532A7",
    outline="")
window.resizable(False, False)
window.mainloop()
