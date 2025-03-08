import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from egg_count import counter

# Global variable for image display
image_label = None
im_path = None  # Initialize the global variable

def runcount():
    if im_path is not None:
        counter(im_path)  # Runs egg counting process with the image path
    display_processed_image()  # Show processed image in GUI

def open_image():
    global image_label, im_path  # Ensure that we use the global variables
    input_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
    if input_path:
        img = Image.open(input_path)
        
        # Fit the image within a 400x400 box while maintaining its aspect ratio
        img.thumbnail((400, 400))
        
        img = ImageTk.PhotoImage(img)
        image_label.config(image=img)
        image_label.image = img  # Prevent garbage collection
        im_path = input_path  # Correctly update the global im_path variable
        print(im_path)  # Debug: Print the selected image path

def display_processed_image():
    """Display the processed image after counting."""
    global image_label
    processed_image_path = "complete.jpg"  # The path to the processed image
    
    try:
        img = Image.open(processed_image_path)
        
        # Fit the image within a 400x400 box while maintaining its aspect ratio
        img.thumbnail((400, 400))
        
        img = ImageTk.PhotoImage(img)
        image_label.config(image=img)
        image_label.image = img  # Prevent garbage collection
    except Exception as e:
        print(f"Error loading processed image: {e}")

def open_run_page():
    global image_label

    root = tk.Tk()
    root.title("Run Mode")
    root.state('zoomed')

    # Create a frame for the canvas and scrollbar
    container = tk.Frame(root)
    container.pack(fill="both", expand=True)

    # Create a canvas with scrollbar
    canvas = tk.Canvas(container)
    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Create a scrollable frame inside the canvas
    scroll_frame = tk.Frame(canvas)
    canvas.create_window((root.winfo_screenwidth() // 2, 0), window=scroll_frame, anchor="n")  # Centered horizontally

    # Configure scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)

    def update_scroll_region(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    scroll_frame.bind("<Configure>", update_scroll_region)

    # Enable mouse wheel scrolling
    def on_mouse_wheel(event):
        canvas.yview_scroll(-1 * (event.delta // 120), "units")

    root.bind_all("<MouseWheel>", on_mouse_wheel)  

    # Wrapper frame to center everything
    wrapper_frame = tk.Frame(scroll_frame)
    wrapper_frame.pack(pady=50)  # Add padding for better spacing

    # Title Label
    label = tk.Label(wrapper_frame, text="Run Mode", font=("Arial", 32))
    label.pack(pady=20)

    # Buttons
    open_button = tk.Button(wrapper_frame, text="Open Image", command=open_image, font=("Arial", 20))
    open_button.pack(pady=20)

    count_button = tk.Button(wrapper_frame, text="Count Image", command=runcount, font=("Arial", 20))
    count_button.pack(pady=20)

    # Image Display
    global image_label
    image_label = tk.Label(wrapper_frame)
    image_label.pack(pady=20)

    # Back Button
    back_button = tk.Button(wrapper_frame, text="Back to Main Page", command=lambda: go_back_to_main(root), font=("Arial", 20))
    back_button.pack(pady=20)

    root.mainloop()

def go_back_to_main(current_root):
    current_root.destroy()
    from main_page import start_main_page  
    start_main_page()
