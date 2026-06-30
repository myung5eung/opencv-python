import numpy as np
import cv2

class Paint:
    def __init__(self, image, title):
        self.image = image
        self.title = title
        self.drawing = False
        self.old_x = 0
        self.old_y = 0
        self.color_num = 0
        self.color = [(255, 0, 0),(0, 255, 0),(0, 0, 255)]

    def onChange(self, value):
        self.color_num = value

    def onMouse(self, event, x, y, flags, param):
        if (event == cv2.EVENT_LBUTTONDOWN):
            self.drawing = True
            self.old_x = x
            self.old_y = y

        elif (event == cv2.EVENT_MOUSEMOVE and self.drawing == True):
            cv2.line( self.image, (self.old_x, self.old_y), (x, y), self.color[self.color_num],2)
            self.old_x = x
            self.old_y = y
            cv2.imshow(self.title, self.image)

        elif (event == cv2.EVENT_LBUTTONUP):
            self.drawing = False


image = np.full((500, 500, 3), 255, np.uint8)
title = "img"
state = Paint(image, title)
cv2.imshow(title, image)
cv2.createTrackbar("Color", title, 0, 2, state.onChange)
cv2.setMouseCallback(title, state.onMouse)
while (True):
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()
