import cv2
import time
from pynput.mouse import Button, Controller

class Contar:
    def __init__(self):
        self.start = 0
        self.finish = 100
        self.final_time = 1
        self.counter = 0
        self.list = []


timer = Contar()
mouse = Controller()


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyes_cascade = cv2.CascadeClassifier("CustomBlinkCascade.xml")
video_capture = cv2.VideoCapture(0)


while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5 , minSize=(20, 30),
                                          flags=cv2.cv.CV_HAAR_SCALE_IMAGE)
    # Draw a rectangle around the faces

    for (x, y, w, h) in faces:
        for i in range(4):
            timer.start = time.time()
            # cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            eyes = eyes_cascade.detectMultiScale(roi_gray, scaleFactor=1.6, minNeighbors=5)#, minSize=(20, 30),
                                              #flags=cv2.cv.CV_HAAR_SCALE_IMAGE)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)
                timer.start = time.time()
            timer.finish = time.time()
            timer.final_time = timer.finish - timer.start
        if timer.final_time == 0:
            timer.counter += 1
        else:
            timer.counter = 0
            print(timer.final_time)
        if timer.counter == 4:
            mouse.click(Button.left, 1)
            print('click')
        else:
            pass
    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()