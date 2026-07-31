# Module 14 - Feature Detection

## Learning Objectives

After completing this module, you will be able to:

- Understand what image features are.
- Detect corners and keypoints in images.
- Extract feature descriptors.
- Match features between images.
- Understand rotation and scale invariant algorithms.
- Choose the appropriate feature detector for different computer vision applications.

---

# What is Feature Detection?

Feature Detection is the process of identifying important points or regions in an image that are unique and can be reliably detected under different conditions.

These points are called:

- Keypoints
- Interest Points
- Features

Examples include:

- Corners
- Edges
- Blobs
- Junctions
- Textured regions

Feature detection is one of the most important concepts in Computer Vision because features remain recognizable even when an object changes position, size, or orientation.

---

# Why Feature Detection is Important?

Feature detection is used in:

- Object Recognition
- Face Recognition
- Image Stitching
- Panorama Creation
- Visual SLAM
- Augmented Reality
- Robot Navigation
- Image Matching
- Motion Tracking
- 3D Reconstruction

---

# Feature Detection Pipeline

Image
↓

Preprocessing (optional)

↓

Feature Detection

↓

Feature Description

↓

Feature Matching

↓

Object Recognition / Tracking

---

# What is a Corner?

A corner is a point where the image intensity changes significantly in multiple directions.

Example:

```
██████
██░░██
██░░██
██████
```

Corners contain much more information than edges.

Examples:

- Window corners
- Building corners
- Chessboard intersections

---

# Types of Image Features

## 1. Edges

Change in intensity in one direction.

Example:

Black → White

---

## 2. Corners

Intensity changes in two directions.

Example:

Rectangle corner

---

## 3. Blobs

Circular regions having similar intensity.

Example:

Coins

Cells

Eyes

---

## 4. Texture

Repeated patterns.

Example:

Grass

Fabric

Wood

Sand

---

# Good Feature Characteristics

A good feature should be:

✔ Unique

✔ Repeatable

✔ Robust to illumination

✔ Robust to rotation

✔ Robust to scale

✔ Noise resistant

---

# Corner Detection vs Feature Detection

Corner Detection

- Detects only corners

Examples:

- Harris
- Shi-Tomasi

Feature Detection

Detects keypoints and computes descriptors.

Examples:

- ORB
- SIFT
- SURF
- BRISK

---

# 1. Harris Corner Detection

## Introduction

Harris Corner Detector was introduced by Chris Harris in 1988.

It detects corners by analyzing intensity variation in different directions.

---

## Principle

If shifting a small image window in any direction causes a large intensity change,

→ It is a corner.

If change occurs only in one direction,

→ Edge.

If no change,

→ Flat region.

---

## Mathematical Idea

Image gradients are calculated:

Ix

Iy

Then Harris Matrix is computed:

M

Corner response:

R = det(M) − k(trace(M))²

where

k ≈ 0.04–0.06

Large positive R

→ Corner

Small R

→ Flat

Negative R

→ Edge

---

## Advantages

- Fast
- Accurate
- Good corner localization
- Rotation invariant

---

## Disadvantages

- Not scale invariant
- Sensitive to noise
- Doesn't generate descriptors

---

## Applications

- Chessboard detection
- Camera calibration
- Tracking

---

# 2. Shi-Tomasi Corner Detector

## Introduction

Shi-Tomasi is an improved version of Harris.

Used extensively in OpenCV.

Function:

goodFeaturesToTrack()

---

## Principle

Instead of Harris response,

Shi-Tomasi uses

Minimum Eigenvalue

Corner Score

R = min(λ1, λ2)

Large value

→ Strong corner

---

## Advantages

- Better than Harris
- Fewer false corners
- Stable
- Excellent tracking

---

## Disadvantages

- Scale sensitive
- Corner detector only

---

## Applications

- Optical Flow
- Object Tracking
- Motion Detection

---

# Harris vs Shi-Tomasi

| Harris | Shi-Tomasi |
|----------|------------|
| Uses Harris response | Uses minimum eigenvalue |
| More corners | Better corners |
| Slightly noisy | Cleaner results |
| Older | Improved |

---

# 3. FAST (Features from Accelerated Segment Test)

## Introduction

FAST is one of the fastest corner detection algorithms.

Designed for real-time applications.

---

## Working Principle

Consider a circle of 16 pixels around a candidate pixel.

If a set of consecutive pixels are significantly brighter or darker than the center,

→ Corner detected.

---

## Advantages

- Extremely fast
- Real-time
- Low computation
- Mobile friendly

---

## Disadvantages

- No descriptors
- Scale sensitive

---

## Applications

- Robotics
- Video processing
- Drone navigation

---

# 4. ORB (Oriented FAST and Rotated BRIEF)

## Introduction

ORB combines

FAST Detector

+

BRIEF Descriptor

Introduced as a free alternative to SIFT and SURF.

---

## Components

Feature Detector:

FAST

Descriptor:

BRIEF

Orientation:

Intensity centroid

---

## Features

Rotation invariant

Noise resistant

Binary descriptors

Very fast

---

## Advantages

- Free
- Fast
- Rotation invariant
- Efficient matching

---

## Disadvantages

- Less accurate than SIFT
- Moderate scale invariance

---

## Applications

- Panorama stitching
- Mobile vision
- Object recognition
- AR

---

# 5. SIFT (Scale Invariant Feature Transform)

## Introduction

Developed by David Lowe (1999).

One of the most famous feature detection algorithms.

---

## Main Idea

Detect features that remain stable under:

Rotation

Scaling

Lighting

Noise

Perspective changes

---

## Steps

1. Scale-space extrema detection
2. Keypoint localization
3. Orientation assignment
4. Descriptor generation

---

## Descriptor

128-dimensional vector

Highly distinctive.

---

## Advantages

- Very accurate
- Rotation invariant
- Scale invariant
- Illumination robust

---

## Disadvantages

- Slow
- Computationally expensive

---

## Applications

- Image matching
- Object recognition
- Image retrieval
- Robotics

---

# 6. SURF (Speeded Up Robust Features)

## Introduction

SURF is a faster alternative to SIFT.

Uses integral images and Hessian matrix approximation.

---

## Features

Scale invariant

Rotation invariant

Fast descriptor computation

---

## Advantages

- Faster than SIFT
- Robust
- Good accuracy

---

## Disadvantages

- Patent restrictions (historically)
- Available in OpenCV contrib

---

## Applications

- Object detection
- Image registration
- Visual localization

---

# 7. BRISK (Binary Robust Invariant Scalable Keypoints)

## Introduction

BRISK combines:

Fast keypoint detection

Binary descriptors

Scale-space detection

---

## Features

Scale invariant

Rotation invariant

Binary descriptor

Fast matching

---

## Advantages

- Lightweight
- Efficient
- Fast
- Good for embedded systems

---

## Disadvantages

- Less accurate than SIFT
- Sensitive to heavy blur

---

## Applications

- Mobile vision
- Real-time tracking
- Object recognition

---

# Feature Descriptor

A descriptor is a numerical representation of the local image around a keypoint.

Example:

Keypoint

↓

Descriptor

↓

Matching

---

# Feature Matching

Feature matching compares descriptors between two images.

Popular Matchers:

- Brute Force Matcher
- FLANN Matcher

---

# Distance Metrics

Binary descriptors:

- Hamming Distance

Floating-point descriptors:

- Euclidean Distance

---

# Detector Comparison

| Algorithm | Corner | Descriptor | Rotation | Scale | Speed |
|------------|---------|------------|----------|--------|-------|
| Harris | ✔ | ✘ | ✔ | ✘ | Fast |
| Shi-Tomasi | ✔ | ✘ | ✔ | ✘ | Fast |
| FAST | ✔ | ✘ | ✘ | ✘ | Very Fast |
| ORB | ✔ | ✔ | ✔ | Partial | Very Fast |
| SIFT | ✔ | ✔ | ✔ | ✔ | Slow |
| SURF | ✔ | ✔ | ✔ | ✔ | Medium |
| BRISK | ✔ | ✔ | ✔ | ✔ | Fast |

---

# Advantages of Feature Detection

- Robust object detection
- Image alignment
- Panorama creation
- Motion estimation
- Camera tracking
- Face recognition

---

# Limitations

- Sensitive to lighting (some methods)
- Noise can affect detection
- Computational cost (SIFT/SURF)
- Scale issues in basic corner detectors

---

# Real-World Applications

## Self Driving Cars

Road signs

Lane markers

Vehicles

---

## Face Recognition

Eyes

Nose

Corners

---

## Augmented Reality

Track marker points

---

## Medical Imaging

Feature matching between scans

---

## Satellite Images

Building detection

Road matching

---

## Robotics

Localization

SLAM

Navigation

---

# Summary

Feature detection is one of the core building blocks of Computer Vision.

This module covered:

- Harris Corner Detection
- Shi-Tomasi Corner Detection
- FAST
- ORB
- SIFT
- SURF
- BRISK

Corner detectors identify important image locations, while feature detectors such as ORB, SIFT, SURF, and BRISK also generate descriptors that enable robust feature matching between images. Choosing the right algorithm depends on the application's requirements for speed, accuracy, scale invariance, rotation invariance, and computational resources.

---

# Key Takeaways

- Harris detects corners using image gradients.
- Shi-Tomasi improves Harris by using minimum eigenvalues.
- FAST is optimized for high-speed corner detection.
- ORB combines FAST with BRIEF descriptors for efficient matching.
- SIFT provides highly distinctive, scale- and rotation-invariant features.
- SURF accelerates SIFT using integral images and Hessian approximation.
- BRISK offers binary descriptors with scale and rotation invariance for real-time applications.
- Descriptors allow reliable feature matching across different images.

---
Reference Link : https://www.geeksforgeeks.org/python/feature-detection-and-matching-with-opencv-python/

---