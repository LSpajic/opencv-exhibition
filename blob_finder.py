import cv2, time, numpy as np

video = cv2.VideoCapture(0)

a = 0
largeBlur = np.ones((7, 7), dtype="float") * (1.0 / (7 * 7))
detector =cv2.SimpleBlobDetector()
while True:
    a = a + 1

    check, frame = video.read()
    frame = cv2.filter2D(frame, -1, largeBlur)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    g_bijela = np.array([0,0,0], dtype=np.uint8)
    do_bijela = np.array([255,255,30], dtype=np.uint8)

    # print(check)
    # print(frame)

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing", frame)

    mask = cv2.inRange(hsv, g_bijela, do_bijela)
    #ovdje ide kod za trazenje blobova 
    cv2.imshow("mask",mask)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

print (a)
video.release()