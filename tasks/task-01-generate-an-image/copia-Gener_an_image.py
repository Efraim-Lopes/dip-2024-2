import argparse
import numpy as np
import cv2
import matplotlib.pyplot as plt

def generate_image(seed, width, height, mean, std):
    """
    Generates a grayscale image with pixel values sampled from a normal distribution.

    Args:
        seed (int): Random seed for reproducibility.
        width (int): Width of the generated image.
        height (int): Height of the generated image.
        mean (float): Mean of the normal distribution.
        std (float): Standard deviation of the normal distribution.

    Returns:
        image (numpy.ndarray): The generated grayscale image.
    """
    ### START CODE HERE ###
    np.random.seed(seed)  # Define the seed for reproducibility
    image = np.random.normal(loc=mean, scale=std, size=(height, width))  # Generate the pixel values

    # Clip the values to [0, 255] range and convert to uint8
    image = np.clip(image, 0, 255).astype(np.uint8)

    # Display histogram
    plt.figure(figsize=(8, 6))
    plt.hist(image.ravel(), bins=256, range=(0, 255), color='gray', alpha=0.7)
    plt.title("Histogram of Pixel Intensities")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")

    # Calculate mean and standard deviation of the image
    mean_val = np.mean(image)
    std_val = np.std(image)
    print(f"Mean pixel intensity: {mean_val:.2f}")
    print(f"Standard deviation of pixel intensity: {std_val:.2f}")

    plt.axvline(mean_val, color='red', linestyle='dashed', linewidth=2, label=f"Mean: {mean_val:.2f}")
    plt.axvline(mean_val + std_val, color='blue', linestyle='dashed', linewidth=2, label=f"Mean + 1SD: {mean_val + std_val:.2f}")
    plt.axvline(mean_val - std_val, color='blue', linestyle='dashed', linewidth=2, label=f"Mean - 1SD: {mean_val - std_val:.2f}")
    plt.legend()
    plt.show()
    ### END CODE HERE ###

    return image

def main():
    parser = argparse.ArgumentParser(description="Generate an image with pixel values sampled from a normal distribution.")
    parser.add_argument('--registration_number', type=int, required=True, help="Student's registration number (used as seed)")
    parser.add_argument('--width', type=int, required=True, help="Width of the image")
    parser.add_argument('--height', type=int, required=True, help="Height of the image")
    parser.add_argument('--mean', type=float, required=True, help="Mean of the normal distribution")
    parser.add_argument('--std', type=float, required=True, help="Standard deviation of the normal distribution")
    parser.add_argument('--output', type=str, required=True, help="Path to save the generated image")

    args = parser.parse_args()

    # Generate the image
    image = generate_image(args.registration_number, args.width, args.height, args.mean, args.std)

    # Save the generated image
    cv2.imwrite(args.output, image)
    print(f"Image successfully generated and saved to {args.output}")

if __name__ == "__main__":
    main()