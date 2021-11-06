import cv2 as cv

cap = cv.VideoCapture(0)  # Webcam

while True:
    isSuccess, img = cap.read()
    cv.imshow('Video', img)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break
