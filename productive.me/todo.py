from sqlite3 import *
from datetime import datetime
from os import path
from sys import argv
from tkinter import *

task = []

def add_task():
    task.append([datetime.now(), entry.get()])
    entry.delete(0, END)
    update_list()

def update_list():
    listbox.delete(0, END)
    for i in task:
        listbox.insert(END, i[1])
    
def save():
    if path.exists('todo.db'):
        conn = connect('todo.db')
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS todo (date TEXT, task TEXT)')
        for i in task:
            cur.execute('INSERT INTO todo VALUES (?, ?)', (i[0], i[1]))
        conn.commit()
        conn.close()
    else:
        print('Database not found')

def load():
    if path.exists('todo.db'):
        conn = connect('todo.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM todo')
        for i in cur.fetchall():
            task.append(i)
        conn.close()
        update_list()
    else:
        print('Database not found')

def delete():
    try:
        task.pop(listbox.curselection()[0])
        update_list()
    except:
        pass

def clear():
    task.clear()
    update_list()

def main():
    global entry, listbox
    root = Tk()
    root.title('To-Do List')
    root.geometry('400x400')
    root.resizable(False, False)
    # root.iconbitmap('todo.ico')

    entry = Entry(root, width=50)
    entry.pack(pady=10)

    frame = Frame(root)
    frame.pack()

    scrollbar = Scrollbar(frame, orient=VERTICAL)
    scrollbar.pack(side=RIGHT, fill=Y)

    listbox = Listbox(frame, width=50, height=15, yscrollcommand=scrollbar.set)
    listbox.pack()

    scrollbar.config(command=listbox.yview)

    add_button = Button(root, text='Add Task', command=add_task)
    add_button.pack(pady=10)

    delete_button = Button(root, text='Delete Task', command=delete)
    delete_button.pack(pady=5)

    clear_button = Button(root, text='Clear All', command=clear)
    clear_button.pack(pady=5)

    save_button = Button(root, text='Save', command=save)
    save_button.pack(pady=5)

    load_button = Button(root, text='Load', command=load)
    load_button.pack(pady=5)

    root.mainloop()

if __name__ == '__main__':
    main()
    