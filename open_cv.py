import cv2
img=cv2.imread('tree.jpg')
cv2.resizeWindow('image',800,600)
cv2.imshow('window',img)
cv2.waitKey(0)
cv2.destroyAllWindows()