import cv2

class LennaG:
    def __init__(self, image):
        self.image = image
        self.b = 0 #밝기 변화량
        self.mode = 0 #트랙바 
        cv2.imshow("dst", self.image)
        cv2.createTrackbar("mode", "dst", 0, 1, self.onChange) #창에 0~1 범위인 트랙바를 생성하고 값이 변하면 onChange 실행
        cv2.setMouseCallback("dst", self.onMouse) #dst창에서 마우스 이벤트가 발생하면 onMouse 실행

    def onChange(self, value):
        self.mode = value #트랙바 값을 mode에 저장

    def onMouse(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            if self.mode == 0: 
                self.b += 10
            else:
                self.b -= 10
            if self.b >= 0:
                dst = cv2.add(self.image, self.b)  #image의 모든 픽셀값에 밝기 변화량을 더함
            else:
                dst = cv2.subtract(self.image, -self.b) #뺌

            cv2.imshow("dst", dst)  #밝기가 조절된 결과 영상을 화면에 출력함


image = cv2.imread("lenna.bmp", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("파일 읽기 오류")

g = LennaG(image) #LennaG 객체를 생성하고 프로그램이 끝날 때까지 유지하기 위함

cv2.waitKey(0)
cv2.destroyAllWindows()
