# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 08:41:21 2021

@author: oguz
"""

import cv2
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.colors import hsv_to_rgb

def Visualize3D_RGB(img_rgb):
    
    r, g, b = cv2.split(img_rgb)
    fig = plt.figure()
    axis = fig.add_subplot(1, 1, 1, projection="3d")
    
    
    pixel_colors = img_rgb.reshape((np.shape(img_rgb)[0]*np.shape(img_rgb)[1], 3))
    norm = colors.Normalize(vmin=-1.,vmax=1.)
    norm.autoscale(pixel_colors)
    pixel_colors = norm(pixel_colors).tolist()
    
    
    axis.scatter(r.flatten(), g.flatten(), b.flatten(), facecolors=pixel_colors, marker=".")
    axis.set_xlabel("Red")
    axis.set_ylabel("Green")
    axis.set_zlabel("Blue")
    plt.show()
    
    

def Visualize3D_HSV(img_hsv):
    
    h, s, v = cv2.split(img_hsv)
    fig = plt.figure()
    axis = fig.add_subplot(1, 1, 1, projection="3d")
    
    pixel_colors = img_hsv.reshape((np.shape(img_hsv)[0]*np.shape(img_hsv)[1], 3))
    norm = colors.Normalize(vmin=-1.,vmax=1.)
    norm.autoscale(pixel_colors)
    pixel_colors = norm(pixel_colors).tolist()
    

    axis.scatter(h.flatten(), s.flatten(), v.flatten(), facecolors=pixel_colors, marker=".")
    axis.set_xlabel("Hue")
    axis.set_ylabel("Saturation")
    axis.set_zlabel("Value")
    plt.show()
    
    
def hsvDisplayer(light_black, dark_black):
     
     lo_square = np.full((10, 10, 3), light_black, dtype=np.uint8) / 255.0
     do_square = np.full((10, 10, 3), dark_black, dtype=np.uint8) / 255.0
     plt.subplot(1, 2, 1)
     plt.imshow(hsv_to_rgb(do_square))
     plt.subplot(1, 2, 2)
     plt.imshow(hsv_to_rgb(lo_square))
     plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    