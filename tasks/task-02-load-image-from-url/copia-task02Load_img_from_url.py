import argparse
import cv2 as cv
import numpy as np
import requests
from io import BytesIO

def load_image_from_url(url, **kwargs):
    """
    Loads an image from an Internet URL with optional arguments for OpenCV's cv.imdecode.
    
    Parameters:
    - url (str): URL of the image.
    - **kwargs: Additional keyword arguments for cv.imdecode (e.g., flags=cv.IMREAD_GRAYSCALE).
    
    Returns:
    - image: Loaded image as a NumPy array or None if loading fails.
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Verifica erros na requisição
        image_array = np.asarray(bytearray(response.content), dtype=np.uint8)
        image = cv.imdecode(image_array, kwargs.get("flags", cv.IMREAD_COLOR))
        return image
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Load an image from a URL.")
    parser.add_argument("url", type=str, help="URL of the image")
    args = parser.parse_args()

    image = load_image_from_url(args.url, flags=cv.IMREAD_COLOR)

    if image is not None:
        # Converter de BGR para RGB para exibição correta, mas nao foi preciso
        #image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
        
        cv.imshow("Loaded Image", image)

        # Exibir cada canal de cor separadamente
        cv.imshow("Red Channel", image[:, :, 2])  # Canal Vermelho
        cv.imshow("Green Channel", image[:, :, 1])  # Canal Verde
        cv.imshow("Blue Channel", image[:, :, 0])  # Canal Azul

        cv.waitKey(0)
        cv.destroyAllWindows()
    else:
        print("Failed to load image.")

if __name__ == "__main__":
    main()
