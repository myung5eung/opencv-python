import cv2
import numpy as np

image = cv2.imread("lenna.bmp", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("영상파일 읽기 오류")

noise = np.zeros(image.shape, dtype=np.int16)
cv2.randn(noise, 0, 20)
dst = image.astype(np.int16) + noise
dst = np.clip(dst, 0, 255).astype(np.uint8)
kernel = np.ones((9, 9), np.float32) / 81
blur = cv2.filter2D(dst, -1, kernel)
cv2.imshow("image", image)
cv2.imshow("Gaussian Noise", dst)
cv2.imshow("Blur", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
