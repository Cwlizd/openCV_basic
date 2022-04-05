import numpy as np
import matplotlib.pyplot as plt
import cv2

img = np.array([[(150, 120, 150) for x in range(601)] for x in range(601)])
img = img.astype(np.uint8)
print(type(img))
print(img.shape)

cv2.imshow("sample2", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("sample2.jpg", img)
