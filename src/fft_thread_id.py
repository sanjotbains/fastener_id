import numpy as np
# import scipy as sp
from scipy.signal import find_peaks
import cv2
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
# import argparse # Not going to need this yet, just writing it all inline for now

def import_image(image_path):
    """
    Load an image from the specified path.
    """
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Failed to load image from {image_path}")
    
    # Filter out noise by applying a Gaussian blur
    img = cv2.GaussianBlur(img, (15, 15), 0)

    return img

def plot_visualization(thread_pitches, img, center_row, peaks, x_freq_in, center_row_orig):
        # TPI plotting
    plt.figure(figsize=(16, 10))

    plt.subplot(121)
    plt.plot(x_freq_in, np.log(center_row)+1)
    plt.scatter(thread_pitches, np.log(center_row[peaks])+1, c='r', marker='x')
    plt.xlim(0, np.max(thread_pitches) * 1.1)
    plt.title('Horizontal Frequency Spectrum with Peaks')
    
    # Spatial plotting
    plt.subplot(122)
    plt.plot(center_row_orig)
    plt.title('Original Image Intensity Profile')
    plt.xlabel('Pixel Position')
    plt.ylabel('Intensity')

    plt.figure()
    plt.imshow(img, cmap='gray')

    plt.show()


# To wrap my head around this, I need to internalize that the individual pixels are
# samples of the mm. 
def analyze_thread_pitch(img, px_per_mm):
    
    # At this point, the value of each individual pixel is a measure of intensity,
    # which is not directly related to the thread pitch.
    
    # Perform FFT
    fft_result = np.fft.fft2(img)
    fft_shifted = np.fft.fftshift(fft_result)  # Shift DC component to center
    magnitude = np.abs(fft_shifted)

    
    # Create frequency axes
    height, width = img.shape
    # x_freq = np.fft.fftshift(np.fft.fftfreq(width)) * width  # Cycles per image width
    # y_freq = np.fft.fftshift(np.fft.fftfreq(height)) * height  # Cycles per image height
    x_freq = np.fft.fftshift(np.fft.fftfreq(n=width, d=1/px_per_mm))  # Cycles per mm
    x_freq_in = x_freq[width//2:] * 25.4  # Convert to cycles per inch

    # # Extract horizontal frequency components (thread pitch is along x-axis)
    # center_row = magnitude[height//2, :]
    # # Going to cut off the negative frequencies for clarity
    # center_row = center_row[width//2:]  # Only keep positive frequencies

    # center_row_orig = img[height//2, :]

    # Sample several lines across the image and determine the peaks of each's spectrum
    
    
    
    peaks, _ = find_peaks(center_row, height=np.mean(center_row)*1.5, distance=10)

    thread_pitches = x_freq_in[peaks]  # Frequencies corresponding to peaks
    
    # Plot results
    # plot_visualization(thread_pitches, img, center_row, peaks, x_freq_in, center_row_orig)        

    return thread_pitches


# Example usage:
# Load and preprocess image
image_path = "src/3_8_16_test_crop_2.jpg"

img = import_image(image_path)
if img is None:
    print("Failed to load image.")

thread_pitches = analyze_thread_pitch(img, px_per_mm=37.75)
# thread_pitches = analyze_thread_pitch("src/bw_grating.png", px_per_mm=(256/25.4))

print("Thread pitches (tpi):", thread_pitches)
