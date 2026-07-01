import cv2
import numpy as np

img = cv2.imread("lenna.bmp", cv2.IMREAD_GRAYSCALE)
if img is None:
    raise Exception("파일 읽기 오류")

rows, cols = img.shape
dst = np.zeros((rows, cols),np.uint8)

for i in range(rows):
    for j in range(cols):
        x = int(img[i, j])

        if (x < 128):
            y = (78 / 128) * x + 50
        else:
            y = (72 / 127) * (x - 128) + 128

        if (y > 255):
            y = 255
        elif y < 0:
            y = 0
        dst[i, j] = int(y)
cv2.imshow("input", img)
cv2.imshow("output", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
