# Module 3 - Image Manipulation

Image manipulation is one of the most important tasks in Computer Vision. It involves modifying an image to improve its appearance, extract useful information, or prepare it for further processing.

OpenCV provides many built-in functions for manipulating images such as resizing, cropping, rotating, flipping, translating, and scaling.

---

# Learning Objectives

After completing this module, you will be able to:

- Resize images without losing quality
- Crop a specific region from an image
- Rotate images at different angles
- Flip images horizontally and vertically
- Translate (move) images
- Understand image scaling
- Maintain the correct aspect ratio

---

# What is Image Manipulation?

Image manipulation refers to changing the appearance or geometry of an image.

Examples include:

- Making an image smaller
- Enlarging an image
- Rotating an image
- Cropping unwanted areas
- Flipping an image
- Moving an image left or right

Image manipulation is widely used in:

- Image preprocessing
- Machine Learning
- Object Detection
- Face Recognition
- Medical Imaging
- Image Augmentation

---

# Original Image

Suppose our original image has

Width = 800 pixels

Height = 600 pixels

```
+-----------------------------+
|                             |
|                             |
|         Original            |
|                             |
|                             |
+-----------------------------+

Width = 800
Height = 600
```

---

# 1. Resize Image

## What is Resizing?

Resizing changes the dimensions (width and height) of an image.

The image can be:

- Enlarged
- Reduced

---

## Why Resize Images?

Resizing is useful because:

- Deep Learning models require fixed image sizes.
- Reduces memory usage.
- Speeds up processing.
- Fits images on screens.

---

## Example

Original

```
800 × 600
```

Resize to

```
400 × 300
```

```
Before

+-------------------------+
|                         |
|                         |
|                         |
+-------------------------+

800 x 600


After

+-------------+
|             |
|             |
+-------------+

400 x 300
```

---

## OpenCV Function

```python
cv2.resize()
```

---

## Important Parameters

| Parameter | Description |
|------------|-------------|
| image | Input image |
| dsize | New size (width,height) |
| fx | Horizontal scale |
| fy | Vertical scale |
| interpolation | Resizing method |

---

## Common Interpolation Methods

### INTER_LINEAR

Default method.

Best for enlarging images.

---

### INTER_AREA

Best for shrinking images.

Produces smoother results.

---

### INTER_CUBIC

Uses neighboring pixels.

Produces high-quality enlarged images.

---

### INTER_LANCZOS4

Highest quality.

Slow but excellent for enlargements.

---

# 2. Crop Image

## What is Cropping?

Cropping removes unwanted portions of an image.

Only a selected region remains.

---

## Example

Original

```
+----------------------+
|                      |
|   Crop this area     |
|      +------+        |
|      |      |        |
|      |      |        |
|      +------+        |
|                      |
+----------------------+
```

After Crop

```
+------+
|      |
|      |
|      |
+------+
```

---

## Why Crop?

- Remove unnecessary background
- Focus on object
- Face detection
- ROI (Region of Interest)

---

## OpenCV Method

Unlike resizing,

Cropping is performed using NumPy slicing.

Example concept:

```
image[y1:y2, x1:x2]
```

---

## Region of Interest (ROI)

ROI means selecting only a useful part of the image.

Example:

```
Entire Image

+-------------------------+
|                         |
|     +-----------+       |
|     |   ROI     |       |
|     +-----------+       |
|                         |
+-------------------------+
```

---

# 3. Rotate Image

## What is Rotation?

Rotation changes the orientation of an image.

Common rotations:

- 90°
- 180°
- 270°
- Custom angle

---

Example

Original

```
A
B
C
```

Rotate 90°

```
C B A
```

---

Rotate 180°

```
C
B
A
```

---

## Why Rotate Images?

- Correct camera orientation
- Data augmentation
- Medical imaging
- OCR preprocessing

---

## OpenCV Functions

```
cv2.rotate()

cv2.getRotationMatrix2D()

cv2.warpAffine()
```

---

## Rotation Matrix

Rotation uses

```
Center
Angle
Scale
```

---

# 4. Flip Image

## What is Flipping?

Flipping creates a mirror image.

---

There are three types.

---

## Horizontal Flip

```
Original

ABCDEF

Horizontal

FEDCBA
```

Mirror across vertical axis.

---

## Vertical Flip

```
Original

A
B
C

Vertical

C
B
A
```

Mirror across horizontal axis.

---

## Both Directions

Image is flipped horizontally and vertically.

Equivalent to rotating 180° in many cases.

---

## OpenCV Function

```
cv2.flip()
```

---

## Flip Codes

| Flip Code | Meaning |
|------------|----------|
| 0 | Vertical |
| 1 | Horizontal |
| -1 | Both |

---

# 5. Translate Image

## What is Translation?

Translation moves an image from one location to another.

The image content does not rotate.

It only shifts.

---

Example

Original

```
+---------------+
|      X        |
|               |
+---------------+
```

Move Right

```
+---------------+
|          X    |
|               |
+---------------+
```

Move Down

```
+---------------+
|               |
|      X        |
+---------------+
```

---

## Translation Directions

Move

- Left
- Right
- Up
- Down

---

## Applications

- Image alignment
- Data augmentation
- Object tracking
- Motion simulation

---

## OpenCV Functions

```
cv2.warpAffine()
```

Uses Translation Matrix.

---

## Translation Matrix

```
|1 0 tx|
|0 1 ty|
```

Where

tx = shift along X

ty = shift along Y

---

# 6. Scale Image

Scaling changes image size by multiplying dimensions with a factor.

---

Example

Scale = 2

```
100 × 100

↓

200 × 200
```

---

Scale = 0.5

```
100 × 100

↓

50 × 50
```

---

## Types of Scaling

### Upscaling

Increase image size.

```
100 × 100

↓

300 × 300
```

---

### Downscaling

Reduce image size.

```
300 × 300

↓

100 × 100
```

---

## Scaling Factors

```
fx = Horizontal Scale

fy = Vertical Scale
```

Example

```
fx = 2

fy = 2
```

Image becomes twice as large.

---

# 7. Aspect Ratio

## What is Aspect Ratio?

Aspect ratio is the relationship between width and height.

Formula

```
Aspect Ratio

=

Width / Height
```

---

Example

```
1920 × 1080

Aspect Ratio

16 : 9
```

---

Example

```
1024 × 768

Aspect Ratio

4 : 3
```

---

## Why Maintain Aspect Ratio?

Maintaining aspect ratio prevents image distortion.

Correct

```
+-------------+
|             |
|             |
+-------------+
```

Incorrect

```
+-----------------------+
|                       |
+-----------------------+
```

Image appears stretched.

---

## Common Aspect Ratios

| Resolution | Ratio |
|------------|-------|
| 1920×1080 | 16:9 |
| 1280×720 | 16:9 |
| 1024×768 | 4:3 |
| 800×800 | 1:1 |
| 1080×1350 | 4:5 |

---

# Image Manipulation Workflow

```
Read Image
      │
      ▼
Resize
      │
      ▼
Crop
      │
      ▼
Rotate
      │
      ▼
Flip
      │
      ▼
Translate
      │
      ▼
Scale
      │
      ▼
Save Image
```

---

# Summary

| Operation | Purpose |
|------------|----------|
| Resize | Change width and height |
| Crop | Extract selected area |
| Rotate | Change orientation |
| Flip | Mirror image |
| Translate | Move image |
| Scale | Increase or decrease size |
| Aspect Ratio | Maintain image proportions |

---

# Key Takeaways

- Resize changes image dimensions.
- Crop extracts only useful regions.
- Rotation changes image orientation.
- Flip creates mirror images.
- Translation shifts image position.
- Scaling enlarges or shrinks images.
- Maintaining aspect ratio prevents distortion.
- These operations are fundamental in Computer Vision, Deep Learning, and Image Processing.

---