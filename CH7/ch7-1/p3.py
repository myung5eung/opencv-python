import numpy as np, cv2, time
image = cv2.imread("rose.bmp", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")
# 엠보싱 마스크 원소 지정
kernel = np.array([[-1, 0, 1],
[-2, 0, 2],
[-1, 0, 1]], dtype=np.float32)
sharp = cv2.filter2D(image, -1, kernel, delta=128)
cv2.imshow("image", image)
cv2.imshow("sharp", sharp)
cv2.waitKey(0)

#0으로설정
import numpy as np, cv2, time
image = cv2.imread("rose.bmp", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")
# 엠보싱 마스크 원소 지정
kernel = np.array([[-1, 0, 1],
[-2, 0, 2],
[-1, 0, 1]], dtype=np.float32)
sharp = cv2.filter2D(image, -1, kernel, delta=0)
cv2.imshow("image", image)
cv2.imshow("sharp", sharp)
cv2.waitKey(0)
