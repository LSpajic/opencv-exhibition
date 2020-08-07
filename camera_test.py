import cv2, time, numpy as np

sharpen = np.array((
	[0, -1, 0],
	[-1, 5, -1],
	[0, -1, 0]), dtype="int")

largeBlur = np.ones((21, 21), dtype="float") * (1.0 / (21 * 21))


video = cv2.VideoCapture(0)

a = 0

while True:
    a = a + 1

    check, frame = video.read()

    # print(check)
    # print(frame)

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.filter2D(frame, -1, largeBlur)
    cv2.imshow("Capturing", frame)

    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

print (a)
video.release()
