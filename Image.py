import cv2
import numpy as np

img = cv2.imread("Resources/flower.jpg")

# define a kernel as matrix of 5x5
kernel = np.ones((5, 5), np.uint8)

# convert image to grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# convert make image blurry
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)

# canny edge detection with threshold
imgCanny = cv2.Canny(img, 150, 200)

# image dilation
imgDilate = cv2.dilate(imgCanny, kernel, iterations=1)

# image erosion
imgEroded = cv2.erode(imgDilate, kernel, iterations=1)

# display images
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilation Image", imgDilate)
cv2.imshow("Eroded Image", imgEroded)

cv2.waitKey(0)
