import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("sample.jpg")
print(img.shape)
img_resize = cv2.resize(img, (int(img.shape[1]*0.5), img.shape[0]*1))
cv2.imshow("sample_resize", img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("sample_resize.jpg", img_resize)
