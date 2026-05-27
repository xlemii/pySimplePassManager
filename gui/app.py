import tkinter as tk
from core.manager import PasswordManager


class App:
    def __init__(self, root):
        self.manager = PasswordManager()
        self.root = root
        self.root.title("Password Manager")

        # --- INPUTS ---
        tk.Label(root, text="Service").grid(row=0, column=0)
        self.service_entry = tk.Entry(root)
        self.service_entry.grid(row=0, column=1)

        tk.Label(root, text="Login").grid(row=1, column=0)
        self.login_entry = tk.Entry(root)
        self.login_entry.grid(row=1, column=1)

        tk.Label(root, text="Password").grid(row=2, column=0)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.grid(row=2, column=1)

        # --- BUTTONS ---
        tk.Button(root, text="Add", command=self.add_entry).grid(row=3, column=0, columnspan=2)
        tk.Button(root, text="Delete", command=self.delete_entry).grid(row=5, column=0, columnspan=2)

        # --- LIST ---
        self.listbox = tk.Listbox(root, width=40)
        self.listbox.grid(row=4, column=0, columnspan=2)

        self.refresh()

    def add_entry(self):
        self.manager.add_entry(
            self.service_entry.get(),
            self.login_entry.get(),
            self.password_entry.get()
        )
        self.refresh()

    def delete_entry(self):
        selected = self.listbox.curselection()

        if not selected:
            return

        index = selected[0]
        self.manager.delete_entry(index)
        self.refresh()

    def refresh(self):
        self.listbox.delete(0, tk.END)

        for entry in self.manager.get_entries():
            self.listbox.insert(
                tk.END,
                f"{entry.service} | {entry.login}"
            )