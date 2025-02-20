import json
import tkinter as tk
from tkinter import messagebox, simpledialog

# File to store contacts
CONTACTS_FILE = "contacts.json"

# Load contacts from JSON file
def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save contacts to JSON file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact():
    name = simpledialog.askstring("Input", "Enter name:")
    if not name:
        return
    phone = simpledialog.askstring("Input", "Enter phone number:")
    email = simpledialog.askstring("Input", "Enter email:")
    address = simpledialog.askstring("Input", "Enter address:")

    contacts = load_contacts()
    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    save_contacts(contacts)
    
    messagebox.showinfo("Success", f"Contact '{name}' added successfully!")
    view_contacts()

# View all contacts
def view_contacts():
    contacts = load_contacts()
    contact_list.delete(0, tk.END)  # Clear the listbox
    
    if not contacts:
        contact_list.insert(tk.END, "No contacts found.")
    else:
        for name, details in contacts.items():
            contact_list.insert(tk.END, f"{name} - {details['Phone']}")

# Search a contact
def search_contact():
    query = simpledialog.askstring("Search", "Enter name or phone number:")
    contacts = load_contacts()
    
    for name, details in contacts.items():
        if query in name or query in details["Phone"]:
            messagebox.showinfo("Contact Found", f"Name: {name}\nPhone: {details['Phone']}\nEmail: {details['Email']}\nAddress: {details['Address']}")
            return
    messagebox.showwarning("Not Found", "No matching contact found.")

# Update a contact
def update_contact():
    name = simpledialog.askstring("Update", "Enter the name of the contact to update:")
    contacts = load_contacts()

    if name in contacts:
        phone = simpledialog.askstring("Input", f"New phone ({contacts[name]['Phone']}):", initialvalue=contacts[name]['Phone'])
        email = simpledialog.askstring("Input", f"New email ({contacts[name]['Email']}):", initialvalue=contacts[name]['Email'])
        address = simpledialog.askstring("Input", f"New address ({contacts[name]['Address']}):", initialvalue=contacts[name]['Address'])

        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        save_contacts(contacts)
        messagebox.showinfo("Success", f"Contact '{name}' updated successfully!")
        view_contacts()
    else:
        messagebox.showerror("Error", "Contact not found!")

# Delete a contact
def delete_contact():
    name = simpledialog.askstring("Delete", "Enter the name of the contact to delete:")
    contacts = load_contacts()

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        messagebox.showinfo("Deleted", f"Contact '{name}' deleted successfully!")
        view_contacts()
    else:
        messagebox.showerror("Error", "Contact not found!")


root = tk.Tk()
root.title("Contact Book by Varsha")
root.geometry("400x400")
root.config(bg='#cdc0ee')

# Buttons
btn_add = tk.Button(root, text="Add Contact", command=add_contact, bg="#e6dff6")
btn_view = tk.Button(root, text="View Contacts", command=view_contacts, bg="#e6dff6")
btn_search = tk.Button(root, text="Search Contact", command=search_contact, bg="#e6dff6")
btn_update = tk.Button(root, text="Update Contact", command=update_contact, bg="#e6dff6")
btn_delete = tk.Button(root, text="Delete Contact", command=delete_contact, bg="#e6dff6")
btn_exit = tk.Button(root, text="Exit", command=root.quit, bg="#e6dff6")


contact_list = tk.Listbox(root, width=50, height=15, bg = "#e7e2ff")
contact_list.pack(pady=10)

# Button Layout
btn_add.pack(pady=5)
btn_view.pack(pady=5)
btn_search.pack(pady=5)
btn_update.pack(pady=5)
btn_delete.pack(pady=5)
btn_exit.pack(pady=5)


view_contacts()

root.mainloop()
