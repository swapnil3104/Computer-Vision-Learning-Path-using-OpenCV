# Module 5 - Color Spaces

## Learning Objectives

After completing this module, you will be able to:

- Understand what a color space is.
- Learn the differences between BGR, RGB, HSV, LAB, YCrCb, and Grayscale.
- Convert images between different color spaces using OpenCV.
- Select the appropriate color space for various computer vision applications.
- Perform color-based image processing.

---

# What is a Color Space?

A **Color Space** is a mathematical model that represents colors using numerical values.

Different color spaces are designed for different purposes such as:

- Image display
- Image editing
- Object detection
- Image segmentation
- Face detection
- Compression
- Medical imaging

Every pixel in an image stores color information according to a particular color space.

---

## Why Do We Need Different Color Spaces?

Imagine trying to identify a red apple.

Using RGB values directly may be difficult because lighting changes affect RGB values significantly.

Instead, using HSV allows us to identify the red color regardless of brightness.

Different color spaces solve different problems.

| Application | Best Color Space |
|-------------|------------------|
| Display Images | RGB |
| OpenCV Processing | BGR |
| Object Detection | HSV |
| Face Detection | YCrCb |
| Image Enhancement | LAB |
| Edge Detection | Grayscale |

---

# Overview of Color Spaces

| Color Space | Channels | Main Purpose |
|-------------|----------|--------------|
| BGR | Blue Green Red | Default OpenCV Format |
| RGB | Red Green Blue | Image Display |
| HSV | Hue Saturation Value | Color Detection |
| LAB | Lightness A B | Color Correction |
| YCrCb | Luminance Chrominance | Face Detection |
| Grayscale | Intensity | Image Processing |

---

# 1. BGR Color Space

## Introduction

BGR stands for:

- Blue
- Green
- Red

Unlike most software libraries, **OpenCV stores images in BGR format by default.**

This means every pixel stores colors in this order:

Blue → Green → Red

Example:

```
Pixel = [255, 0, 0]
```

This represents:

Blue = 255

Green = 0

Red = 0

Result:

Blue Color

---

## Channel Order

```
[B, G, R]
```

Example:

```
[255,255,255]
```

White

```
[0,0,0]
```

Black

```
[0,0,255]
```

Red

```
[0,255,0]
```

Green

```
[255,0,0]
```

Blue

---

## OpenCV Example

```python
import cv2

image = cv2.imread("sample.jpg")

print(image[100,100])
```

Output

```
[145 182 210]
```

Meaning

```
Blue =145
Green=182
Red=210
```

---

## Advantages

- Default format in OpenCV
- Faster processing
- No conversion required

---

## Disadvantages

- Not suitable for displaying using Matplotlib
- Human-readable order is different

---

# 2. RGB Color Space

## Introduction

RGB stands for

- Red
- Green
- Blue

RGB is the most commonly used color space for

- Displays
- Cameras
- Websites
- Mobile Apps
- Photoshop

Each pixel contains

```
[R,G,B]
```
---
## RGB 

![RGB](images\rgb.png)
---

## Example

```
[255,0,0]
```

Red

```
[0,255,0]
```

Green

```
[0,0,255]
```

Blue

---

## Convert BGR to RGB

```python
import cv2

image=cv2.imread("sample.jpg")

rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
```

---

## Display using Matplotlib

```python
import cv2
import matplotlib.pyplot as plt

image=cv2.imread("sample.jpg")

rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

plt.imshow(rgb)
plt.axis("off")
plt.show()
```

---

## Why Convert?

OpenCV

```
BGR
```

Matplotlib

```
RGB
```

Without conversion, colors appear incorrect.

---

# 3. HSV Color Space

## Introduction

HSV stands for

- Hue
- Saturation
- Value

HSV separates color information from brightness.

This makes color detection much easier.

---

## Components

### Hue

Represents the actual color.

Example

- Red
- Green
- Blue
- Yellow

OpenCV Hue Range

```
0–179
```

---

### Saturation

Represents color purity.

Low Saturation -> Gray color

High Saturation -> Pure color

Range

```
0-255
```

---

### Value

Represents brightness.

Low Value -> Dark

High Value -> Bright

Range

```
0-255
```

---

## HSV Diagram

```
Hue
↓

Color

Saturation
↓

Purity

Value
↓

Brightness
```
---
## HSV

![HSV](images\hsv.png)
---

## Convert to HSV

```python
import cv2

image=cv2.imread("sample.jpg")

hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
```

---

## Color Detection Example

Detect Blue Objects

```python
import cv2
import numpy as np

image=cv2.imread("sample.jpg")

hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

lower=np.array([100,150,0])
upper=np.array([140,255,255])

mask=cv2.inRange(hsv,lower,upper)

cv2.imshow("Mask",mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

## Applications

- Object Detection
- Color Tracking
- Traffic Sign Detection
- Fruit Detection
- Ball Tracking

---

# 4. LAB Color Space

## Introduction

LAB consists of

- L = Lightness
- A = Green ↔ Red
- B = Blue ↔ Yellow

Unlike RGB, brightness is stored separately.

---

## Components

### L

Brightness

Range

```
0-255
```

---

### A

Green to Red

Negative -> Green

Positive -> Red

---

### B

Blue to Yellow

Negative -> Blue

Positive -> Yellow

---
## LAB

![LAB](images\lab.jpg)

---

## Convert to LAB

```python
import cv2

image=cv2.imread("sample.jpg")

lab=cv2.cvtColor(image,cv2.COLOR_BGR2LAB)
```

---

## Advantages

- Better illumination handling
- Excellent for color correction
- Widely used in image enhancement

---

## Applications

- Medical Imaging
- Image Enhancement
- Skin Detection
- Color Matching

---

# 5. YCrCb Color Space

## Introduction

YCrCb separates brightness from color.

Components

- Y
- Cr
- Cb

---

## Meaning

### Y

Brightness

### Cr

Red Difference

### Cb

Blue Difference

---
## LAB

![YCRCB](images\YCbCr.png)

---

## Convert

```python
import cv2

image=cv2.imread("sample.jpg")

ycrcb=cv2.cvtColor(image,cv2.COLOR_BGR2YCrCb)
```

---

## Applications

- Face Detection
- Skin Detection
- JPEG Compression
- Video Compression

---

# 6. Grayscale

## Introduction

Grayscale images contain only intensity values.

No color information exists.

Each pixel has only one value.

Range

```
0-255
```

---

## Example

```
0
```

Black

```
255
```

White

```
128
```

Gray

---

## Convert

```python
import cv2

image=cv2.imread("sample.jpg")

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
```

---

## Advantages

- Faster Processing
- Less Memory
- Better for Edge Detection

---

## Applications

- OCR
- Face Detection
- Thresholding
- Contour Detection
- Edge Detection

---

# Conversion Table

| From | To | OpenCV Code |
|-------|----|-------------|
| BGR | RGB | cv2.COLOR_BGR2RGB |
| RGB | BGR | cv2.COLOR_RGB2BGR |
| BGR | HSV | cv2.COLOR_BGR2HSV |
| HSV | BGR | cv2.COLOR_HSV2BGR |
| BGR | LAB | cv2.COLOR_BGR2LAB |
| LAB | BGR | cv2.COLOR_LAB2BGR |
| BGR | YCrCb | cv2.COLOR_BGR2YCrCb |
| YCrCb | BGR | cv2.COLOR_YCrCb2BGR |
| BGR | Gray | cv2.COLOR_BGR2GRAY |
| Gray | BGR | cv2.COLOR_GRAY2BGR |

---

# Complete Example

```python
import cv2

image = cv2.imread("sample.jpg")

rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original (BGR)", image)
cv2.imshow("HSV", hsv)
cv2.imshow("LAB", lab)
cv2.imshow("YCrCb", ycrcb)
cv2.imshow("Gray", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

# Real-World Applications

| Industry | Color Space Used |
|----------|------------------|
| Medical Imaging | LAB |
| Autonomous Vehicles | HSV |
| Face Recognition | YCrCb |
| Traffic Sign Detection | HSV |
| Image Editing | RGB |
| CCTV Analytics | Grayscale |
| OCR Systems | Grayscale |
| Satellite Imaging | LAB |

---

# Comparison Table

| Feature | BGR | RGB | HSV | LAB | YCrCb | Gray |
|----------|-----|-----|-----|------|--------|------|
| Channels | 3 | 3 | 3 | 3 | 3 | 1 |
| Brightness Separate | No | No | Yes | Yes | Yes | Only Brightness |
| Human Friendly | No | Yes | Yes | Moderate | Moderate | Yes |
| Object Detection | Poor | Poor | Excellent | Good | Good | No |
| Face Detection | Fair | Fair | Good | Good | Excellent | Fair |
| Image Enhancement | Fair | Fair | Good | Excellent | Good | Limited |
| Memory Usage | Medium | Medium | Medium | Medium | Medium | Low |

---

# Summary

- **BGR** is the default color space in OpenCV.
- **RGB** is mainly used for displaying images on screens and with Matplotlib.
- **HSV** separates color from brightness, making it ideal for color-based object detection.
- **LAB** separates lightness from color information and is widely used for image enhancement and color correction.
- **YCrCb** separates luminance from chrominance and is commonly used for face detection and image/video compression.
- **Grayscale** contains only intensity values, reducing memory usage and speeding up many computer vision tasks.

Choosing the right color space depends on the application:
- Use **BGR** for general OpenCV processing.
- Use **RGB** for visualization.
- Use **HSV** for color segmentation and tracking.
- Use **LAB** for enhancement under varying lighting conditions.
- Use **YCrCb** for skin and face detection.
- Use **Grayscale** for edge detection, thresholding, OCR, and other intensity-based operations.

---

Reference Link : https://www.geeksforgeeks.org/computer-graphics/difference-between-rgb-cmyk-hsv-and-yiq-color-models/

---