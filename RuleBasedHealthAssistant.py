import tkinter as tk
from WelcomeWindow import WelcomeWindow

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw() 
    WelcomeWindow(root)
    root.mainloop()
