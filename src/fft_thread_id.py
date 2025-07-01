import numpy as np
import scipy as sp
import cv2
import argparse # Not going to need this yet, just writing it all inline for now

img = cv2.imread("test_img1.png", cv2.IMREAD_UNCHANGED)

if img is None:
    print("Failed to load image.")

# Convert to grayscale if the image is not already in grayscale
if len(img.shape) == 3 and img.shape[2] == 3:
    print("Converting image to grayscale.")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Perform FFT on the whole image, no preprocessing
print("Performing FFT on the image.")
fft_result = np.fft.fft2(img)
fft_magnitude = np.abs(fft_result)

# Visualize the FFT result
fft_magnitude_log = np.log(fft_magnitude + 1)  # Log scale
fft_magnitude_normalized = cv2.normalize(fft_magnitude_log, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
cv2.imshow("FFT Magnitude", fft_magnitude_normalized)
cv2.waitKey(0)
cv2.destroyAllWindows()

