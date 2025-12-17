import mediapipe as mp
import cv2
import pyautogui as pg
mp_hands=mp.solutions.hands
mp_obj=mp_hands.Hands(min_detection_confidence=0.5)
mp_draw=mp.solutions.drawing_utils
def gesture(a,b):
    fings=[]
    tips=[mp_hands.HandLandmark.INDEX_FINGER_TIP,mp_hands.HandLandmark.RING_FINGER_TIP,mp_hands.HandLandmark.MIDDLE_FINGER_TIP,mp_hands.HandLandmark.PINKY_TIP]
    for i in tips:
        if a.landmark[i].y<a.landmark[i-2].y:
            fings.append(1)
    thumb=a.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumbi=a.landmark[mp_hands.HandLandmark.THUMB_IP]
    if b=="Right" and thumb.x>thumbi.x or b=="Left" and thumb.x<thumbi.x:
        fings.append(1)
    if sum(fings)==5:
        return True
    else:
        return False
cam=cv2.VideoCapture(0)
while True:
    _,cap=cam.read()
    res=mp_obj.process(cv2.cvtColor(cap,cv2.COLOR_BGR2RGB))
    if res.multi_hand_landmarks:
        for i,j in zip(res.multi_hand_landmarks,res.multi_handedness):
            hinfo=j.classification[0].label
            gest=gesture(i,hinfo) 
            mp_draw.draw_landmarks(cap,i,mp_hands.HAND_CONNECTIONS)
            print(gest)
            if gest:
                pg.scroll(500)
            else:
                pg.scroll(-500)
    cv2.imshow('win',cap)
    cv2.waitKey(1)