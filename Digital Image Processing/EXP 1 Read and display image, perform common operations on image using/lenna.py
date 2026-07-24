import cv2

# Load the image from the same folder or specified path
img = cv2.imread('Lenna.jpeg', cv2.IMREAD_UNCHANGED)

# Show the image in a window titled 'Lenna'
cv2.imshow('Lenna', img)

# Wait indefinitely until any key is pressed
cv2.waitKey(0)