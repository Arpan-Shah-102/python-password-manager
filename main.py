from tkinter import *
from tkinter import ttk
import ctypes

import random_pass as rp
import save_pass as sp
import view_pass as vp
import search_pass as spw

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except Exception:
    pass

window = Tk()
window.call('tk', 'scaling', 2)

logo = PhotoImage(file='logo.png')

logo_canvas = Canvas(window, width=300, height=400, highlightthickness=0)
logo_canvas.create_image(150, 200, image=logo)
logo_canvas.grid(row=0, column=0, columnspan=3)

ttk.Label(window, text='Website:', width=16).grid(row=1, column=0)
ttk.Label(window, text='Email/Username:', width=16).grid(row=2, column=0)
ttk.Label(window, text='Password:', width=16).grid(row=3, column=0)

website = ttk.Entry(window, width=26)
website.grid(row=1, column=1)
website.focus()

email = ttk.Entry(window, width=45)
email.grid(row=2, column=1, columnspan=2)

password = ttk.Entry(window, width=26)
password.grid(row=3, column=1)

ttk.Button(window, width=18, padding=0, text="Search", command=lambda: spw.SearchPasswords().search(website)).grid(row=1, column=2)
ttk.Button(window, width=18, padding=0, text='Generate Password', command=lambda: rp.RandomPassword().get_pass(password)).grid(row=3, column=2)
ttk.Button(window, width=38, padding=0, text="Add", command=lambda: sp.SavePassword().save(website, email, password)).grid(row=4, column=1, columnspan=2, sticky='e')
ttk.Button(window, width=22, padding=0, text="View Saved Passwords", command=lambda: vp.ViewPassword().view()).grid(row=4, column=0, columnspan=2, sticky='w')

window.title('My Pass - Password Manager')
window.config(padx=50, pady=50)
window.mainloop()
