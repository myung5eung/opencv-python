import cv2
import numpy as np

def mycalcGrayHist(img):
    hist = np.zeros((256, 1), np.float32)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            pixel = img[i, j]
            hist[pixel, 0] += 1
    return hist
def GrayHist(hist):
    himg = np.full((100, 256), 255, np.uint8)
    hist = cv2.normalize(hist, None, 0, himg.shape[0], cv2.NORM_MINMAX)
    for i in range(255):
        y1 = int(hist[i, 0])
        y2 = int(hist[i + 1, 0])
        cv2.line(himg, (i, 100 - y1), (i + 1, 100 - y2), 0)
    return himg
img = cv2.imread("lenna.bmp", cv2.IMREAD_GRAYSCALE)
if img is None:
    raise Exception("파일 읽기 오류")
hist = mycalcGrayHist(img)
himg = GrayHist(hist)
cv2.imshow("src", img)
cv2.imshow("srcHist", himg)
cv2.waitKey(0)
cv2.destroyAllWindows()
