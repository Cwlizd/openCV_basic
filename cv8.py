import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("sample.jpg")

img_covert = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
cv2.imshow("sample L*a*b", img_covert)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("sample_Lab.jpg", img_covert)

img_bitwise_not = cv2.bitwise_not(img)
cv2.imshow("sample bitwise_not", img_bitwise_not)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("sample_bitwise_not.jpg", img_bitwise_not)
