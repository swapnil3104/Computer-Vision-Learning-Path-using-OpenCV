# Module 8 - Thresholding

## Learning Objectives

After completing this module, you will be able to:

- Understand the concept of image thresholding.
- Convert grayscale images into binary images.
- Apply Binary Thresholding.
- Apply Inverse Thresholding.
- Use Adaptive Thresholding for uneven lighting.
- Use Otsu's Thresholding for automatic threshold selection.
- Choose the correct thresholding technique for different applications.

---

# What is Thresholding?

Thresholding is an image segmentation technique used to separate objects from the background by converting a grayscale image into a binary (black and white) image.

Instead of having multiple intensity values (0–255), the output image contains only two values:

- **0 (Black)**
- **255 (White)**

Thresholding is one of the simplest and most widely used image processing techniques.

---

# Why Do We Need Thresholding?

Many computer vision tasks require identifying objects separately from the background.

Thresholding helps:

- Separate foreground from background
- Detect text in documents
- Detect shapes
- Prepare images for OCR
- Count objects
- Detect defects
- Segment medical images

---

# Prerequisite

Thresholding works best on **Grayscale Images**.

A color image should first be converted to grayscale.

```python
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```

---

# Understanding Pixel Intensities

Grayscale images contain pixel values from:

| Pixel Value | Meaning |
|-------------|----------|
| 0 | Black |
| 50 | Dark Gray |
| 128 | Gray |
| 200 | Light Gray |
| 255 | White |

Thresholding decides whether a pixel becomes black or white based on a threshold value.

---
# Types of Thresholding in Image Processing

Thresholding is a segmentation technique that converts a grayscale or color image into a binary or segmented image by comparing pixel values with one or more threshold values.

Different thresholding methods are suitable for different lighting conditions, image types, and applications.

---

# 1. Simple Thresholding (Binary Thresholding)

## Definition

Simple Thresholding uses a **single fixed threshold value** for the entire image.

Each pixel is compared with this threshold.

If the pixel value is greater than the threshold, it is assigned one value (usually white). Otherwise, it is assigned another value (usually black).

---

## Formula

```
If Pixel > Threshold

Output = 255

Else

Output = 0
```

---

## OpenCV Function

```python
ret, thresh = cv2.threshold(
    gray,
    127,
    255,
    cv2.THRESH_BINARY
)
```

---

## Advantages

- Fast
- Easy to implement
- Suitable for images with uniform lighting

---

## Disadvantages

- Does not work well under uneven lighting
- Threshold value must be selected manually

---

## Applications

- Barcode detection
- Shape detection
- Basic object segmentation
- Document preprocessing

---

# 2. Adaptive Thresholding

## Definition

Adaptive Thresholding calculates a different threshold value for every small region of the image instead of using one global value.

This makes it effective for images with shadows or uneven illumination.

---

## Types

### Adaptive Mean Threshold

Uses the average intensity of neighboring pixels.

```python
cv2.ADAPTIVE_THRESH_MEAN_C
```

---

### Adaptive Gaussian Threshold

Uses a weighted Gaussian average of neighboring pixels.

```python
cv2.ADAPTIVE_THRESH_GAUSSIAN_C
```

---

## OpenCV Function

```python
adaptive = cv2.adaptiveThreshold(
    gray,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    11,
    2
)
```

---

## Advantages

- Excellent for uneven lighting
- Handles shadows effectively
- Produces better segmentation

---

## Disadvantages

- Slower than simple thresholding
- Requires tuning parameters

---

## Applications

- OCR
- Document scanning
- Sudoku solving
- License plate recognition

---

# 3. Otsu's Thresholding

## Definition

Otsu's Thresholding automatically determines the optimal threshold value by analyzing the image histogram.

The user does not specify the threshold manually.

---

## OpenCV Function

```python
ret, otsu = cv2.threshold(
    gray,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)
```

---

## Advantages

- Automatic threshold selection
- No manual tuning
- Effective for bimodal histograms

---

## Disadvantages

- Less effective for uneven lighting
- Sensitive to heavy noise

---

## Applications

- Medical image segmentation
- Industrial inspection
- OCR
- Microscopy

---

# 4. Multilevel Thresholding

## Definition

Multilevel Thresholding uses **multiple threshold values** to divide an image into more than two intensity regions.

Instead of separating the image into only black and white, it creates multiple classes.

Example

```
0–80      → Class 1

81–160    → Class 2

161–255   → Class 3
```

---

## Advantages

- Better segmentation for complex images
- Retains more intensity information

---

## Disadvantages

- Higher computational cost
- More complex implementation

---

## Applications

- Medical imaging
- Satellite image analysis
- Material inspection
- Brain MRI segmentation

---

# 5. Color Thresholding

## Definition

Color Thresholding segments objects based on color rather than grayscale intensity.

It is commonly performed in the HSV color space.

---

## OpenCV Function

```python
mask = cv2.inRange(hsv, lower_color, upper_color)
```

Example

```python
lower_red = np.array([0,120,70])
upper_red = np.array([10,255,255])

mask = cv2.inRange(hsv, lower_red, upper_red)
```

---

## Advantages

- Detects colored objects accurately
- Works well in real-time applications

---

## Disadvantages

- Sensitive to lighting changes
- Requires proper color range selection

---

## Applications

- Traffic sign detection
- Fruit sorting
- Ball tracking
- Object tracking
- Robot vision

---

# 6. Local Thresholding

## Definition

Local Thresholding divides the image into small regions and computes a threshold for each region individually.

Unlike adaptive thresholding, different local thresholding algorithms (such as Niblack, Sauvola, and Bernsen) use different statistical methods.

---

## Common Algorithms

- Niblack Thresholding
- Sauvola Thresholding
- Bernsen Thresholding

---

## Advantages

- Works well for documents
- Handles uneven backgrounds

---

## Disadvantages

- Computationally expensive
- More parameters to tune

---

## Applications

- Historical document restoration
- OCR
- Medical image analysis

---

# 7. Global Thresholding

## Definition

Global Thresholding uses one threshold value for the entire image.

Binary Thresholding is the most common example of global thresholding.

---

## Formula

```
Single Threshold

↓

Entire Image

↓

Binary Output
```

---

## Advantages

- Very fast
- Simple implementation

---

## Disadvantages

- Poor performance under varying illumination

---

## Applications

- Controlled environments
- Industrial automation
- Machine vision

---

# 8. Iterative Thresholding

## Definition

Iterative Thresholding automatically estimates the optimal threshold by repeatedly updating it until convergence.

---

## Algorithm

### Step 1

Choose an initial threshold.

---

### Step 2

Divide pixels into two groups.

- Group A
- Group B

---

### Step 3

Calculate the average intensity of both groups.

---

### Step 4

Compute a new threshold.

```
New Threshold

=

(Mean1 + Mean2)

/

2
```

---

### Step 5

Repeat until the threshold no longer changes.

---

## Advantages

- Automatic threshold estimation
- Better than manually selecting a threshold

---

## Disadvantages

- Slower than binary thresholding
- Multiple iterations required

---

## Applications

- Medical imaging
- Image segmentation
- Object detection

---

# Comparison Table

| Threshold Type | Automatic | Uneven Lighting | Speed | Output Classes |
|----------------|-----------|-----------------|-------|----------------|
| Simple Thresholding | No | Poor | Very Fast | 2 |
| Adaptive Thresholding | Local | Excellent | Medium | 2 |
| Otsu's Thresholding | Yes | Moderate | Fast | 2 |
| Multilevel Thresholding | Depends | Good | Slow | Multiple |
| Color Thresholding | User Defined | Moderate | Fast | Color Mask |
| Local Thresholding | Local | Excellent | Slow | 2 |
| Global Thresholding | No | Poor | Very Fast | 2 |
| Iterative Thresholding | Yes | Good | Medium | 2 |

---

# Which Thresholding Method Should You Use?

| Situation | Recommended Method |
|------------|-------------------|
| Uniform lighting | Simple / Global Thresholding |
| Uneven lighting | Adaptive Thresholding |
| Unknown threshold value | Otsu's Thresholding |
| Multiple intensity regions | Multilevel Thresholding |
| Detect colored objects | Color Thresholding |
| Historical documents | Local Thresholding |
| Automatic threshold estimation | Iterative Thresholding |
| OCR | Adaptive or Otsu Thresholding |

---

# Real-World Applications

- OCR and document scanning
- Medical image segmentation
- Satellite image processing
- Industrial quality inspection
- Face detection preprocessing
- Traffic sign recognition
- Fingerprint recognition
- Autonomous vehicles
- Robot vision
- Object tracking

---

# Summary

Thresholding is one of the most important image segmentation techniques in computer vision.

- **Simple (Global) Thresholding** uses one fixed threshold for the entire image.
- **Adaptive Thresholding** calculates thresholds for local neighborhoods and performs well under uneven lighting.
- **Otsu's Thresholding** automatically computes an optimal threshold using the image histogram.
- **Multilevel Thresholding** divides an image into multiple intensity classes.
- **Color Thresholding** segments objects based on color ranges, usually in the HSV color space.
- **Local Thresholding** computes thresholds for small regions using local image statistics.
- **Global Thresholding** applies a single threshold to the whole image and is best for uniformly illuminated scenes.
- **Iterative Thresholding** repeatedly updates the threshold value until it converges to a stable solution.


Reference Link : https://www.geeksforgeeks.org/python/image-filtering-using-convolution-in-opencv/