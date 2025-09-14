import tkinter as tk
from PIL import Image, ImageTk
import os
from BaseWindow import BaseWindow

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")

class InvalidInputPopup(BaseWindow):
    def __init__(self, master, app_icon):
        self.app_icon = app_icon
        super().__init__(master, title="Invalid Input", size="420x120", icon=self.app_icon)
        self.resizable(False, False)  

    def build_ui(self):
        container = tk.Frame(self, padx=10, pady=10)
        container.pack(fill="both", expand=True)
        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=1)

        x_icon = Image.open(os.path.join(ASSETS_DIR, "circularXbutton.png")).resize((30, 30), Image.Resampling.LANCZOS)
        self.x_icon_photo = ImageTk.PhotoImage(x_icon)

        tk.Label(container, image=self.x_icon_photo).grid(row=0, column=0, padx=10, pady=5, sticky="n")
        tk.Label(container, text="Please input numerical value for the temperature", font=("Arial", 10), fg="black", wraplength=280, justify="left").grid(row=0, column=1, sticky="w", padx=5)
        tk.Button(container, text="OK", font=("Arial", 10, "bold"), width=12, bg="lightgray", command=self.destroy).grid(row=1, column=0, columnspan=2, pady=10, sticky="n")
