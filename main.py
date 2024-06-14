import numpy as np
import cv2

cap = cv2.VideoCapture(0)

imgBackground = cv2.imread('Resources/background.png')

while cap.isOpened():
    flags, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('img', gray)
    cv2.imshow('img', imgBackground)
    if cv2.waitKey(0):
        break

cap.release()
cv2.destroyAllWindows()