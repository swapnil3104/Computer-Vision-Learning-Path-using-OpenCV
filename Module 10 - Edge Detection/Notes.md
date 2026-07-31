# Module 10 - Edge Detection

# Introduction

Edge Detection is one of the most important image processing techniques in computer vision. It is used to identify the boundaries of objects within an image. An edge is a region where there is a sudden change in pixel intensity. Detecting these edges helps computers understand the shape, size, and location of objects.

Edge detection is widely used in:

- Object Detection
- Image Segmentation
- Face Recognition
- Medical Image Analysis
- Autonomous Vehicles
- Robotics
- Industrial Inspection
- OCR (Optical Character Recognition)

OpenCV provides several edge detection algorithms, each designed for different purposes.

---

# What is an Edge?

An edge is the boundary between two regions having different intensity values.

Example:

A black square on a white background has four strong edges because the intensity changes abruptly.

```
White White White White
White Black Black White
White Black Black White
White White White White
```

The transition from white pixels to black pixels creates edges.

---

# Why Edge Detection?

Edge detection helps reduce the amount of image data while preserving important structural information.

Advantages:

- Detect object boundaries
- Reduce unnecessary image information
- Improve image segmentation
- Assist in feature extraction
- Increase recognition accuracy
- Prepare images for higher-level computer vision tasks

---

# Types of Edge Detection Operators

OpenCV mainly provides:

1. Sobel Operator
2. Scharr Operator
3. Laplacian Operator
4. Canny Edge Detection

---

# 1. Sobel Operator

## Introduction

The Sobel operator is a first-order derivative operator used to detect edges by calculating the gradient of image intensity.

It detects:

- Horizontal edges
- Vertical edges

or both together.

Instead of directly calculating derivatives, Sobel combines smoothing and differentiation, making it less sensitive to noise.

---

## How Sobel Works

Sobel applies convolution kernels.

### Horizontal Gradient (X Direction)

```
-1 0 +1
-2 0 +2
-1 0 +1
```

Detects vertical edges.

---

### Vertical Gradient (Y Direction)

```
-1 -2 -1
 0  0  0
+1 +2 +1
```

Detects horizontal edges.

---

## Mathematical Formula

Gradient Magnitude

```
G = √(Gx² + Gy²)
```

Where

- Gx = Gradient in X direction
- Gy = Gradient in Y direction

Larger gradient means stronger edge.

---

## Parameters

```
cv2.Sobel()

Parameters:

src
ddepth
dx
dy
ksize
```

### src

Input image.

### ddepth

Output image depth.

Usually

```
cv2.CV_64F
```

---

### dx

Derivative order in x direction.

```
dx = 1
```

detects vertical edges.

---

### dy

Derivative order in y direction.

```
dy = 1
```

detects horizontal edges.

---

### ksize

Kernel size.

Common values

```
3
5
7
```

---

## Advantages

- Simple
- Fast
- Noise resistant
- Detects edge direction

---

## Disadvantages

- Misses weak edges
- Produces thick edges
- Sensitive to kernel size

---

# Example

Original Image

```
██████████████

████      ████

████      ████

██████████████
```

Sobel Output

```
||||||||||||||

||          ||

||          ||

||||||||||||||
```

Edges become highlighted.

---

# 2. Scharr Operator

## Introduction

Scharr is an improved version of Sobel.

It provides more accurate gradient calculation especially when kernel size equals 3.

Scharr is preferred when high precision edge detection is required.

---

## Why Scharr?

The Sobel operator sometimes introduces approximation errors.

Scharr reduces these errors by using different kernels.

---

## Scharr Kernels

Horizontal

```
-3 0 +3
-10 0 +10
-3 0 +3
```

Vertical

```
-3 -10 -3
 0   0  0
+3 +10 +3
```

Notice the larger weights.

These improve accuracy.

---

## Function

```
cv2.Scharr()
```

Parameters are similar to Sobel.

---

## Advantages

- Better accuracy
- Better edge localization
- Excellent for fine details

---

## Disadvantages

- Slightly slower than Sobel
- Supports fixed kernel

---

# Sobel vs Scharr

| Feature | Sobel | Scharr |
|----------|--------|---------|
| Accuracy | Good | Better |
| Speed | Faster | Slightly slower |
| Precision | Moderate | High |
| Kernel | Variable | Fixed |
| Noise Resistance | Good | Better |

---

# 3. Laplacian Operator

## Introduction

Unlike Sobel, Laplacian detects edges in all directions.

It is based on the second derivative.

Instead of detecting edge direction, it detects rapid intensity changes.

---

## Mathematical Formula

```
∇²I

=

∂²I/∂x²

+

∂²I/∂y²
```

---

## Kernel

Typical Laplacian kernel

```
0 1 0

1 -4 1

0 1 0
```

Another version

```
1 1 1

1 -8 1

1 1 1
```

---

## Function

```
cv2.Laplacian()
```

---

## Parameters

```
src

ddepth

ksize
```

---

## Advantages

- Detects edges in every direction
- Simple implementation
- Highlights fine details

---

## Disadvantages

- Very sensitive to noise
- Usually Gaussian Blur is applied before Laplacian

Pipeline

```
Image

↓

Gaussian Blur

↓

Laplacian

↓

Output
```

---

# Example

Input

```
█████████

██     ██

██     ██

█████████
```

Output

```
#########

#       #

#       #

#########
```

---

# 4. Canny Edge Detection

## Introduction

Canny Edge Detection is considered one of the best edge detection algorithms.

Developed by:

John F. Canny (1986)

It detects clean, thin, and continuous edges while reducing noise.

---

## Canny Algorithm Steps

Step 1

Noise Reduction

↓

Step 2

Gradient Calculation

↓

Step 3

Non-Maximum Suppression

↓

Step 4

Double Threshold

↓

Step 5

Edge Tracking by Hysteresis

---

## Step 1 – Noise Reduction

Image is first blurred using Gaussian Blur.

```
Original

↓

Gaussian Blur

↓

Smoothed Image
```

This removes unwanted noise.

---

## Step 2 – Gradient Calculation

Sobel operator computes

- Gx
- Gy

Gradient magnitude

```
G = √(Gx² + Gy²)
```

---

## Step 3 – Non-Maximum Suppression

Keeps only the strongest edge pixels.

Removes thick edges.

Result:

Thin edges.

---

## Step 4 – Double Threshold

Two thresholds are used.

```
Low Threshold

High Threshold
```

Pixels are classified as

- Strong Edge
- Weak Edge
- Non Edge

---

## Step 5 – Edge Tracking by Hysteresis

Weak edges connected to strong edges are preserved.

Others are discarded.

Result:

Continuous edges.

---

## Function

```
cv2.Canny()
```

---

## Parameters

```
image

threshold1

threshold2
```

Example

```
edges = cv2.Canny(image,100,200)
```

---

## Choosing Thresholds

Example

```
50,150

100,200

150,300
```

Higher threshold

↓

Fewer edges

Lower threshold

↓

More edges

---

## Advantages

- Very accurate
- Thin edges
- Low noise
- Automatic edge connectivity
- Excellent for computer vision

---

## Disadvantages

- Slightly slower
- Threshold selection is important

---

# Comparison of Edge Detection Methods

| Feature | Sobel | Scharr | Laplacian | Canny |
|----------|--------|---------|------------|--------|
| Derivative | First | First | Second | Multi-stage |
| Detect Direction | Yes | Yes | No | Yes |
| Noise Handling | Good | Better | Poor | Excellent |
| Edge Thickness | Thick | Thick | Thick | Thin |
| Accuracy | Good | Better | Moderate | Excellent |
| Speed | Fast | Fast | Fast | Moderate |
| Best Use | General edges | Accurate gradients | All-direction edges | High-quality edge detection |

---

# Workflow of Edge Detection

```
Input Image

↓

Convert to Grayscale

↓

(Optional)
Gaussian Blur

↓

Edge Detection

↓

Output Edge Image
```

---

# Applications of Edge Detection

- Face Detection
- Medical Imaging
- Fingerprint Recognition
- Autonomous Driving
- Lane Detection
- Industrial Quality Inspection
- OCR Systems
- Satellite Image Analysis
- Object Tracking
- Image Segmentation
- Shape Detection
- Robotics
- Barcode Detection
- License Plate Recognition

---

# Best Practices

- Convert images to grayscale before detecting edges.
- Apply Gaussian Blur to reduce image noise.
- Use Sobel for basic gradient detection.
- Use Scharr when more accurate gradients are required.
- Apply Laplacian only after smoothing the image.
- Use Canny for clean and reliable edge detection in most applications.
- Experiment with threshold values in Canny for different image types.
- Normalize or convert gradient images before displaying them.

---

# Summary

Edge Detection identifies boundaries by detecting rapid changes in pixel intensity. OpenCV provides multiple algorithms, each suited for different tasks. Sobel and Scharr calculate first-order gradients, Laplacian uses second-order derivatives to detect edges in all directions, and Canny combines multiple processing stages to produce thin, accurate, and noise-resistant edges. Among all methods, Canny Edge Detection is generally considered the most effective for real-world computer vision applications due to its high accuracy and reliable edge connectivity.

---
# Key Takeaways

- Edge detection identifies object boundaries by detecting sudden intensity changes.
- Sobel computes first-order gradients in horizontal and vertical directions.
- Scharr improves gradient accuracy, especially with a 3×3 kernel.
- Laplacian uses second-order derivatives to detect edges in all directions.
- Canny combines smoothing, gradient calculation, non-maximum suppression, double thresholding, and hysteresis to produce high-quality edges.
- Gaussian Blur is commonly used before edge detection to minimize the effect of noise.
- Canny is the preferred choice for most practical computer vision applications because it produces thin, continuous, and accurate edges.

___

Reference Link : https://www.geeksforgeeks.org/digital-logic/image-edge-detection-operators-in-digital-image-processing/