import cv2
import numpy as np

def nothing(x):
    pass


cap = cv2.VideoCapture(0)
cv2.namedWindow('TrackBar')
cv2.createTrackbar('L - H', 'TrackBar', 0, 179, nothing)
cv2.createTrackbar('L - S', 'TrackBar', 0, 255, nothing)
cv2.createTrackbar('L - V', 'TrackBar', 0, 255, nothing)
cv2.createTrackbar('U - H', 'TrackBar', 179, 179, nothing)
cv2.createTrackbar('U - S', 'TrackBar', 255, 255, nothing)
cv2.createTrackbar('U - V', 'TrackBar', 255, 255, nothing)



while(1):
    # Take each frame
    ret, frame = cap.read()
    if ret == False :
        break
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos('L - H', 'TrackBar')
    l_s = cv2.getTrackbarPos('L - S', 'TrackBar')
    l_v = cv2.getTrackbarPos('L - V', 'TrackBar')
    u_h = cv2.getTrackbarPos('U - H', 'TrackBar')
    u_s = cv2.getTrackbarPos('U - S', 'TrackBar')
    u_v = cv2.getTrackbarPos('U - V', 'TrackBar')


    # define range of blue color in HSV
    lower_color = np.array([l_h, l_s, l_v])
    upper_color = np.array([u_h, u_s,u_v])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_color, upper_color)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()