import tkinter as tk

from ui.frames.auth_frame import AuthFrame

from ui.frames.main_frame import MainFrame
from models.user import User


class EventManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Event Management App")
        self.root.geometry("800x600")

        self.auth_frame = AuthFrame(root=self)

        self.main_frame = MainFrame(root=self)

        self.user: User or None = None


