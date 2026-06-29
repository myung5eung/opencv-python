import numpy as np
import cv2

image = np.zeros((500, 500, 3), np.uint8)
image[:] = 255
title = "img"
drawing = False
old_x = 0
old_y = 0
color_num = 0
def onChange(value):
    global color_num
    color_num = value
def onMouse(event, x, y, flags, param):
    global image, drawing, old_x, old_y, color_num
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        old_x = x
        old_y = y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if color_num == 0:
                color = (255, 0, 0)
            elif color_num == 1:
                color = (0, 255, 0)
            else:
                color = (0, 0, 255)

            cv2.line(image, (old_x, old_y), (x, y), color, 2)
            old_x = x
            old_y = y
            cv2.imshow(title, image)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

cv2.imshow(title, image)
cv2.createTrackbar("Color", title, 0, 2, onChange)
cv2.setMouseCallback(title, onMouse)

while True:
    cv2.imshow(title, image)
    key = cv2.waitKey(30)

    if key == ord('q'):
        break

cv2.destroyAllWindows()
