import cv2
face_detector=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)
while True:
    r,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face=face_detector.detectMultiScale(gray,1.1,5,minSize=(40,40))
    for (w,x,y,z) in face:
        cv2.rectangle(gray,(w,x),(w+y,x+z),(255,0,255),2)
    cv2.imshow('win',gray)
    cv2.waitKey(1)