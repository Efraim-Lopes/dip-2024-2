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
    # Your implementation 
    
    # 1. Mean Squared Error
    mse = np.mean((i1 - i2) ** 2)

    # 2. Peak Signal-to-Noise Ratio
    psnr = 10 * np.log10(1.0 / mse) if mse != 0 else float('inf')

    # 3. Simplified SSIM
    window_size = 3
    pad = window_size // 2
    padded_i1 = np.pad(i1, pad, mode='reflect')
    padded_i2 = np.pad(i2, pad, mode='reflect')
    ssim_total = 0
    count = 0

    c1 = 0.01 ** 2
    c2 = 0.03 ** 2

    for y in range(pad, i1.shape[0] + pad):
        for x in range(pad, i1.shape[1] + pad):
            win1 = padded_i1[y - pad:y + pad + 1, x - pad:x + pad + 1]
            win2 = padded_i2[y - pad:y + pad + 1, x - pad:x + pad + 1]

            mu1 = np.mean(win1)
            mu2 = np.mean(win2)
            sigma1 = np.var(win1)
            sigma2 = np.var(win2)
            sigma12 = np.mean((win1 - mu1) * (win2 - mu2))

            numerator = (2 * mu1 * mu2 + c1) * (2 * sigma12 + c2)
            denominator = (mu1**2 + mu2**2 + c1) * (sigma1 + sigma2 + c2)
            ssim_total += numerator / denominator
            count += 1

    ssim = ssim_total / count

    # 4. Normalized Pearson Correlation Coefficient
    i1_flat = i1.flatten()
    i2_flat = i2.flatten()
    i1_mean = i1_flat - np.mean(i1_flat)
    i2_mean = i2_flat - np.mean(i2_flat)

    denom = np.linalg.norm(i1_mean) * np.linalg.norm(i2_mean)
    npcc = np.dot(i1_mean, i2_mean) / denom if denom != 0 else 0

    return {
        "mse": mse,
        "psnr": psnr,
        "ssim": ssim,
        "npcc": npcc
    }

    pass


if __name__ == "__main__":
    np.random.seed(42)  # pra garantir reprodutibilidade

    # Criar imagem base com valores entre 0 e 1
    img1 = np.random.rand(100, 100)

    # Criar imagem parecida, com pequeno ruído
    noise = np.random.normal(loc=0.0, scale=0.01, size=(100, 100))  # ruído pequeno
    img2 = np.clip(img1 + noise, 0, 1)  # somar ruído e manter entre 0 e 1
    
    # Chamar a função
    result = compare_images(img1, img2)

    # Exibir os resultados
    for key, value in result.items():
        print(f"{key}: {value}")
