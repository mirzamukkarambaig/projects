import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread("IMG_2687.png")

# Convert to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Show the original image
plt.subplot(2, 2, 3)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("RGB Image")

# Show the original grayscale image
plt.subplot(2, 2, 4)
plt.imshow(gray_img, cmap='gray')
plt.title("Original Image")

# Convert the grayscale image to float32
gray_img = gray_img.astype(np.float32) / 255.0

# Add Gaussian noise to the image
noisy_img = gray_img + np.random.normal(0, 0.1, gray_img.shape)

# Define the Gaussian kernel
sigma = 1
kernel_size = 3
kernel = np.fromfunction(
    lambda x, y: np.exp(-((x - 1)**2 + (y - 1)**2) / (2 * sigma**2)),
    (kernel_size, kernel_size)
)
kernel /= np.sum(kernel)

# Apply the Gaussian filter
output_img = cv2.filter2D(noisy_img, -1, kernel)

# Adjust the subplot layout
plt.subplots_adjust(hspace=0.5)  # Increase vertical spacing

# Display the images
plt.subplot(2, 2, 1)
plt.imshow(noisy_img, cmap='gray')
plt.title("Noisy Image")

plt.subplot(2, 2, 2)
plt.imshow(output_img, cmap='gray')
plt.title("Noise Reduced Image")

plt.show()
