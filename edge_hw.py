import cv2
import matplotlib.pyplot as plt
import numpy as np
img=cv2.imread('tree.jpg')
plt.imshow(cv2.bitwise_or(cv2.Sobel(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY),cv2.CV_64F,0,1,ksize=5).astype(np.uint8),cv2.Sobel(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY),cv2.CV_64F,1,0,ksize=3).astype(np.uint8)))
plt.imshow(cv2.Canny(img,100,300))
plt.imshow(cv2.Laplacian(img,cv2.CV_64F))
plt.imshow(cv2.GaussianBlur(cv2.cvtColor(img,cv2.COLOR_BGR2RGB),(11,13),0))
plt.imshow(cv2.medianBlur(cv2.cvtColor(img,cv2.COLOR_BGR2RGB),13))
plt.show()