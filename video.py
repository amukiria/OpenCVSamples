import cv2

capture = cv2.VideoCapture("Resources/road.mp4")

while True:
    success, img = capture.read()
    cv2.imshow("Output", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
