import cv2
import numpy as np
import os

# Load image from path
def load_image(image_path):
    return cv2.imread(image_path)

# Calculate image brightness (used for detecting transparency)
def get_brightness(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return np.mean(gray)

# Check if the image is colorful (based on saturation)
def is_colorful(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    saturation = hsv[:, :, 1]
    high_sat_pixels = np.sum(saturation > 80)
    total_pixels = saturation.size
    return (high_sat_pixels / total_pixels) > 0.2

# Assign to correct belt
def assign_belt(image):
    
    brightness = get_brightness(image)
    if brightness > 180:
        return "Conveyor B (Transparent)"
    elif is_colorful(image):
        return "Conveyor C (Colorful)"
    else:
        return "Conveyor A (Black)"

# Run classification on a folder of images
def classify_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.jpg', '.png', '.jpeg')):
            path = os.path.join(folder_path, filename)
            image = load_image(path)
            if image is not None:
                result = assign_belt(image)
                print(f"{filename} → {result}")
            else:
                print(f"Failed to load {filename}")

# RUN TEST HERE
if __name__ == "__main__":
    print("Classifying Black Images:")
    classify_folder("dataset/black")
    
    print("\nClassifying Transparent Images:")
    classify_folder("dataset/transparent")

    print("\nClassifying Colorful Images:")
    classify_folder("dataset/colorful")
