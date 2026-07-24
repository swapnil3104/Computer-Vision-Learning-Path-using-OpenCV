# Computer Vision

> Learn the fundamentals of Computer Vision using Python and OpenCV.

---

# Table of Contents

1. What is Computer Vision?
2. Applications of Computer Vision
3. OpenCV Introduction
4. Reading Images
5. Displaying Images
6. Saving Images
7. Image Formats
8. Color Spaces Overview

---

# What is Computer Vision?

## Definition

**Computer Vision (CV)** is a field of Artificial Intelligence (AI) that enables computers to **see, understand, analyze, and interpret images and videos**, similar to how humans use their eyes and brain.

Computer Vision extracts meaningful information from visual data so that machines can make intelligent decisions.

In simple words:

> **Computer Vision teaches computers how to understand images and videos.**

---

## How Humans See vs Computers See

| Human Vision | Computer Vision |
|--------------|-----------------|
| Eyes capture light | Camera captures light |
| Brain processes the image | Computer processes pixels |
| Recognizes objects naturally | Uses algorithms to detect objects |
| Understands the environment | Makes decisions based on image analysis |

---

## Computer Vision Workflow

```text
Camera/Image
      │
      ▼
Image Acquisition
      │
      ▼
Preprocessing
(Resize, Blur, Denoise)
      │
      ▼
Feature Extraction
      │
      ▼
Object Detection / Recognition
      │
      ▼
Decision Making
```

---

## Why Learn Computer Vision?

Computer Vision is one of the fastest-growing fields in Artificial Intelligence.

It is used in:

- Self-driving cars
- Medical diagnosis
- Robotics
- Manufacturing
- Security systems
- Agriculture
- Sports analytics
- Retail automation

---

## Types of Computer Vision Tasks

### 1. Image Classification

Predicts what is present in an image.

Example:

```
Image
↓

Cat
```

---

### 2. Object Detection

Detects and locates objects inside an image.

Example:

```
Person
Car
Dog
Traffic Light
```

Each object receives a bounding box.

---

### 3. Image Segmentation

Assigns every pixel to an object.

Instead of drawing boxes, segmentation outlines the exact shape.

---

### 4. Face Detection

Finds human faces in an image.

Applications:

- Face Unlock
- Attendance System
- CCTV

---

### 5. Face Recognition

Recognizes **who** the person is.

Example:

```
Face Found

↓

Swapnil Patil
```

---

### 6. Object Tracking

Tracks moving objects across video frames.

Example:

- Football tracking
- Car tracking
- Person tracking

---

### 7. OCR (Optical Character Recognition)

Extracts text from images.

Example:

```
Image

↓

"Invoice No. 12345"
```

---

### 8. Pose Estimation

Detects body joints.

Applications:

- Fitness apps
- Yoga monitoring
- Sports analysis

---

# Applications of Computer Vision

Computer Vision is used in almost every modern industry.

---

## 1. Healthcare

Applications:

- Disease Detection
- X-Ray Analysis
- MRI Analysis
- CT Scan Analysis
- Cancer Detection
- Eye Disease Detection

Example:

Detect diabetic retinopathy from retinal images.

---

## 2. Autonomous Vehicles

Applications:

- Lane Detection
- Traffic Sign Recognition
- Pedestrian Detection
- Vehicle Detection

Examples:

Tesla

Waymo

Mercedes Autonomous Driving

---

## 3. Security & Surveillance

Applications:

- Face Recognition
- Intruder Detection
- Number Plate Recognition
- Crowd Monitoring

Examples:

Airport security

Smart cities

CCTV systems

---

## 4. Agriculture

Applications:

- Crop Disease Detection
- Fruit Counting
- Weed Detection
- Soil Analysis

---

## 5. Manufacturing

Applications:

- Defect Detection
- Product Inspection
- Robot Guidance
- Quality Control

---

## 6. Retail

Applications:

- Self Checkout
- Shelf Monitoring
- Customer Tracking
- Product Recognition

---

## 7. Banking

Applications:

- Signature Verification
- Check Processing
- Document Verification

---

## 8. Sports

Applications:

- Ball Tracking
- Player Tracking
- Goal Detection
- Performance Analytics

---

## 9. Robotics

Applications:

- Object Grasping
- Navigation
- Obstacle Detection

---

## 10. Smart Phones

Applications:

- Portrait Mode
- Face Unlock
- QR Scanner
- Augmented Reality

---

# OpenCV Introduction

## What is OpenCV?

**OpenCV** stands for:

> **Open Source Computer Vision Library**

It is the world's most popular open-source library for Computer Vision and Image Processing.

Website:

https://opencv.org/

---

## Features of OpenCV

- Open Source
- Free to Use
- Cross Platform
- Fast Performance
- Real-Time Processing
- Large Community
- Supports Deep Learning

---

## Programming Languages Supported

- Python
- C++
- Java
- JavaScript

Python is the most commonly used language for beginners.

---

## Installing OpenCV

```bash
pip install opencv-python
```

Install additional modules:

```bash
pip install opencv-contrib-python
```

---

## Importing OpenCV

```python
import cv2
```

Check version:

```python
print(cv2.__version__)
```

Example Output

```
4.12.0
```

---

## Why OpenCV?

OpenCV provides ready-made functions for:

- Image Processing
- Video Processing
- Object Detection
- Face Recognition
- Image Transformation
- Machine Learning
- Deep Learning

---

# Reading Images

Reading an image means loading it from storage into memory.

---

## Syntax

```python
cv2.imread(filename, flags)
```

---

## Parameters

| Parameter | Description |
|------------|-------------|
| filename | Path to the image |
| flags | Image reading mode |

---

## Reading a Color Image

```python
import cv2

image = cv2.imread("cat.jpg")
```

---

## Reading a Grayscale Image

```python
image = cv2.imread("cat.jpg", cv2.IMREAD_GRAYSCALE)
```

---

## Reading an Unchanged Image

```python
image = cv2.imread("cat.png", cv2.IMREAD_UNCHANGED)
```

---

## Common Flags

| Flag | Description |
|------|-------------|
| IMREAD_COLOR | Loads color image |
| IMREAD_GRAYSCALE | Loads grayscale |
| IMREAD_UNCHANGED | Loads alpha channel |

---

## Check if Image Loaded Successfully

```python
if image is None:
    print("Image not found")
else:
    print("Image Loaded Successfully")
```

---

# Displaying Images

OpenCV provides a window to display images.

---

## Syntax

```python
cv2.imshow(window_name, image)
```

---

## Example

```python
import cv2

image = cv2.imread("cat.jpg")

cv2.imshow("Cat Image", image)

cv2.waitKey(0)

cv2.destroyAllWindows()
```

---

## Explanation

### imshow()

Displays image.

### waitKey(0)

Waits until any key is pressed.

### destroyAllWindows()

Closes all windows.

---

# Saving Images

Images can be saved after processing.

---

## Syntax

```python
cv2.imwrite(filename, image)
```

---

## Example

```python
import cv2

image = cv2.imread("cat.jpg")

cv2.imwrite("new_cat.jpg", image)
```

---

## Save Grayscale Image

```python
gray = cv2.imread("cat.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imwrite("gray_cat.jpg", gray)
```

---

# Image Formats

OpenCV supports many image formats.

---

## Common Formats

| Format | Extension | Compression | Transparency |
|----------|-----------|-------------|--------------|
| JPEG | .jpg | Lossy | No |
| PNG | .png | Lossless | Yes |
| BMP | .bmp | None | No |
| TIFF | .tiff | Lossless | Yes |
| WEBP | .webp | Lossy/Lossless | Yes |

---

## JPEG

Advantages

- Small file size
- Best for photographs

Disadvantages

- Quality decreases after compression

---

## PNG

Advantages

- Lossless
- Transparent background

Disadvantages

- Larger file size

---

## BMP

Advantages

- High quality

Disadvantages

- Very large file size

---

## TIFF

Advantages

- High-quality images
- Used in printing and medical imaging

---

## WEBP

Advantages

- Smaller size
- Better quality than JPEG
- Supports transparency

---

# Color Spaces Overview

A **Color Space** defines how colors are represented numerically in an image.

Different applications use different color spaces depending on the task.

---

## Common Color Spaces

| Color Space | Channels | Typical Use |
|-------------|----------|-------------|
| BGR | Blue, Green, Red | Default in OpenCV |
| RGB | Red, Green, Blue | Display and visualization |
| Grayscale | Intensity only | Image processing |
| HSV | Hue, Saturation, Value | Color detection |
| LAB | Lightness, A, B | Color correction |
| YCrCb | Luminance, Chrominance | Video compression |

---

## BGR

OpenCV stores images in **BGR** order instead of RGB.

Example:

```
Pixel

Blue
Green
Red
```

---

## RGB

Most image viewers use RGB.

```
Red
Green
Blue
```

---

## Grayscale

Contains only one channel.

Pixel values:

```
0 → Black

255 → White
```

---

## HSV

HSV separates color information from brightness.

| Component | Meaning |
|------------|----------|
| H | Hue |
| S | Saturation |
| V | Value |

Useful for:

- Color detection
- Object tracking
- Segmentation

---

## LAB

Components:

- L → Lightness
- A → Green ↔ Red
- B → Blue ↔ Yellow

Used in:

- Image enhancement
- Color correction

---

## YCrCb

Components:

- Y → Brightness
- Cr → Red Difference
- Cb → Blue Difference

Used in:

- Video encoding
- Face detection
- Compression

---

## Converting Color Spaces

```python
import cv2

image = cv2.imread("cat.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
```

---

# Summary

In this module, you learned:

- What Computer Vision is
- Real-world applications of Computer Vision
- Introduction to OpenCV
- How to install and import OpenCV
- How to read images using `cv2.imread()`
- How to display images using `cv2.imshow()`
- How to save images using `cv2.imwrite()`
- Different image file formats and their use cases
- Common color spaces such as BGR, RGB, Grayscale, HSV, LAB, and YCrCb

---

# Next Module

➡️ **Module 2: Image Basics**

Topics:

- Pixels
- Resolution
- Width & Height
- Channels
- Image Properties
- Accessing Pixel Values
- Modifying Pixels
- Copying Images