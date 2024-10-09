import random
import string
import tkinter as tk
from tkinter import messagebox


def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)  


def copy_to_clipboard():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Success", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Error", "No password to copy!")


root = tk.Tk()
root.title("Password Generator")


tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)


length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)


generate_btn = tk.Button(root, text="Generate Password", command=generate_password)
generate_btn.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


password_entry = tk.Entry(root, width=30)
password_entry.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()