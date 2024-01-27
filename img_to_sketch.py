import numpy as np
import imageio
import cv2
import matplotlib.pyplot as plt
import scipy.ndimage

img = cv2.imread("bd.png")
print(img)
cv2.imshow('original image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

imge = cv2.imread("dark.jpg")
plt.imshow(imge)
plt.axis(False)
plt.show()

def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, .1140])
    
def dodge(front, back):
    final_sketch = front*255/(255-back)
    final_sketch[final_sketch > 255] = 255
    final_sketch[back == 255] = 255
    
    return final_sketch.astype('unit8')

ss = imageio.imread(img)
gray = rgb2gray(ss)

i = 255 - gray

blur = scipy.ndimage.filters.gaussian_filter(i, sigma= 13)

r = dodge(blur, gray)

cv2.imwrite('bd.png', r)
    
    