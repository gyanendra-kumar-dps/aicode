import cv2
fd=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
camera=cv2.VideoCapture(0)
while True:
    r,frame=camera.read()
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=fd.detectMultiScale(gray_frame,1.1,5,minSize=(30,30))
    for (w,x,y,z) in faces:
        cv2.rectangle(frame,(w,x),(w+y,x+z),(255,0,255),2)
    cv2.putText(frame,f"Face count:{len(faces)}",(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),2,cv2.LINE_AA)
    cv2.imshow('win',frame)
    cv2.waitKey(1)