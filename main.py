"""
Event management application
"""

from dotenv import load_dotenv
import tkinter as tk

from ui.root_window import EventManagementApp

load_dotenv()

if __name__ == "__main__":
    root = tk.Tk()
    app = EventManagementApp(root)
    root.mainloop()
