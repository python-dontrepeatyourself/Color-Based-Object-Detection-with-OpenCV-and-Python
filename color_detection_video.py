import numpy as np
import cv2


# initialize the video capture object
cap = cv2.VideoCapture("examples/1.mp4")

# grab the width, height, and fps of the frames in the video stream.
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# initialize the FourCC and a video writer object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('output.mp4', fourcc, fps, (frame_width, frame_height))

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("There is no more frame to read, exiting...")
        break

    # convert from BGR to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # lower and upper limits for the blue color
    lower_limit = np.array([99, 135, 51])
    upper_limit = np.array([116, 226, 255])

    mask = cv2.inRange(hsv_frame, lower_limit, upper_limit)
    bbox = cv2.boundingRect(mask)

    # if we get a bounding box, use it to draw a rectangle on the image
    if bbox is not None:
        x, y, w, h = bbox
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    else:
        print("Object not detected")

    cv2.imshow('frame', frame)
    # write the frame to the output file
    output.write(frame)
    if cv2.waitKey(30) == ord('q'):
        break

cap.release()
output.release()
cv2.destroyAllWindows()
