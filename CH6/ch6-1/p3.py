import cv2

class BrightnessApp:
    def __init__(self, image):
        self.image = image
        self.b = 0
        cv2.imshow("dst", self.image)
        cv2.createTrackbar("bar", "dst", 0, 1, self.onChange)
        cv2.setMouseCallback("dst", self.onMouse)

    def onChange(self, value):
        self.show()

    def onMouse(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            mode = cv2.getTrackbarPos("bar", "dst")
            if mode == 0:
                self.b += 10
            else:
                self.b -= 10
            self.b = max(-255, min(255, self.b))
            self.show()

    def show(self):
        if self.b >= 0:
            dst = cv2.add(self.image, self.b)
        else:
            dst = cv2.subtract(self.image, -self.b)

        cv2.imshow("dst", dst)


image = cv2.imread("lenna.bmp", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("파일 읽기 오류")
a = BrightnessApp(image)

cv2.waitKey(0)
cv2.destroyAllWindows()
