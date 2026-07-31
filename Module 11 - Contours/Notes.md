# Module 11 - Contours

# Introduction

Contours are one of the most useful features in OpenCV for detecting and analyzing the shape of objects in an image. A contour is a curve joining all the continuous points having the same color or intensity. In simple words, contours represent the boundaries of objects.

Contours are usually detected from binary images where the object is white (foreground) and the background is black.

OpenCV provides many functions to find, draw, and analyze contours, making them useful for object detection, shape analysis, image segmentation, and computer vision applications.

---

# What is a Contour?

A contour is a sequence of connected points that forms the outline or boundary of an object.

Example:

```
Original Object

   ########
  #        #
 #          #
 #          #
  #        #
   ########

Contour

************
*          *
*          *
************
```

The contour follows the outer boundary of the object.

---

# Why Use Contours?

Contours provide useful information about objects in an image.

Applications include:

- Object Detection
- Shape Recognition
- Image Segmentation
- Motion Detection
- Medical Image Analysis
- Industrial Inspection
- Counting Objects
- Gesture Recognition
- OCR (Optical Character Recognition)

---

# Steps for Finding Contours

A typical contour detection pipeline is:

```
Input Image
      │
      ▼
Convert to Grayscale
      │
      ▼
Apply Threshold or Canny
      │
      ▼
Find Contours
      │
      ▼
Analyze Contours
```

---

# Binary Image Requirement

Contours work best on binary images.

Example:

Original Image

```
████████████
██      ████
██      ████
████████████
```

Thresholded Image

```
111111111111
110000001111
110000001111
111111111111
```

White pixels represent the object.

---

# 1. Find Contours

## Introduction

The `cv2.findContours()` function detects object boundaries in a binary image.

---

## Syntax

```python
contours, hierarchy = cv2.findContours(
    image,
    mode,
    method
)
```

---

## Parameters

### image

Binary image.

Usually obtained after:

- Thresholding
- Canny Edge Detection

---

### mode

Determines which contours are retrieved.

Common modes:

### RETR_EXTERNAL

Retrieves only the outermost contours.

```
Object

*******
* *** *
* *** *
*******

Result

Only Outer Boundary
```

---

### RETR_LIST

Returns all contours.

No parent-child relationship.

---

### RETR_TREE

Returns all contours with complete hierarchy.

Useful for nested objects.

---

### RETR_CCOMP

Returns contours in two levels.

---

## method

Specifies contour approximation.

### CHAIN_APPROX_NONE

Stores every contour point.

Large memory usage.

---

### CHAIN_APPROX_SIMPLE

Stores only important points.

Reduces memory significantly.

Preferred in most applications.

---

# Output

The function returns

```
contours
```

List containing contour points.

and

```
hierarchy
```

Relationship between contours.

---

# 2. Draw Contours

## Introduction

Detected contours can be drawn on an image.

---

## Syntax

```python
cv2.drawContours(
    image,
    contours,
    contourIndex,
    color,
    thickness
)
```

---

## Parameters

### image

Original image.

---

### contours

Contours returned by `findContours()`.

---

### contourIndex

```
-1
```

Draw all contours.

```
0
```

Draw only first contour.

---

### color

Example

```python
(0,255,0)
```

Green contour.

---

### thickness

Example

```python
2
```

Line thickness.

---

## Example

Original

```
██████████

██      ██

██      ██

██████████
```

After Drawing

```
**********

*        *

*        *

**********
```

---

# 3. Contour Area

## Introduction

Contour area measures the total number of pixels enclosed by a contour.

It is useful for:

- Removing small objects
- Filtering noise
- Object size measurement

---

## Syntax

```python
cv2.contourArea(contour)
```

---

## Example

Rectangle

```
Width = 100

Height = 50

Area

100 × 50

=

5000 pixels²
```

---

## Applications

- Detect largest object
- Remove noise
- Count object sizes

---

# 4. Contour Perimeter

## Introduction

Perimeter is the total boundary length of a contour.

Also called Arc Length.

---

## Syntax

```python
cv2.arcLength(
    contour,
    True
)
```

---

## Parameters

```
True
```

Closed contour.

```
False
```

Open contour.

---

## Example

Rectangle

```
100 × 50

Perimeter

2 × (100+50)

=

300 pixels
```

---

## Applications

- Shape matching
- Polygon approximation
- Object measurement

---

# 5. Image Moments

## Introduction

Image moments are statistical values calculated from contour pixels.

Moments help calculate:

- Area
- Center (Centroid)
- Orientation
- Shape properties

---

## Syntax

```python
M = cv2.moments(contour)
```

---

## Common Moments

```
M["m00"]
```

Area

---

```
M["m10"]
```

X Moment

---

```
M["m01"]
```

Y Moment

---

## Centroid Formula

```
Center X

Cx = M10 / M00

Center Y

Cy = M01 / M00
```

---

## Example

Object

```
*******
*     *
*     *
*******
```

Center

```
    X
```

The centroid represents the object's center.

---

## Applications

- Object Tracking
- Robot Navigation
- Shape Recognition
- Motion Detection

---

# 6. Convex Hull

## Introduction

A Convex Hull is the smallest convex boundary that completely encloses a contour.

Imagine stretching a rubber band around an object.

The rubber band forms the convex hull.

---

## Example

Original Shape

```
      *

   *     *

 *         *

     *

```

Convex Hull

```
***********

*         *

*         *

***********
```

The hull removes inward dents.

---

## Syntax

```python
cv2.convexHull(contour)
```

---

## Applications

- Shape Analysis
- Finger Detection
- Gesture Recognition
- Object Recognition
- Defect Detection

---

# Convex Hull vs Contour

| Contour | Convex Hull |
|----------|-------------|
| Exact object boundary | Smallest convex boundary |
| Can contain inward curves | No inward curves |
| Represents original shape | Represents convex shape |

---

# Contour Hierarchy

Hierarchy explains the relationship between contours.

Example

```
Outer Circle

   ********

   *      *

   * **** *

   * **** *

   *      *

   ********
```

The inner contour becomes the child of the outer contour.

---

# Complete Contour Workflow

```
Read Image
      │
      ▼
Convert to Grayscale
      │
      ▼
Threshold / Canny
      │
      ▼
Find Contours
      │
      ▼
Draw Contours
      │
      ▼
Calculate Area
      │
      ▼
Calculate Perimeter
      │
      ▼
Find Moments
      │
      ▼
Find Convex Hull
```

---

# Applications of Contours

- Object Detection
- Shape Recognition
- Face Detection
- Fingerprint Analysis
- Medical Imaging
- Robotics
- OCR
- Industrial Quality Inspection
- Coin Counting
- Traffic Sign Detection
- Gesture Recognition
- License Plate Detection
- Cell Detection
- Fruit Sorting

---

# Best Practices

- Convert the image to grayscale before contour detection.
- Apply thresholding or Canny edge detection to create a binary image.
- Remove noise using Gaussian Blur or morphological operations.
- Use `RETR_EXTERNAL` when only outer boundaries are required.
- Use `CHAIN_APPROX_SIMPLE` to reduce memory usage.
- Filter contours by area to ignore small noisy regions.
- Use image moments to find the centroid of detected objects.
- Apply a convex hull for shape analysis and defect detection.

---

# Summary

Contours represent the boundaries of objects in an image and are essential for shape analysis in OpenCV. Using `findContours()`, we can detect object outlines from binary images. `drawContours()` visualizes the detected boundaries, while `contourArea()` and `arcLength()` measure the size and perimeter of objects. Image moments help determine properties such as the centroid, and `convexHull()` creates the smallest convex boundary enclosing a contour. Together, these techniques form the foundation for object detection, tracking, and many computer vision applications.

---

# Key Takeaways

- A contour is the boundary or outline of an object.
- Contours are usually detected from binary images.
- `findContours()` extracts object boundaries.
- `drawContours()` displays contour outlines.
- `contourArea()` calculates the enclosed area.
- `arcLength()` calculates the contour perimeter.
- `moments()` computes geometric properties like the centroid.
- `convexHull()` creates the smallest convex boundary around an object.
- Contours are widely used for object detection, tracking, measurement, and shape analysis in computer vision.

---
Reference Link : https://www.geeksforgeeks.org/computer-vision/what-are-contours-in-computer-vision/

---