import cv2
import numpy as np


def nothing(x):
    pass


org_img = cv2.imread('mountain.jpg')

cv2.namedWindow('image')

font = cv2.FONT_HERSHEY_SIMPLEX

# create trackbars for color change
cv2.createTrackbar('value', 'image', 0, 255, nothing)

drawing = False
ix, iy = -1, -1
cx, cy = -1, -1

# mouse callback function
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, cx,cy, drawing, img

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        cx, cy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        ix, iy = -1, -1
        cx, cy = -1, -1
        drawing = False


cv2.setMouseCallback('image', draw_rectangle)





while True:
    img = org_img.copy()

    value = cv2.getTrackbarPos('value', 'image')
    if drawing == True:
        cv2.rectangle(img, (ix, iy), (cx, cy), (0, 0, 255), -1)

    cv2.putText(
        img,
        f'Mouse position : ({ix}, {iy}) - ({cx}, {cy}) - {value}',
        (10, 30),
        font,
        1,
        (0, 0, 0),
        2,
        cv2.LINE_AA
    )

    cv2.imshow('image', img)

    k = cv2.waitKey(10) & 0xFF
    if k == 27:
        break


cv2.destroyAllWindows()