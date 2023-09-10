import tkinter as tk
from tkinter import ttk
import random
import string

# Function to generate a random password
def generate_password(length):
    # Define character sets for each category
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Ensure the password length is at least 8 characters
    if length < 8:
        return "Password length should be at least 8 characters."

    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

# Function to generate a password and display it in the GUI
def generate_password_gui():
    length = int(length_var.get())
    password = generate_password(length)
    result_label.config(text=f"Generated Password: {password}")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create a label and entry for password length
length_label = ttk.Label(root, text="Password Length:")
length_label.pack()

length_var = tk.StringVar()
length_entry = ttk.Entry(root, textvariable=length_var)
length_entry.pack()

# Create a button to generate a password
generate_button = ttk.Button(root, text="Generate Password", command=generate_password_gui)
generate_button.pack()

# Create a label to display the generated password
result_label = ttk.Label(root, text="")
result_label.pack()

# Start the GUI main loop
root.mainloop()
