# Module 17 - Video Processing using OpenCV

## Introduction

Video processing is one of the most important applications of computer vision. Unlike image processing, where a single image is analyzed, video processing deals with a sequence of images (frames) displayed rapidly to create motion.

A video is nothing more than a collection of images called **frames**. OpenCV provides powerful tools to read, display, analyze, modify, and save videos.

---

# Learning Objectives

After completing this module, you will be able to:

- Read videos using OpenCV
- Display video frame-by-frame
- Capture video from a webcam
- Save processed videos
- Understand video FPS
- Access video properties
- Build basic real-time computer vision applications

---

# What is a Video?

A video is a sequence of images displayed continuously.

Example:

```
Frame 1
↓

Frame 2
↓

Frame 3
↓

Frame 4
↓

...

30 Frames every second
```

Human eyes perceive this rapid sequence as motion.

---

# Important Video Terms

| Term | Description |
|-------|-------------|
| Frame | A single image in a video |
| FPS | Frames displayed per second |
| Resolution | Width × Height of each frame |
| Codec | Compression format used to store video |
| Duration | Total playback time |
| Frame Count | Total number of frames |

---

# OpenCV Video Classes

The two most commonly used classes are:

### 1. VideoCapture

Used for:

- Reading video files
- Reading webcam
- Reading IP camera

Example:

```python
cap = cv2.VideoCapture("video.mp4")
```

or

```python
cap = cv2.VideoCapture(0)
```

---

### 2. VideoWriter

Used for:

- Saving processed video
- Recording webcam
- Creating videos from frames

Example:

```python
writer = cv2.VideoWriter(...)
```

---

# 1. Read Video

## What is Video Reading?

Reading a video means opening a video file and extracting frames one-by-one.

OpenCV reads one frame at a time.

```
Video

↓

Frame 1

↓

Frame 2

↓

Frame 3

↓

Display
```

---

## Video Reading Process

```
Open Video

↓

Read First Frame

↓

Display

↓

Read Next Frame

↓

Repeat

↓

End Video
```

---

## Syntax

```python
cap = cv2.VideoCapture("video.mp4")
```

---

### Reading Frames

```python
ret, frame = cap.read()
```

Where

- ret → True if frame is successfully read
- frame → image/frame

---

Example:

```
Frame 1

↓

Frame 2

↓

Frame 3

↓

Frame 4
```

---

## End of Video

When video finishes,

```
ret = False
```

which means there are no more frames.

---

# Video Display Loop

```
Open Video

↓

Read Frame

↓

Show Frame

↓

Wait

↓

Read Next Frame

↓

Until End
```

---

# Why Read Frame-by-Frame?

Because every frame can be processed independently.

Example operations:

- Face Detection
- Object Detection
- Motion Detection
- Tracking
- Filtering
- OCR
- Lane Detection

---

# Advantages

✔ Low memory usage

✔ Real-time processing

✔ Easy frame manipulation

✔ Suitable for AI applications

---

# 2. Write Video

## What is Video Writing?

Video writing means saving processed frames into a new video file.

Example:

Original Video

↓

Convert to Grayscale

↓

Draw Objects

↓

Save New Video

---

# Video Writing Workflow

```
Read Frame

↓

Process Frame

↓

Write Frame

↓

Repeat
```

---

# VideoWriter

OpenCV uses

```python
cv2.VideoWriter()
```

---

## Required Parameters

### Output File Name

Example

```
output.mp4
```

---

### Codec

Specifies compression format.

Common codecs:

| Codec | Format |
|---------|---------|
| XVID | AVI |
| MJPG | AVI |
| mp4v | MP4 |
| DIVX | AVI |

---

### FPS

Frames saved every second.

Example

```
30 FPS
```

---

### Frame Size

Example

```
640 × 480
```

Every frame written must have the same size.

---

## Video Writing Flow

```
Frame

↓

Processing

↓

VideoWriter

↓

Saved Video
```

---

## Applications

- CCTV Recording
- Video Compression
- Screen Recording
- Surveillance
- AI Output Videos
- Sports Analysis

---

# 3. Webcam

## What is Webcam Capture?

Instead of reading a video file, OpenCV can capture live frames directly from a webcam.

```
Webcam

↓

Frame

↓

Frame

↓

Frame

↓

Display
```

---

## Webcam Index

```
0 → Default webcam

1 → External webcam

2 → Second external webcam
```

Example

```python
cap = cv2.VideoCapture(0)
```

---

## Webcam Workflow

```
Open Webcam

↓

Capture Frame

↓

Display

↓

Process

↓

Repeat
```

---

## Real-Time Processing

Examples:

```
Webcam

↓

Face Detection

↓

Object Detection

↓

Hand Tracking

↓

Display Result
```

---

## Advantages

✔ Live video

✔ Real-time AI

✔ Motion detection

✔ Video recording

---

# 4. FPS (Frames Per Second)

## What is FPS?

FPS means

**Frames Per Second**

It indicates how many images are displayed every second.

Example

```
30 FPS

↓

30 images displayed every second
```

---

## Example

Suppose

Video Duration = 10 seconds

FPS = 30

Then

```
Total Frames

=

30 × 10

=

300 Frames
```

---

## Common FPS Values

| FPS | Usage |
|------|-------|
| 15 | Low quality |
| 24 | Movies |
| 30 | Standard videos |
| 60 | Gaming |
| 120 | Slow motion |

---

## Why FPS Matters?

Higher FPS

✔ Smooth video

✔ Better motion

✔ Better tracking

Lower FPS

✔ Smaller file size

✔ Less computation

---

## Real FPS vs Video FPS

Video FPS

Stored inside video.

Real FPS

Actual processing speed of your computer.

Sometimes

```
Video FPS = 30

Processing FPS = 18
```

because processing is slow.

---

## FPS Formula

```
FPS

=

Number of Frames

÷

Time
```

Example

```
60 Frames

Processed in

2 Seconds

FPS = 30
```

---

# 5. Video Properties

Every video contains metadata called **properties**.

OpenCV allows reading these properties.

---

## Common Properties

### Width

Frame width.

Example

```
640 pixels
```

---

### Height

Frame height.

Example

```
480 pixels
```

---

### FPS

Frames displayed every second.

Example

```
30 FPS
```

---

### Frame Count

Total frames inside video.

Example

```
1200 Frames
```

---

### Duration

Duration can be calculated as

```
Duration

=

Frame Count

÷

FPS
```

Example

```
300 Frames

30 FPS

=

10 Seconds
```

---

## Brightness

Some webcams support brightness control.

---

## Contrast

Controls image contrast.

---

## Saturation

Controls color intensity.

---

## Exposure

Controls camera exposure.

---

## Gain

Amplifies sensor signal.

---

# Frequently Used Video Properties

| Property | Description |
|-----------|-------------|
| CAP_PROP_FRAME_WIDTH | Width |
| CAP_PROP_FRAME_HEIGHT | Height |
| CAP_PROP_FPS | FPS |
| CAP_PROP_FRAME_COUNT | Number of Frames |
| CAP_PROP_POS_FRAMES | Current Frame |
| CAP_PROP_POS_MSEC | Current Time |
| CAP_PROP_BRIGHTNESS | Brightness |
| CAP_PROP_CONTRAST | Contrast |
| CAP_PROP_SATURATION | Saturation |
| CAP_PROP_EXPOSURE | Exposure |

---

# Video Processing Pipeline

```
Video File

↓

VideoCapture

↓

Read Frame

↓

Processing

↓

Display

↓

VideoWriter

↓

Saved Video
```

---

# Applications of Video Processing

## Security

- CCTV
- Surveillance
- Motion Detection

---

## Healthcare

- Patient Monitoring
- Medical Video Analysis

---

## Sports

- Player Tracking
- Ball Detection
- Performance Analysis

---

## Autonomous Vehicles

- Lane Detection
- Traffic Sign Recognition
- Obstacle Detection

---

## Entertainment

- Snapchat Filters
- Instagram Filters
- AR Effects

---

## Robotics

- Navigation
- Object Tracking
- Vision Systems

---

## Industrial Automation

- Product Inspection
- Quality Control
- Defect Detection

---

# Advantages of Video Processing

- Real-time analysis
- Automation
- AI integration
- Easy frame extraction
- Supports multiple formats
- Cross-platform
- Efficient with OpenCV

---

# Limitations

- High CPU/GPU usage
- Large storage requirements
- Processing may be slow for HD/4K videos
- Requires proper codecs
- Webcam quality affects results

---

# Best Practices

- Always check if the video is opened successfully.
- Release `VideoCapture` and `VideoWriter` objects after use.
- Use appropriate codecs for compatibility.
- Match frame size when writing videos.
- Avoid unnecessary processing for better FPS.
- Display frames using `cv2.imshow()`.
- Exit loops gracefully using keyboard events.

---

# Summary

In this module, you learned:

- How videos are represented as sequences of frames.
- How to read videos using `VideoCapture`.
- How to write processed videos using `VideoWriter`.
- How to capture live video from a webcam.
- The meaning and importance of FPS.
- How to retrieve video properties such as width, height, frame count, and duration.
- The complete workflow of video processing using OpenCV.

This knowledge forms the foundation for advanced topics such as **object detection, motion tracking, background subtraction, action recognition, optical flow, and deep learning-based video analytics**.