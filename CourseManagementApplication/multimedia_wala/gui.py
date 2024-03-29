from tkinter import messagebox
from tkinter import *
from tkinter import ttk
import os
import sys
import subprocess, webbrowser
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
    canvas,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=create_gui,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(1160, 20, anchor="nw", window=button_1)

# button_1.place(
#    x=1160.0,
#     y=20.0,
#     width=56.0,
#     height=56.0
# )


def routinesfile():

    # Change to the next folder
    next_folder = os.path.join(
        os.getcwd().replace("multimedia_wala", "routines"))
    os.chdir(next_folder)

    # Run the gui.py file
    subprocess.Popen([sys.executable, 'gui.py'])

    window.destroy()


def requestsfile():

    # Change to the next folder
    next_folder = os.path.join(os.getcwd().replace(
        "multimedia_wala", "requests_notdone"))
    os.chdir(next_folder)

    # Run the gui.py file
    subprocess.Popen([sys.executable, 'gui.py'])

    window.destroy()


def computingfile():

    # Change to the next folder
    next_folder = os.path.join(os.getcwd().replace(
        "multimedia_wala", "computing_wala"))
    os.chdir(next_folder)

    # Run the gui.py file
    subprocess.Popen([sys.executable, 'gui.py'])

    window.destroy()


def multimediafile():

    # Change to the next folder
    next_folder = os.path.join(os.getcwd().replace(
        "multimedia_wala", "multimedia_wala"))
    os.chdir(next_folder)

    # Run the gui.py file
    subprocess.Popen([sys.executable, 'gui.py'])

    window.destroy()


def marketingfile():

    # Change to the next folder
    next_folder = os.path.join(os.getcwd().replace(
        "multimedia_wala", "marketing_wala"))
    os.chdir(next_folder)

    # Run the gui.py file
    subprocess.Popen([sys.executable, 'gui.py'])

    window.destroy()


def languagefile():

    # Change to the next folder
    next_folder = os.path.join(os.getcwd().replace(
        "multimedia_wala", "language_wala"))
    os.chdir(next_folder)

    # Run the gui.py file
    subprocess.Popen([sys.executable, 'gui.py'])

    window.destroy()


def designingfile():

    # Change to the next folder
    next_folder = os.path.join(os.getcwd().replace(
        "multimedia_wala", "designing_wala"))
    os.chdir(next_folder)

    # Run the gui.py file
    subprocess.Popen([sys.executable, 'gui.py'])

    window.destroy()


def homefile():

    # Change to the next folder
    next_folder = os.path.join(
        os.getcwd().replace("multimedia_wala", "homepage"))
    print(next_folder)
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
    font=("lexend deca", 16)
)
canvas.create_window(717, 16, anchor="nw", window=entry_1)

# entry_1.place(
#     x=717.0,
#     y=16.0,
#     width=275.0,
#     height=32.0
# )

button_image_2 = PhotoImage(
    file=("notification.png"))
button_2 = Button(
    canvas,
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=create_gui,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(1100, 31, anchor="nw", window=button_2)

# button_2.place(
#     x=1100.0,
#     y=31.615699768066406,
#     width=29.694091796875,
#     height=29.550003051757812
# )


def buildfile():

    # Change to the next folder
    next_folder = os.path.join(os.getcwd().replace("multimedia_wala", "build"))
    os.chdir(next_folder)

    # Run the gui.py file
    subprocess.Popen([sys.executable, 'gui.py'])

    window.destroy()


button_image_3 = PhotoImage(
    file=("home.png"))
button_3 = Button(
    canvas,
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=buildfile,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(388, 31, anchor="nw", window=button_3)

# button_3.place(
#     x=388.0,
#     y=31.0,
#     width=61.0,
#     height=28.0
# )

button_image_4 = PhotoImage(
    file=("routines.png"))
button_4 = Button(
    canvas,
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=routinesfile,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(546, 34, anchor="nw", window=button_4)

# button_4.place(
#     x=546.0,
#     y=34.0,
#     width=65.0,
#     height=20.0
# )

button_image_5 = PhotoImage(
    file=("requests.png"))
button_5 = Button(
    canvas,
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=requestsfile,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(628, 31, anchor="nw", window=button_5)

# button_5.place(
#    x=628.0,
#     y=31.0,
#     width=65.0,
#     height=20.0
# )

button_image_6 = PhotoImage(
    file=("courses.png"))
button_6 = Button(
    canvas,
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(459, 31, anchor="nw", window=button_6)

# button_6.place(
#     x=459.0,
#     y=31.0,
#     width=61.0,
#     height=28.0
# )

# header ends

image_image_1 = PhotoImage(
    file=("image_1.png"))
image_1 = canvas.create_image(
    761.0,
    342.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=("image_2.png"))
image_2 = canvas.create_image(
    340.0,
    300.21270751953125,
    image=image_image_2
)


button_image_7 = PhotoImage(
    file=("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=computingfile,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(400, 457, anchor="nw", window=button_7)


button_image_8 = PhotoImage(
    file=("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=homefile,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(260, 456, anchor="nw", window=button_8)


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
canvas.create_window(526, 457, anchor="nw", window=button_9)


button_image_10 = PhotoImage(
    file=("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=designingfile,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(660, 457, anchor="nw", window=button_10)


button_image_11 = PhotoImage(
    file=("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=languagefile,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(785, 457, anchor="nw", window=button_11)


button_image_12 = PhotoImage(
    file=("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=marketingfile,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(925, 457, anchor="nw", window=button_12)


canvas.create_text(
    700.0,
    180.0,
    anchor="nw",
    text="Multimedia\nCourses",
    fill="#646ECB",
    font=("OpenSans Bold", 60 * -1)
)

canvas.create_text(
    793.0,
    320.0,
    anchor="nw",
    text="Unlock your potential with our transformative courses.",
    fill="#0018FF",
    font=("Poppins Regular", 15 * -1)
)

canvas.create_rectangle(
    94.0,
    531.0,
    336.0,
    775.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    94.0,
    828.0,
    336.0,
    1072.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    388.0,
    531.0,
    630.0,
    775.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    388.0,
    828.0,
    630.0,
    1072.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    691.0,
    531.0,
    933.0,
    775.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    691.0,
    828.0,
    933.0,
    1072.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    987.0,
    533.0,
    1229.0,
    777.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    987.0,
    830.0,
    1229.0,
    1074.0,
    fill="#FFFFFF",
    outline="")

image_image_3 = PhotoImage(
    file=("image_3.png"))
image_3 = canvas.create_image(
    215.0,
    593.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=("image_4.png"))
image_4 = canvas.create_image(
    215.0,
    890.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=("image_5.png"))
image_5 = canvas.create_image(
    509.0,
    593.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=("image_6.png"))
image_6 = canvas.create_image(
    509.0,
    890.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=("image_7.png"))
image_7 = canvas.create_image(
    812.0,
    593.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=("image_8.png"))
image_8 = canvas.create_image(
    812.0,
    890.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=("image_9.png"))
image_9 = canvas.create_image(
    1108.0,
    595.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=("image_10.png"))
image_10 = canvas.create_image(
    1108.0,
    892.0,
    image=image_image_10
)

canvas.create_text(
    107.0,
    691.731689453125,
    anchor="nw",
    text="Digital Marketing",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    107.0,
    988.731689453125,
    anchor="nw",
    text="Digital Marketing",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    401.0,
    691.731689453125,
    anchor="nw",
    text="Introduction to Multimedia",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    401.0,
    988.731689453125,
    anchor="nw",
    text="Computing React Course",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    704.0,
    691.731689453125,
    anchor="nw",
    text="Inbound Marketing",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    704.0,
    988.731689453125,
    anchor="nw",
    text="Mobile Development with Flutter",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    1000.0,
    693.731689453125,
    anchor="nw",
    text="Design With Figma",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    1000.0,
    990.731689453125,
    anchor="nw",
    text="Web Development with Django",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

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
canvas.create_window(107, 661, anchor="nw", window=button_13)


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
canvas.create_window(107, 958, anchor="nw", window=button_14)


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
canvas.create_window(401, 661, anchor="nw", window=button_15)


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
canvas.create_window(401, 958, anchor="nw", window=button_16)


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
canvas.create_window(704, 661, anchor="nw", window=button_17)


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
canvas.create_window(704, 958, anchor="nw", window=button_18)


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
canvas.create_window(1000, 663, anchor="nw", window=button_19)


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
canvas.create_window(1000, 960, anchor="nw", window=button_20)


image_image_11 = PhotoImage(
    file=("image_11.png"))
image_11 = canvas.create_image(
    215.0,
    683.8292236328125,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=("image_12.png"))
image_12 = canvas.create_image(
    215.0,
    980.8292236328125,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=("image_13.png"))
image_13 = canvas.create_image(
    509.0,
    683.8292236328125,
    image=image_image_13
)

image_image_14 = PhotoImage(
    file=("image_14.png"))
image_14 = canvas.create_image(
    509.0,
    980.8292236328125,
    image=image_image_14
)

image_image_15 = PhotoImage(
    file=("image_15.png"))
image_15 = canvas.create_image(
    812.0,
    683.8292236328125,
    image=image_image_15
)

image_image_16 = PhotoImage(
    file=("image_16.png"))
image_16 = canvas.create_image(
    812.0,
    980.8292236328125,
    image=image_image_16
)

image_image_17 = PhotoImage(
    file=("image_17.png"))
image_17 = canvas.create_image(
    1108.0,
    685.8292236328125,
    image=image_image_17
)

image_image_18 = PhotoImage(
    file=("image_18.png"))
image_18 = canvas.create_image(
    1108.0,
    982.8292236328125,
    image=image_image_18
)

# Code for fetching api data of multimedia


def bbc():
    try:
        # Replace 'YOUR_API_URL' with the actual API endpoint URL
        response = requests.get('https://virtuedu.com/api_virtuedu/modules/')
        data_list = response.json()

        # Check if any data has 'module_id' as '123Eth'
        found_data = [data for data in data_list if data.get(
            'module_id') == 'bbc']

        if found_data:
            new_window = Toplevel()
            new_window.geometry("500x500")
            new_window.title("Fetched Data")

            y_position = 30

            # Format and display the data in labels
            for data in found_data:
                title_label = Label(new_window, text=f"Title: {data.get('module_name')}",
                                    font=("Lexend deca", 15, "bold"), wraplength=400, justify=LEFT)
                title_label.place(x=30, y=y_position)
                y_position += title_label.winfo_reqheight()

                description_label = Label(new_window, text=f"Description: {data.get('module_description')}",
                                          wraplength=400, justify=LEFT)
                description_label.place(x=30, y=y_position)
                y_position += description_label.winfo_reqheight()

                tutor_label = Label(new_window, text=f"Tutor: {data.get('tutor_name')}",
                                    wraplength=400, justify=LEFT)
                tutor_label.place(x=30, y=y_position)
                y_position += tutor_label.winfo_reqheight()

                # Add other labels to display other data as needed

                separator = Frame(new_window, height=2, bd=1, relief=SUNKEN)
                separator.pack(fill=X, padx=5, pady=5)
                y_position += 10

        else:
            messagebox.showinfo(
                "Info", "Data is not available for module_id '123Eth'")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error fetching data from the API: {e}")


button_image_21 = PhotoImage(
    file=("button_21.png"))
button_21 = Button(
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command=bbc,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(108, 747, anchor="nw", window=button_21)


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
canvas.create_window(108, 1044, anchor="nw", window=button_22)

# Code for fetching API of Intro to multimedia module


def multi001():
    try:
        # Replace 'YOUR_API_URL' with the actual API endpoint URL
        response = requests.get('https://virtuedu.com/api_virtuedu/modules/')
        data_list = response.json()

        # Check if any data has 'module_id' as '123Eth'
        found_data = [data for data in data_list if data.get(
            'module_id') == 'multi001']

        if found_data:
            new_window = Toplevel()
            new_window.geometry("500x500")
            new_window.title("Fetched Data")

            y_position = 30

            # Format and display the data in labels
            for data in found_data:
                title_label = Label(new_window, text=f"Title: {data.get('module_name')}",
                                    font=("Lexend deca", 15, "bold"), wraplength=400, justify=LEFT)
                title_label.place(x=30, y=y_position)
                y_position += title_label.winfo_reqheight()

                description_label = Label(new_window, text=f"Description: {data.get('module_description')}",
                                          wraplength=400, justify=LEFT)
                description_label.place(x=30, y=y_position)
                y_position += description_label.winfo_reqheight()

                tutor_label = Label(new_window, text=f"Tutor: {data.get('tutor_name')}",
                                    wraplength=400, justify=LEFT)
                tutor_label.place(x=30, y=y_position)
                y_position += tutor_label.winfo_reqheight()

                # Add other labels to display other data as needed

                separator = Frame(new_window, height=2, bd=1, relief=SUNKEN)
                separator.pack(fill=X, padx=5, pady=5)
                y_position += 10

        else:
            messagebox.showinfo(
                "Info", "Data is not available for module_id '123Eth'")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error fetching data from the API: {e}")


button_image_23 = PhotoImage(
    file=("button_23.png"))
button_23 = Button(
    image=button_image_23,
    borderwidth=0,
    highlightthickness=0,
    command=multi001,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(402, 747, anchor="nw", window=button_23)


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
canvas.create_window(402, 1044, anchor="nw", window=button_24)

# Code to fetch api of Email Marketing Certification


def inbound():
    try:
        # Replace 'YOUR_API_URL' with the actual API endpoint URL
        response = requests.get('https://virtuedu.com/api_virtuedu/modules/')
        data_list = response.json()

        found_data = [data for data in data_list if data.get(
            'module_id') == 'inbound']

        if found_data:
            new_window = Toplevel()
            new_window.geometry("500x500")
            new_window.title("Fetched Data")

            y_position = 30

            # Format and display the data in labels
            for data in found_data:
                title_label = Label(new_window, text=f"Title: {data.get('module_name')}",
                                    font=("Lexend deca", 15, "bold"), wraplength=400, justify=LEFT)
                title_label.place(x=30, y=y_position)
                y_position += title_label.winfo_reqheight()

                description_label = Label(new_window, text=f"Description: {data.get('module_description')}",
                                          wraplength=400, justify=LEFT)
                description_label.place(x=30, y=y_position)
                y_position += description_label.winfo_reqheight()

                tutor_label = Label(new_window, text=f"Tutor: {data.get('tutor_name')}",
                                    wraplength=400, justify=LEFT)
                tutor_label.place(x=30, y=y_position)
                y_position += tutor_label.winfo_reqheight()

                # Add other labels to display other data as needed

                separator = Frame(new_window, height=2, bd=1, relief=SUNKEN)
                separator.pack(fill=X, padx=5, pady=5)
                y_position += 10

        else:
            messagebox.showinfo(
                "Info", "Data is not available for module_id '123Eth'")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error fetching data from the API: {e}")


button_image_25 = PhotoImage(
    file=("button_25.png"))
button_25 = Button(
    image=button_image_25,
    borderwidth=0,
    highlightthickness=0,
    command=inbound,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(705, 747, anchor="nw", window=button_25)


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
canvas.create_window(705, 1044, anchor="nw", window=button_26)

def Design001():
    try:
        # Replace 'YOUR_API_URL' with the actual API endpoint URL
        response = requests.get('https://virtuedu.com/api_virtuedu/modules/')
        data_list = response.json()

        # Check if any data has 'module_id' as '123Eth'
        found_data = [data for data in data_list if data.get(
            'module_id') == 'Design001']

        if found_data:
            new_window = Toplevel()
            new_window.geometry("500x500")
            new_window.title("Fetched Data")

            y_position = 30

            # Format and display the data in labels
            for data in found_data:
                title_label = Label(new_window, text=f"Title: {data.get('module_name')}",
                                    font=("Lexend deca", 15, "bold"), wraplength=400, justify=LEFT)
                title_label.place(x=30, y=y_position)
                y_position += title_label.winfo_reqheight()

                description_label = Label(new_window, text=f"Description: {data.get('module_description')}",
                                          wraplength=400, justify=LEFT)
                description_label.place(x=30, y=y_position)
                y_position += description_label.winfo_reqheight()

                tutor_label = Label(new_window, text=f"Tutor: {data.get('tutor_name')}",
                                    wraplength=400, justify=LEFT)
                tutor_label.place(x=30, y=y_position)
                y_position += tutor_label.winfo_reqheight()

                # Add other labels to display other data as needed

                separator = Frame(new_window, height=2, bd=1, relief=SUNKEN)
                separator.pack(fill=X, padx=5, pady=5)
                y_position += 10

        else:
            messagebox.showinfo(
                "Info", "Data is not available for module_id '123Eth'")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error fetching data from the API: {e}")

button_image_27 = PhotoImage(
    file=("button_27.png"))
button_27 = Button(
    image=button_image_27,
    borderwidth=0,
    highlightthickness=0,
    command=Design001,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(1001, 749, anchor="nw", window=button_27)


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
canvas.create_window(1001, 1046, anchor="nw", window=button_28)


canvas.create_text(
    107.0,
    708.0,
    anchor="nw",
    text="Learn about the basics of Multimedia Design \nand development with the help of this exceptional\ncourse. Get a certificate proving your dedication to the course.",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_text(
    107.0,
    1005.0,
    ancho="nw",
    text="Learn about the basics of Multimedia Design \nand development with the help of this exceptional\ncourse. Get a certificate proving your dedication to the course.",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_text(
    401.0,
    708.0,
    anchor="nw",
    text="Learn about the basics of Multimedia Design \nand development with the help of this exceptional\ncourse. Get a certificate proving your dedication to the course.",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_text(
    401.0,
    1005.0,
    anchor="nw",
    text="Learn about the basics of Multimedia Design \nand development with the help of this exceptional\ncourse. Get a certificate proving your dedication to the course.",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_text(
    704.0,
    708.0,
    anchor="nw",
    text="Learn about the basics of Multimedia Design \nand development with the help of this exceptional\ncourse. Get a certificate proving your dedication to the course.",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_text(
    704.0,
    1005.0,
    anchor="nw",
    text="Learn about the basics of Multimedia Design \nand development with the help of this exceptional\ncourse. Get a certificate proving your dedication to the course.",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_text(
    1000.0,
    710.0,
    anchor="nw",
    text="Learn about the basics of Multimedia Design \nand development with the help of this exceptional\ncourse. Get a certificate proving your dedication to the course.",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_text(
    1000.0,
    1007.0,
    anchor="nw",
    text="Learn about the basics of Multimedia Design \nand development with the help of this exceptional\ncourse. Get a certificate proving your dedication to the course.",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_rectangle(
    0.0,
    1189.0,
    1280.0,
    1455.0,
    fill="#3532A7",
    outline="")


# footer



canvas.create_text(
    62.0,
    1214.0,
    anchor="nw",
    text="VirtuEdu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 32 * -1)
)

canvas.create_text(
    506.0,
    1254.0,
    anchor="nw",
    text="Menu",
    fill="#fff",
    font=("Poppins SemiBold", 24 * -1)
)

canvas.create_text(
    740.0,
    1254.0,
    anchor="nw",
    text="Menu",
    fill="#fff",
    font=("Poppins SemiBold", 24 * -1)
)

canvas.create_text(
    1010.0,
    1254.0,
    anchor="nw",
    text="Menu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 24 * -1)
)

canvas.create_text(
    88.0,
    1260.0,
    anchor="nw",
    text="Learn Anywhere, Achieve Everywhere",
    fill="#FFFFFF",
    font=("Poppins Regular", 11 * -1)
)

canvas.create_text(
    50.0,
    1274.0,
    anchor="nw",
    text="Our innovative online learning platform empowers students\nto pursue their educational goals from anywhere in the world.\nWith flexible schedules and high-quality courses, we provide the\ntools and resources necessary for you to excel in your studies\nand succeed in any endeavor. Join our global community of\nlearners and unlock your full potential with Virtu Edu.",
    fill="#fff",
    font=("Poppins Medium", 12 * -1)
)


def Homes():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("multimedia_wala","build"))
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
    text= "Home",
    bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    
)
canvas.create_window(506, 1304, anchor="nw", window=button_3)

# button_3.place(
#     x=518.0,
#     y=2615.0,
#     width=30.0,
#     height=15.0
# )


button_image_112 = PhotoImage(
    file=("button_3.png"))
button_112 = Button(
    # image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=create_gui,
    relief="flat",
    text= "About Us",
    bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    

)
canvas.create_window(506, 1330, anchor="nw", window=button_112)

def Courses():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("multimedia_wala","homepage"))
        os.chdir(next_folder)

        # Run the gui.py file
        subprocess.Popen([sys.executable, 'gui.py'])

        window.destroy()


coursesbtn = Button(

    borderwidth=0,
    highlightthickness=0,
    
    relief="flat",
    text= "Courses",
    bg="#3532A7",
    fg="#fff",
    cursor="hand2",
    command=homefile
    

)
canvas.create_window(506, 1364, anchor="nw", window=coursesbtn)


events = PhotoImage(
    file=("button_3.png"))
eventbtn = Button(
    # image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=create_gui,
    relief="flat",
    text= "Events",
    bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    

)
canvas.create_window(506, 1394, anchor="nw", window=eventbtn)

def Routines():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("multimedia_wala","routines"))
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
    text= "Routines",    
    bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    

)
canvas.create_window(506, 1424, anchor="nw", window=routinebtn)

def termsandcondition():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("multimedia_wala","termsandconditions"))
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
    text= "Terms and Conditions",  
    bg="#3532A7",
    fg="#fff",
    cursor="hand2"

    

)
canvas.create_window(740, 1304, anchor="nw", window=termsandcon)


def alert1():
      # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("multimedia_wala","PrivacyPolicy"))
        os.chdir(next_folder)

        # Run the gui.py file
        subprocess.Popen([sys.executable, 'gui.py'])

        window.destroy()
   

privacy = Button(
    # image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=alert1,
    relief="flat",
    text= "Privacy Policy",
    bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    

)
canvas.create_window(740, 1334, anchor="nw", window=privacy)

def Support():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("multimedia_wala","support"))
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
    text= "Support",
    bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    

)
canvas.create_window(740, 1364, anchor="nw", window=support)

def contact():

    # Change to the next folder
    next_folder = os.path.join(
        os.getcwd().replace("multimedia_wala", "contact"))
    os.chdir(next_folder)

    # Run the gui.py file
    subprocess.Popen([sys.executable, 'gui.py'])

    window.destroy()

contact = Button(
    # image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=contact,
    relief="flat",
    text= "Contact Us",
    bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    

)
canvas.create_window(740, 1394, anchor="nw", window=contact)

cden = Button(
    # image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: webbrowser.open_new(r"http://www.cden.org.np"),
    relief="flat",
    text= "CDEN",
       bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    

)
canvas.create_window(1010, 1304, anchor="nw", window=cden)

ioe = Button(
    # image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: webbrowser.open_new(r"http://www.ioe.edu.np"),
    relief="flat",
    text= "IOE",
       bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    

)
canvas.create_window(1010, 1334, anchor="nw", window=ioe)

tu = Button(
    # image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: webbrowser.open_new(r"http://www.tu.edu.np"),
    relief="flat",
    text= "TU",
       bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    

)
canvas.create_window(1010, 1364, anchor="nw", window=tu)

cu = Button(
    # image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: webbrowser.open_new(r"http://www.coventry.ac.uk"),
    relief="flat",
    text= "Coventry University",
    bg="#3532A7",
    fg="#fff",
    cursor="hand2"
    

)
canvas.create_window(1010, 1394, anchor="nw", window=cu)

button_image_225 = PhotoImage(
    file=("home.png"))
button_225 = Button(
    image=button_image_225,
    borderwidth=0,
    highlightthickness=0,
    command=buildfile,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(388, 31, anchor="nw", window=button_225)



window.resizable(False, False)
window.mainloop()
