import cv2
import numpy as np

img = cv2.imread('S4_Fall_Road.png', cv2.IMREAD_GRAYSCALE)
img=cv2.resize(img, (640, 480))
cv2.imshow('Road Sign', img)

cv2.waitKey(0)
cv2.destroyAllWindows()