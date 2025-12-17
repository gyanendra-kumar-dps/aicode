import mediapipe as mp
import cv2
import numpy as np
import time
cam=cv2.VideoCapture(0)
hand_lib=mp.solutions.hands
hand_obj=hand_lib.Hands(min_detection_confidence=0.7)
drawing_utils=mp.solutions.drawing_utils
FILTERS=[None,'negative','sepia','blur','grayscale','sobel','laplacian','scharr']
current_filter=0
DEBOUNCE=1
pinch=False
capture_request=False
pinching_progress=True
def get_filter(image,filter_type):
    if filter_type=='negative':
        return cv2.bitwise_not(image)
    elif filter_type=='sepia':
        sepia_filter=np.array([[0.272, 0.534, 0.131],[0.349, 0.686, 0.168],[0.393, 0.769, 0.189]])
        return np.clip(cv2.transform(image,sepia_filter),0,255).astype('uint8')
    elif filter_type=='blur':
        return cv2.GaussianBlur(image,(15,15),sigmaX=1)
    elif filter_type=='grayscale':
        return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    elif filter_type=='sobel':
        sobelx=cv2.Sobel(image,cv2.CV_64F,1,0,ksize=3)
        sobely=cv2.Sobel(image,cv2.CV_64F,0,1,ksize=3)
        sobelxy=cv2.bitwise_or(sobelx.astype('uint8'),sobely.astype('uint8'))
        return sobelxy
    elif filter_type=='laplacian':
        lap=cv2.Laplacian(image,cv2.CV_64F)
        return lap
    elif filter_type=='scharr':
        scharr=cv2.Scharr(image,cv2.CV_64F,1,0)
        return scharr
    return image
while True:
    _,cap=cam.read()
    h,w=cap.shape[:2]
    img_rgb=cv2.cvtColor(cap,cv2.COLOR_BGR2RGB)
    results=hand_obj.process(img_rgb)
    if results.multi_hand_landmarks:
        for i in results.multi_hand_landmarks:
            drawing_utils.draw_landmarks(cap,i,hand_lib.HAND_CONNECTIONS)
            lm=i.landmark
            tips={
                name:(int(lm[idx].x*w),int(lm[idx].y*h))
                for name,idx in {
                    'thumb':hand_lib.HandLandmark.THUMB_TIP,
                    'index':hand_lib.HandLandmark.INDEX_FINGER_TIP,
                    'middle':hand_lib.HandLandmark.MIDDLE_FINGER_TIP,
                    'ring':hand_lib.HandLandmark.RING_FINGER_TIP,
                    'pinky':hand_lib.HandLandmark.PINKY_TIP,
                }.items()
            }
            colors=[(255,0,255),(255,255,0),(0,255,0),(0,0,255),(255,0,0)]
            for i,(name,(x,y)) in enumerate(tips.items()):
                cv2.circle(cap,(x,y),10,colors[i],cv2.FILLED)
            thumb_x, thumb_y = tips['thumb']
        index_x, index_y = tips['index']
        current_time = time.time()
        pinch = abs(thumb_x - index_x) < 30 and abs(thumb_y - index_y) < 30
        if pinch and not pinching_progress:
            pinching_progress = True; capture_request = True
        if not pinch and pinching_progress:
            pinching_progress = False
        elif any(abs(thumb_x - tips[finger][0]) < 30 and abs(thumb_y - tips[finger][1]) < 30
            for finger in ['middle', 'ring', 'pinky']):
                last_action_time=0
                if current_time - last_action_time > 1:
                    current_filter = (current_filter + 1) % len(FILTERS)
                    capture=True
                    last_action_time = current_time
                    print("Filter changed to:", FILTERS[current_filter] or "None")
    filtered_img = get_filter(cap, FILTERS[current_filter])
    display_img = cv2.cvtColor(filtered_img, cv2.COLOR_GRAY2BGR) if FILTERS[current_filter]=='GRAYSCALE' else filtered_img
    if capture_request:
            if cv2.waitKey(1) & 0xFF == ord('q'):
                exit()
            cv2.imshow(f"win", display_img)
            capture=False
            cv2.waitKey(1) 