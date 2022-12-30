import cv2
from deepface import DeepFace
import numpy as np
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video=cv2.VideoCapture(0)

while video.isOpened():

    _ , frame = video.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=5)

    for x,y,w,h in face:

        img = cv2.rectangle(frame,(x,y),(x+w,y+h), (0,0,255),1)
        try:

            analyze = DeepFace.analyze(frame,actions=['emotion'])
            x = analyze['dominant_emotion']
            #print(x)
            #text = str(x)

        except:


            print("No face")

    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    fontColor = (255, 0, 0)

    org = (240, 350)
    text = str(x)

    cv2.putText(frame,text, org, font, fontScale, fontColor)
    cv2.imshow('video', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):

        break

video.release()
cv2.destroyAllWindows()

#Test(1)<On Image>
# img=cv2.imread('happy.jpg')
# analyze = DeepFace.analyze(img,actions=['emotion'])
# print(analyze)
# print(analyze['dominant_emotion'])





