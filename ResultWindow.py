import tkinter as tk
from BaseWindow import BaseWindow
from HealthExpertSystem import HealthExpertSystem

class ResultWindow(BaseWindow):
    def __init__(self, master, app_icon, logo_photo, name, temp, breathing, headache, cough, sore, allergy):
        self.app_icon = app_icon
        self.logo_photo = logo_photo
        self.name = name
        self.temp = temp
        self.breathing = breathing
        self.headache = headache
        self.cough = cough
        self.sore = sore
        self.allergy = allergy
        super().__init__(master, title="Diagnosis & Treatment Result", size="720x500", icon=self.app_icon)

    def build_ui(self):
        header = tk.Frame(self)
        header.pack(pady=10)
        tk.Label(header, image=self.logo_photo).pack(side="left", padx=10)
        tk.Label(header, text="Diagnosis & Treatment Result", font=("Arial", 16, "bold")).pack(side="left")

        content = tk.Frame(self, bg="lightgray", padx=20, pady=20)
        content.pack(fill="both", expand=True, padx=30, pady=10)

        labels = ["Patient Name:", "Diagnosis:", "Condition:", "Treatment:"]
        system = HealthExpertSystem(self.temp, self.breathing, self.headache, self.cough, self.sore, self.allergy)
        values = [self.name, system.get_diagnosis(), system.get_condition(), system.get_treatment()]

        for i in range(len(labels)):
            tk.Label(content, text=labels[i], font=("Arial", 14, "bold"), bg="lightgray").grid(row=i, column=0, sticky="w", padx=5, pady=5)
            fg_color = "red" if system.is_abnormal(labels[i], values[i]) else "black"
            tk.Label(content, text=values[i], font=("Arial", 14), bg="lightgray", fg=fg_color).grid(row=i, column=1, sticky="w", padx=10, pady=5)

        quote = "Stay positive, stay strong, and your body will heal faster."
        tk.Label(content, text=f"💡 {quote}", font=("Arial", 11, "italic"), fg="black", bg="lightgray", wraplength=400, justify="right").grid(row=len(labels), column=1, sticky="e", pady=(130, 0))
        tk.Button(self, text="OK", font=("Arial", 12, "bold"), width=12, bg="lightgray", command=self.destroy).pack(pady=10)
