import numpy as np
import cv2
# image1 = np.zeros((400, 400), np.uint8)
# image1[:] = 255    

# image2 = np.zeros((400, 400), np.uint8)
# image2[:] = 255    
# h, w = image1.shape
# pt1 = (w // 4, h // 4)
# pt2 = (w * 3 // 4, h * 3 // 4)
# cv2.rectangle(image1, pt1, pt2, 0, 1)
# cv2.line(image1, pt1, pt2, 0, 1)
# cv2.line(image1, (w // 4, h * 3 // 4), (w * 3 // 4, h // 4), 0, 1)

# cv2.rectangle(image2, pt1, pt2, 0, 1)
# center = (w // 2, h // 2)
# cv2.circle(image2, center, w // 4, 0)
# cv2.imshow("src1", image1)
# cv2.imshow("src2", image2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# image = cv2.imread('lenna.bmp',cv2.IMREAD_COLOR)
# if image is None:
#     raise Exception("파일 읽기 오류")
# h, w = image.shape[:2]
# hang = h // 4
# yeol = w // 4
# cv2.line(image, (0, hang), (w, hang), (255,255,255), 1)
# cv2.line(image, (yeol, 0), (yeol, h), (255,255,255), 1)

# cv2.line(image, (0, hang*2), (w, hang*2), (255,255,255), 1)
# cv2.line(image, (yeol*2, 0), (yeol*2, h), (255,255,255), 1)

# cv2.line(image, (0, hang*3), (w, hang*3), (255,255,255), 1)
# cv2.line(image, (yeol*3, 0), (yeol*3, h), (255,255,255), 1)

# cv2.line(image, (0, h-hang), (w, h-hang), (255,255,255), 1)
# cv2.line(image, (w-yeol, 0), (w-yeol, h), (255,255,255), 1)
# cv2.imshow("Line", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# image = np.zeros((400, 1200, 3), np.uint8)

# image[:, 0:400] = (255, 0, 0)    
# image[:, 400:800] = (0, 255, 0)   
# image[:, 800:1200] = (0, 0, 255)

# r = image[:, 0:400]
# cv2.rectangle(r, (100, 100), (300, 300), (255, 255, 255), 15)
# c = image[:, 400:800]
# cv2.circle(c, (200, 200), 100, (255, 255, 255), 15)
# x = image[:, 800:1200]
# cv2.line(x, (100, 100), (300, 300), (255, 255, 255), 15)
# cv2.line(x, (300, 100), (100, 300), (255, 255, 255), 15)

# cv2.imshow("img", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#4번
# image = np.zeros((300, 300, 3), np.uint8)

# cnt = 0
# running = False

# while True:
#     image[:] = 255
#     cv2.putText(image, str(cnt),(120, 170),cv2.FONT_HERSHEY_SIMPLEX,3, (0, 0, 0), 5)
#     cv2.imshow('watch', image)

#     key = cv2.waitKey(1000)

#     if key == ord('s'):
#         running = True
#     elif key == ord('t'):
#         running = False
#     elif key == ord('r'):
#         cnt = 0
#         running = False
#     elif key == ord('q'):
#         break

#     if running:
#         cnt += 1

# cv2.destroyAllWindows()

#5번
image = np.zeros((500, 500, 3), np.uint8)
image[:] = 255

h, w = image.shape[:2]
rows, cols = 5, 5

ch = h // rows
cw = w // cols

row, col = 2, 2  # 시작 위치


def draw(image, r, c):
    image[:] = 255

    # grid
    for i in range(1, rows):
        cv2.line(image, (0, i * ch), (w, i * ch), (0, 0, 0), 1)

    for i in range(1, cols):
        cv2.line(image, (i * cw, 0), (i * cw, h), (0, 0, 0), 1)

    # selected cell
    x1 = c * cw
    y1 = r * ch
    x2 = (c + 1) * cw
    y2 = (r + 1) * ch

    cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), -1)

while True:
    draw(image, row, col)
    cv2.imshow("grid", image)

    key = cv2.waitKey(30)  # 핵심: 0 ❌ → 30 ⭕ (계속 루프)

    # 종료 키
    if key == 27 or key == ord('q'):
        break

    # 방향키
    if key == 224:
        key2 = cv2.waitKey(0)

        if key2 == 72:
            row -= 1
        elif key2 == 80:
            row += 1
        elif key2 == 75:
            col -= 1
        elif key2 == 77:
            col += 1

    row = max(0, min(rows - 1, row))
    col = max(0, min(cols - 1, col))

cv2.destroyAllWindows()
