import string
import tkinter as tk
from tkinter import ttk, messagebox
import random
import pyperclip
import json


# -----------------------------Search Website ----------------------------------#
def search_website():
    website = website_entry.get().strip()
    if website == "":
        messagebox.showerror("Oops", "Please enter a website.")
        return
    try:
        with open('Day 029/data.json', 'r') as datafile:
            data = json.load(datafile)
    except FileNotFoundError:
        messagebox.showinfo("Oops", "No data found.")
    else:
        website = website_entry.get().strip()
        if website in data:
            username = data[website]['username']
            password = data[website]['password']
            messagebox.showinfo(website, f"Username: {username}\nPassword: {password}")
        else:
            messagebox.showinfo("Oops", "No entry found.")
        

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Generate Password button
def generate_password():
    password = [str(random.randint(0,9)) for _ in range(random.randint(2,4))]
    special_characters = "!@#$%^&*()-_=+[]{}|;:,.<>/?"
    password += [random.choice(special_characters) for _ in range(random.randint(2,4))]
    password += [random.choice(string.ascii_lowercase) for _ in range(random.randint(8,10))]
    random.shuffle(password)
    password_str = ''.join(password)
    pyperclip.copy(password_str)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password_str)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password(website, username, password):
    if website == "" or username == "" or password == "":
        messagebox.showerror("Oops", "Please enter all fields.")
        return False
    
    new_data_dict = {
        website : {
            "username" : username,
            "password" : password
        }
    }
    
    try:
        with open('Day 029/data.json', 'r') as datafile:
            data = json.load(datafile)
            
    except FileNotFoundError:
        with open('Day 029/data.json', 'w') as datafile:
            json.dump(new_data_dict, datafile, indent=4)
    else:
        if data[website] is not None:
            response = messagebox.askyesno("Update Password", f"A password already exists for {website}. Do you want to update it?")
            if response:
                data.update(new_data_dict)   
                with open('Day 029/data.json', 'w') as datafile:
                    json.dump(data, datafile, indent=4)
            else:
                messagebox.showinfo("Information", "Existing password wasn't updated")
            
    return True
# ---------------------------- UI SETUP ------------------------------- #

root = tk.Tk()
root.title("Password Manager")
root.config(padx=20, pady=20)

# Create a style
style = ttk.Style()
style.configure('TLabel', padding=(0, 5))  # Add some vertical padding to labels

# Image canvas
canvas = tk.Canvas(width=200, height=200)
lock_image = tk.PhotoImage(file="Day 029/logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=0, columnspan=3, pady=(0, 20))

# Website
website_label = ttk.Label(text="Website:")
website_label.grid(row=1, column=0, sticky="e")
website_entry = ttk.Entry(width=21)
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew")
website_search = ttk.Button(text="Search", command=search_website)
website_search.grid(row=1, column=2, sticky="ew")
website_entry.focus()

# Username
username_label = ttk.Label(text="Email/Username:")
username_label.grid(row=2, column=0, sticky="e")
username_entry = ttk.Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2, sticky="ew")

# Password
password_label = ttk.Label(text="Password:")
password_label.grid(row=3, column=0, sticky="e")
password_entry = ttk.Entry(width=21)
password_entry.grid(row=3, column=1, sticky="ew")
generate_password_button = ttk.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="ew")

# Add Password button
def add_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    if(save_password(website, username, password)):
        website_entry.delete(0, tk.END)
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

add_password_button = ttk.Button(text="Add", command=add_password)
add_password_button.grid(row=4, column=1, columnspan=2, sticky="ew", pady=(10, 0))

# Configure grid columns
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

root.mainloop()