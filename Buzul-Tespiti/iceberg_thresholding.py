# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 12:55:35 2021

@author: oguz
"""

from tensorflow.keras.models import load_model
import cv2 as cv
import imutils

model = load_model('E:/brain_tumor_detector.h5')

