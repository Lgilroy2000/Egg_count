import tkinter as tk

def open_train_page():
    # Close main page before opening new one
    root = tk.Tk()  # Create a new Tkinter root for this page
    root.title("Train Mode")
    root.state('zoomed')

    # Label
    label = tk.Label(root, text="Train Mode Activated", font=("Arial", 32))
    label.pack(pady=50)

    # Back button to return to main page
    back_button = tk.Button(root, text="Back to Main Page", command=lambda: go_back_to_main(root), font=("Arial", 20))
    back_button.pack(pady=20)

    root.mainloop()

def go_back_to_main(current_root):
    current_root.destroy()  # Close this window
    from main_page import start_main_page  # Import here to avoid circular import issues
    start_main_page()  # Reopen main page
