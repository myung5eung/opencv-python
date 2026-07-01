import cv2
import numpy as np

img = cv2.imread("lenna.bmp", cv2.IMREAD_GRAYSCALE)
if img is None:
    raise Exception("파일 읽기 오류")

count= img.shape[0]*img.shape[1] 
minVal, maxVal, _, _ = cv2.minMaxLoc(img)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
maxf = int(hist.max())
maxp = int(hist.argmax())
f80 = int(hist[80, 0])
print(f"영상의 전체 픽셀수: {count}")
print(f"영상에서 픽셀값의 최소값: {int(minVal)}")
print(f"영상에서 픽셀값의 최대값: {int(maxVal)}")
print(f"빈도수가 가장 많은 픽셀값과 빈도수: {maxp}, {maxf}")
print(f"픽셀값 80의 빈도수: {f80}")
cv2.imshow("src", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
