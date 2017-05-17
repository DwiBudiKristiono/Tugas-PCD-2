import numpy as np
import cv2
#import library numpy dan cv2/opencv

img = cv2.imread('1.jpg')
lpf = cv2.filter2D(img,-1,np.ones((5,5),np.float32)/25) #membuat low pass filter dengan kernel 5x5

cv2.imshow('Gambar Asli',img)  #menampilkan gambar asli
cv2.imshow('Low Pass Filter',lpf)  #menampilkan gambar yang sudah diedit dengan low pass filter


cv2.waitKey()
cv2.destroyAllWindows()

