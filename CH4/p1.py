import numpy as np
import cv2
lu=0
ld=0
mm=0

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global ld
        ld+=1
        print(f"EVENT_LBUTTONDOWN: {ld}")
    elif event == cv2.EVENT_LBUTTONUP:
        global lu
        lu+=1
        print(f"EVENT_LBUTTONUP: {lu}")
    elif event == cv2.EVENT_MOUSEMOVE:
        global mm
        mm+=1
        print(f"EVENT_MOUSEMOVE: {mm}")

image =  cv2.imread('lenna.bmp',cv2.IMREAD_COLOR)
if image is None:
    raise Exception("파일 읽기 오류")

cv2.imshow('Mouse Event', image)
cv2.setMouseCallback('Mouse Event', onMouse)

cv2.waitKey(0)
cv2.destroyAllWindows()
