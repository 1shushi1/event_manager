import tkinter as tk
from tkinter import messagebox

from models.user import User
from services.implemented.auth_service import AuthService
from utils.auth import get_hashed_password


class AuthFrame(tk.Frame):
    def __init__(self, root):
        """
        Constructor for AuthFrame
        :param root:
        """
        super().__init__(master=root.root)
        self.root_window = root
        self.pack(pady=50)
        self.add_content()

    def add_content(self):
        """
        Adding field components
        :return:
        """
        self.username_label = tk.Label(self, text="Username:")
        self.username_label.grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        self.password_label = tk.Label(self, text="Password:")
        self.password_label.grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.grid(row=2, columnspan=2, pady=10)

        self.register_button = tk.Button(self, text="Register", command=self.register)
        self.register_button.grid(row=3, columnspan=2, pady=10)

    def login(self):
        """
        Login method
        :return:
        """
        username = self.username_entry.get()
        password = self.password_entry.get()

        user = AuthService().login(username, password)
        if user is not None:
            self.root_window.user = user
            self.pack_forget()  # Убираем окно авторизации
            self.root_window.main_frame.pack(fill=tk.BOTH, expand=True)  # Показываем основное окно
        else:
            messagebox.showerror("Error", "Please enter username and password.")

    def register(self):
        """
        Register Method
        :return:
        """
        username = self.username_entry.get()
        password = self.password_entry.get()

        user = AuthService().register(User(username=username, password=get_hashed_password(password)))
        if user is not None:
            self.root_window.user = user
            self.pack_forget()  # Убираем окно авторизации
            self.root_window.main_frame.pack(fill=tk.BOTH, expand=True)  # Показываем основное окно
        else:
            messagebox.showerror("Error", "Please enter username and password.")
