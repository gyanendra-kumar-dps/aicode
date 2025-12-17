import cv2
import matplotlib.pyplot as plt
import numpy
image=cv2.imread("tree.jpg")
height=image.shape[0]
width=image.shape[1]
center_width=width//2
center_height=height//2
matrix=cv2.getRotationMatrix2D((center_width,center_height),45,1)
rotate=cv2.warpAffine(image,matrix,(width,height))
brighter=cv2.add(rotate,numpy.full(rotate.shape,50,dtype=numpy.uint8))
cropped_image=brighter[100:300]
plt.imshow(cropped_image)
plt.show()