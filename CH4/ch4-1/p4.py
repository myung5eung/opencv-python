import numpy as np
import cv2

c = 0

def onChange(value):
    global c
    c += 1
    print(f"트랙바 이벤트 횟수: {c}\n트랙바 위치: {value}")

image = cv2.imread('lenna.bmp',cv2.IMREAD_COLOR)
title = "Trackbar"
cv2.imshow(title, image)
cv2.createTrackbar("bar", title, 0, 255, onChange)

while True:
    if cv2.waitKey(1000) == 27: break
cv2.destroyAllWindows()
