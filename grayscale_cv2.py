import cv2
image=cv2.imread('tree.jpg')
grayscale_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
resized=cv2.resize(grayscale_image,(224,224))
cv2.imshow('win',resized)
key=cv2.waitKey(0)
if key==ord('q'):
    cv2.imwrite('resized.jpg',resized)