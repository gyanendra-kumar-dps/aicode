import cv2
import numpy as np
cam=cv2.VideoCapture(0)
while True:
    _,cap=cam.read()
    hsv=cv2.cvtColor(cap,cv2.COLOR_BGR2HSV)
    min_range=np.array([0,20,70],dtype='uint8')
    max_range=np.array([20,255,255],dtype='uint8')
    m=cv2.inRange(hsv,min_range,max_range)
    res=cv2.bitwise_and(cap,cap,mask=m)
    cont,_=cv2.findContours(m,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    if cont:
        max_cont=max(cont,key=cv2.contourArea)
        if cv2.contourArea(max_cont)>500:
            w,x,y,z=cv2.boundingRect(max_cont)
            cv2.rectangle(cap,(w,x),(w+y,x+z),(0,255,0),3)
            centx=w+y//2
            centy=x+z//2
            cv2.circle(cap,(centx,centy),5,(0,0,255))
    cv2.imshow('win',res)
    cv2.waitKey(1)