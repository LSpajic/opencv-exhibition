import cv2, time, numpy as np

video = cv2.VideoCapture(0)

a = 0

while True:
    a = a + 1

    check, frame = video.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    g_bijela = np.array([0,0,200], dtype=np.uint8)
    do_bijela = np.array([255,55,255], dtype=np.uint8)

    # print(check)
    # print(frame)

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing", frame)
    mask = cv2.inRange(hsv, g_bijela, do_bijela)

    cv2.imshow('mask',mask)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

print (a)
video.release()