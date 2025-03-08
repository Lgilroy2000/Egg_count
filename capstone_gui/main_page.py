import tkinter as tk
from train_page import open_train_page
from run_page import open_run_page

class MainPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Mode Selector")
        self.root.state('zoomed')

        # Create welcome label
        welcome_label = tk.Label(self.root, text="Welcome!\nSelect a Mode", font=("Arial", 48))
        welcome_label.pack(pady=50)

        # Create frame for buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(expand=True)

        # Create buttons
        train_button = tk.Button(button_frame, text="Train Mode", command=self.open_train_mode, width=20, height=2, font=("Arial", 48))
        run_button = tk.Button(button_frame, text="Run Mode", command=self.open_run_mode, width=20, height=2, font=("Arial", 48))

        # Place buttons in the center
        train_button.pack(pady=20)
        run_button.pack(pady=20)

    def open_train_mode(self):
        self.root.destroy()  # Close main window
        open_train_page()  # Open train page

    def open_run_mode(self):
        self.root.destroy()  # Close main window
        open_run_page()  # Open run page

def start_main_page():
    root = tk.Tk()
    app = MainPage(root)
    root.mainloop()

start_main_page()
