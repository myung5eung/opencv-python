import numpy as np
import cv2
image1 = np.zeros((400, 400), np.uint8)
image1[:] = 255    

image2 = np.zeros((400, 400), np.uint8)
image2[:] = 255    
h, w = image1.shape
pt1 = (w // 4, h // 4)
pt2 = (w * 3 // 4, h * 3 // 4)
cv2.rectangle(image1, pt1, pt2, 0, 1)
cv2.line(image1, pt1, pt2, 0, 1)
cv2.line(image1, (w // 4, h * 3 // 4), (w * 3 // 4, h // 4), 0, 1)

cv2.rectangle(image2, pt1, pt2, 0, 1)
center = (w // 2, h // 2)
cv2.circle(image2, center, w // 4, 0)
cv2.imshow("src1", image1)
cv2.imshow("src2", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#5번
import numpy as np
import cv2
image = np.zeros((500, 500, 3), np.uint8)

rows, cols = 5, 5
h, w = image.shape[:2]
ch = h//rows
cw = w//cols
row, col= 2, 2

while True:
    image[:] = 255

    for i in range(1, rows):
        cv2.line(image, (0, i * ch), (w, i * ch), (0, 0, 0), 1)
    for i in range(1, cols):
        cv2.line(image, (i * cw, 0), (i * cw, h), (0, 0, 0), 1)

    cv2.rectangle(image,(col * cw, row * ch),((col + 1) * cw, (row + 1) * ch),(255, 0, 0),-1)
    cv2.imshow("src", image)
    key = cv2.waitKeyEx(30)
    if key == ord('q'):
        break
    elif key == 0x260000:
        row -= 1
    elif key == 0x280000:
        row += 1
    elif key == 0x250000:
        col -= 1
    elif key == 0x270000:
        col += 1
    row = max(0, min(rows - 1, row))
    col = max(0, min(cols - 1, col))

cv2.destroyAllWindows()
