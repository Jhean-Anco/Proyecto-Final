import tkinter as tk
from src.gui.login_window import LoginWindow

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()
