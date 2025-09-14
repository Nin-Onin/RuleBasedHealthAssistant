import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
from BaseWindow import BaseWindow
from ResultWindow import ResultWindow
from InvalidInputPopup import InvalidInputPopup

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")

class MainWindow(BaseWindow):
    def __init__(self, master=None, app_icon=None):
        self.app_icon = app_icon
        logo_img = Image.open(os.path.join(ASSETS_DIR, "expertSystemLogo.png")).resize((50, 50), Image.Resampling.LANCZOS)
        self.logo_photo = ImageTk.PhotoImage(logo_img)
        super().__init__(master, title="Rule-Based Health Assistant", size="720x500", icon=self.app_icon)

    def build_ui(self):
        header = tk.Frame(self)
        header.pack(pady=10)
        tk.Label(header, image=self.logo_photo).pack(side="left", padx=10)
        tk.Label(header, text="Rule-Based Health Assistant", font=("Arial", 16, "bold")).pack(side="left")

        # Patient
        name_frame = tk.Frame(self, bg="lightgray", padx=10, pady=10)
        name_frame.pack(pady=5, anchor="w", padx=30, fill="x")
        tk.Label(name_frame, text="Patient's Name:", bg="lightgray", font=("Arial", 12, "bold")).pack(side="left", padx=5)
        self.name_entry = tk.Entry(name_frame, width=30, font=("Arial", 12))
        self.name_entry.pack(side="left", padx=5)

        temp_breathing = tk.Frame(self, padx=10, pady=10)
        temp_breathing.pack(pady=5, fill="x", padx=20)

        # Temperature
        temp_frame = tk.Frame(temp_breathing, bg="lightgray", padx=10, pady=10)
        temp_frame.pack(side="left", anchor="w")
        tk.Label(temp_frame, text="Enter Temperature (°C):", bg="lightgray", font=("Arial", 12, "bold")).pack(side="left", padx=5)
        self.temp_entry = tk.Entry(temp_frame, width=10, font=("Arial", 12))
        self.temp_entry.pack(side="left", padx=5)

        # Breathing
        breathing_frame = tk.Frame(temp_breathing, bg="lightgray", padx=10, pady=10)
        breathing_frame.pack(side="right", anchor="e")
        tk.Label(breathing_frame, text="Type of Breathing:", bg="lightgray", font=("Arial", 12, "bold")).pack(side="left", padx=5)
        self.breathing_var = tk.StringVar()
        breathing_dropdown = ttk.Combobox(breathing_frame, textvariable=self.breathing_var, state="readonly", values=["None", "Light", "Heavy"], width=15, justify="center")
        breathing_dropdown.set("Select Below")
        breathing_dropdown.pack(side="left", padx=5)

        container = tk.Frame(self)
        container.pack(pady=5, fill="x", padx=30)

        # Symptoms
        symptom_frame = tk.Frame(container, bg="lightgray", padx=10, pady=10)
        symptom_frame.pack(side="left", fill="both", expand=True)
        tk.Label(symptom_frame, text=" Patient's Symptoms:", bg="lightgray", font=("Arial", 12, "bold")).pack(anchor="w")
        self.headache_var = tk.BooleanVar()
        self.cough_var = tk.BooleanVar()
        self.sore_throat_var = tk.BooleanVar()
        checkbox_font = ("Arial", 11, "bold")
        tk.Checkbutton(symptom_frame, text="Headache", variable=self.headache_var, bg="lightgray", font=checkbox_font).pack(anchor="w", padx=40, pady=3)
        tk.Checkbutton(symptom_frame, text="Cough", variable=self.cough_var, bg="lightgray", font=checkbox_font).pack(anchor="w", padx=40, pady=3)
        tk.Checkbutton(symptom_frame, text="Sore Throat", variable=self.sore_throat_var, bg="lightgray", font=checkbox_font).pack(anchor="w", padx=40, pady=3)

        # Allergy
        allergy_frame = tk.Frame(container, bg="lightgray", padx=10, pady=10)
        allergy_frame.pack(side="left", fill="both", expand=True, padx=(39, 0))
        tk.Label(allergy_frame, text=" Allergy to Antibiotics:", bg="lightgray", font=("Arial", 12, "bold")).pack(anchor="w")
        self.allergy_var = tk.StringVar(value="None")
        tk.Radiobutton(allergy_frame, text="Yes", variable=self.allergy_var, value="Yes", bg="lightgray", font=checkbox_font).pack(anchor="w", pady=3, padx=50)
        tk.Radiobutton(allergy_frame, text="No", variable=self.allergy_var, value="No", bg="lightgray", font=checkbox_font).pack(anchor="w", pady=3, padx=50)

        tk.Button(self, text="Evaluate", command=self.evaluate, bg="lightgray", font=("Arial", 12, "bold"), width=15).pack(pady=20)

    def evaluate(self):
        try:
            name = self.name_entry.get()
            temp = float(self.temp_entry.get())
            breathing = self.breathing_var.get().lower() if self.breathing_var.get() else "none"
            headache = self.headache_var.get()
            cough = self.cough_var.get()
            sore = self.sore_throat_var.get()
            allergy = (self.allergy_var.get() == "Yes")
        except ValueError:
            self.temp_entry.delete(0, tk.END)
            InvalidInputPopup(self.master, self.app_icon)
            return

        ResultWindow(self.master, self.app_icon, self.logo_photo, name, temp, breathing, headache, cough, sore, allergy)
