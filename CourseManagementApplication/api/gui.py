from tkinter import Tk, Label, Button
import requests

def get_data_from_api():
    response = requests.get('http://127.0.0.1:8000/api_virtuedu/modules/')
    return response.json()

def show_data():
    data = get_data_from_api()
    data_window = Tk()
    data_window.title("Data from API")
    for i, item in enumerate(data):
        label = Label(data_window, text=item)
        label.pack()
    data_window.mainloop()

root = Tk()
root.title("REST API App")
button = Button(root, text="Get Data", command=show_data)
button.pack()
root.mainloop()
