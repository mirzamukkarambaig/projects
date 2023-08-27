# Image Noise Reduction using Gaussian Filter

This Python script demonstrates an implementation of a Gaussian filter for noise reduction in images using OpenCV and Matplotlib. It performs the following operations:

1. Load an image.
2. Convert the loaded image to grayscale.
3. Add Gaussian noise to the grayscale image.
4. Apply a Gaussian filter to the noisy image to reduce the noise.
5. Display the original RGB image, the original grayscale image, the noisy image, and the noise-reduced image side by side.

## Code Details

Here's a brief explanation of the Python libraries and functions used in the script:

- `cv2.imread()`: Reads an image file using OpenCV.
- `cv2.cvtColor()`: Converts an RGB image to grayscale using OpenCV.
- `cv2.filter2D()`: Applies a filter to an image using OpenCV.
- `plt.subplot()`: Allows for multiple plots in the same figure using Matplotlib.
  
The Gaussian filter is created using a 3x3 kernel. The kernel is applied to the image via convolution to reduce the noise.

## Dependencies

- OpenCV (`cv2`)
- NumPy (`numpy`)
- Matplotlib (`matplotlib`)

You can install these using pip:

```bash
pip install opencv-python numpy matplotlib
```

## How to Run

To run this script, you'll need an image file in the path specified in the `cv2.imread()` function. If you want to use a different image, change the filename accordingly.

Once the image file is in place, simply run the Python script.

## Output

The script will display a figure with four images:

1. The original RGB image.
2. The original grayscale version of the image.
3. The noisy image (grayscale with Gaussian noise).
4. The image after noise reduction (grayscale with Gaussian noise reduced by the Gaussian filter).
