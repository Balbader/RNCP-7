from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    This function takes a path to an image file as input and returns
    a NumPy array containing the pixel content of the image.
    The function first opens the image file and checks if the image
    is in JPG or JPEG format. If not, it raises a ValueError.
    The function then converts the image to RGB format if it is not already.
    The function then converts the image into a NumPy array and returns it.
    """
    try:
        # Open the image file
        with Image.open(path) as img:
            # Check if the image is in JPG or JPEG format
            if img.format not in ['JPEG', 'JPG']:
                raise ValueError("Only JPG and JPEG formats are supported.")

            # Print the image format
            print(f"Image format: {img.format}")

            # Convert the image to RGB format if not already
            if img.mode != 'RGB':
                img = img.convert('RGB')

            # Convert the image into a NumPy array (to get pixel content)
            pixels = np.array(img)

            # Print the pixel content (in RGB)
            print(f"Pixel content (RGB) at [0,0]:\
                {pixels[0, 0]}")  # Example pixel at (0,0)

            return pixels

    except FileNotFoundError:
        print("\033[31mError: The file was not found.\033[0m")
    except ValueError as ve:
        print(f"\033[31mError: {ve}\033[0m")
    except Exception as e:
        print(f"\033[31mAn unexpected error occurred: {e}\033[0m")


def main():
    ft_load("landscape.jpg")


if __name__ == "__main__":
    main()
