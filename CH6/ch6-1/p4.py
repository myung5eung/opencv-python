import cv2
import numpy as np

class srcimage:
    def __init__(self, image):
        self.image = image
        self.start = None
        self.drawing = False
        cv2.imshow("image", self.image)
        cv2.setMouseCallback("image", self.onMouse)

    def onMouse(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.start = (x, y)
            self.drawing = True
        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing = False
            x1, y1 = self.start
            x2, y2 = x, y
            x_min, x_max = min(x1, x2), max(x1, x2)
            y_min, y_max = min(y1, y2), max(y1, y2)
            roi = self.image[y_min:y_max, x_min:x_max]
            roi = cv2.add(roi, 100)
            self.image[y_min:y_max, x_min:x_max] = roi
            cv2.imshow("image", self.image)

image = cv2.imread("lenna.bmp", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("파일 읽기 오류")

app = srcimage(image)

cv2.waitKey(0)
cv2.destroyAllWindows()
