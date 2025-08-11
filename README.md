# FastFastenerID

A tool for identifying hardware fasteners (bolts, screws, etc.) from images and, eventually, video feeds. The project leverages computer vision and signal processing to estimate fastener dimensions and characteristics.

## Goals

- Identify fastener type and location in an image using computer vision (CNN-based).
- Estimate diameter and length using a known background pattern.
- Detect thread pitch using classic signal processing (FFT).
- Develop preprocessing filters to highlight threads.
- Use color data to infer material (stretch goal).

## Accomplished

- Outlined initial approach for fastener identification.
- Researched background pattern usage for dimension estimation.
- Experimenting with FFTs on images of threaded fasteners on various backgrounds.

## In Progress

- Testing preprocessing filters (e.g., Laplacian) to enhance thread visibility.
- Aligning fastener images for consistent analysis.
- Using ruled graph paper for calibration (OpenCV).

## Future

- Integrate video feed processing.
- Train and deploy CNN models for cap type and localization.
- Refine thread detection and pitch estimation.
- Expand material identification using color analysis.
- Improve robustness to background variation.

---
*This project is in early development. Contributions and feedback are welcome!*
