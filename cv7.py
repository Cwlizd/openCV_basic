import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("sample.jpg")

aff_matrix = cv2.getRotationMatrix2D((img.shape[1]/2, img.shape[0]/2), 30, 0.8)
img_rotate = cv2.warpAffine(img, aff_matrix, (img.shape[1], img.shape[0]))
cv2.imshow("sample rotate", img_rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("sample_ratate.jpg", img_rotate)

sample_90rotate = cv2.rotate(img, 0)
cv2.imshow("sample rotate90", sample_90rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("sample_rotate90.jpg", sample_90rotate)
