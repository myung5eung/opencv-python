import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        image[:,:,2].fill(0)
        image[:,:,1].fill(0)
        image[:,:,0].fill(255)
        cv2.imshow(title, param)
    elif event == cv2.EVENT_LBUTTONDOWN :
        image[:,:,2].fill(255)
        image[:,:,1].fill(0)
        image[:,:,0].fill(0)
        cv2.imshow(title, param)

image = np.zeros((300, 500, 3), np.uint8)
title = "Trackbar & Mouse Event"
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse, image)
while True:
    key=cv2.waitKey(1)
    if key ==27:
        break
cv2.destroyAllWindows()
