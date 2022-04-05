import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("sample.jpg")
cv2.imshow("sampic", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
