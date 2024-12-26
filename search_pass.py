from tkinter import messagebox as m
import json

class SearchPasswords:
    def search(self, website):
        website_content = website.get().title()
        try:
            with open('weather_data.json', 'r') as file:
                data = json.load(file)
                m.showinfo(website, f'Username/Email: {data[website_content]['email']}\nPassword: {data[website_content]['password']}')
                website.delete(0, 'end')
        except FileNotFoundError:
            m.showerror("Error", "File not found, please make a password to create a file.")
        except KeyError:
            m.showerror("Error", "Username/Password not found, please enter a valid website.")
