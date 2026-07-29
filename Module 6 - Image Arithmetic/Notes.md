# Module 6 - Image Arithmetic

## Learning Objectives

After completing this module, you will be able to:

- Perform arithmetic operations on images.
- Add and subtract images and pixel values.
- Apply bitwise operations for masking and image processing.
- Blend two images together.
- Create transparent image overlays.
- Understand practical applications of image arithmetic.

---

# What is Image Arithmetic?

Image Arithmetic refers to mathematical operations performed on images. Since an image is simply a matrix of pixel values, arithmetic operations can be applied to every pixel.

OpenCV provides several functions to perform these operations efficiently.

Common operations include:

- Addition
- Subtraction
- Multiplication
- Division
- Bitwise AND
- Bitwise OR
- Bitwise XOR
- Bitwise NOT
- Image Blending
- Transparency

---

# Understanding Pixel Values

Each pixel contains intensity values.

Example:

```
RGB Image

Pixel = [120, 50, 200]

Blue = 120
Green = 50
Red = 200
```

Grayscale Image

```
Pixel = 180
```

Pixel values range from:

```
0 → Black
255 → White
```

---

# Image Addition

## Definition

Image Addition means adding the corresponding pixel values of two images.

Formula

```
Output = Image1 + Image2
```

Example

Image A

```
100
```

Image B

```
50
```

Result

```
150
```

---

## Overflow Problem

Normal addition may exceed 255.

Example

```
250 + 50 = 300
```

Maximum pixel value is

```
255
```

OpenCV automatically saturates values.

Result becomes

```
255
```

instead of

```
44
```

(as in NumPy uint8 overflow)

---

# cv2.add()

Syntax

```python
result = cv2.add(image1, image2)
```

Advantages

- Handles overflow properly
- Saturation arithmetic
- Preferred over NumPy addition

---

## Example

```python
import cv2

img1 = cv2.imread("image1.jpg")
img2 = cv2.imread("image2.jpg")

result = cv2.add(img1, img2)

cv2.imshow("Added Image", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

## Adding Brightness

Instead of another image, we can add a constant value.

Example

```python
import cv2
import numpy as np

image = cv2.imread("sample.jpg")

brightness = np.full(image.shape, 50, dtype=np.uint8)

bright = cv2.add(image, brightness)

cv2.imshow("Original", image)
cv2.imshow("Brightened", bright)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

# Image Subtraction

## Definition

Subtract one image from another.

Formula

```
Output = Image1 - Image2
```

---

## Example

```python
import cv2

img1 = cv2.imread("image1.jpg")
img2 = cv2.imread("image2.jpg")

result = cv2.subtract(img1, img2)

cv2.imshow("Subtracted", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

## Darkening an Image

```python
import cv2
import numpy as np

image = cv2.imread("sample.jpg")

dark = np.full(image.shape, 50, dtype=np.uint8)

result = cv2.subtract(image, dark)

cv2.imshow("Dark Image", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

# Difference Between NumPy and OpenCV Addition

NumPy

```python
import numpy as np

a = np.uint8([250])
b = np.uint8([20])

print(a+b)
```

Output

```
14
```

Because

```
270 % 256 = 14
```

---

OpenCV

```python
import cv2

print(cv2.add(a,b))
```

Output

```
255
```

OpenCV uses saturation arithmetic.

---

# Bitwise Operations

Bitwise operations manipulate pixels using binary values.

Available operations

- AND
- OR
- XOR
- NOT

These are mainly used for

- Image masking
- Background removal
- Object extraction
- Region of Interest (ROI)

---

# Bitwise AND

Keeps only common white pixels.

Syntax

```python
cv2.bitwise_and(image1, image2)
```

Example

```python
import cv2

img1 = cv2.imread("image1.jpg")
img2 = cv2.imread("image2.jpg")

result = cv2.bitwise_and(img1, img2)

cv2.imshow("AND", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

# Bitwise OR

Combines both images.

Syntax

```python
cv2.bitwise_or(image1, image2)
```

Example

```python
result = cv2.bitwise_or(img1, img2)
```

---

# Bitwise XOR

Shows different pixels.

Syntax

```python
cv2.bitwise_xor(image1, image2)
```

Example

```python
result = cv2.bitwise_xor(img1, img2)
```

---

# Bitwise NOT

Inverts image colors.

Syntax

```python
result = cv2.bitwise_not(image)
```

Example

```python
import cv2

image = cv2.imread("sample.jpg")

negative = cv2.bitwise_not(image)

cv2.imshow("Negative", negative)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

# Image Blending

## Definition

Blending combines two images with different weights.

Formula

```
Output = α(Image1) + β(Image2) + γ
```

Where

```
α = weight of first image

β = weight of second image

γ = brightness adjustment
```

---

## Syntax

```python
cv2.addWeighted(image1,
                alpha,
                image2,
                beta,
                gamma)
```

---

## Example

```python
import cv2

img1 = cv2.imread("image1.jpg")
img2 = cv2.imread("image2.jpg")

blend = cv2.addWeighted(img1,
                        0.7,
                        img2,
                        0.3,
                        0)

cv2.imshow("Blended", blend)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

# Changing Blend Ratio

```
0.5 + 0.5

Equal Mix
```

```
0.8 + 0.2

Mostly Image 1
```

```
0.2 + 0.8

Mostly Image 2
```

---

# Transparency

Transparency is achieved using image blending.

Example

```
Foreground = Logo

Background = Photo

Result

Transparent Logo
```

---

## Example

```python
import cv2

background = cv2.imread("background.jpg")
logo = cv2.imread("logo.jpg")

logo = cv2.resize(logo,
                  (background.shape[1],
                   background.shape[0]))

transparent = cv2.addWeighted(background,
                              0.8,
                              logo,
                              0.2,
                              0)

cv2.imshow("Transparent Overlay",
           transparent)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

# Practical Example

Adding watermark

```python
import cv2

image = cv2.imread("photo.jpg")
watermark = cv2.imread("logo.png")

watermark = cv2.resize(
    watermark,
    (image.shape[1],
     image.shape[0])
)

result = cv2.addWeighted(
    image,
    0.9,
    watermark,
    0.1,
    0
)

cv2.imshow("Watermarked", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

# Applications

Image arithmetic is used in:

- Image enhancement
- Image restoration
- Object detection
- Background subtraction
- Medical imaging
- Satellite image analysis
- Face recognition
- Watermarking
- Image fusion
- Computer vision

---

# Best Practices

✔ Always use `cv2.add()` instead of NumPy addition.

✔ Images should have the same dimensions.

✔ Images should have the same number of channels.

✔ Use `cv2.addWeighted()` for transparency.

✔ Use bitwise operations with masks.

---

# Summary

In this module you learned:

- Image Addition
- Image Subtraction
- Difference between OpenCV and NumPy arithmetic
- Bitwise AND
- Bitwise OR
- Bitwise XOR
- Bitwise NOT
- Image Blending
- Transparency
- Watermarking
- Practical applications

These operations form the foundation of many Computer Vision tasks such as image enhancement, masking, segmentation, and image fusion.

---
