import numpy as np
import cv2

image = np.zeros((500, 500, 3), np.uint8)
image[:] = 255
x, y = 250, 250
step = 50
while True:
    cv2.imshow("src", image)
    key = cv2.waitKeyEx(30)
    if key == ord('q'):
        break
    elif key == 0x250000:
        nx = x - step
        ny = y
        if nx >= 0:
            cv2.line(image, (x, y), (nx, ny), (0, 0, 0), 1)
            x, y = nx, ny
    elif key == 0x260000:
        nx = x
        ny = y - step
        if ny >= 0:
            cv2.line(image, (x, y), (nx, ny), (0, 0, 0), 1)
            x, y = nx, ny
    elif key == 0x270000:
        nx = x + step
        ny = y
        if nx < 500:
            cv2.line(image, (x, y), (nx, ny), (0, 0, 0), 1)
            x, y = nx, ny
    elif key == 0x280000:
        nx = x
        ny = y + step
        if ny < 500:
            cv2.line(image, (x, y), (nx, ny), (0, 0, 0), 1)
            x, y = nx, ny
cv2.destroyAllWindows()
