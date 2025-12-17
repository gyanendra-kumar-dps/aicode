import cv2
import matplotlib.pyplot as plt
image=cv2.imread("tree.jpg")
cv2.arrowedLine(image,(0,30),(600,30),(255,0,255),1,cv2.LINE_AA)
plt.imshow(image)
plt.show()