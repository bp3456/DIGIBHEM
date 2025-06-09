import tkinter as tk
from tkinter import messagebox
import json
import os
from utils import load_users, save_users


class AccountWindow:
    def __init__(self, username):
        self.username = username
        self.users = load_users()
        self.user_data = self.users[username]
        self.balance = self.user_data.get("balance", 0)

        self.window = tk.Tk()
        self.window.title("Account Dashboard")
        
        self.window.attributes("-fullscreen", True)
        self.window.bind("<Escape>", lambda e: self.window.attributes("-fullscreen", False))

        font_style = ("Arial", 20)

        tk.Label(self.window, text=f"Logged in as: {username}", font=font_style).pack(pady=30)

        tk.Button(self.window, text="Check Balance", command=self.check_balance, font=font_style, width=20).pack(pady=30)
        tk.Button(self.window, text="Deposit", command=self.deposit, font=font_style, width=20).pack(pady=30)
        tk.Button(self.window, text="Withdraw", command=self.withdraw, font=font_style, width=20).pack(pady=30)
        tk.Button(self.window, text="Transaction History", command=self.show_history, font=font_style, width=20).pack(pady=30)
        tk.Button(self.window, text="Logout", command=self.logout, font=font_style, width=20, fg="red").pack(pady=30)

        self.window.mainloop()

    def check_balance(self):
        users = load_users()
        balance = users[self.username]["balance"]
        balance_window = tk.Toplevel(self.window)
        balance_window.title("Check Balance")
        balance_window.geometry("600x400")

        tk.Label(balance_window, text="Your Current Balance", font=("Arial", 24)).pack(pady=40)
        tk.Label(balance_window, text=f"₹{balance}", font=("Arial", 36, "bold"), fg="green").pack(pady=20)

    def deposit(self):
        self.transaction_window("Deposit")

    def withdraw(self):
        self.transaction_window("Withdraw")

    def transaction_window(self, type_):
        def perform():
            amount = entry.get()
            if not amount.isdigit():
                messagebox.showerror("Error", "Invalid amount")
                return

            amount = int(amount)
            users = load_users()

            if type_ == "Withdraw" and users[self.username]["balance"] < amount:
                messagebox.showerror("Error", "Insufficient funds")
                return

            if type_ == "Deposit":
                users[self.username]["balance"] += amount
            else:
                users[self.username]["balance"] -= amount

            save_users(users)
            self.save_transaction(type_, amount)
            messagebox.showinfo("Success", f"{type_} of ₹{amount} successful")
            win.destroy()

        win = tk.Toplevel(self.window)
        win.title(type_)
        win.geometry("800x600")

        tk.Label(win, text=f"{type_} Amount", font=("Arial", 24)).pack(pady=30)

        entry = tk.Entry(win, font=("Arial", 24), width=20)
        entry.pack(pady=20)

        tk.Button(win, text=type_, command=perform, font=("Arial", 20), width=15).pack(pady=30)

    def save_transaction(self, type_, amount):
        folder = "transactions"
        os.makedirs(folder, exist_ok=True)
        path = os.path.join(folder, f"{self.username}_transactions.json")

        data = []
        if os.path.exists(path):
            with open(path, "r") as f:
                data = json.load(f)

        data.append({
            "type": type_,
            "amount": amount
        })

        with open(path, "w") as f:
            json.dump(data, f, indent=4)

    def show_history(self):
        path = f"transactions/{self.username}_transactions.json"
        if not os.path.exists(path):
            messagebox.showinfo("History", "No transactions found.")
            return

        with open(path, "r") as f:
            data = json.load(f)

        history_window = tk.Toplevel(self.window)
        history_window.title("Transaction History")
        history_window.geometry("800x600")

        for txn in data:
            tk.Label(history_window, text=f"{txn['type']}: ₹{txn['amount']}", font=("Arial", 18)).pack(pady=5)

    def logout(self):
        confirm = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if confirm:
            self.window.destroy()
