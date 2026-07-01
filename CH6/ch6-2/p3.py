import cv2
import numpy as np

img = cv2.imread("lenna.bmp", cv2.IMREAD_GRAYSCALE)
if img is None:
    raise Exception("파일 읽기 오류")

rows, cols = img.shape  #행과 열 크기를 저장함
dst = np.zeros((rows, cols), np.uint8)  #결과 영상을 저장할 배열 생성

for i in range(rows):
    for j in range(cols):
        x = int(img[i, j])  #현재 위치의 원본 픽셀값을 정수형으로 저장함

        if x < 128:
            y = (78 / 128) * x + 50  #x가 128보다 작을 때 첫 번째 직선식 적용
        else:
            y = (72 / 127) * (x - 128) + 128  #x가 128 이상일 때 두 번째 직선식 적용

        if y > 255:
            y = 255  #255보다 크면 255로 저장함
        elif y < 0:
            y = 0  #0보다 작으면 0으로 저장함

        dst[i, j] = int(y)  #계산된 픽셀값을 결과 영상에 저장함

cv2.imshow("input", img)
cv2.imshow("output", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
