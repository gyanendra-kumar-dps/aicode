import cv2
import matplotlib.pyplot as plt
rgb_image=cv2.cvtColor(cv2.imread("tree.jpg"),cv2.COLOR_BGR2RGB)
cv2.rectangle(rgb_image,(100,200),(200,400),(255,0,255),2)
cv2.circle(rgb_image,(150,300),20,(0,255,255),3)
cv2.line(rgb_image,(200,300),(320,330),(255,55,90),2)
cv2.putText(rgb_image,"Hi guys!!",(50,400),cv2.FONT_HERSHEY_SIMPLEX,1,(255,25,40),2)
cv2.arrowedLine(rgb_image,(100,120),(20,200),(255,100,100),3,cv2.LINE_AA)
plt.figure(figsize=(5,2.5))
plt.title('annotations in cv2')
plt.imshow(rgb_image)
plt.show()