import cv2
import matplotlib.pyplot as mb
img=cv2.imread('tree.jpg')
BGR2RGB_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
mb.imshow(BGR2RGB_img)
RGB2GRAY_img=cv2.cvtColor(BGR2RGB_img,cv2.COLOR_RGB2GRAY)
cropped_array=img[100:200,200:300]
mb.imshow(RGB2GRAY_img)
mb.imshow(cropped_array)
mb.title('cropped image')
mb.show()