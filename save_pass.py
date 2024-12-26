from tkinter import messagebox as m
import json

class SavePassword:
    def save(self, website, email, password):
        def new_file():
            with open('weather_data.json', 'w') as file:
                json.dump(new_data, file, indent=2)

        inputed_website = website.get().title()
        inputed_email = email.get().title()
        inputed_pass = password.get().title()

        new_data = {
            inputed_website: {
                "website": inputed_website,
                "email": inputed_email,
                "password": inputed_pass
            }
        }

        if inputed_pass == "" or inputed_email == "" or inputed_website == "":
            m.showerror("Missing a requirement",
                        "You are missing one of the required boxes. Please fill all of the boxes before saving")
            return 0

        is_ok = m.askyesno("Are you sure you want to save the password?", f"Are you sure you want to save the information below?\n\nWebsite: {inputed_website}\nEmail/Username: {inputed_email}\nPassword: {inputed_pass}")
        if is_ok:
            website.delete(0, 'end')
            password.delete(0, 'end')

            website.focus()

            try:
                with open('weather_data.json') as old_data_file:
                    content = old_data_file.read()
                    old_data_file.seek(0)
                    if content != "" and content != "{}":
                        data = json.load(old_data_file)
                        data.update(new_data)
                        with open('weather_data.json', 'w') as data_file:
                            json.dump(data, data_file, indent=2)
                        m.showinfo("Saved Successfully", "Password saved successfully.")
                    else:
                        new_file()
                        m.showinfo("Saved Successfully", "Password saved successfully in 'weather_data.json'")
            except Exception:
                new_file()
                m.showinfo("Created File and Saved Successfully", "File 'weather_data.json' created and saved password successfully.")
