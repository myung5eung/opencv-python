import cv2

def onChange(value):
    dst = cv2.add(image, value)
    cv2.imshow("dst", dst)

image = cv2.imread("lenna.bmp", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("파일 읽기 오류")

cv2.imshow("dst", image)

cv2.createTrackbar("bar", "dst", 0, 100, onChange)

cv2.waitKey(0)
cv2.destroyAllWindows()
