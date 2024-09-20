from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def zoom_image(image: np.ndarray, zoom_factor: int) -> np.ndarray:
    """
    Zoom in on an image by repeating pixels.
    Args:
        image (np.ndarray): The input image as a NumPy array.
        zoom_factor (int): The factor by which to zoom in.
    Returns:
        np.ndarray: The zoomed-in image as a NumPy array.
    """
    # Get the dimensions of the input image
    height, width, channels = image.shape

    # Calculate the new dimensions of the zoomed-in image
    new_height = height * zoom_factor
    new_width = width * zoom_factor

    # Create a new array to store the zoomed-in image
    zoomed_image = np.zeros((new_height, new_width, channels), dtype=image.dtype)

    # Fill the new array with repeated pixels from the original image
    for i in range(new_height):
        for j in range(new_width):
            original_i = i // zoom_factor
            original_j = j // zoom_factor
            zoomed_image[i, j] = image[original_i, original_j]

    return zoomed_image

if __name__ == "__main__":
    image = ft_load("animal.jpeg")
    print(image)
    zoomed_image = zoom_image(image, 3)
    print(zoomed_image.shape)
