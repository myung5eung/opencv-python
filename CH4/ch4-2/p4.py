import numpy as np
import cv2
image = np.zeros((300, 300, 3), np.uint8)

cnt = 0
running = False

while True:
    image[:] = 255
    cv2.putText(image, str(cnt),(120, 170),cv2.FONT_HERSHEY_SIMPLEX,3, (0, 0, 0), 5)
    cv2.imshow('watch', image)

    key = cv2.waitKey(1000)

    if key == ord('s'):
        running = True
    elif key == ord('t'):
        running = False
    elif key == ord('r'):
        cnt = 0
        running = False
    elif key == ord('q'):
        break

    if running:
        cnt += 1

cv2.destroyAllWindows()
