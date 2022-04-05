import numpy as np
import matplotlib.pyplot as plt
import cv2

img = np.array([[(x, int((x+y)/2), y) for x in range(256)]
               for y in range(256)])

img = img.astype(np.uint8)

cv2.imshow("sample3", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("sample3.jpg", img)
