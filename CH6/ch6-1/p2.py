import cv2

def onChange(value):
    dst = cv2.add(image, value) #image의 모든 픽셀값에 트랙바 값 value를 더함
    cv2.imshow("dst", dst)  #밝기가 조절된 결과 영상을 화면에 출력함

image = cv2.imread("lenna.bmp", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("파일 읽기 오류")

cv2.imshow("dst", image)

cv2.createTrackbar("bar", "dst", 0, 100, onChange) #창에 0~100 범위인 트랙바를 생성하고 값이 변하면 onChange 실행

cv2.waitKey(0)
cv2.destroyAllWindows()
