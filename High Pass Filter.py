import numpy as np
import cv2
from scipy import ndimage
#import library numpy dan cv2/opencv

img = cv2.imread('1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
data = np.array(gray, dtype=float)


kernel = np.array([[-9, 9, -9, ],
                   [ 9, 0,  9, ],
                   [-9, 9, -9, ]])
highpass_5x5 = ndimage.convolve(data, kernel)

cv2.imshow('Gambar Asli',img)   #menampilkan gambar asli
cv2.imshow('High Pass Filter',highpass_5x5) #menampilkan gambar yang sudah diedit dengan high pass filter

cv2.waitKey(0)
cv2.destroyAllWindows()
