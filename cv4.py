import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("sample.jpg")
print(img.shape)
cv2.imshow("sample", img)

img_cut = img[0:(img.shape[0]*2//3), 0:(img.shape[1]*2//3)]
cv2.imshow("sample cut", img_cut)
cv2.imwrite("sample4_cut.jpg", img_cut)
cv2.waitKey(0)
cv2.destroyAllWindows()
