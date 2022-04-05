import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("sample.jpg")
img_flip = cv2.flip(img, -1)
cv2.imshow("img flip", img_flip)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("sample_flip.jpg", img_flip)
