import cv2
# Open the device at the ID 0
cap = cv2.VideoCapture(0)
#Check whether user selected camera is opened successfully.
if not (cap.isOpened()):
    print("Could not open video device")
#To set the resolution
# cap.set(cv2.CV_CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.WINDOW_AUTOSIZE)

while(True):
# Capture frame-by-frame
    ret, frame = cap.read()
# Display the resulting frame
    cv2.imshow('preview',frame)
#Waits for a user input to quit the application
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
