import cv2
import numpy as np

capture = cv2.VideoCapture("stopwatch.avi")
if not capture.isOpened():
    raise Exception("파일 읽기 오류")
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = capture.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps)
size = (width, height)                    
fourcc = cv2.VideoWriter_fourcc(*'XVID')
writer = cv2.VideoWriter("output.avi", fourcc, fps, size)
if not writer.isOpened():
    raise Exception("동영상 파일 저장 오류")
while True:
    ret, frame = capture.read()
    if not ret:
        break
    result = cv2.add(frame, 100)
    writer.write(result)
    cv2.imshow("original", frame)
    cv2.imshow("output", result)
    key = cv2.waitKey(delay)
    if key == ord('q') or key == ord('Q'):
        break

capture.release()
writer.release()
cv2.destroyAllWindows()
