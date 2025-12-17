import cv2
image=cv2.imread('tree.jpg')
grayscale_image=cv2.cvtColor(image,cv2.CV_32F)
cv2.imshow('win',grayscale_image)
resized=cv2.resize(grayscale_image,(1000,1000))
key=cv2.waitKey(0)
if key==ord('q'):
    cv2.imwrite('resized.jpg',resized)