from tkinter import *
from tkinter import ttk
from tkinter import messagebox as m
import json

class ViewPassword:
    def view(self):
        def delete_all():
            delete_all_true = m.askyesno("Are you sure about this?", "Are you sure you want to delete all your passwords? You cannot get them back.")
            if delete_all_true:
                with open('weather_data.json', 'w') as file:
                    json.dump({}, file, indent=2)
                m.showwarning("Deleted", "Deleted all passwords successfully.")
                view_passwords.destroy()
                self.view()

        def delete(item):
            delete_true = m.askyesno("Are you sure?", "Are you sure you want to delete this password? You cannot get it back.")
            if delete_true:
                with open('weather_data.json') as file:
                    data = json.load(file)
                if item in data:
                    del data[item]
                with open('weather_data.json', 'w') as file:
                    json.dump(data, file, indent=2)
                m.showwarning("Deleted", "Deleted the password successfully.")
                view_passwords.destroy()
                self.view()

        view_passwords = Toplevel()
        view_passwords.title("View Saved Passwords")
        view_passwords.config(pady=20, padx=20)

        try:
            with open('weather_data.json') as file:
                content = json.load(file)
        except FileNotFoundError:
            content = {}

        Label(view_passwords, text="Website | Username/Email | Password", font=('Arial', 18, 'bold')).pack()
        Label(view_passwords, text="#----------------------------------------------------------------------------------------#", font=('Arial', 12, 'bold')).pack()

        if content:
            for data in content:
                information = f"{content[data]['website']} | {content[data]['email']} | {content[data]['password']}"
                frame = Frame(view_passwords)
                Label(frame, text=information).pack(side='left')
                ttk.Button(frame, text="Delete", command=lambda: delete(data)).pack(side='right', padx=10)
                frame.pack()
            ttk.Button(view_passwords, text="Delete All Passwords", command=delete_all).pack(pady=5)
        else:
            Label(view_passwords, text="No passwords saved.", font=("Arial", 14)).pack()
