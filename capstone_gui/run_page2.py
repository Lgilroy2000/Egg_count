import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from egg_count import counter
import os
import cv2

# Global variable for image display
image_label = None
im_path = None  # Initialize the global variable


def runcount():
    
      # Runs egg counting process with the image path
    display_image(counter("current.jpg"))  # Show processed image in GUI

def take_picture():
    print("taking pictue")
    #os.system("rpicam-still --output test.jpg")

    import cv2

    # Open the webcam (use 0 for the default camera)
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()

    # Capture a frame
    ret, frame = cap.read()

    # If frame is read correctly, ret is True
    if ret:
        # Save the frame as an image
        cv2.imwrite("current.jpg", frame)
        print("Image saved as webcam_image.jpg")
    else:
        print("Error: Could not read frame.")

#    Release the webcam
    cap.release()

    # Close any OpenCV windows
    cv2.destroyAllWindows()

    im_path="test.jpg"
    display_image("Current.jpg")

def display_image(image_path):
    """Display the processed image after counting."""
    global image_label

    
    try:
        img = Image.open(image_path)
        
        # Fit the image within a 400x400 box while maintaining its aspect ratio
        img.thumbnail((1000, 1000))
        
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
    img_button = tk.Button(wrapper_frame, text="Take Picture", command=take_picture, font=("Arial", 20))
    img_button.pack(pady=20)

    count_button = tk.Button(wrapper_frame, text="Count Image", command=runcount, font=("Arial", 20))
    count_button.pack(pady=20)

    # Image Display
    global image_label
    image_label = tk.Label(wrapper_frame)
    image_label.pack(pady=20)

    # Back Button
    #back_button = tk.Button(wrapper_frame, text="Back to Main Page", command=lambda: go_back_to_main(root), font=("Arial", 20))
    #back_button.pack(pady=20)

    root.mainloop()

def go_back_to_main(current_root):
    current_root.destroy()
    from main_page import start_main_page  
    start_main_page()
open_run_page()
