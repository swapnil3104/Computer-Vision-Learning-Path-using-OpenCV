import cv2

# Load the original image
path = r'E:\COLLEGE NOTES\SEM 7th Notes\Practical\DIP\EXP 1\albert einstein.jpg'
image = cv2.imread(path)

# Check if the image is loaded properly
if image is None:
    print("Error: Image not found or unable to load.")
else:
    # Resize image to 50% of its original size
    scale_percent = 50  # percentage of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    new_size = (width, height)

    # Resize the image
    resized_image = cv2.resize(image, new_size, interpolation=cv2.INTER_AREA)

    # Display the resized image
    cv2.imshow("Resized Image", resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
