# image_geometry_exercise.py
# STUDENT'S EXERCISE FILE

"""
Exercise:
Implement a function `apply_geometric_transformations(img)` that receives a grayscale image
represented as a NumPy array (2D array) and returns a dictionary with the following transformations:

1. Translated image (shift right and down)
2. Rotated image (90 degrees clockwise)
3. Horizontally stretched image (scale width by 1.5)
4. Horizontally mirrored image (flip along vertical axis)
5. Barrel distorted image (simple distortion using a radial function)

You must use only NumPy to implement these transformations. Do NOT use OpenCV, PIL, skimage or similar libraries.

Function signature:
    def apply_geometric_transformations(img: np.ndarray) -> dict:

The return value should be like:
{
    "translated": np.ndarray,
    "rotated": np.ndarray,
    "stretched": np.ndarray,
    "mirrored": np.ndarray,
    "distorted": np.ndarray
}
"""

import numpy as np

def apply_geometric_transformations(img: np.ndarray) -> dict:
    # Your implementation here

    height, width = img.shape

    # 1. Translated Image (shift right and down)
    # Matriz de translação
    t_x, t_y = 20, 30  # Exemplo de deslocamento (20px à direita, 30px para baixo)
    translated = np.zeros_like(img)
    for y in range(height):
        for x in range(width):
            if 0 <= y + t_y < height and 0 <= x + t_x < width:
                translated[y + t_y, x + t_x] = img[y, x]
    ###########

    # 2. Rotated Image (90 degrees clockwise)
    # Matriz de rotação (90 graus no sentido horário)
    rotated = np.rot90(img, -1)
    ##########

    # 3. Horizontally Stretched Image (scale width by 1.5)
    # Matriz de escala
    scale_factor = 1.5
    new_width = int(width * scale_factor)
    stretched = np.zeros((height, new_width), dtype=img.dtype)
    for y in range(height):
        for x in range(new_width):
            orig_x = int(x / scale_factor)
            if orig_x < width:
                stretched[y, x] = img[y, orig_x]
    ############

    # 4. Horizontally Mirrored Image (flip along vertical axis)
    # Matriz de espelhamento
    mirrored = np.fliplr(img)
    ###########

    # 5. Barrel Distorted Image    
    center_y, center_x = height // 2, width // 2
    distorted = np.zeros_like(img)

    k = 0.1 # Definir o coeficiente de distorção

    for y in range(height):
        for x in range(width):
            norm_x = (x - center_x) / center_x
            norm_y = (y - center_y) / center_y
            r = np.sqrt(norm_x**2 + norm_y**2)
            factor = 1 + k * r**2  

            src_x = int(center_x + norm_x * factor * center_x)
            src_y = int(center_y + norm_y * factor * center_y)

            if 0 <= src_x < width and 0 <= src_y < height:
                distorted[y, x] = img[src_y, src_x]
    #############

    return {
        "translated": translated,
        "rotated": rotated,
        "stretched": stretched,
        "mirrored": mirrored,
        "distorted": distorted
    }
    pass