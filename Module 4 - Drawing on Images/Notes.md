# Module 4 - Drawing on Images

Drawing on images is one of the fundamental features of OpenCV. It allows us to create shapes, annotate images, highlight objects, and display information visually. Drawing functions are widely used in computer vision applications such as object detection, image annotation, face recognition, medical imaging, and surveillance systems.

OpenCV provides several built-in functions to draw geometric shapes and text directly onto an image.

---

# Learning Objectives

After completing this module, you will be able to:

- Draw straight lines on an image
- Draw rectangles
- Draw circles
- Draw ellipses
- Draw polygons
- Add text to an image
- Use different font styles
- Customize drawing color and thickness
- Create simple image annotations

---

# Why Draw on Images?

Drawing functions are useful for:

- Highlighting detected objects
- Drawing bounding boxes
- Displaying measurements
- Image annotation
- Creating diagrams
- Showing prediction labels
- Visual debugging

---

# Coordinate System in OpenCV

Before drawing anything, it is important to understand the image coordinate system.

Unlike the Cartesian coordinate system used in mathematics, OpenCV considers the **top-left corner** as the origin.

```
(0,0)
 +----------------------------------------→ X
 |
 |
 |
 |
 |
 ↓
 Y
```

Example:

```
Width  = 640 pixels
Height = 480 pixels

Top Left      = (0,0)

Center         = (320,240)

Bottom Right   = (639,479)
```

---

# Colors in OpenCV

OpenCV uses the **BGR** color format instead of RGB.

| Color | BGR Value |
|--------|-----------|
| Black | (0,0,0) |
| White | (255,255,255) |
| Blue | (255,0,0) |
| Green | (0,255,0) |
| Red | (0,0,255) |
| Yellow | (0,255,255) |
| Cyan | (255,255,0) |
| Magenta | (255,0,255) |

---

# Thickness

Most drawing functions allow specifying thickness.

```
Thickness = 1

────────────

Thickness = 5

════════════
```

Special value:

```
thickness = -1
```

fills the shape completely.

---

# 1. Drawing Lines

## What is a Line?

A line connects two points.

```
Point A ●-------------------------● Point B
```

---

## OpenCV Function

```python
cv2.line()
```

---

## Syntax

```python
cv2.line(image,
         start_point,
         end_point,
         color,
         thickness)
```

---

## Parameters

| Parameter | Description |
|------------|-------------|
| image | Input image |
| start_point | Starting coordinate |
| end_point | Ending coordinate |
| color | BGR color |
| thickness | Line width |

---

## Example

```
(50,100) ---------------------- (500,100)
```

---

## Applications

- Road lane detection
- Graph plotting
- Coordinate systems
- Distance measurement
- Image annotation

---

# Example Code

```python
import cv2
import numpy as np

image = np.zeros((400,600,3),dtype=np.uint8)

cv2.line(image,
         (50,100),
         (500,100),
         (0,255,0),
         3)

cv2.imshow("Line",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

# 2. Drawing Rectangles

## What is a Rectangle?

A rectangle is defined using two corner points.

```
+----------------------+
|                      |
|                      |
|                      |
+----------------------+
```

---

## OpenCV Function

```python
cv2.rectangle()
```

---

## Syntax

```python
cv2.rectangle(image,
              pt1,
              pt2,
              color,
              thickness)
```

---

## Filled Rectangle

```
thickness = -1
```

---

## Example

```
Top Left      = (100,100)

Bottom Right  = (300,250)
```

---

## Applications

- Object Detection
- Face Detection
- Vehicle Detection
- OCR

---

# Example Code

```python
import cv2
import numpy as np

image = np.zeros((400,600,3),dtype=np.uint8)

cv2.rectangle(image,
              (100,100),
              (300,250),
              (255,0,0),
              3)

cv2.imshow("Rectangle",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

# Filled Rectangle

```python
cv2.rectangle(image,
              (100,100),
              (300,250),
              (255,0,0),
              -1)
```

---

# 3. Drawing Circles

## What is a Circle?

A circle is defined using:

- Center
- Radius

```
      *****
   **       **
  *     ●     *
   **       **
      *****
```

---

## OpenCV Function

```python
cv2.circle()
```

---

## Syntax

```python
cv2.circle(image,
           center,
           radius,
           color,
           thickness)
```

---

## Parameters

| Parameter | Description |
|------------|-------------|
| center | Center point |
| radius | Radius |
| color | BGR |
| thickness | Border width |

---

## Applications

- Marking keypoints
- Face landmarks
- Ball tracking
- Feature detection

---

# Example Code

```python
import cv2
import numpy as np

image = np.zeros((500,500,3),dtype=np.uint8)

cv2.circle(image,
           (250,250),
           100,
           (0,0,255),
           4)

cv2.imshow("Circle",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

# Filled Circle

```python
cv2.circle(image,
           (250,250),
           100,
           (0,255,0),
           -1)
```

---

# 4. Drawing Ellipse

## What is an Ellipse?

An ellipse looks like a stretched circle.

```
      **********
   ***          ***
 **                **
 **                **
   ***          ***
      **********
```

---

## OpenCV Function

```python
cv2.ellipse()
```

---

## Syntax

```python
cv2.ellipse(image,
            center,
            axes,
            angle,
            startAngle,
            endAngle,
            color,
            thickness)
```

---

## Parameters

| Parameter | Description |
|------------|-------------|
| center | Ellipse center |
| axes | Major and minor axis |
| angle | Rotation |
| startAngle | Start |
| endAngle | End |
| thickness | Border width |

---

## Applications

- Eye detection
- Face landmarks
- Medical imaging

---

# Example Code

```python
import cv2
import numpy as np

image = np.zeros((500,500,3),dtype=np.uint8)

cv2.ellipse(image,
            (250,250),
            (150,80),
            0,
            0,
            360,
            (255,255,0),
            3)

cv2.imshow("Ellipse",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

# 5. Drawing Polygons

## What is a Polygon?

A polygon consists of multiple connected vertices.

Example:

Triangle

```
      ●
     / \
    /   \
   ●-----●
```

Pentagon

```
    ●
  ●   ●
  ●   ●
    ●
```

---

## OpenCV Function

```python
cv2.polylines()
```

---

## Steps

1. Create points
2. Convert to NumPy array
3. Draw polygon

---

# Example Code

```python
import cv2
import numpy as np

image = np.zeros((500,500,3),dtype=np.uint8)

points = np.array([[100,100],
                   [300,80],
                   [400,250],
                   [250,400],
                   [80,250]])

cv2.polylines(image,
              [points],
              True,
              (0,255,255),
              3)

cv2.imshow("Polygon",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

# Filled Polygon

```python
cv2.fillPoly(image,
             [points],
             (255,0,255))
```

---

# 6. Writing Text

## What is Text Annotation?

Text can be written directly on images.

Example

```
+----------------------+

    OpenCV Tutorial

+----------------------+
```

---

## OpenCV Function

```python
cv2.putText()
```

---

## Syntax

```python
cv2.putText(image,
            text,
            position,
            font,
            fontScale,
            color,
            thickness)
```

---

## Parameters

| Parameter | Description |
|------------|-------------|
| image | Input image |
| text | Text string |
| position | Bottom-left corner |
| font | Font type |
| fontScale | Text size |
| color | BGR |
| thickness | Line width |

---

# Example Code

```python
import cv2
import numpy as np

image = np.zeros((300,700,3),dtype=np.uint8)

cv2.putText(image,
            "Hello OpenCV",
            (70,150),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.5,
            (0,255,0),
            3)

cv2.imshow("Text",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

# 7. Fonts in OpenCV

OpenCV supports several built-in fonts.

| Font Constant | Description |
|---------------|-------------|
| FONT_HERSHEY_SIMPLEX | Default font |
| FONT_HERSHEY_PLAIN | Small font |
| FONT_HERSHEY_DUPLEX | Smooth font |
| FONT_HERSHEY_COMPLEX | Professional font |
| FONT_HERSHEY_TRIPLEX | Thick font |
| FONT_HERSHEY_COMPLEX_SMALL | Compact font |
| FONT_HERSHEY_SCRIPT_SIMPLEX | Script style |
| FONT_HERSHEY_SCRIPT_COMPLEX | Fancy script |

---

# Example of Different Fonts

```python
import cv2
import numpy as np

image = np.zeros((500,700,3),dtype=np.uint8)

cv2.putText(image,"Simple",(30,60),
            cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)

cv2.putText(image,"Plain",(30,120),
            cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)

cv2.putText(image,"Complex",(30,180),
            cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)

cv2.putText(image,"Triplex",(30,240),
            cv2.FONT_HERSHEY_TRIPLEX,1,(0,255,255),2)

cv2.putText(image,"Script",(30,320),
            cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,(255,0,255),2)

cv2.imshow("Fonts",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

# Drawing Multiple Shapes

```python
import cv2
import numpy as np

image = np.ones((600,800,3),dtype=np.uint8)*255

cv2.line(image,(50,50),(300,50),(255,0,0),3)

cv2.rectangle(image,(50,100),(250,250),(0,255,0),3)

cv2.circle(image,(500,180),80,(0,0,255),4)

cv2.ellipse(image,(500,420),(120,60),0,0,360,(255,255,0),3)

points=np.array([[300,320],[420,260],[560,340],[520,500],[350,480]])

cv2.polylines(image,[points],True,(255,0,255),3)

cv2.putText(image,
            "OpenCV Drawing",
            (180,580),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,0,0),
            2)

cv2.imshow("Drawing Demo",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

# Summary Table

| Function | Purpose |
|----------|---------|
| `cv2.line()` | Draw a straight line |
| `cv2.rectangle()` | Draw a rectangle |
| `cv2.circle()` | Draw a circle |
| `cv2.ellipse()` | Draw an ellipse |
| `cv2.polylines()` | Draw polygons |
| `cv2.fillPoly()` | Draw filled polygons |
| `cv2.putText()` | Write text |
| Font Constants | Select font style |

---

# Best Practices

- Use appropriate colors for visibility.
- Keep text readable with sufficient font size.
- Use filled shapes (`thickness=-1`) for highlighting.
- Maintain consistent line thickness across annotations.
- Label detected objects clearly in computer vision applications.
- Use contrasting colors when drawing on colorful images.

---

# Key Takeaways

- OpenCV provides simple functions for drawing geometric shapes and text.
- The image origin `(0,0)` is located at the top-left corner.
- Colors are specified in **BGR** format.
- Shapes can be outlined or filled using the `thickness` parameter.
- Text can be customized with different fonts, colors, sizes, and thickness.
- Drawing functions are essential for image annotation, object detection, and visualization in computer vision projects.