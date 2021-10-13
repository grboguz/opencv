# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 08:29:07 2021

@author: oguz
"""
# https://realpython.com/python-opencv-color-spaces/
# https://medium.com/srm-mic/color-segmentation-using-opencv-93efa7ac93e2

import cv2
import numpy as np
import matplotlib.pyplot as plt
from Graph3D import Visualize3D_RGB as vis3d_rgb
from Graph3D import Visualize3D_HSV as vis3d_hsv
from Graph3D import hsvDisplayer as hsv_disp




img = cv2.imread("bird.jpg")
#print(img)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# vis3d_rgb(img_rgb)
# vis3d_hsv(img_hsv)

lower_blue = (55,0,0)
upper_blue = (118,255,255)

mask = cv2.inRange(img_hsv,lower_blue,upper_blue)
# cv2.imshow("MAsk", mask)
result = cv2.bitwise_and(img_rgb, img_rgb, mask=mask)
# cv2.imshow("result", result)


plt.subplot(1,2,1)
plt.imshow(mask, cmap="gray")

plt.subplot(1,2,2)
plt.imshow(result)

plt.show()




















