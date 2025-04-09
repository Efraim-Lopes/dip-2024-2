# image_similarity_exercise.py
# STUDENT'S EXERCISE FILE

"""
Exercise:
Implement a function `compare_images(i1, i2)` that receives two grayscale images
represented as NumPy arrays (2D arrays of shape (H, W)) and returns a dictionary with the following metrics:

1. Mean Squared Error (MSE)
2. Peak Signal-to-Noise Ratio (PSNR)
3. Structural Similarity Index (SSIM) - simplified version without using external libraries
4. Normalized Pearson Correlation Coefficient (NPCC)

You must implement these functions yourself using only NumPy (no OpenCV, skimage, etc).

Each function should be implemented as a helper function and called inside `compare_images(i1, i2)`.

Function signature:
    def compare_images(i1: np.ndarray, i2: np.ndarray) -> dict:

The return value should be like:
{
    "mse": float,
    "psnr": float,
    "ssim": float,
    "npcc": float
}

Assume that i1 and i2 are normalized grayscale images (values between 0 and 1).
"""

import numpy as np

def compare_images(i1: np.ndarray, i2: np.ndarray) -> dict:
    # Your implementation here

    # 1. Mean Squared Error (MSE)
    mse = np.mean((i1 - i2) ** 2)

    # 2. Peak Signal-to-Noise Ratio (PSNR)
    if mse == 0:
        psnr = float('inf')
    else:
        psnr = 10 * np.log10(1.0 / mse)  # máximo valor possível é 1 (imagem normalizada)

    # 3. Structural Similarity Index (SSIM) - simplificada
    mu_x = np.mean(i1)
    mu_y = np.mean(i2)
    sigma_x = np.var(i1)
    sigma_y = np.var(i2)
    sigma_xy = np.mean((i1 - mu_x) * (i2 - mu_y))

    C1 = 0.01 ** 2
    C2 = 0.03 ** 2

    ssim = ((2 * mu_x * mu_y + C1) * (2 * sigma_xy + C2)) / \
           ((mu_x ** 2 + mu_y ** 2 + C1) * (sigma_x + sigma_y + C2))

    # 4. Normalized Pearson Correlation Coefficient (NPCC)
    numerator = np.sum((i1 - mu_x) * (i2 - mu_y))
    denominator = np.sqrt(np.sum((i1 - mu_x) ** 2)) * np.sqrt(np.sum((i2 - mu_y) ** 2))
    npcc = numerator / denominator if denominator != 0 else 0

    return {
        "mse": mse,
        "psnr": psnr,
        "ssim": ssim,
        "npcc": npcc
    }
    
    pass


if __name__ == "__main__":
    # Criar duas imagens de teste (5x5) com valores normalizados entre 0 e 1
    img1 = np.ones((5, 5)) * 0.5  # imagem com todos os pixels = 0.5
    img2 = np.ones((5, 5)) * 0.5  # igual à anterior → todas as métricas devem dar perfeito

    # Modificar levemente img2 para testar diferenças
    img2[0, 0] = 0.6
    img2[4, 4] = 0.4

    # Chamar a função
    result = compare_images(img1, img2)

    # Exibir os resultados
    for key, value in result.items():
        print(f"{key}: {value}")