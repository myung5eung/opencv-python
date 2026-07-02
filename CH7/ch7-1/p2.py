import numpy as np, cv2, time
image = cv2.imread("lenna.bmp", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

kernel = np.ones((7, 7), np.float32) / 49
blur = cv2.filter2D(image, -1, kernel)
cv2.imshow("image1", image)
cv2.imshow("blur3", blur)
cv2.waitKey(0)
kernel2 = np.array([[-1, -1, -1],
[-1, 9, -1],
[-1, -1, -1]], dtype=np.float32)
sharp = cv2.filter2D(image, -1, kernel2)
cv2.imshow("image2", image)
cv2.imshow("sharp", sharp)
cv2.waitKey(0)
