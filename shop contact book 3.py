import tkinter as tk
from tkinter import simpledialog, messagebox

Contacts = {}

def creating():
    store_name = simpledialog.askstring("Store Name", "Enter your store name:")

    phone_number = simpledialog.askstring("Phone Number", "Enter your phone number:")

    email = simpledialog.askstring("Email", "Enter your email ID:")
    address = simpledialog.askstring("Address", "Enter your address:")
    
    Contacts[store_name] = {
        "phone number": phone_number,
        "email": email,
        "address": address
    }
    messagebox.showinfo("Saved", f"{store_name}'s details saved.")

def view():
    name = simpledialog.askstring("View Shop", "Enter the store name you want to view:")
    if name in Contacts:
        details = Contacts[name]
        info = f"{name}'s details:\n"
        for key, value in details.items():
            info += f"{key}: {value}\n"
        messagebox.showinfo("Shop Details", info)
    else:
        messagebox.showerror("Error", "Store details not present")

def edit():
    name = simpledialog.askstring("Edit Shop", "Enter the store name you want to edit:")
    if name in Contacts:
        field = simpledialog.askstring("Field", "Enter field to update (phone number/email/address):")
        if field in Contacts[name]:
            new_value = simpledialog.askstring("New Value", f"Enter new value for {field}:")
            Contacts[name][field] = new_value
            messagebox.showinfo("Updated", f"{field} updated for {name}.")
        else:
            messagebox.showerror("Error", "Invalid field.")
    else:
        messagebox.showerror("Error", "Store not found.")

def delete():
    name = simpledialog.askstring("Delete Shop", "Enter the shop name you want to delete:")
    if name in Contacts:
        Contacts.pop(name)
        messagebox.showinfo("Deleted", f"{name} has been deleted.")
    else:
        messagebox.showerror("Error", "Shop not found.")

def show_all():
    if not Contacts:
        messagebox.showinfo("All Shops", "No data is present.")
    else:
        msg = ""
        for name, detail in Contacts.items():
            msg += f"{name}:\n"
            for key, value in detail.items():
                msg += f"  {key}: {value}\n"
            msg += "\n"
        messagebox.showinfo("All Shop Details", msg)

def exit_app():
    root.destroy()


root = tk.Tk()
root.title("Shop Contact Manager")

tk.Label(root, text="Shop Contact Manager", font=("Arial", 14)).pack(pady=10)
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add Shop", width=15, command=creating).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="View Shop", width=15, command=view).grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Edit Shop", width=15, command=edit).grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Delete Shop", width=15, command=delete).grid(row=1, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Show All", width=15, command=show_all).grid(row=2, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Exit", width=15, command=exit_app).grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
