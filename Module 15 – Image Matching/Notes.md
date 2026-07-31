# Module 15 - Image Matching

## Introduction

Image Matching is one of the most important concepts in Computer Vision. It is used to determine whether two images contain the same object or to locate a smaller image inside a larger image.

Image matching techniques are widely used in:

- Object Detection
- Face Recognition
- Image Registration
- Robot Navigation
- Panorama Stitching
- Medical Imaging
- OCR Systems
- Industrial Inspection
- Augmented Reality

OpenCV provides two major image matching approaches:

1. Template Matching
2. Feature Matching

---

# 1. Template Matching

## Definition

Template Matching is a technique used to locate a small image (called a **template**) inside a larger image.

OpenCV slides the template across the source image and calculates how similar the template is at every location.

The location with the highest similarity is considered the best match.

---

## Working Principle

Suppose:

- Large Image = Scene
- Small Image = Template

The algorithm performs:

1. Place template at top-left corner.
2. Compare template pixels with image pixels.
3. Compute similarity score.
4. Move template one pixel.
5. Repeat until the entire image is scanned.
6. Return the best matching position.

---

## Syntax

```python
result = cv2.matchTemplate(image, template, method)
```

---

## Parameters

| Parameter | Description |
|------------|-------------|
| image | Original image |
| template | Small image to search |
| method | Matching algorithm |

---

## Matching Methods

| Method | Description |
|---------|-------------|
| TM_CCOEFF | Correlation coefficient |
| TM_CCOEFF_NORMED | Normalized correlation coefficient |
| TM_CCORR | Cross correlation |
| TM_CCORR_NORMED | Normalized cross correlation |
| TM_SQDIFF | Squared difference |
| TM_SQDIFF_NORMED | Normalized squared difference |

---

## Best Methods

Usually used:

- TM_CCOEFF_NORMED
- TM_CCORR_NORMED

For SQDIFF methods:

Lowest value = Best Match

For all other methods:

Highest value = Best Match

---

## Advantages

- Easy to implement
- Fast
- Accurate for identical images

---

## Disadvantages

Template Matching fails when:

- Object rotates
- Object changes scale
- Illumination changes
- Perspective changes
- Occlusion occurs

---

## Applications

- Logo Detection
- QR Code Detection
- UI Automation
- Industrial Inspection
- PCB Component Detection

---
Reference : https://www.geeksforgeeks.org/python/template-matching-using-opencv-in-python/
---

# 2. Feature Matching

## Definition

Feature Matching compares two images using unique keypoints instead of comparing every pixel.

Instead of using pixel values, Feature Matching detects important points like:

- Corners
- Edges
- Blobs
- Texture

Then it compares these features between images.

---

## Workflow

Image A

↓

Detect Keypoints

↓

Compute Descriptors

↓

Detect Keypoints in Image B

↓

Compute Descriptors

↓

Match Descriptors

↓

Filter Good Matches

↓

Display Matches

---

## Components

Feature Matching has two major parts.

### Step 1

Feature Detector

Examples:

- SIFT
- SURF
- ORB
- BRISK
- FAST

---

### Step 2

Descriptor Matcher

Examples:

- BFMatcher
- FLANN

---

## Advantages

- Rotation invariant
- Scale invariant
- Robust to lighting changes
- Works for different viewpoints

---

## Applications

- Object Recognition
- Panorama Stitching
- Image Registration
- AR Applications
- Visual SLAM
---
Reference : https://www.geeksforgeeks.org/computer-vision/feature-matching-in-computer-vision-techniques-and-applications/
---

# 3. BFMatcher (Brute Force Matcher)

## Definition

BFMatcher compares every descriptor from the first image with every descriptor from the second image.

It chooses the closest descriptor using a distance metric.

It is called **Brute Force** because it checks all possibilities.

---

## Working

Descriptor A

↓

Compare with Descriptor 1

↓

Compare with Descriptor 2

↓

Compare with Descriptor 3

↓

...

↓

Select minimum distance

---

## Distance Metrics

### NORM_L2

Used for:

- SIFT
- SURF

Measures Euclidean distance.

---

### NORM_HAMMING

Used for:

- ORB
- BRISK
- BRIEF

Measures Hamming distance.

---

## Syntax

```python
bf = cv2.BFMatcher()
matches = bf.match(desc1, desc2)
```

---

## Cross Check

```python
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
```

Cross Check improves matching quality.

---

## Advantages

- Simple
- Accurate
- Easy to understand

---

## Disadvantages

- Slow
- Compares every descriptor
- Not suitable for huge datasets

---

# 4. FLANN Matcher

## Definition

FLANN stands for:

**Fast Library for Approximate Nearest Neighbors**

Instead of checking every descriptor, FLANN uses optimized search structures.

It is much faster for large datasets.

---

## Working

Descriptors

↓

Build Search Tree

↓

Nearest Neighbor Search

↓

Approximate Best Match

---

## Algorithms Used

For floating descriptors:

- KD Tree

For binary descriptors:

- LSH

---

## Syntax

```python
matcher = cv2.FlannBasedMatcher(index_params, search_params)
```

---

## Parameters

### index_params

Defines indexing algorithm.

Example:

```python
index_params = dict(
    algorithm=1,
    trees=5
)
```

---

### search_params

Controls search quality.

```python
search_params = dict(checks=50)
```

---

## Ratio Test

David Lowe proposed Ratio Test.

Instead of taking one nearest match:

Take two nearest matches.

Accept match only if:

Distance(first) < 0.75 × Distance(second)

This removes false matches.

---

## Advantages

- Very fast
- Excellent for large datasets
- More scalable than BFMatcher

---

## Disadvantages

- More difficult to configure
- Approximate matching
- Small accuracy tradeoff

---

# BFMatcher vs FLANN

| Feature | BFMatcher | FLANN |
|----------|-----------|--------|
| Speed | Slow | Fast |
| Accuracy | High | Very High |
| Large Dataset | Poor | Excellent |
| Complexity | Simple | Moderate |
| Search Type | Exact | Approximate |
| Memory | Low | Moderate |

---

# Template Matching vs Feature Matching

| Feature | Template Matching | Feature Matching |
|----------|------------------|------------------|
| Rotation | No | Yes |
| Scale Change | No | Yes |
| Illumination Change | Poor | Good |
| Occlusion | Poor | Good |
| Speed | Fast | Moderate |
| Robustness | Low | High |
| Accuracy | High (same object) | High (different views) |

---

# Complete Image Matching Pipeline

Input Images

↓

Preprocessing

↓

Feature Detection

↓

Descriptor Extraction

↓

Descriptor Matching

↓

Filter Good Matches

↓

Draw Matches

↓

Object Localization

---

# Real-World Applications

## Face Recognition

Compare facial features.

---

## Fingerprint Matching

Compare fingerprint minutiae.

---

## Panorama Stitching

Find overlapping regions.

---

## Mobile Visual Search

Match products using camera images.

---

## Industrial Inspection

Detect defective products.

---

## Medical Imaging

Register MRI and CT scans.

---

## Robot Navigation

Match landmarks for localization.

---

# Summary

- Template Matching compares pixels directly.
- Feature Matching compares keypoints and descriptors.
- BFMatcher performs exhaustive descriptor comparison.
- FLANN performs fast approximate nearest-neighbor search.
- Feature Matching is robust to rotation, scale, and illumination changes, making it suitable for real-world computer vision tasks.