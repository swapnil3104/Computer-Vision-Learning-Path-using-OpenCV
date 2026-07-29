# Module 7 - Image Filtering

## Learning Objectives

After completing this module, you will be able to:

- Understand why image filtering is used.
- Remove different types of image noise.
- Smooth images using different filtering techniques.
- Preserve edges while reducing noise.
- Sharpen blurry images.
- Choose the appropriate filter for different applications.

---

# What is Image Filtering?

Image Filtering is a technique used to modify or improve an image by changing the value of pixels based on their neighboring pixels.

Filtering is one of the most important concepts in Computer Vision and Digital Image Processing.

It is used for:

- Removing noise
- Reducing blur
- Smoothing images
- Detecting edges
- Enhancing important features
- Preparing images for machine learning

OpenCV provides many built-in filtering functions.

---

# Why Do We Need Image Filtering?

Real-world images often contain imperfections such as:

- Camera noise
- Dust
- Low lighting
- Compression artifacts
- Motion blur
- Sensor errors

Filtering helps improve image quality before performing:

- Face Detection
- Object Detection
- OCR
- Medical Image Analysis
- Image Segmentation
- Image Classification

---

# Types of Image Filtering

Image filtering can be divided into two categories.

## 1. Smoothing Filters

Used for:

- Noise Removal
- Blur Effect
- Softening Images

Examples:

- Blur
- Gaussian Blur
- Median Blur
- Bilateral Filter

---

## 2. Sharpening Filters

Used for:

- Increasing details
- Highlighting edges
- Improving image clarity

Example:

- Kernel-based Sharpening

---

# How Filtering Works

Filtering works using a small matrix called a **Kernel** or **Filter**.

The kernel moves across every pixel.

For each position:

1. Multiply neighboring pixels by kernel values.
2. Add all results.
3. Replace the center pixel.

This process is called **Convolution**.

---

# What is a Kernel?

A Kernel is a small matrix.

Example:

```
1 1 1
1 1 1
1 1 1
```

or

```
0 -1 0
-1 5 -1
0 -1 0
```

The kernel determines how the image will change.

---

# Blur (Average Blur)

## What is Blur?

Average Blur smooths an image by replacing each pixel with the average value of neighboring pixels.

It is the simplest filtering technique.

OpenCV Function

```python
cv2.blur()
```

Syntax

```python
blurred = cv2.blur(image, (5,5))
```

Parameters

| Parameter | Description |
|------------|-------------|
| image | Input image |
| (5,5) | Kernel Size |

---

## How Average Blur Works

Suppose the neighborhood is

```
100 120 140

110 130 150

120 140 160
```

Average

```
(100+120+140+110+130+150+120+140+160)/9
```

New center pixel becomes

```
130
```

---

## Advantages

- Very simple
- Fast
- Removes small noise

---

## Disadvantages

- Blurs edges
- Removes image details

---

## Applications

- Image preprocessing
- Removing tiny noise
- Background smoothing

---

# Gaussian Blur

## What is Gaussian Blur?

Gaussian Blur performs weighted averaging.

Nearby pixels receive higher importance than distant pixels.

Instead of simple average, Gaussian distribution is used.

OpenCV Function

```python
cv2.GaussianBlur()
```

Syntax

```python
blurred = cv2.GaussianBlur(image, (5,5), 0)
```

Parameters

| Parameter | Description |
|------------|-------------|
| image | Input image |
| (5,5) | Kernel Size |
| 0 | Sigma value |

---

## Gaussian Kernel Example

```
1 2 1

2 4 2

1 2 1
```

After normalization

```
1/16

2/16

4/16
```

Center pixels receive larger weights.

---

## Advantages

- Natural smoothing
- Less edge distortion
- Better than average blur

---

## Disadvantages

- Slight edge loss
- Cannot preserve sharp boundaries perfectly

---

## Applications

- Noise reduction
- Face recognition
- Medical images
- Computer vision preprocessing

---

# Median Blur

## What is Median Blur?

Median Blur replaces the center pixel with the median value instead of the average.

OpenCV Function

```python
cv2.medianBlur()
```

Syntax

```python
blurred = cv2.medianBlur(image,5)
```

---

## Example

Pixel values

```
10

12

15

16

250
```

Sorted

```
10

12

15

16

250
```

Median

```
15
```

The noisy value 250 is removed automatically.

---

## Why Median Blur?

Average would produce

```
60
```

Median produces

```
15
```

Thus, Median Blur removes impulse noise effectively.

---

## Advantages

- Excellent for Salt & Pepper Noise
- Preserves edges better
- Removes outliers

---

## Disadvantages

- Slower than average blur
- Not ideal for Gaussian noise

---

## Applications

- Medical images
- Document scanning
- Removing Salt & Pepper Noise

---

# Bilateral Filter

## What is Bilateral Filtering?

Bilateral Filtering smooths the image while preserving edges.

Unlike other blur techniques, it considers:

- Pixel distance
- Pixel intensity difference

OpenCV Function

```python
cv2.bilateralFilter()
```

Syntax

```python
filtered = cv2.bilateralFilter(image,9,75,75)
```

Parameters

| Parameter | Description |
|------------|-------------|
| 9 | Diameter |
| 75 | Sigma Color |
| 75 | Sigma Space |

---

## Why Bilateral Filter?

Suppose two neighboring pixels

```
100

105
```

Difference is small.

They will be averaged.

Suppose

```
100

220
```

Difference is huge.

The filter keeps them separate.

Thus edges remain sharp.

---

## Advantages

- Removes noise
- Keeps edges
- High quality output

---

## Disadvantages

- Slow
- Computationally expensive

---

## Applications

- Portrait enhancement
- Medical imaging
- Face detection
- Photography

---

# Sharpening

## What is Sharpening?

Sharpening increases the visibility of edges.

It makes images appear clearer and more detailed.

---

## Why Sharpen Images?

Sometimes images become blurry because of:

- Motion
- Camera focus
- Compression
- Blur filters

Sharpening restores edge information.

---

## Sharpening Kernel

Example

```
0 -1 0

-1 5 -1

0 -1 0
```

Center pixel gets higher importance.

Neighboring pixels are subtracted.

This increases edge contrast.

---

## OpenCV Implementation

Using filter2D()

```python
kernel = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])

sharp = cv2.filter2D(image,-1,kernel)
```

---

## Advantages

- Better details
- Clear edges
- Improved readability

---

## Disadvantages

- Amplifies noise
- Over-sharpening causes artifacts

---

## Applications

- OCR
- Satellite images
- Medical images
- Photography
- Security cameras

---

# Comparison of Filters

| Filter | Removes Noise | Preserves Edges | Speed | Best For |
|---------|--------------|----------------|--------|----------|
| Blur | Yes | No | Very Fast | Simple smoothing |
| Gaussian Blur | Yes | Moderate | Fast | Natural blur |
| Median Blur | Excellent | Good | Medium | Salt & Pepper Noise |
| Bilateral Filter | Excellent | Excellent | Slow | Edge-preserving smoothing |
| Sharpening | No | Enhances Edges | Fast | Detail enhancement |

---

# Which Filter Should You Use?

| Situation | Recommended Filter |
|------------|-------------------|
| Small random noise | Blur |
| Gaussian noise | Gaussian Blur |
| Salt & Pepper Noise | Median Blur |
| Preserve edges | Bilateral Filter |
| Increase details | Sharpening |

---

# Real-World Applications

## Mobile Camera

- Gaussian Blur
- Sharpening

---

## Medical Imaging

- Median Blur
- Bilateral Filter

---

## Self Driving Cars

- Gaussian Blur
- Bilateral Filter

---

## OCR

- Median Blur
- Sharpening

---

## Face Detection

- Gaussian Blur

---

## Security Systems

- Sharpening

---

# Summary

- Filtering improves image quality.
- Blur performs simple averaging.
- Gaussian Blur uses weighted averaging.
- Median Blur replaces pixels with the median value and removes Salt & Pepper noise.
- Bilateral Filter smooths images while preserving edges.
- Sharpening enhances image details using convolution kernels.
- Selecting the right filter depends on the type of noise and the application.

---

# Key Takeaways

✔ Image filtering improves image quality.

✔ Blur uses average values.

✔ Gaussian Blur uses weighted averages.

✔ Median Blur removes impulse noise.

✔ Bilateral Filter preserves edges while smoothing.

✔ Sharpening increases edge contrast.

✔ Choosing the correct filter improves Computer Vision accuracy.