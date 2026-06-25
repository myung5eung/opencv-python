import cv2
image = cv2.imread('lenna.bmp',cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("파일 읽기 오류")

bright = image.copy()
dark = image.copy()

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if(int(bright[i][j])+50>255):
            bright[i][j]=255
        else:
            bright[i][j]+=50
        if(int(dark[i][j])-50<0):
            dark[i][j]=0
        else:
            dark[i][j]-=50

cv2.imshow('Lenna Image', image)
cv2.imshow('bright Image', bright)
cv2.imshow('dark Image', dark)
cv2.waitKey(0)
cv2.destroyAllWindows()
