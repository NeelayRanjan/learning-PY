import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of green color in HSV
    lower_green = np.array([100,50,50])
    upper_green = np.array([130,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_green, upper_green)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
    cv.imshow('original',frame)
    cv.imshow('mask',mask)
    cv.imshow('result',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
