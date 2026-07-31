# Module 12 - Histograms

## Learning Objectives

After completing this module, you will be able to:

- Understand what an image histogram is.
- Analyze image brightness and contrast using histograms.
- Perform Histogram Equalization to improve image contrast.
- Apply CLAHE (Contrast Limited Adaptive Histogram Equalization) for local contrast enhancement.
- Compare histograms of different images using various comparison methods.
- Implement histogram operations using OpenCV and Python.

---

# 1. Introduction to Histograms

A **Histogram** is a graphical representation of the distribution of pixel intensity values in an image.

Instead of displaying where pixels are located, a histogram shows **how many pixels exist for each intensity value**.

For an 8-bit grayscale image:

- Minimum intensity = **0 (Black)**
- Maximum intensity = **255 (White)**

A histogram helps us understand:

- Image brightness
- Contrast
- Dynamic range
- Exposure
- Distribution of colors

---

## Histogram Representation

### X-Axis

Represents pixel intensity values.

```
0 ---------------------------- 255
Black                     White
```

### Y-Axis

Represents the number of pixels having each intensity.

```
Frequency

|
|
|         ███
|       ███████
|    ███████████
|______________________________
 0                  255
```

---

# Why Histograms are Important

Histograms are widely used in Computer Vision because they help determine:

- Whether an image is dark
- Whether an image is bright
- Whether contrast is low
- Whether contrast is high
- Image quality
- Exposure problems

---

# Histogram of Different Images

## Dark Image

Most pixels lie near 0.

```
Frequency

█████████████
██████████
██████
██
________________________________
0                           255
```

Characteristics

- Underexposed
- Less visible details
- Mostly black pixels

---

## Bright Image

Most pixels lie near 255.

```
Frequency

                         ████████
                      ███████████
                   ██████████████
________________________________
0                           255
```

Characteristics

- Overexposed
- Too much brightness
- White regions dominate

---

## Low Contrast Image

Pixels are concentrated within a small intensity range.

```
Frequency

          ██████████
        █████████████
       ███████████████
________________________________
0                           255
```

Characteristics

- Flat appearance
- Poor visibility
- Lack of details

---

## High Contrast Image

Pixels spread across the full intensity range.

```
Frequency

██     ███      ███
███   █████   █████
████████████████████
________________________________
0                           255
```

Characteristics

- Better visibility
- More details
- Sharper appearance

---

# Types of Histograms

## 1. Grayscale Histogram

Uses one channel.

Range:

```
0 - 255
```

Used for:

- Contrast analysis
- Brightness analysis
- Image enhancement

---

## 2. RGB Histogram

Uses three channels:

- Red
- Green
- Blue

Each channel has its own histogram.

```
Red Histogram

███████

Green Histogram

██████████

Blue Histogram

████████
```

Used in:

- Color analysis
- Color correction
- Object recognition

---

# OpenCV Histogram Functions

## Calculate Histogram

```python
cv2.calcHist()
```

Syntax

```python
cv2.calcHist(images,
             channels,
             mask,
             histSize,
             ranges)
```

Parameters

### images

Input image

### channels

Which channel to calculate.

Example

```
0 → Blue / Gray
1 → Green
2 → Red
```

### mask

Optional mask.

```
None
```

means entire image.

### histSize

Number of bins.

Usually

```
256
```

### ranges

Intensity range

```
[0,256]
```

---

# Example Histogram Calculation

```python
hist = cv2.calcHist(
    [gray],
    [0],
    None,
    [256],
    [0,256]
)
```

---

# Display Histogram

Using Matplotlib

```python
plt.plot(hist)
```

---

# Applications of Histograms

- Image enhancement
- Medical imaging
- Face recognition
- Satellite images
- Machine learning
- Object detection
- Image retrieval
- Computer vision

---

# 2. Histogram Equalization

Histogram Equalization is a technique that improves image contrast by redistributing pixel intensities over the entire intensity range.

Instead of concentrating pixels in one region, it spreads them across 0–255.

---

## Before Equalization

```
██████████
████████
██████
```

Low contrast

---

## After Equalization

```
██ ███ ███ ███ ███
██████████████████
```

Better distribution

---

# Advantages

- Improves visibility
- Enhances details
- Increases contrast
- Better feature extraction

---

# Disadvantages

- May amplify noise
- Changes brightness
- Not suitable for all images

---

# OpenCV Function

```python
cv2.equalizeHist()
```

Syntax

```python
equalized = cv2.equalizeHist(gray)
```

Works only on

- Grayscale images

---

# Applications

- Medical images
- X-rays
- Satellite images
- OCR
- Face detection

---

# 3. CLAHE

CLAHE stands for

**Contrast Limited Adaptive Histogram Equalization**

It improves local contrast while preventing excessive noise amplification.

Unlike normal histogram equalization, CLAHE processes small regions (tiles) independently.

---

# Working of CLAHE

Image

↓

Divide into tiles

↓

Histogram Equalization

↓

Clip histogram

↓

Merge tiles

↓

Enhanced image

---

# Why CLAHE?

Normal histogram equalization sometimes makes noise stronger.

CLAHE limits enhancement using a clipping threshold.

---

# Advantages

- Better local contrast
- Preserves details
- Reduces over-enhancement
- Excellent for medical imaging

---

# Disadvantages

- Slightly slower
- More parameters
- Tile size selection matters

---

# OpenCV Function

```python
cv2.createCLAHE()
```

Example

```python
clahe = cv2.createCLAHE(
    clipLimit=2.0,
    tileGridSize=(8,8)
)

result = clahe.apply(gray)
```

---

# CLAHE Parameters

## clipLimit

Controls contrast enhancement.

Higher value

More contrast

Lower value

Less contrast

---

## tileGridSize

Number of image tiles.

Example

```
(8,8)
```

means divide image into 8×8 regions.

---

# Applications

- Medical imaging
- Night vision
- License plate recognition
- Surveillance
- Satellite images

---

# Histogram Equalization vs CLAHE

| Feature | Histogram Equalization | CLAHE |
|----------|-----------------------|--------|
| Global | Yes | No |
| Local Enhancement | No | Yes |
| Noise Handling | Poor | Better |
| Speed | Faster | Slower |
| Image Quality | Moderate | Better |
| Medical Imaging | Limited | Excellent |

---

# 4. Histogram Comparison

Histogram Comparison measures the similarity between two images based on their histograms.

Instead of comparing every pixel, histogram comparison compares the distribution of pixel intensities.

---

# Why Histogram Comparison?

Useful for

- Image matching
- Image retrieval
- Duplicate image detection
- Object tracking
- Scene recognition

---

# Steps

Image 1

↓

Histogram

↓

Image 2

↓

Histogram

↓

Compare

↓

Similarity Score

---

# OpenCV Function

```python
cv2.compareHist()
```

Syntax

```python
cv2.compareHist(hist1, hist2, method)
```

---

# Histogram Comparison Methods

## 1. Correlation

Measures similarity.

Range

```
-1 to 1
```

- 1 → Perfect match
- 0 → No relation
- -1 → Opposite

OpenCV

```python
cv2.HISTCMP_CORREL
```

---

## 2. Chi-Square Distance

Measures difference.

Smaller value

Better match

OpenCV

```python
cv2.HISTCMP_CHISQR
```

---

## 3. Intersection

Measures overlap between histograms.

Higher value

Better match

OpenCV

```python
cv2.HISTCMP_INTERSECT
```

---

## 4. Bhattacharyya Distance

Measures similarity using statistical distance.

Range

```
0 → Perfect match
1 → Completely different
```

OpenCV

```python
cv2.HISTCMP_BHATTACHARYYA
```

---

# Example Comparison

```python
score = cv2.compareHist(
    hist1,
    hist2,
    cv2.HISTCMP_CORREL
)
```

---

# Applications

- Image retrieval
- Face recognition
- Video tracking
- Object detection
- Medical image analysis
- Duplicate image search

---

# Workflow of Histogram Processing

```
Input Image
      │
      ▼
Calculate Histogram
      │
      ▼
Analyze Contrast
      │
      ├─────────────► Histogram Equalization
      │
      ├─────────────► CLAHE
      │
      └─────────────► Histogram Comparison
      │
      ▼
Enhanced Image / Similarity Score
```

---

# Advantages of Histogram Techniques

- Easy to implement
- Fast computation
- Improves contrast
- Better visualization
- Useful in Computer Vision
- Supports image matching
- Enhances medical images

---

# Limitations

- Ignores spatial information
- Histogram Equalization may amplify noise
- Histogram Comparison cannot distinguish images with similar intensity distributions but different content
- CLAHE requires parameter tuning

---

# Real-World Applications

- Medical Imaging
- Satellite Image Processing
- Face Recognition
- OCR Systems
- Security Surveillance
- Autonomous Vehicles
- Object Tracking
- Image Search Engines
- Image Enhancement
- Industrial Inspection

---

# Summary

In this module, you learned:

- What an image histogram is and how it represents the distribution of pixel intensities.
- How to calculate and visualize histograms using OpenCV.
- How Histogram Equalization enhances image contrast.
- How CLAHE improves local contrast while reducing noise amplification.
- How Histogram Comparison measures similarity between images using Correlation, Chi-Square, Intersection, and Bhattacharyya Distance.
- Real-world applications, advantages, limitations, and workflow of histogram-based image processing techniques.

These histogram techniques form the foundation of many image enhancement and computer vision applications, making them essential tools for preprocessing, feature analysis, and image comparison.