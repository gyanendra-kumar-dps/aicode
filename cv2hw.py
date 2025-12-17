import cv2
import matplotlib.pyplot as plt
import numpy as np
image=cv2.imread('tree.jpg')
rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
(h,w)=image.shape[:2]
print(h,w)
center=(w//2,h//2)
rt=cv2.getRotationMatrix2D(center,180,1.0)
rotate=cv2.warpAffine(image,rt,(w,h))
rotated_img=cv2.cvtColor(rotate,cv2.COLOR_BGR2RGB)
plt.imshow(rotated_img)
plt.show()
plt.imshow(rotated_img[100:400])
plt.show()
brightness=np.ones(image.shape,dtype='uint8')*100
bright_img=cv2.add(image,brightness)
rgb_bright=cv2.cvtColor(bright_img,cv2.COLOR_BGR2RGB)
plt.imshow(rgb_bright)
plt.show()