import cv2
import numpy as np

img = cv2.imread("lenna.bmp", cv2.IMREAD_GRAYSCALE)
if img is None:
    raise Exception("파일 읽기 오류")

count = img.shape[0] * img.shape[1]  #영상의 전체 픽셀 수를 계산함
minVal, maxVal, _, _ = cv2.minMaxLoc(img)  #영상의 최소 픽셀값과 최대 픽셀값을 구함
hist = cv2.calcHist([img], [0], None, [256], [0, 256])  #그레이스케일 영상의 히스토그램을 구함

maxf = 0  #가장 큰 빈도수를 저장할 변수
maxp = 0  #가장 큰 빈도수를 가진 픽셀값을 저장할 변수

for i in range(256):
    if hist[i, 0] > maxf:
        maxf = int(hist[i, 0])  #빈도수를 저장함
        maxp = i  #픽셀값을 저장함

f80 = int(hist[80, 0])  #픽셀값 80의 빈도수를 구함
print(f"영상의 전체 픽셀수: {count}")
print(f"영상에서 픽셀값의 최소값: {int(minVal)}")
print(f"영상에서 픽셀값의 최대값: {int(maxVal)}")
print(f"빈도수가 가장 많은 픽셀값과 빈도수: {maxp}, {maxf}")
print(f"픽셀값 80의 빈도수: {f80}")

cv2.imshow("src", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
