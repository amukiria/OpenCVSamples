import cv2
import numpy as np

img = cv2.imread("Resources/vw_beetle.jpg")
print(img.shape)

imgResize = cv2.resize(img, (300,200))
print(imgResize.shape)

imgCropped = img[100:400, 200:500]
print(imgCropped.shape)

cv2.imshow("Output",img)
cv2.imshow("Resize", imgResize)
cv2.imshow("Cropped", imgCropped)

cv2.waitKey(0)