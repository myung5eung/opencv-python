import numpy as np
import cv2

image = cv2.imread('lenna.bmp', cv2.IMREAD_COLOR)
if image is None:
    raise Exception("파일 읽기 오류")

h, w = image.shape[:2]
hang = h // 4
yeol = w // 4

for i in range(1, 4):
    cv2.line(image, (0, hang * i), (w, hang * i), (255, 255, 255), 1)
    cv2.line(image, (yeol * i, 0), (yeol * i, h), (255, 255, 255), 1)

cv2.imshow("Line", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
