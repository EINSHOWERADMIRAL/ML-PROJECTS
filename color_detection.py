
import pandas as pd
import cv2
import numpy as np

# Load the color data from the CSV file
color_data_df = pd.read_csv('color_data.csv')

# Function to detect color by clicking on an image
def detect_color_on_click(image_path):
    image = cv2.imread(image_path)

    # Function to calculate distance and return the closest color name
    def get_closest_color(r, g, b):
        min_dist = float('inf')
        closest_color = None
        for i, row in color_data_df.iterrows():
            dist = np.sqrt((r - row['R'])**2 + (g - row['G'])**2 + (b - row['B'])**2)
            if dist < min_dist:
                min_dist = dist
                closest_color = row['color_name']
        return closest_color

    # Mouse callback function
    def mouse_callback(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            b, g, r = image[y, x]
            color_name = get_closest_color(r, g, b)
            print(f"Color at ({x}, {y}): {color_name}, RGB: ({r}, {g}, {b})")

    cv2.imshow('Image', image)
    cv2.setMouseCallback('Image', mouse_callback)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
if __name__ == "__main__":
    image_path = 'sample_image.jpg'  # Replace with your image file path
    detect_color_on_click(image_path)
