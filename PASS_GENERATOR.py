# GUI BASED PASSWORD GENERATOR

import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())

    # Define the character sets to generate password from
    character_sets = []
    if include_uppercase.get():
        character_sets.append(string.ascii_uppercase)
    if include_lowercase.get():
        character_sets.append(string.ascii_lowercase)
    if include_digits.get():
        character_sets.append(string.digits)
    if include_special_chars.get():
        character_sets.append(string.punctuation)

    if not character_sets:
        messagebox.showerror("Error", "Please select at least one character set.")
        return

    password = ""
    for _ in range(length):
        character_set = random.choice(character_sets)
        password += random.choice(character_set)

    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)

root = tk.Tk()
root.title("Password Generator")

# Set the window size
root.geometry("400x275")
root.resizable(False, False)  # Fix window size

# Checkbox variables
include_uppercase = tk.BooleanVar()
include_lowercase = tk.BooleanVar()
include_digits = tk.BooleanVar()
include_special_chars = tk.BooleanVar()

# Password length label and entry
length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=5)

length_entry = tk.Entry(root)
length_entry.pack()

# Character set checkboxes
uppercase_checkbox = tk.Checkbutton(root, text="Uppercase Letters", variable=include_uppercase)
uppercase_checkbox.pack()

lowercase_checkbox = tk.Checkbutton(root, text="Lowercase Letters", variable=include_lowercase)
lowercase_checkbox.pack()

digits_checkbox = tk.Checkbutton(root, text="Digits", variable=include_digits)
digits_checkbox.pack()

special_chars_checkbox = tk.Checkbutton(root, text="Special Characters", variable=include_special_chars)
special_chars_checkbox.pack()

# Generate password button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Generated password entry
password_entry = tk.Entry(root, width=30)
password_entry.pack()

root.mainloop()