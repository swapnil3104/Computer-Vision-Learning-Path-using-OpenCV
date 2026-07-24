import cv2
import numpy as np
path = 'E:\COLLEGE NOTES\SEM 7th Notes\Practical\Digital Image Processing\Exp 5 To Implement Point Transformations\landscape.jpg'
image = cv2.imread('landscape.jpg')
if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh_val = int(input("Enter threshold value (0–255): "))
    ret, thresh1 = cv2.threshold(gray, thresh_val, 255, cv2.THRESH_BINARY)
    cv2.imshow("User Input Threshold", thresh1)
    cv2.waitKey(0)
else:
    print("Image not found or unable to load")