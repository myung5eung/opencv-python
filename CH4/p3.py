import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"좌표: ({x},{y}), 화소값(B,G,R): {int(param[y,x][0]),int(param[y,x][1]),int(param[y,x][2])}")

image =  cv2.imread('lenna.bmp',cv2.IMREAD_COLOR)
if image is None:
    raise Exception("파일 읽기 오류")

cv2.imshow('Mouse Event', image)
cv2.setMouseCallback('Mouse Event', onMouse, image)
while True:
    key=cv2.waitKey(1)
    if key ==27:
        break
cv2.destroyAllWindows()
