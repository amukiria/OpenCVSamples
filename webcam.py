import cv2

# access default webcam
cap = cv2.VideoCapture(0)

# set the width. height and brightness values respectively
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

# loop through and display each frame in the video
while True:
    success, img = cap.read()
    cv2.imshow("Output", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
