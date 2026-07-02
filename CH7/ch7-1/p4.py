import cv2
import numpy as np
class SrcImage:
    def __init__(self, image):
        self.image = image
        self.start = None
        self.kernel = np.ones((5, 5), np.float32) / 25
        cv2.imshow("image", self.image)
        cv2.setMouseCallback("image", self.onMouse)

    def onMouse(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.start = (x, y)
        elif event == cv2.EVENT_LBUTTONUP:
            if self.start is None:
                return
            x1, y1 = self.start
            x2, y2 = x, y
            x_min, x_max = min(x1, x2), max(x1, x2)
            y_min, y_max = min(y1, y2), max(y1, y2)
            if (x_max - x_min) < 2 or (y_max - y_min) < 2:
                return
            roi = self.image[y_min:y_max, x_min:x_max].copy()
            roii = cv2.filter2D(roi, -1, self.kernel)
            self.image[y_min:y_max, x_min:x_max] = roii

            cv2.imshow("image", self.image)


image = cv2.imread("lenna.bmp", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("파일 읽기 오류")

g = SrcImage(image)

cv2.waitKey(0)
cv2.destroyAllWindows()
