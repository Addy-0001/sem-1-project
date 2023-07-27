from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("1280x800")
window.configure(bg="#EEEFF3")

# Create a Canvas widget with a scrollbar
canvas = Canvas(window, height=200)
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
    2529.0,
    1280.0,
    2795.0,
    fill="#82B4FF",
    outline="")

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
    y=38.9105224609375,
    width=17.694091796875,
    height=35.137451171875
)

image_image_1 = PhotoImage(
    file=("image_1.png"))
image_1 = canvas.create_image(
    359.0,
    294.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=("image_2.png"))
image_2 = canvas.create_image(
    974.0001220703125,
    221.4852294921875,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=("image_3.png"))
image_3 = canvas.create_image(
    752.0001220703125,
    276.3968505859375,
    image=image_image_3
)

canvas.create_text(
    738.0,
    214.0,
    anchor="nw",
    text="Privacy Policy",
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

canvas.create_text(
    62.0,
    2557.0,
    anchor="nw",
    text="VirtuEdu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 32 * -1)
)

canvas.create_text(
    506.0,
    2572.0,
    anchor="nw",
    text="Menu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 24 * -1)
)

canvas.create_text(
    740.0,
    2572.0,
    anchor="nw",
    text="Menu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 24 * -1)
)

canvas.create_text(
    1010.0,
    2572.0,
    anchor="nw",
    text="Menu",
    fill="#FFFFFF",
    font=("Poppins SemiBold", 24 * -1)
)

canvas.create_text(
    62.0,
    2603.0,
    anchor="nw",
    text="Learn Anywhere, Achieve Everywhere",
    fill="#FFFFFF",
    font=("Poppins Regular", 11 * -1)
)

canvas.create_text(
    62.0,
    2628.0,
    anchor="nw",
    text="Our innovative online learning platform empowers students to \n pursue  their educational goals from anywhere in the world. \n With flexible schedules and high-quality courses, we provide the tools \nand resources necessary for you to excel in your studies and succeed \n in any endeavor. Join our global community of learners and unlock your \n full potential with Virtu Edu.",
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
    x=518.0,
    y=2615.0,
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
    x=749.0,
    y=2612.0,
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
    x=1023.0,
    y=2612.0,
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
    x=1023.0,
    y=2637.0,
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
    x=1024.0,
    y=2662.0,
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
    x=1024.0,
    y=2687.0,
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
    x=751.0,
    y=2637.0,
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
    x=751.0,
    y=2662.0,
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
    x=751.0,
    y=2687.0,
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
    x=518.0,
    y=2640.0,
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
    x=518.0,
    y=2665.0,
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
    x=518.0,
    y=2690.0,
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
    x=518.0,
    y=2715.0,
    width=39.0,
    height=15.0
)

button_image_16 = PhotoImage(
    file=("home.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_16 clicked"),
    relief="flat"
)
button_16.place(
    x=385.0,
    y=31.0,
    width=43.0,
    height=20.0
)

button_image_17 = PhotoImage(
    file=("courses.png"))
button_17 = Button(
    window,
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Course Button Clicked"),
    relief="flat"
)
canvas.create_window(459, 28, anchor="nw", window=button_17)

button_image_18 = PhotoImage(
    file=("routines.png"))
button_18 = Button(
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_18 clicked"),
    relief="flat"
)
button_18.place(
    x=446.0,
    y=32.0,
    # width=69.0,
    # height=20.0
)

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

canvas.create_text(
    44.0,
    467.0,
    anchor="nw",
    text="Privacy Policy for VirtuEdu\nAt VirtuEdu, we are committed to protecting your privacy and ensuring the security of any personal information you provide to us. This \nPrivacy Policy outlines how we collect, use, and safeguard your personal information \when you access and use our web application.\n\nInformation Collection and Use:\nWe may collect certain personally identifiable information from you, such as your name, email address, and other contact details when \nyou register for our courses or interact with our website. This information is used to provide you with the requested services, improve \nour courses and services, and communicate important updates and announcements."
"\n\nData Security:"
"\nWe take appropriate measures to protect the security of your personal information and prevent unauthorized access, disclosure, alteration, \nor destruction of data. We use industry-standard security technologies and procedures to ensure the confidentiality and integrity of your \ninformation."

"\n\nData Retention:"
"\nWe retain your personal information only for as long as necessary to fulfill the purposes for which it was collected and as required by \napplicable laws and regulations. Once the purpose is fulfilled, we will securely dispose of or anonymize your personal information."

"\n\nCookies and Tracking Technologies:"
"\nOur website may use cookies and similar tracking technologies to enhance your browsing experience, analyze usage patterns, and \npersonalize content. You can choose to disable cookies through your browser settings, but this may affect the functionality of our website."

"\n\nThird-Party Disclosure:"
"\nWe do not sell, trade, or otherwise transfer your personal information to third parties unless we have your consent or are required by \nlaw to do so. However, we may share non-personally identifiable information with trusted third-party service providers to help us operate \nour website and deliver our services."

"\n\nChildren's Privacy:"
"\nOur services are not intended for children under the age of 13. We do not knowingly collect personal information from individuals under \n13 years of age. If you believe that we may have collected personal information from a child under 13, please contact us, and we will \npromptly remove the information."

"\n\nChanges to this Privacy Policy:"
"\nWe reserve the right to update or modify this Privacy Policy at any time. Any changes will be effective immediately upon posting the \nupdated policy on our website. We encourage you to review this Privacy Policy periodically to stay informed about how we protect your \npersonal information."

"\n\nContact Us:"
"\nIf you have any questions, concerns, or requests regarding this Privacy Policy or the handling of your personal information, please contact \nus at  heypsycho339@gmail.com"

"\n\nBy using the VirtuEdu web application, you consent to the terms of this Privacy Policy and the collection and use of your personal \ninformation as described herein."

,
    fill="#000000",
    font=("lexend deca", 15,)
)

canvas.create_text(
    44.0,
    1500.0,
    anchor="nw",
    text="All other terms and conditions as applicable under the Terms and Conditions of Us \n will be applicable to You and will be read along with this Privacy Policy.",
    fill="#000000",
    font=("Poppins Medium", 24 * -1)
)
# Update the scroll region to include the entire frame
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))
window.resizable(False, False)
window.mainloop()
