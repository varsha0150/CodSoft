import random
import string
import tkinter as tk
from tkinter import messagebox

# Generate a random password of the specified length
def generate_password():
   
    try:
        length = int(entry_length.get())  # Get user input for password length
        if length < 1:
            messagebox.showerror("Error", "Password length must be at least 1!")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        entry_password.delete(0, tk.END)  # Clear the previous password
        entry_password.insert(0, password)  # Display new password
    except ValueError:
        messagebox.showerror("Error","Please enter a valid number for password length!")

# Copy the generated password to clipboard
def copy_password():
    
    password = entry_password.get()
    if password:
        ws.clipboard_clear()
        ws.clipboard_append(password)
        ws.update()
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")

# Create GUI window
ws = tk.Tk()
ws.title("Password Generator by Varsha")
ws.geometry("400x250")
ws.configure(bg="#d6b3ff") 



# Password Length Input
label_length = tk.Label(ws, text="Enter password length:", font=("Arial", 12), bg="#d6b3ff")
label_length.pack()
entry_length = tk.Entry(ws, font=("Arial", 12),bg="#e6dff6")
entry_length.pack(pady=5)

# Generate Button
btn = tk.Button(ws, text="Generate Password", font=("Arial", 12, "bold"), bg="#ad97e3", fg="black", command=generate_password)
btn.pack(pady=10)

# Password Display Entry
entry_password = tk.Entry(ws, font=("Arial", 14), width=30, justify="center", bg = "#e6dff6")
entry_password.pack(pady=5)

# Copy Button
btn_copy = tk.Button(ws, text="Copy Password", font=("Arial", 12, "bold"), bg="#ad97e3", fg="black", command=copy_password)
btn_copy.pack(pady=5)


ws.mainloop()
