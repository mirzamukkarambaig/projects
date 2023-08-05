# Image Noise Reduction using Gaussian Filter

This MATLAB script demonstrates an implementation of a Gaussian filter for noise reduction in images. It performs the following operations:

1. Load an image.
2. Convert the loaded image to grayscale.
3. Add Gaussian noise to the grayscale image.
4. Apply a Gaussian filter to the noisy image to reduce the noise.
5. Display the original image, the grayscale image, the noisy image, and the noise-reduced image side by side.

## Code Details

Here's a brief explanation of the MATLAB commands used in the script:

- `imread()`: Reads an image file.
- `rgb2gray()`: Converts an RGB image to grayscale.
- `im2double()`: Converts the grayscale image to double precision.
- `imnoise()`: Adds Gaussian noise to the grayscale image.
- `imshow()`: Displays an image in a figure window.
- `padarray()`: Pads the array (image) with zeros on both sides.
- `subplot()`: Allows for multiple plots in the same figure.

The Gaussian filter is manually created using a 3x3 kernel. The kernel is applied to the image via convolution to reduce the noise.

## How to Run

To run this script, you'll need an image file in the path. If you want to use a different image, change the filename in the `imread()` function.

Once the image file is in place, simply run the script in MATLAB.

## Output

The script will display a figure with four images:

1. The original image.
2. The grayscale version of the original image.
3. The noisy image (grayscale with Gaussian noise).
4. The image after noise reduction (grayscale with Gaussian noise reduced by the Gaussian filter).