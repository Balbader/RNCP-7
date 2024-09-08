import numpy as np
import os


def ft_load(path: str) -> np.array:
    """
    Load an image from a File
    :param path: str: Path to the File
    :return: np.array: Image as a numpy array
    """
    try:
        if not os.path.exists(path):
            raise FileNotFoundError("File not found")
        image = np.load(path)
        print(f"The shape of the image is: {image.shape}")
        return image
    except FileNotFoundError:
        print(f"File {path} not found")
        return None
