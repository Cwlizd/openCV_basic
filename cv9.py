import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("sample.jpg")

thr, img_bin = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)

cv2.imshow("sample bin", img_bin)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("img_bin.jpg", img_bin)
