import tkinter as tk
from datetime import datetime, timedelta

def generate_card():
    today = datetime.now()
    future_date = today + timedelta(days=15)
    
    card_title = f"Today's Date: {today.strftime('%Y-%m-%d')}"
    card_content = f"15 Days Later: {future_date.strftime('%Y-%m-%d')}"

    title_label.config(text=card_title)
    content_label.config(text=card_content)

root = tk.Tk()
root.title("Date Card Generator")

button_44 = tk.Button(root, text="Generate Card", command=generate_card)
button_44.pack(padx=20, pady=20)

title_label = tk.Label(root, text="", font=("Helvetica", 16))
title_label.pack(padx=10, pady=10)

content_label = tk.Label(root, text="", font=("Helvetica", 14))
content_label.pack(padx=10, pady=10)

root.mainloop()
