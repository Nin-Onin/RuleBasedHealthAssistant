import tkinter as tk
from abc import ABC, abstractmethod
from PIL import Image, ImageTk

class BaseWindow(tk.Toplevel, ABC):
    def __init__(self, master=None, title="Window", size="720x500", icon=None):
        super().__init__(master)
        self.title(title)
        self.geometry(size)
        self.resizable(False, False)
        self.center_window(size)
        if icon:
            self.iconphoto(False, icon)
        self.build_ui()

    def center_window(self, size):
        width, height = map(int, size.split("x"))
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    @abstractmethod
    def build_ui(self):
        pass
