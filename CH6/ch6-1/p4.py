import cv2

class srcimage:
    def __init__(self, image):
        self.image = image
        self.start = None  #마우스 드래그 시작 좌표를 저장함

        cv2.imshow("image", self.image)
        cv2.setMouseCallback("image", self.onMouse)  #image 창에서 마우스 이벤트가 발생하면 onMouse 실행

    def onMouse(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.start = (x, y)  #왼쪽 버튼을 누른 위치를 시작 좌표로 저장함

        elif event == cv2.EVENT_LBUTTONUP:
            x1, y1 = self.start  #저장된 시작 좌표를 가져옴
            x2, y2 = x, y  #마우스를 뗀 위치를 끝 좌표로 저장함

            x_min, x_max = min(x1, x2), max(x1, x2)  #선택 영역의 x좌표 범위를 구함
            y_min, y_max = min(y1, y2), max(y1, y2)  #선택 영역의 y좌표 범위를 구함

            if x_min == x_max or y_min == y_max:
                return  #선택한 영역의 크기가 0이면 처리하지 않아서 그냥 리턴

            roi = self.image[y_min:y_max, x_min:x_max]  #마우스로 드래그한 영역만 잘라냄
            roi = cv2.add(roi, 100)  #선택한 영역의 모든 픽셀값에 100을 더함
            self.image[y_min:y_max, x_min:x_max] = roi  #밝게 만든 영역을 원본 영상에 다시 저장함

            cv2.imshow("image", self.image)  #밝기가 조절된 결과 영상을 화면에 출력함


image = cv2.imread("lenna.bmp", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("파일 읽기 오류")

g = srcimage(image) #객체를 생성하고 프로그램이 끝날 때까지 유지하기 위함

cv2.waitKey(0)
cv2.destroyAllWindows()
