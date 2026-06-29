import numpy as np
import cv2
image1 = np.zeros((400, 400), np.uint8)
image1[:] = 255    

image2 = np.zeros((400, 400), np.uint8)
image2[:] = 255    
h, w = image1.shape
pt1 = (w // 4, h // 4)
pt2 = (w * 3 // 4, h * 3 // 4)
cv2.rectangle(image1, pt1, pt2, 0, 1)
cv2.line(image1, pt1, pt2, 0, 1)
cv2.line(image1, (w // 4, h * 3 // 4), (w * 3 // 4, h // 4), 0, 1)

cv2.rectangle(image2, pt1, pt2, 0, 1)
center = (w // 2, h // 2)
cv2.circle(image2, center, w // 4, 0)
cv2.imshow("src1", image1)
cv2.imshow("src2", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
