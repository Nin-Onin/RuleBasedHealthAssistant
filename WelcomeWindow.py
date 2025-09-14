import tkinter as tk
from PIL import Image, ImageTk
import os
from BaseWindow import BaseWindow
from MainWindow import MainWindow

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")

class WelcomeWindow(BaseWindow):
    def __init__(self, master=None):
        self.app_icon = ImageTk.PhotoImage(Image.open(os.path.join(ASSETS_DIR, "expertSystemLogo.png")))
        super().__init__(master, title="Welcome", size="720x500", icon=self.app_icon)

    def build_ui(self):
        big_logo_img = Image.open(os.path.join(ASSETS_DIR, "expertSystemLogo.png")).resize((200, 200), Image.Resampling.LANCZOS)
        self.big_logo_photo = ImageTk.PhotoImage(big_logo_img)

        frame = tk.Frame(self, padx=20, pady=20)
        frame.pack(fill="both", expand=True)

        content = tk.Frame(frame)
        content.pack(pady=40)

        logo_label = tk.Label(content, image=self.big_logo_photo)
        logo_label.pack(side="left", padx=20)

        text_container = tk.Frame(content)
        text_container.pack(side="left", padx=20)

        tk.Label(text_container, text="Welcome!", font=("Arial", 18, "italic")).pack(anchor="center")
        tk.Label(text_container, text="Rule-Based Health Assistant", font=("Arial", 18, "bold")).pack(anchor="center")
        tk.Button(frame, text="Get Started", font=("Arial", 12, "bold"), bg="lightgray", width=15, command=self.start_main).pack(pady=50)

    def start_main(self):
        self.destroy()
        MainWindow(self.master, self.app_icon)
