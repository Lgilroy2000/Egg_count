import os
from ultralytics import YOLO
import cv2

# Global variable to count eggs
eggcount = 0  

def counter(im_path):
    global eggcount  # Ensure global variable is used inside function

    # Path to the image
    image_path = im_path  # Replace with your image file path
    output_image_path = 'complete.jpg'  # Path for saving the output image

    # Load the image
    image = cv2.imread(image_path)

    # Ensure image is loaded correctly
    if image is None:
        print("Error: Unable to load image. Check the file path.")
        return

    # Load the YOLO model
    model_path = r'C:\Users\logan\OneDrive\Desktop\eggCountV2\runs\detect\train\weights\best.pt'  # Use raw string
    model = YOLO(model_path)

    # Threshold for detecting objects
    threshold = 0.05

    # Perform object detection
    results = model(image)[0]  # Run the model on the image

    # Iterate over detections and draw bounding boxes
    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            # Draw a rectangle around the detected object
            cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)

            # Put the class label above the bounding box
            """
            cv2.putText(image, results.names[int(class_id)].upper(), 
                        (int(x1), int(y1 - 10)), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)
            """
            # Increment egg count
            eggcount += 1

    # Save the output image
    cv2.imwrite(output_image_path, image)

    
    print("Eggs counted:", eggcount)
    

# Run the function

