import numpy as np
import imageio.v2 as imageio
import cv2
import matplotlib.pyplot as plt
import scipy.ndimage

img = cv2.imread("bd.png")
print(img)
cv2.imshow('original image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    