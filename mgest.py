import mediapipe as mps
import cv2
import os
# current_volume = int(os.c(
#         "osascript -e 'output volume of (get volume settings)'"
#     ))
cam=cv2.VideoCapture(0)
hand=mps.solutions.hands
hand_obj=hand.Hands(min_detection_confidence=0.7,min_tracking_confidence=0.7)
draw=mps.solutions.drawing_utils
while True:
    _,ret=cam.read()
    result=hand_obj.process(cv2.cvtColor(ret, cv2.COLOR_BGR2RGB))
    if result.multi_hand_landmarks:
        for i,handlm in enumerate(result.multi_hand_landmarks):  
            draw.draw_landmarks(ret,handlm,hand.HAND_CONNECTIONS)
    cv2.imshow('',ret)
    cv2.waitKey(1)