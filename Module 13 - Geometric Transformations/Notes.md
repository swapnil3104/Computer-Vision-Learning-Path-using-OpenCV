# Module 13 - Geometric Transformations

## Learning Objectives

After completing this module, you will be able to:

- Understand geometric transformations in digital image processing.
- Learn the difference between Affine, Perspective, and Homography transformations.
- Apply these transformations using OpenCV.
- Understand transformation matrices and coordinate mapping.
- Use geometric transformations in real-world computer vision applications.

---

# Introduction

Geometric transformations modify the **position**, **orientation**, **shape**, or **viewpoint** of an image without changing its pixel values.

Unlike image filtering, geometric transformations move pixels from one location to another using mathematical equations.

They are widely used in:

- Computer Vision
- Image Registration
- Object Detection
- Augmented Reality
- Robotics
- Medical Imaging
- Document Scanning
- Panorama Stitching

---

# Types of Geometric Transformations

This module covers three important transformations:

1. Affine Transform
2. Perspective Transform
3. Homography

---

# Coordinate System

Images use a coordinate system.

```
(0,0)
 +-----------------------------> X

 |
 |
 |
 |
 V

 Y
```

Every pixel has coordinates

```
(x, y)
```

A transformation calculates a new coordinate

```
(x', y')
```

---

# Transformation Matrix

A transformation uses a matrix.

General form

```
[x']
[y'] = T × [x]
            [y]
            [1]
```

where

- T = Transformation Matrix
- (x,y) = Original Point
- (x',y') = New Point

---

# 1. Affine Transform

## Definition

An Affine Transformation changes an image while preserving:

- Straight lines
- Parallel lines
- Relative distances on parallel lines

However,

- Angles may change.
- Lengths may change.

---

# Characteristics

Affine transformation supports

- Translation
- Rotation
- Scaling
- Shearing

It **does not preserve perspective**.

---

# Affine Matrix

Affine uses a **2 × 3 matrix**

```
| a11 a12 tx |
| a21 a22 ty |
```

where

```
tx = Translation in X

ty = Translation in Y
```

---

# How Affine Works

Original

```
□
```

↓

Rotate

↓

Scale

↓

Translate

↓

Shear

↓

New Image

---

# Three Control Points

Affine transformation requires

**3 corresponding points**

Example

```
Original

A
B
C

↓

Destination

A'
B'
C'
```

OpenCV calculates the matrix using these points.

---

# OpenCV Function

```python
cv2.getAffineTransform()
```

Syntax

```python
matrix = cv2.getAffineTransform(srcPoints, dstPoints)
```

Apply transformation

```python
cv2.warpAffine()
```

Syntax

```python
result = cv2.warpAffine(
    image,
    matrix,
    (width,height)
)
```

---

# Applications

- Image alignment
- Image registration
- OCR preprocessing
- Face alignment
- Object tracking

---

# Advantages

- Fast
- Easy to compute
- Preserves straight lines
- Good for small viewpoint changes

---

# Limitations

- Cannot correct perspective distortion.
- Requires corresponding points.
- Cannot model camera viewpoint changes.

---

# 2. Perspective Transform

## Definition

Perspective Transformation changes the viewing angle of an image.

It simulates how objects appear from different camera positions.

Unlike affine transformation,

Perspective Transformation **preserves perspective**.

---

# Characteristics

Perspective transformation can

- Rotate
- Translate
- Scale
- Warp
- Correct perspective

---

# Example

Original Image

```
□□□□
□□□□
□□□□
```

Viewed from an angle

```
  /------
 /      /
/------/
```

Perspective transform converts it back into a rectangle.

---

# Perspective Matrix

Perspective transformation uses a

**3 × 3 matrix**

```
| a b c |
| d e f |
| g h i |
```

---

# Four Control Points

Perspective transformation requires

**4 corresponding points**

```
Original

P1
P2
P3
P4

↓

Destination

P1'
P2'
P3'
P4'
```

---

# OpenCV Function

```python
cv2.getPerspectiveTransform()
```

Syntax

```python
matrix = cv2.getPerspectiveTransform(
    src,
    dst
)
```

Apply transformation

```python
cv2.warpPerspective()
```

Syntax

```python
output = cv2.warpPerspective(
    image,
    matrix,
    (width,height)
)
```

---

# Applications

- Document Scanner
- License Plate Detection
- QR Code Detection
- Bird's Eye View
- Road Lane Detection

---

# Advantages

- Corrects camera perspective
- Produces realistic transformations
- Better than affine for tilted images

---

# Limitations

- Requires four accurate points.
- Slightly slower than affine.
- Sensitive to incorrect point selection.

---

# Affine vs Perspective

| Feature | Affine | Perspective |
|----------|---------|-------------|
| Matrix | 2×3 | 3×3 |
| Control Points | 3 | 4 |
| Parallel Lines | Preserved | Not always |
| Perspective | No | Yes |
| Speed | Faster | Slower |

---

# 3. Homography

## Definition

A Homography is a mathematical transformation that maps one plane to another.

It is one of the most important concepts in Computer Vision.

Homography estimates the relationship between two images of the same planar object.

---

# Example

Image 1

```
Notebook
```

↓

Different Camera Angle

↓

Image 2

Homography maps

```
Image1 → Image2
```

---

# Homography Matrix

Homography also uses a

**3 × 3 matrix**

```
| h11 h12 h13 |
| h21 h22 h23 |
| h31 h32 h33 |
```

---

# Minimum Points

Homography requires

**At least 4 matching points**

Usually more points are used for better accuracy.

---

# Finding Homography

OpenCV Function

```python
cv2.findHomography()
```

Syntax

```python
H, mask = cv2.findHomography(
    srcPoints,
    dstPoints
)
```

---

# Applying Homography

Use

```python
cv2.warpPerspective()
```

because homography produces a perspective transformation matrix.

---

# Feature Matching

Homography is usually calculated after feature detection.

Common feature detectors

- ORB
- SIFT
- SURF
- AKAZE
- BRISK

Workflow

```
Image 1

↓

Feature Detection

↓

Feature Matching

↓

Find Homography

↓

Warp Perspective

↓

Aligned Image
```

---

# Applications

- Panorama Stitching
- Augmented Reality
- Object Recognition
- Camera Calibration
- Image Registration
- Drone Mapping
- Satellite Image Alignment

---

# Advantages

- Highly accurate
- Works with different viewpoints
- Supports panorama generation
- Handles perspective changes

---

# Limitations

- Requires good feature matches.
- Computationally expensive.
- Fails with insufficient matching points.
- Works best for planar surfaces.

---

# Affine vs Perspective vs Homography

| Feature | Affine | Perspective | Homography |
|----------|---------|-------------|------------|
| Matrix Size | 2×3 | 3×3 | 3×3 |
| Control Points | 3 | 4 | 4 or more |
| Rotation | Yes | Yes | Yes |
| Translation | Yes | Yes | Yes |
| Scaling | Yes | Yes | Yes |
| Shearing | Yes | Yes | Yes |
| Perspective Correction | No | Yes | Yes |
| Feature Matching | No | No | Yes |
| Panorama | No | No | Yes |

---

# OpenCV Functions Summary

| Function | Purpose |
|----------|----------|
| cv2.getAffineTransform() | Compute affine transformation matrix |
| cv2.warpAffine() | Apply affine transformation |
| cv2.getPerspectiveTransform() | Compute perspective matrix |
| cv2.warpPerspective() | Apply perspective transformation |
| cv2.findHomography() | Compute homography matrix |

---

# Real-World Applications

## Affine Transform

- Face Alignment
- OCR
- Image Registration
- Object Tracking

---

## Perspective Transform

- Document Scanner
- Road Lane Detection
- QR Code Scanner
- Bird's Eye View

---

## Homography

- Panorama Stitching
- Augmented Reality
- Robotics
- Drone Navigation
- Camera Calibration
- Medical Image Alignment

---

# Workflow of Geometric Transformations

```
Input Image
      │
      ▼
Select Corresponding Points
      │
      ▼
Compute Transformation Matrix
      │
      ├────────► Affine Transform
      │
      ├────────► Perspective Transform
      │
      └────────► Homography
      │
      ▼
Warp Image
      │
      ▼
Output Image
```

---

# Advantages of Geometric Transformations

- Image alignment
- Camera correction
- Viewpoint correction
- Image stitching
- Feature matching
- Image registration
- Improved object detection
- Essential for computer vision applications

---

# Limitations

- Accurate point selection is critical.
- Perspective and Homography are computationally more expensive than Affine.
- Noise or incorrect feature matches can reduce accuracy.
- Homography assumes that the scene is approximately planar.

---

# Summary

In this module, you learned:

- What geometric transformations are and why they are important in image processing.
- How **Affine Transformation** uses a 2×3 matrix and three control points to perform translation, rotation, scaling, and shearing while preserving straight and parallel lines.
- How **Perspective Transformation** uses a 3×3 matrix and four control points to correct viewpoint distortions and simulate camera perspective.
- How **Homography** maps one planar image to another using feature correspondences and is widely used in panorama stitching, augmented reality, and image registration.
- The OpenCV functions used for these transformations, their advantages, limitations, and real-world applications.

These geometric transformations form the foundation of many advanced computer vision systems, enabling accurate image alignment, viewpoint correction, and scene reconstruction.

---
Reference Link : https://www.geeksforgeeks.org/electronics-engineering/geometric-transformation-in-image-processing-1/
---