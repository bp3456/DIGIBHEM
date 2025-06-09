from utils import load_users, save_users
from account import AccountWindow
import tkinter as tk
from tkinter import messagebox
import json
import os

USERS_FILE = "users.json"


def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)


class LoginWindow:
    def __init__(self, master):
        self.master = master
        master.title("Login System")

        
        master.attributes("-fullscreen", True)
        master.bind("<Escape>", lambda e: master.attributes("-fullscreen", False))

        font_style = ("Arial", 20)

        tk.Label(master, text="Username", font=font_style).pack(pady=20)
        self.username_entry = tk.Entry(master, font=font_style)
        self.username_entry.pack()

        tk.Label(master, text="Password", font=font_style).pack(pady=20)
        self.password_entry = tk.Entry(master, show="*", font=font_style)
        self.password_entry.pack()

        tk.Button(master, text='Login', command=self.login, font=font_style, width=12).pack(pady=20)
        tk.Button(master, text='Register', command=self.register, font=font_style, width=12).pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        users = load_users()
        if username in users and users[username]['password'] == password:
            messagebox.showinfo("Success", "Login successful!")
            self.master.destroy()
            AccountWindow(username)
        else:
            messagebox.showerror("Error", "Invalid credentials!")

    def register(self):
        RegisterWindow(self.master)


class RegisterWindow:
    def __init__(self, master):
        self.top = tk.Toplevel(master)
        self.top.title("Register")
        self.top.geometry("500x700")

        font_style = ("Arial", 16)

        tk.Label(self.top, text="Name", font=font_style).pack(pady=10)
        self.name_entry = tk.Entry(self.top, font=font_style)
        self.name_entry.pack()

        tk.Label(self.top, text="Email", font=font_style).pack(pady=10)
        self.email_entry = tk.Entry(self.top, font=font_style)
        self.email_entry.pack()

        tk.Label(self.top, text="Username", font=font_style).pack(pady=10)
        self.username_entry = tk.Entry(self.top, font=font_style)
        self.username_entry.pack()

        tk.Label(self.top, text="Password", font=font_style).pack(pady=10)
        self.password_entry = tk.Entry(self.top, show="*", font=font_style)
        self.password_entry.pack()

        tk.Label(self.top, text="Mobile Number", font=font_style).pack(pady=10)
        self.mobile_entry = tk.Entry(self.top, font=font_style)
        self.mobile_entry.pack()

        tk.Label(self.top, text="Minimum Balance (₹500)", font=font_style).pack(pady=10)
        self.balance_entry = tk.Entry(self.top, font=font_style)
        self.balance_entry.pack()

        tk.Button(self.top, text="Register", command=self.register_user, font=font_style).pack(pady=20)

    def register_user(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        mobile = self.mobile_entry.get()
        balance = self.balance_entry.get()

        if not (name and email and username and password and mobile and balance):
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            balance = float(balance)
            if balance < 100:
                messagebox.showerror("Error", "Minimum balance must be at least ₹100")
                return
        except ValueError:
            messagebox.showerror("Error", "Balance must be a number")
            return

        users = load_users()
        if username in users:
            messagebox.showerror("Error", "User already exists!")
        else:
            users[username] = {
                "name": name,
                "email": email,
                "password": password,
                "mobile": mobile,
                "balance": balance
            }
            save_users(users)
            messagebox.showinfo("Success", "Registered successfully!")
            self.top.destroy()
