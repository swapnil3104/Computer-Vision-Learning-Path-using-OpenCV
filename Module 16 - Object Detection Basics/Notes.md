# Module 16 - Object Detection Basics

# Table of Contents

1. Introduction to Object Detection
2. What is Object Detection?
3. Difference Between Image Classification, Localization, and Object Detection
4. Haar Cascade Classifier
5. How Haar Cascade Works
6. Haar-like Features
7. Integral Image
8. AdaBoost Algorithm
9. Cascade Classifier
10. Face Detection
11. Eye Detection
12. Smile Detection
13. Advantages of Haar Cascade
14. Limitations of Haar Cascade
15. Applications
16. Best Practices
17. Summary
18. Interview Questions

---

# Module 16 - Object Detection Basics

Object Detection is one of the most important applications of Computer Vision. Unlike image classification, which only predicts the class of an image, object detection identifies the location of objects and classifies them simultaneously.

OpenCV provides several techniques for object detection. One of the oldest and fastest techniques is the **Haar Cascade Classifier**, which is widely used for detecting faces, eyes, smiles, and other objects.

---

# What is Object Detection?

Object Detection is the process of:

- Finding objects in an image
- Identifying what the object is
- Drawing a bounding box around each object

Example:

Input Image

```
👨😊
```

Output

```
+-----------+
|   Face    |
|  👨😊      |
+-----------+

Eyes: 2
Smile: 1
```

The detector returns:

- Object position (x, y)
- Width
- Height

---

# Image Classification vs Localization vs Object Detection

| Task | Output |
|-------|---------|
| Image Classification | Dog |
| Object Localization | Dog + Bounding Box |
| Object Detection | Dog + Box, Cat + Box, Person + Box |

Example

Classification

```
Image
↓

Dog
```

Localization

```
+-------+
| Dog   |
+-------+
```

Object Detection

```
+-------+
| Dog   |
+-------+

+------+
| Cat  |
+------+

+---------+
| Person  |
+---------+
```

---

# What is Haar Cascade?

Haar Cascade is a machine learning-based object detection algorithm developed by **Paul Viola** and **Michael Jones** in 2001.

It is one of the earliest real-time face detection methods.

The algorithm is already trained.

OpenCV provides pre-trained XML files like:

```
haarcascade_frontalface_default.xml

haarcascade_eye.xml

haarcascade_smile.xml

haarcascade_profileface.xml

haarcascade_fullbody.xml
```

---

# Why is it called Haar?

It uses **Haar-like Features** to detect objects.

Instead of looking at every pixel individually, it compares the brightness difference between neighboring rectangular regions.

Example

```
White Area

██████

Black Area

░░░░░░

Feature Value

Sum(White) - Sum(Black)
```

If the difference matches a learned pattern, the object may exist.

---

# Haar-like Features

These features detect edges, lines, and center-surround patterns.

## 1. Edge Feature

```
████░░░░
```

Difference between left and right intensity.

Useful for:

- Face edges
- Nose edges

---

## 2. Line Feature

```
░░████░░
```

Useful for:

- Nose bridge
- Lips

---

## 3. Four Rectangle Feature

```
██░░
░░██
```

Useful for:

- Eyes
- Complex textures

---

# Integral Image

Calculating pixel sums repeatedly is slow.

Integral Image allows extremely fast rectangle sum calculations.

Formula

```
Integral(x,y)

=

Current Pixel

+

Left

+

Top

-

Top Left
```

Instead of scanning thousands of pixels repeatedly, rectangle sums become almost instantaneous.

This makes Haar Cascade very fast.

---

# AdaBoost Algorithm

Thousands of Haar features are generated.

Most are useless.

AdaBoost selects only the most important features.

Steps

```
Thousands of Features

↓

Evaluate

↓

Remove Weak Features

↓

Keep Strong Features

↓

Final Classifier
```

This significantly improves detection speed.

---

# Cascade Classifier

Rather than checking every feature simultaneously, Haar Cascade uses multiple stages.

```
Image

↓

Stage 1

↓

Stage 2

↓

Stage 3

↓

Stage N

↓

Object Found
```

If an image region fails at any stage, it is immediately rejected.

Example

```
Window

↓

Is brightness correct?

No

↓

Reject

(No further processing)
```

Only promising regions continue.

This makes detection very fast.

---

# Detection Pipeline

```
Input Image

↓

Convert to Grayscale

↓

Sliding Window

↓

Haar Features

↓

AdaBoost

↓

Cascade

↓

Detected Object
```

---

# Why Convert to Grayscale?

Color information is not required.

Grayscale

- Faster
- Less memory
- Easier computation

```
RGB

↓

Gray

↓

Detection
```

---

# Face Detection

Face Detection identifies human faces within an image.

OpenCV provides

```
haarcascade_frontalface_default.xml
```

Detection Process

```
Image

↓

Grayscale

↓

Detect Faces

↓

Draw Rectangle
```

Result

```
+------------+
|   FACE     |
|            |
+------------+
```

---

# Face Detection Parameters

## scaleFactor

Controls image scaling.

Example

```
1.05

↓

More accurate

↓

Slower
```

```
1.3

↓

Faster

↓

May miss faces
```

---

## minNeighbors

Controls false positives.

Small value

```
3

↓

More detections

↓

More false positives
```

Large value

```
8

↓

More accurate

↓

May miss small faces
```

---

## minSize

Minimum object size.

Example

```
(30,30)
```

Objects smaller than this are ignored.

---

# Eye Detection

Eye Detection is usually performed only inside the detected face.

Cascade file

```
haarcascade_eye.xml
```

Pipeline

```
Detect Face

↓

Crop Face Region

↓

Detect Eyes

↓

Draw Rectangles
```

Result

```
+-------------+
|  O     O    |
|             |
+-------------+
```

---

# Why Detect Eyes After Face?

Searching the entire image for eyes is slow.

Instead:

```
Image

↓

Face

↓

Eyes
```

This improves:

- Speed
- Accuracy

---

# Smile Detection

Smile detection identifies smiling mouths.

Cascade file

```
haarcascade_smile.xml
```

Pipeline

```
Face

↓

Mouth Region

↓

Smile Detector
```

Result

```
😊
```

---

# Detection Flow

```
Camera

↓

Frame

↓

Gray

↓

Face

↓

Eyes

↓

Smile

↓

Display
```

---

# Applications

## Face Unlock

```
Camera

↓

Detect Face

↓

Unlock
```

---

## Attendance System

```
Camera

↓

Face Detection

↓

Recognition

↓

Attendance
```

---

## Driver Monitoring

```
Driver

↓

Face

↓

Eyes

↓

Drowsiness Detection
```

---

## Photo Applications

```
Detect Faces

↓

Auto Focus

↓

Beautification
```

---

## Security Systems

```
CCTV

↓

Human Face

↓

Alert
```

---

# Advantages of Haar Cascade

- Very fast
- Lightweight
- Works in real time
- Easy to use
- Pre-trained models available
- Suitable for CPU
- No GPU required

---

# Limitations

- Sensitive to lighting
- Sensitive to rotation
- Poor with occlusions
- Not suitable for complex scenes
- Lower accuracy than modern deep learning methods
- Cannot detect many object categories effectively

---

# Haar Cascade vs Deep Learning

| Feature | Haar Cascade | Deep Learning |
|----------|-------------|---------------|
| Speed | Very Fast | Moderate |
| Accuracy | Medium | High |
| GPU Needed | No | Usually Yes |
| Training | Pre-trained XML | Large Dataset |
| Small Devices | Excellent | Moderate |
| Multiple Objects | Limited | Excellent |

---

# Common OpenCV Haar Cascade Files

| XML File | Purpose |
|-----------|----------|
| haarcascade_frontalface_default.xml | Face Detection |
| haarcascade_eye.xml | Eye Detection |
| haarcascade_smile.xml | Smile Detection |
| haarcascade_profileface.xml | Side Face Detection |
| haarcascade_fullbody.xml | Full Body Detection |
| haarcascade_upperbody.xml | Upper Body Detection |

---

# Best Practices

- Always convert images to grayscale before detection.
- Use appropriate `scaleFactor` and `minNeighbors` values.
- Detect faces before detecting eyes or smiles.
- Resize very large images to improve speed.
- Avoid poor lighting conditions for better accuracy.
- Use high-quality frontal images for best results.

---

# Real-World Applications

- Smartphone Face Unlock
- CCTV Surveillance
- Smart Attendance Systems
- Driver Drowsiness Detection
- Video Conferencing
- Camera Auto Focus
- Emotion Analysis (with additional models)
- Human-Computer Interaction

---

# Summary

- Object Detection locates and identifies objects in an image.
- Haar Cascade is a fast, classical object detection algorithm.
- It uses Haar-like features, Integral Images, AdaBoost, and Cascade Classifiers.
- OpenCV provides pre-trained XML classifiers for face, eye, and smile detection.
- Face detection is typically performed before eye and smile detection to improve efficiency.
- Haar Cascade is lightweight and suitable for real-time applications, but modern deep learning methods generally provide higher accuracy.

---
