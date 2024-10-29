import cv2
capture = cv2 Virtualcapture(0)

while True:
    _, frame = capture.read()
    cv2.imshow("capture from webcam", frame)
    if cv2.waitkey(1) == 27:
        break
capture.release()
cv2.destroyAllwindows()