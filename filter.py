import cv2
import numpy as np
image=cv2.imread('tree.jpg')
def filtered_img(tp):
    f_image=image.copy()
    if tp=="red":
        f_image[:,:,0]=0
        f_image[:,:,1]=0
    elif tp=="green":
        f_image[:,:,0]=0
        f_image[:,:,2]=0
    elif tp=="blue":
        f_image[:,:,1]=0
        f_image[:,:,2]=0
    elif tp=="inc_blue":
        f_image[:,:,0]=cv2.add(f_image[:,:,0],50)
    elif tp=="dec_green":
        f_image[:,:,2]=cv2.subtract(f_image[:,:,2],50)
    return f_image
if image is None:
    print('error!!')
else:
    f_img=image
    while True:
        cv2.imshow('f_img',f_img)
        key=cv2.waitKey(0)&0b11111111
        if key==ord('r'):
            f_img=filtered_img('red')
        elif key==ord('g'):
            f_img=filtered_img('green')
        elif key==ord('b'):
            f_img=filtered_img('blue')
        elif key==ord('w'):
            f_img=filtered_img('inc_blue')
        elif key==ord('s'):
            f_img=filtered_img('dec_green')