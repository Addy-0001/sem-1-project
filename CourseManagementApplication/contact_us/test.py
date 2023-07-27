import tkinter as tk
import requests

def fetch_data():
    try:
        response = requests.get('http://127.0.0.1:8000/api_virtuedu/contact/')
        response.raise_for_status()  # Raise exception if response status code is not 2xx
        data = response.json()

        if data:
            contact_name = data[0]['contact_name']
            email = data[0]['email']
            message = data[0]['message']

            # Display the data in Tkinter
            label_contact_name.config(text=f"Contact Name: {contact_name}")
            label_email.config(text=f"Email: {email}")
            label_message.config(text=f"Message: {message}")
        else:
            # Handle no data scenario
            label_contact_name.config(text="No data available")
            label_email.config(text="")
            label_message.config(text="")
    except requests.exceptions.RequestException as e:
        # Handle network errors
        label_contact_name.config(text="Network Error")
        label_email.config(text="")
        label_message.config(text=str(e))

# Create Tkinter window
window = tk.Tk()

# Create labels to display data
label_contact_name = tk.Label(window)
label_contact_name.pack()

label_email = tk.Label(window)
label_email.pack()

label_message = tk.Label(window)
label_message.pack()

# Create button to fetch data
button_fetch_data = tk.Button(window, text="Fetch Data", command=fetch_data)
button_fetch_data.pack()

# Start Tkinter event loop
window.mainloop()
