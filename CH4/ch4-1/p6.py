import numpy as np
import cv2

image = np.zeros((200, 400, 3), np.uint8)
i=0

while True:
    image.fill(0)
    image[:,:,i%3].fill(255)
    i = i+1
    cv2.imshow('win', image)
    if cv2.waitKey(1000) == 27: break
cv2.destroyAllWindows()
