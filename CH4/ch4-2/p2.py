import numpy as np
import cv2

image = cv2.imread('lenna.bmp',cv2.IMREAD_COLOR)
if image is None:
    raise Exception("파일 읽기 오류")
h, w = image.shape[:2]
hang = h // 4
yeol = w // 4
cv2.line(image, (0, hang), (w, hang), (255,255,255), 1)
cv2.line(image, (yeol, 0), (yeol, h), (255,255,255), 1)

cv2.line(image, (0, hang*2), (w, hang*2), (255,255,255), 1)
cv2.line(image, (yeol*2, 0), (yeol*2, h), (255,255,255), 1)

cv2.line(image, (0, hang*3), (w, hang*3), (255,255,255), 1)
cv2.line(image, (yeol*3, 0), (yeol*3, h), (255,255,255), 1)

cv2.line(image, (0, h-hang), (w, h-hang), (255,255,255), 1)
cv2.line(image, (w-yeol, 0), (w-yeol, h), (255,255,255), 1)
cv2.imshow("Line", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
