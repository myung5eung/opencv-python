import cv2
import numpy as np
img = cv2.imread("lenna.bmp", cv2.IMREAD_GRAYSCALE)
if img is None:
    raise Exception("파일 읽기 오류")
minVal1, maxVal1, _, _ = cv2.minMaxLoc(img)
con1 = maxVal1 - minVal1
scale = 2
bright = np.zeros(img.shape, img.dtype)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        tmp = scale * int(img[i, j])
        if (tmp > 255):
            bright[i, j] = 255
        elif tmp < 0:
            bright[i, j] = 0
        else:
            bright[i, j] = tmp

minVal2, maxVal2, _, _ = cv2.minMaxLoc(bright)
con2 = maxVal2 - minVal2
alpha = 2
beta = -128 * alpha + 128
dark = np.zeros(img.shape, img.dtype)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        tmp = alpha * int(img[i, j]) + beta
        if (tmp > 255):
            dark[i, j] = 255
        elif (tmp < 0):
            dark[i, j] = 0
        else:
            dark[i, j] = tmp

minVal3, maxVal3, _, _ = cv2.minMaxLoc(dark)
con3 = maxVal3 - minVal3
print(f"원본 영상의 최소값: {minVal1}, 최대값: {maxVal1}, 명암비: {con1}")
print(f"기본적인 명암비 조절의 최소값: {minVal2}, 최대값: {maxVal2}, 명암비: {con2}")
print(f"효과적인 명암비 조절의 최소값: {minVal3}, 최대값: {maxVal3}, 명암비: {con3}")
cv2.imshow("img", img)
cv2.imshow("bright", bright)
cv2.imshow("dark", dark)

cv2.waitKey(0)
cv2.destroyAllWindows()
