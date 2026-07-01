import cv2
import numpy as np

def mycalcGrayHist(img):
    hist = np.zeros((256, 1), np.float32)  # 256개의 빈을 가진 히스토그램 배열을 생성함

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            pixel = img[i, j]  # 현재 위치의 픽셀값을 가져옴
            hist[pixel, 0] += 1  # 해당 픽셀값의 빈도수를 1 증가시킴

    return hist  # 직접 계산한 히스토그램을 반환함

def mydrawGrayHistImage(hist):
    himg = np.full((100, 256), 255, np.uint8)  # 히스토그램을 그릴 흰색 영상을 생성함

    hist = cv2.normalize(hist, None, 0, himg.shape[0] - 1, cv2.NORM_MINMAX)  # 빈도수를 영상 높이에 맞게 정규화함

    for i in range(255):
        y1 = int(hist[i, 0])  # 현재 픽셀값의 정규화된 빈도수를 저장함
        y2 = int(hist[i + 1, 0])  # 다음 픽셀값의 정규화된 빈도수를 저장함

        cv2.line(himg, (i, 99 - y1), (i + 1, 99 - y2), 0)  # 현재 빈도수와 다음 빈도수를 직선으로 연결함

    return himg  # 히스토그램 그래프 영상을 반환함

img = cv2.imread("lenna.bmp", cv2.IMREAD_GRAYSCALE)
if img is None:
    raise Exception("파일 읽기 오류")

hist = mycalcGrayHist(img)  # cv2.calcHist를 사용하지 않고 히스토그램을 직접 계산함
himg = mydrawGrayHistImage(hist)  # 히스토그램을 선 그래프로 그림

cv2.imshow("src", img)
cv2.imshow("srcHist", himg)

cv2.waitKey(0)
cv2.destroyAllWindows()
