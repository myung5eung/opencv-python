import cv2

camera = cv2.VideoCapture(0) # 0번 카메라 연결
if camera.isOpened() == False: raise Exception("카메라 연결 안됨")
width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("width: %d" % width)
print("height: %d" % height)
fps = 10 # 초당 프레임 수
delay = round(1000/ fps) # 프레임 간 지연 시간
size = (width, height) # 동영상 파일 해상도
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # 압축 코덱 설정
writer = None
recording=False

while True:
    
    ret, frame = camera.read()
    if not ret:
        break
    cv2.imshow("frame", frame)
    key = cv2.waitKey(delay)
    if key == ord('s'):
        if writer is None:
            filename = input("저장할 파일명 입력: ")
            writer = cv2.VideoWriter(filename, fourcc, fps, size)
            recording = True
        else:
            print("재시작")
        
        recording=True

        
    elif key == ord('e'):
        if recording == True:
            recording = False
            print("일시정지")
            cur_key='e'

    elif key == ord('q') or key == ord('Q'):
        break

    if recording == True and writer is not None:
        writer.write(frame)

if writer is not None:
    writer.release()
camera.release()
cv2.destroyAllWindows()  
