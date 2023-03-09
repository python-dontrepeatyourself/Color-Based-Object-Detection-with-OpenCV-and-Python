import cv2
import numpy as np
import os


# Create a function to get the HSV values from the trackbar
def get_hsv_values(val):
    pass


# Create a window to display the frame
cv2.namedWindow('frame')

# Create a trackbar for Hue
cv2.createTrackbar('H min', 'frame', 0, 179, get_hsv_values)
cv2.createTrackbar('H max', 'frame', 179, 179, get_hsv_values)

# Create a trackbar for Saturation
cv2.createTrackbar('S min', 'frame', 0, 255, get_hsv_values)
cv2.createTrackbar('S max', 'frame', 255, 255, get_hsv_values)

# Create a trackbar for Value
cv2.createTrackbar('V min', 'frame', 0, 255, get_hsv_values)
cv2.createTrackbar('V max', 'frame', 255, 255, get_hsv_values)


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Convert the frame to HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get the current HSV values from the trackbars
    h_min = cv2.getTrackbarPos('H min', 'frame')
    h_max = cv2.getTrackbarPos('H max', 'frame')
    s_min = cv2.getTrackbarPos('S min', 'frame')
    s_max = cv2.getTrackbarPos('S max', 'frame')
    v_min = cv2.getTrackbarPos('V min', 'frame')
    v_max = cv2.getTrackbarPos('V max', 'frame')

    # Set the lower and upper HSV limits
    lower_limit = np.array([h_min, s_min, v_min])
    upper_limit = np.array([h_max, s_max, v_max])

    # Create a mask for the specified color range
    mask = cv2.inRange(hsv_frame, lower_limit, upper_limit)

    # Apply the mask to the original frame
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Show the frame, the mask, and the result
    cv2.imshow("orginal", frame)
    cv2.imshow("mask", mask)
    cv2.imshow('result', result)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Print the current HSV values
    print('H min: {}, H max: {}, S min: {}, S max: {}, V min: {}, V max: {}'.format(
        h_min, h_max, s_min, s_max, v_min, v_max))
# Release the resources and close the window
cap.release()
cv2.destroyAllWindows()
