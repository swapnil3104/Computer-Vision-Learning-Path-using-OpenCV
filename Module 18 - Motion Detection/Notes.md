# Module 18 - Motion Detection using OpenCV

## Introduction

Motion Detection is one of the most fundamental applications of computer vision. It involves detecting moving objects in a sequence of video frames by analyzing changes between consecutive frames.

Motion detection is widely used in surveillance systems, smart security cameras, traffic monitoring, robotics, sports analytics, and human activity recognition.

Unlike object detection, motion detection does not necessarily identify *what* the object is—it simply determines *whether something has moved*.

OpenCV provides several techniques to detect motion efficiently, including:

- Frame Difference
- Background Subtraction
- Optical Flow

---

# Learning Objectives

After completing this module, you will be able to:

- Understand the concept of motion detection.
- Detect movement using Frame Difference.
- Separate foreground from background using Background Subtraction.
- Track motion using Optical Flow.
- Build real-time motion detection applications.
- Understand the advantages and limitations of different motion detection techniques.

---

# What is Motion Detection?

Motion detection is the process of identifying moving objects by comparing video frames captured over time.

Instead of analyzing a single image, motion detection compares multiple frames to determine changes.

```
Frame 1

↓

Frame 2

↓

Frame 3

↓

Difference

↓

Motion Detected
```

---

# Applications of Motion Detection

- CCTV Surveillance
- Smart Security Systems
- Intruder Detection
- Traffic Monitoring
- Vehicle Counting
- Human Activity Recognition
- Gesture Recognition
- Sports Analytics
- Robotics Navigation
- Wildlife Monitoring

---

# Motion Detection Pipeline

```
Video Capture

↓

Read Current Frame

↓

Read Previous Frame

↓

Compare Frames

↓

Detect Motion

↓

Highlight Moving Objects

↓

Display Result
```

---

# Types of Motion Detection Techniques

| Technique | Description |
|-----------|-------------|
| Frame Difference | Compares two consecutive frames |
| Background Subtraction | Separates moving objects from the background |
| Optical Flow | Tracks motion of pixels between frames |

---

# 1. Frame Difference

## What is Frame Difference?

Frame Difference is the simplest motion detection technique.

It detects motion by calculating the absolute difference between two consecutive video frames.

If there is no movement:

```
Frame A

=

Frame B

Difference = 0
```

If an object moves:

```
Frame A

≠

Frame B

Difference > 0

Motion Detected
```

---

# Working Principle

```
Previous Frame

↓

Current Frame

↓

Absolute Difference

↓

Threshold

↓

Motion Mask
```

---

# Steps

### Step 1

Capture previous frame.

↓

### Step 2

Capture current frame.

↓

### Step 3

Calculate difference.

↓

### Step 4

Convert difference into binary image.

↓

### Step 5

Find moving regions.

---

# Frame Difference Formula

```
Difference

=

| Current Frame - Previous Frame |
```

Where

- Small values → No movement
- Large values → Motion

---

# Thresholding

After calculating difference,

pixels greater than a threshold become white.

```
Difference

↓

Threshold

↓

Binary Image
```

White = Motion

Black = Background

---

# Advantages

✔ Very simple

✔ Fast

✔ Low computation

✔ Real-time performance

---

# Limitations

- Sensitive to noise
- Camera movement causes false detection
- Cannot detect slow-moving objects accurately
- Requires continuous frame comparison

---

# Applications

- Motion alarms
- Simple surveillance
- Occupancy detection
- Object counting

---

# 2. Background Subtraction

## What is Background Subtraction?

Background subtraction separates moving objects (foreground) from the static scene (background).

Instead of comparing only two frames, it maintains a background model.

```
Background

↓

Current Frame

↓

Subtract Background

↓

Foreground Mask
```

---

# Background Model

A background model represents the static part of the scene.

Example

```
Empty Room

↓

Background Model
```

When a person enters

```
Current Frame

↓

Subtract Background

↓

Person Detected
```

---

# Workflow

```
Video

↓

Background Model

↓

Subtract

↓

Foreground

↓

Noise Removal

↓

Detected Object
```

---

# OpenCV Background Subtractors

OpenCV provides built-in algorithms:

### MOG2

```python
cv2.createBackgroundSubtractorMOG2()
```

Features:

- Adaptive background
- Detects shadows
- Suitable for outdoor scenes

---

### KNN

```python
cv2.createBackgroundSubtractorKNN()
```

Features:

- Uses K-Nearest Neighbors
- Robust to lighting changes
- Good for dynamic backgrounds

---

# Foreground Mask

After subtraction:

```
White

↓

Moving Object
```

```
Black

↓

Background
```

---

# Noise Removal

Foreground masks often contain noise.

Morphological operations improve the mask:

- Erosion
- Dilation
- Opening
- Closing

---

# Advantages

✔ More accurate than Frame Difference

✔ Handles static backgrounds well

✔ Works with multiple moving objects

✔ Suitable for surveillance

---

# Limitations

- Sensitive to sudden lighting changes
- Camera must remain stationary
- Background model requires time to adapt

---

# Applications

- Smart CCTV
- Parking systems
- Crowd monitoring
- Intruder detection
- Traffic analysis

---

# 3. Optical Flow

## What is Optical Flow?

Optical Flow estimates the motion of every pixel between consecutive frames.

Instead of detecting only moving regions, it calculates the direction and speed of movement.

```
Frame 1

↓

Frame 2

↓

Track Pixel Movement

↓

Motion Vectors
```

---

# Motion Vector

Each moving pixel has

- Direction
- Magnitude

Example

```
↓

↓

↓

↓

Object Moving Down
```

or

```
→ → → →

Object Moving Right
```

---

# Optical Flow Assumption

The brightness of a moving object remains approximately constant between consecutive frames.

Only its position changes.

---

# Types of Optical Flow

## Sparse Optical Flow

Tracks selected feature points.

Example:

- Corners
- Interest points

Algorithm:

Lucas-Kanade Optical Flow

```
cv2.calcOpticalFlowPyrLK()
```

Advantages:

- Fast
- Efficient
- Real-time tracking

---

## Dense Optical Flow

Tracks every pixel.

Algorithm:

Farneback Optical Flow

```
cv2.calcOpticalFlowFarneback()
```

Advantages:

- Complete motion field
- More accurate

Disadvantages:

- Computationally expensive

---

# Optical Flow Workflow

```
Frame 1

↓

Feature Detection

↓

Frame 2

↓

Track Features

↓

Motion Vectors

↓

Display Motion
```

---

# Motion Visualization

Motion vectors are often drawn as arrows.

```
•

↓

•

↓

•

↓

Object Moving
```

---

# Advantages

✔ Tracks object movement

✔ Estimates motion direction

✔ Useful for video stabilization

✔ Supports object tracking

✔ Works in robotics

---

# Limitations

- Computationally intensive
- Sensitive to illumination changes
- Fast motion may reduce accuracy
- Occlusion affects tracking

---

# Applications

- Object Tracking
- Drone Navigation
- Autonomous Vehicles
- Video Stabilization
- Gesture Recognition
- Human Motion Analysis
- Robot Navigation

---

# Comparison of Motion Detection Techniques

| Feature | Frame Difference | Background Subtraction | Optical Flow |
|----------|------------------|------------------------|--------------|
| Speed | Very Fast | Fast | Moderate to Slow |
| Accuracy | Low | Medium to High | High |
| Detect Direction | No | No | Yes |
| Camera Must Be Static | Yes | Yes | Not Always |
| Pixel Tracking | No | No | Yes |
| Complexity | Low | Medium | High |
| Real-Time | Yes | Yes | Depends on Hardware |

---

# Complete Motion Detection Pipeline

```
Video Capture

↓

Read Frames

↓

Preprocessing

↓

Motion Detection Algorithm

↓

Threshold / Foreground Mask

↓

Morphological Operations

↓

Contour Detection

↓

Bounding Boxes

↓

Display Result
```

---

# Real-World Applications

## Security Systems

- Intruder detection
- CCTV surveillance
- Smart alarms

---

## Traffic Monitoring

- Vehicle detection
- Traffic density estimation
- Speed analysis

---

## Sports Analytics

- Player tracking
- Ball tracking
- Performance analysis

---

## Healthcare

- Patient monitoring
- Fall detection
- Activity recognition

---

## Robotics

- Robot navigation
- Obstacle avoidance
- Path planning

---

## Autonomous Vehicles

- Detect moving pedestrians
- Detect vehicles
- Collision avoidance

---

## Wildlife Monitoring

- Animal movement tracking
- Forest surveillance

---

# Advantages of Motion Detection

- Real-time analysis
- Low hardware requirements (for simple methods)
- Easy to implement
- Supports automation
- Useful in many AI applications
- Can be combined with object detection

---

# Limitations

- Camera shake causes false motion.
- Sudden lighting changes reduce accuracy.
- Shadows may be detected as motion.
- Weather conditions can introduce noise.
- Optical Flow requires higher computational power.
- Occlusion and overlapping objects can affect tracking.

---

# Best Practices

- Use grayscale frames for faster processing.
- Apply Gaussian Blur to reduce noise before detecting motion.
- Use thresholding to eliminate minor differences.
- Apply morphological operations to clean foreground masks.
- Use contours to identify moving objects.
- Keep the camera fixed for Frame Difference and Background Subtraction.
- Choose Optical Flow when direction and speed of motion are important.

---

# Summary

In this module, you learned:

- Motion detection identifies moving objects by analyzing changes between video frames.
- **Frame Difference** is the simplest and fastest method, comparing consecutive frames.
- **Background Subtraction** builds a background model to isolate moving foreground objects, making it suitable for surveillance.
- **Optical Flow** estimates the movement of pixels, providing both the direction and magnitude of motion, making it ideal for object tracking and advanced computer vision tasks.
- These techniques serve as the foundation for advanced applications such as **people tracking, vehicle detection, gesture recognition, autonomous navigation, video analytics, and intelligent surveillance systems**.