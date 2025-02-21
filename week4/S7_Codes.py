
import cv2

# Load the image
image = cv2.imread("square.png")

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not open or find the image.")
else:
    # Get the dimensions of the image
    (h, w) = image.shape[:2]

    # Calculate the center of the image
    center_x = w // 2
    center_y = h // 2
    center = (center_x, center_y)

    # Define the rotation angle and scale
    angle = 90
    scale = 0.5

    # Get the rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
    print(rotation_matrix)

    # Rotate the image
    rotated_img = cv2.warpAffine(image, rotation_matrix, (w, h))

    # Display the rotated image
    cv2.imshow('frame', rotated_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()