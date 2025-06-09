import tkinter as tk
from auth import LoginWindow


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()
