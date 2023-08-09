from tkinter import messagebox
from tkinter import *
from tkinter import ttk
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
def buildfile():
 
        # Change to the next folder
        next_folder = os.path.join(os.getcwd().replace("homepage","build"))
        os.chdir(next_folder)

        # Run the gui.py file
        subprocess.Popen([sys.executable, 'gui.py'])

        window.destroy()


def routinesfile():

    # Change to the next folder
    next_folder = os.path.join(os.getcwd().replace("homepage", "routines"))
    os.chdir(next_folder)

    # Run the gui.py file
    subprocess.Popen([sys.executable, 'gui.py'])

    window.destroy()


def requestsfile():

    # Change to the next folder
    next_folder = os.path.join(
        os.getcwd().replace("homepage", "requests_notdone"))
    os.chdir(next_folder)

    # Run the gui.py file
    subprocess.Popen([sys.executable, 'gui.py'])

    window.destroy()


def computingfile():

    # Change to the next folder
    next_folder = os.path.join(
        os.getcwd().replace("homepage", "computing_wala"))
    os.chdir(next_folder)

    # Run the gui.py file
    subprocess.Popen([sys.executable, 'gui.py'])

    window.destroy()


def multimediafile():

    # Change to the next folder
    next_folder = os.path.join(
        os.getcwd().replace("homepage", "multimedia_wala"))
    os.chdir(next_folder)

    # Run the gui.py file
    subprocess.Popen([sys.executable, 'gui.py'])

    window.destroy()


def marketingfile():

    # Change to the next folder
    next_folder = os.path.join(
        os.getcwd().replace("homepage", "marketing_wala"))
    os.chdir(next_folder)

    # Run the gui.py file
    subprocess.Popen([sys.executable, 'gui.py'])

    window.destroy()


def languagefile():

    # Change to the next folder
    next_folder = os.path.join(os.getcwd().replace("homepage", "language_wala"))
    os.chdir(next_folder)

    # Run the gui.py file
    subprocess.Popen([sys.executable, 'gui.py'])

    window.destroy()


def designingfile():

    # Change to the next folder
    next_folder = os.path.join(
        os.getcwd().replace("homepage", "designing_wala"))
    os.chdir(next_folder)

    # Run the gui.py file
    subprocess.Popen([sys.executable, 'gui.py'])

    window.destroy()


def homefile():

    # Change to the next folder
    next_folder = os.path.join(os.getcwd().replace("homepage", "homepage"))
    print(next_folder)
    os.chdir(next_folder)

    # Run the gui.py file
    subprocess.Popen([sys.executable, 'gui.py'])

    window.destroy()


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
    relief="flat",
    cursor="hand2"
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
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
canvas.create_window(717, 20, anchor="nw", window=entry_1)


button_image_2 = PhotoImage(
    file=("notification.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=create_gui,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(1110, 31, anchor="nw", window=button_2)


image_image_1 = PhotoImage(
    file=("image_1.png"))
image_1 = canvas.create_image(
    496.0,
    295.0,
    image=image_image_1
)

button_image_3 = PhotoImage(
    file=("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=computingfile,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(400, 457, anchor="nw", window=button_3)


button_image_4 = PhotoImage(
    file=("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=homefile,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(260, 456, anchor="nw", window=button_4)


button_image_5 = PhotoImage(
    file=("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=multimediafile,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(526, 457, anchor="nw", window=button_5)


button_image_6 = PhotoImage(
    file=("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=designingfile,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(660, 457, anchor="nw", window=button_6)

button_image_7 = PhotoImage(
    file=("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=languagefile,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(785, 457, anchor="nw", window=button_7)


button_image_8 = PhotoImage(
    file=("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=marketingfile,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(925, 457, anchor="nw", window=button_8)


canvas.create_text(
    797.0,
    195.0,
    anchor="nw",
    text="Our Courses",
    fill="#646ECB",
    font=("OpenSans Bold", 60 * -1)
)

canvas.create_text(
    794.0,
    285.0,
    anchor="nw",
    text="Unlock your potential with our transformative courses.",
    fill="#646ECB",
    font=("Poppins Regular", 15 * -1)
)

canvas.create_rectangle(
    972.0,
    1429.0,
    1214.0,
    1673.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    969.0,
    1114.0,
    1211.0,
    1358.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    972.0,
    814.0,
    1214.0,
    1058.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    972.0,
    529.0,
    1214.0,
    773.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    671.0,
    1429.0,
    913.0,
    1673.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    668.0,
    1114.0,
    910.0,
    1358.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    671.0,
    814.0,
    913.0,
    1058.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    671.0,
    529.0,
    913.0,
    773.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    363.0,
    1429.0,
    605.0,
    1673.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    360.0,
    1114.0,
    602.0,
    1358.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    363.0,
    814.0,
    605.0,
    1058.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    363.0,
    529.0,
    605.0,
    773.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    54.0,
    1429.0,
    296.0,
    1673.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    51.0,
    1114.0,
    293.0,
    1358.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    54.0,
    814.0,
    296.0,
    1058.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    54.0,
    529.0,
    296.0,
    773.0,
    fill="#FFFFFF",
    outline="")

image_image_2 = PhotoImage(
    file=("image_2.png"))
image_2 = canvas.create_image(
    1093.0,
    1491.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=("image_3.png"))
image_3 = canvas.create_image(
    1090.0,
    1176.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=("image_4.png"))
image_4 = canvas.create_image(
    1093.0,
    876.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=("image_5.png"))
image_5 = canvas.create_image(
    1093.0,
    591.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=("image_6.png"))
image_6 = canvas.create_image(
    792.0,
    1491.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=("image_7.png"))
image_7 = canvas.create_image(
    789.0,
    1176.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=("image_8.png"))
image_8 = canvas.create_image(
    792.0,
    876.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=("image_9.png"))
image_9 = canvas.create_image(
    792.0,
    591.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=("image_10.png"))
image_10 = canvas.create_image(
    484.0,
    1491.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=("image_11.png"))
image_11 = canvas.create_image(
    481.0,
    1176.0,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=("image_12.png"))
image_12 = canvas.create_image(
    484.0,
    876.0,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=("image_13.png"))
image_13 = canvas.create_image(
    484.0,
    591.0,
    image=image_image_13
)

image_image_14 = PhotoImage(
    file=("image_14.png"))
image_14 = canvas.create_image(
    175.0,
    1491.0,
    image=image_image_14
)

image_image_15 = PhotoImage(
    file=("image_15.png"))
image_15 = canvas.create_image(
    172.0,
    1176.0,
    image=image_image_15
)

image_image_16 = PhotoImage(
    file=("image_16.png"))
image_16 = canvas.create_image(
    175.0,
    876.0,
    image=image_image_16
)

image_image_17 = PhotoImage(
    file=("image_17.png"))
image_17 = canvas.create_image(
    175.0,
    591.0,
    image=image_image_17
)

canvas.create_text(
    985.0,
    1589.731689453125,
    anchor="nw",
    text="SQLite3 Database",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    982.0,
    1274.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    985.0,
    974.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    985.0,
    689.731689453125,
    anchor="nw",
    text="HTML Basics",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    684.0,
    1589.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    681.0,
    1274.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    684.0,
    974.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    684.0,
    689.731689453125,
    anchor="nw",
    text="CSS Basics",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    376.0,
    1589.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    373.0,
    1274.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    376.0,
    974.731689453125,
    anchor="nw",
    text="Introduction to User Experience Design",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    376.0,
    689.731689453125,
    anchor="nw",
    text="Tkinter Basics",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    67.0,
    1589.731689453125,
    anchor="nw",
    text="HTML Basics",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    64.0,
    1274.731689453125,
    anchor="nw",
    text="CSS Basics",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    67.0,
    974.731689453125,
    anchor="nw",
    text="Tkinter Basics",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

canvas.create_text(
    67.0,
    689.731689453125,
    anchor="nw",
    text="SQLite3 Database",
    fill="#000000",
    font=("OpenSans SemiboldItalic", 12 * -1)
)

image_image_18 = PhotoImage(
    file=("image_18.png"))
image_18 = canvas.create_image(
    1028.0,
    1564.12548828125,
    image=image_image_18
)

image_image_19 = PhotoImage(
    file=("image_19.png"))
image_19 = canvas.create_image(
    1025.0,
    1249.12548828125,
    image=image_image_19
)

image_image_20 = PhotoImage(
    file=("image_20.png"))
image_20 = canvas.create_image(
    1028.0,
    949.12548828125,
    image=image_image_20
)

image_image_21 = PhotoImage(
    file=("image_21.png"))
image_21 = canvas.create_image(
    1028.0,
    664.12548828125,
    image=image_image_21
)

image_image_22 = PhotoImage(
    file=("image_22.png"))
image_22 = canvas.create_image(
    727.0,
    1564.12548828125,
    image=image_image_22
)

image_image_23 = PhotoImage(
    file=("image_23.png"))
image_23 = canvas.create_image(
    724.0,
    1249.12548828125,
    image=image_image_23
)

image_image_24 = PhotoImage(
    file=("image_24.png"))
image_24 = canvas.create_image(
    727.0,
    949.12548828125,
    image=image_image_24
)

image_image_25 = PhotoImage(
    file=("image_25.png"))
image_25 = canvas.create_image(
    727.0,
    664.12548828125,
    image=image_image_25
)

image_image_26 = PhotoImage(
    file=("image_26.png"))
image_26 = canvas.create_image(
    419.0,
    1564.12548828125,
    image=image_image_26
)

image_image_27 = PhotoImage(
    file=("image_27.png"))
image_27 = canvas.create_image(
    416.0,
    1249.12548828125,
    image=image_image_27
)

image_image_28 = PhotoImage(
    file=("image_28.png"))
image_28 = canvas.create_image(
    419.0,
    949.12548828125,
    image=image_image_28
)

image_image_29 = PhotoImage(
    file=("image_29.png"))
image_29 = canvas.create_image(
    419.0,
    664.12548828125,
    image=image_image_29
)

image_image_30 = PhotoImage(
    file=("image_30.png"))
image_30 = canvas.create_image(
    110.0,
    1564.12548828125,
    image=image_image_30
)

image_image_31 = PhotoImage(
    file=("image_31.png"))
image_31 = canvas.create_image(
    107.0,
    1249.12548828125,
    image=image_image_31
)

image_image_32 = PhotoImage(
    file=("image_32.png"))
image_32 = canvas.create_image(
    110.0,
    949.12548828125,
    image=image_image_32
)

image_image_33 = PhotoImage(
    file=("image_33.png"))
image_33 = canvas.create_image(
    110.0,
    664.12548828125,
    image=image_image_33
)

image_image_34 = PhotoImage(
    file=("image_34.png"))
image_34 = canvas.create_image(
    1093.0,
    1581.8292236328125,
    image=image_image_34
)

image_image_35 = PhotoImage(
    file=("image_35.png"))
image_35 = canvas.create_image(
    1090.0,
    1266.8292236328125,
    image=image_image_35
)

image_image_36 = PhotoImage(
    file=("image_36.png"))
image_36 = canvas.create_image(
    1093.0,
    966.8292236328125,
    image=image_image_36
)

image_image_37 = PhotoImage(
    file=("image_37.png"))
image_37 = canvas.create_image(
    1093.0,
    681.8292236328125,
    image=image_image_37
)

image_image_38 = PhotoImage(
    file=("image_38.png"))
image_38 = canvas.create_image(
    792.0,
    1581.8292236328125,
    image=image_image_38
)

image_image_39 = PhotoImage(
    file=("image_39.png"))
image_39 = canvas.create_image(
    789.0,
    1266.8292236328125,
    image=image_image_39
)

image_image_40 = PhotoImage(
    file=("image_40.png"))
image_40 = canvas.create_image(
    792.0,
    966.8292236328125,
    image=image_image_40
)

image_image_41 = PhotoImage(
    file=("image_41.png"))
image_41 = canvas.create_image(
    792.0,
    681.8292236328125,
    image=image_image_41
)

image_image_42 = PhotoImage(
    file=("image_42.png"))
image_42 = canvas.create_image(
    484.0,
    1581.8292236328125,
    image=image_image_42
)

image_image_43 = PhotoImage(
    file=("image_43.png"))
image_43 = canvas.create_image(
    481.0,
    1266.8292236328125,
    image=image_image_43
)

image_image_44 = PhotoImage(
    file=("image_44.png"))
image_44 = canvas.create_image(
    484.0,
    966.8292236328125,
    image=image_image_44
)

image_image_45 = PhotoImage(
    file=("image_45.png"))
image_45 = canvas.create_image(
    484.0,
    681.8292236328125,
    image=image_image_45
)

image_image_46 = PhotoImage(
    file=("image_46.png"))
image_46 = canvas.create_image(
    175.0,
    1581.8292236328125,
    image=image_image_46
)

image_image_47 = PhotoImage(
    file=("image_47.png"))
image_47 = canvas.create_image(
    172.0,
    1266.8292236328125,
    image=image_image_47
)

image_image_48 = PhotoImage(
    file=("image_48.png"))
image_48 = canvas.create_image(
    175.0,
    966.8292236328125,
    image=image_image_48
)

image_image_49 = PhotoImage(
    file=("image_49.png"))
image_49 = canvas.create_image(
    175.0,
    681.8292236328125,
    image=image_image_49
)

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
button_9.place(
    x=986.0,
    y=1645.79443359375,
    width=66.7545166015625,
    height=18.074081420898438
)

button_image_10 = PhotoImage(
    file=("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(983, 1331, anchor="nw", window=button_10)

button_10.place(
    x=983.0,
    y=1330.79443359375,
    width=66.7545166015625,
    height=18.074081420898438
)

button_image_11 = PhotoImage(
    file=("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(986, 1030, anchor="nw", window=button_11)


def Web001():
    try:
        # Replace 'YOUR_API_URL' with the actual API endpoint URL
        response = requests.get('https://virtuedu.com/api_virtuedu/modules/')
        data_list = response.json()

        # Check if any data has 'module_id' as '123Eth'
        found_data = [data for data in data_list if data.get(
            'module_id') == 'Web001']

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


button_image_12 = PhotoImage(
    file=("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=Web001,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(986, 745, anchor="nw", window=button_12)


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
canvas.create_window(685, 1645, anchor="nw", window=button_13)


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
canvas.create_window(682, 1130, anchor="nw", window=button_14)

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
canvas.create_window(685, 1030, anchor="nw", window=button_15)


def Web002():
    try:
        # Replace 'YOUR_API_URL' with the actual API endpoint URL
        response = requests.get('https://virtuedu.com/api_virtuedu/modules/')
        data_list = response.json()

        # Check if any data has 'module_id' as '123Eth'
        found_data = [data for data in data_list if data.get(
            'module_id') == 'Web002']

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


button_image_16 = PhotoImage(
    file=("button_16.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=Web002,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(685, 745, anchor="nw", window=button_16)


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
canvas.create_window(377, 1645, anchor="nw", window=button_17)


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
canvas.create_window(374, 1330, anchor="nw", window=button_18)

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
canvas.create_window(377, 1030, anchor="nw", window=button_19)


def soft002():
    try:
        # Replace 'YOUR_API_URL' with the actual API endpoint URL
        response = requests.get('https://virtuedu.com/api_virtuedu/modules/')
        data_list = response.json()

        # Check if any data has 'module_id' as '123Eth'
        found_data = [data for data in data_list if data.get(
            'module_id') == 'soft002']

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


button_image_20 = PhotoImage(
    file=("button_20.png"))
button_20 = Button(
    image=button_image_20,
    borderwidth=0,
    highlightthickness=0,
    command=soft002,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(377, 745, anchor="nw", window=button_20)


button_image_21 = PhotoImage(
    file=("button_21.png"))
button_21 = Button(
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_21 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(68, 1645, anchor="nw", window=button_21)


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
canvas.create_window(65, 1330, anchor="nw", window=button_22)


button_image_23 = PhotoImage(
    file=("button_23.png"))
button_23 = Button(
    image=button_image_23,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_23 clicked"),
    relief="flat",
    cursor="hand2"
)
canvas.create_window(68, 1030, anchor="nw", window=button_23)


# Importing data for button 24
def Web003():
    try:
        # Replace 'YOUR_API_URL' with the actual API endpoint URL
        response = requests.get('https://virtuedu.com/api_virtuedu/modules/')
        data_list = response.json()

        # Check if any data has 'module_id' as '123Eth'
        found_data = [data for data in data_list if data.get(
            'module_id') == 'Web003']

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


button_image_24 = PhotoImage(
    file=("button_24.png"))
button_24 = Button(
    image=button_image_24,
    borderwidth=0,
    highlightthickness=0,
    command=Web003,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(68, 745, anchor="nw", window=button_24)

button_24.place(
    x=68.0,
    y=745.79443359375,
    width=66.7545166015625,
    height=18.0740966796875
)

canvas.create_text(
    985.0,
    1606.0,
    anchor="nw",
    text="Learn about the basics of ",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_text(
    982.0,
    1291.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with \nour Introduction to User Experience Design course. Dive into the \nworld of interactive design, learn the fundamentals of user-centered \nthinking, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_text(
    985.0,
    991.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with \nour Introduction to User Experience Design course. Dive into the \nworld of interactive design, learn the fundamentals of user-centered \nthinking, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_text(
    985.0,
    706.0,
    anchor="nw",
    text="Learn about the basics of web page development using HTML. Dive \ninto the world of web pages and learn about the DOM.\n(Document Object Model)",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_text(
    684.0,
    1606.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with \nour Introduction to User Experience Design course. Dive into the \nworld of interactive design, learn the fundamentals of user-centered \nthinking, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_text(
    681.0,
    1291.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with \nour Introduction to User Experience Design course. Dive into the \nworld of interactive design, learn the fundamentals of user-centered \nthinking, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_text(
    684.0,
    991.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with \nour Introduction to User Experience Design course. Dive into the \nworld of interactive design, learn the fundamentals of user-centered \nthinking, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_text(
    684.0,
    706.0,
    anchor="nw",
    text="Learn about developing responsive web applications using CSS.\nLearn about flex box and grid layouts and get lost in the \nbeautiful world of CSS Design.",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_text(
    376.0,
    1606.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with \nour Introduction to User Experience Design course. Dive into the \nworld of interactive design, learn the fundamentals of user-centered \nthinking, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_text(
    373.0,
    1291.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with \nour Introduction to User Experience Design course. Dive into the \nworld of interactive design, learn the fundamentals of user-centered \nthinking, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_text(
    376.0,
    991.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with \nour Introduction to User Experience Design course. Dive into the \nworld of interactive design, learn the fundamentals of user-centered \nthinking, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_text(
    376.0,
    706.0,
    anchor="nw",
    text="Learn about the basics of developing responsive software using\ntkinter. Explore the world of python development as you would like\nto.",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_text(
    67.0,
    1606.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with \nour Introduction to User Experience Design course. Dive into the \nworld of interactive design, learn the fundamentals of user-centered \nthinking, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_text(
    64.0,
    1291.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with \nour Introduction to User Experience Design course. Dive into the \nworld of interactive design, learn the fundamentals of user-centered \nthinking, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_text(
    67.0,
    991.0,
    anchor="nw",
    text="Discover the art of crafting exceptional user experiences with \nour Introduction to User Experience Design course. Dive into the \nworld of interactive design, learn the fundamentals of user-centered \nthinking, and acquire the skills to create intuitive,",
    fill="#000000",
    font=("OpenSans Regular", 7 * -1)
)

canvas.create_text(
    67.0,
    706.0,
    anchor="nw",
    text="Learn about creating tables, rows and defining the attributes of a \ndatabase. Learn all there is to learn about Database management.",
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

button_image_25 = PhotoImage(
    file=("home.png"))
button_25 = Button(
    image=button_image_25,
    borderwidth=0,
    highlightthickness=0,
    command=buildfile,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(394, 31, anchor="nw", window=button_25)


button_image_26 = PhotoImage(
    file=("routines.png"))
button_26 = Button(
    image=button_image_26,
    borderwidth=0,
    highlightthickness=0,
    command=routinesfile,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(542, 32, anchor="nw", window=button_26)


button_image_27 = PhotoImage(
    file=("requests.png"))
button_27 = Button(
    image=button_image_27,
    borderwidth=0,
    highlightthickness=0,
    command=requestsfile,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(624, 32, anchor="nw", window=button_27)


button_image_28 = PhotoImage(
    file=("courses.png"))
button_28 = Button(
    image=button_image_28,
    borderwidth=0,
    highlightthickness=0,
    command=homefile,
    relief="flat",
    cursor="hand2"
)
canvas.create_window(460, 32, anchor="nw", window=button_28)


window.resizable(False, False)
window.mainloop()
