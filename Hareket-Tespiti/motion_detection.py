# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 09:34:42 2021

@author: oguz
"""

# https://gist.github.com/pknowledge/623515e8ab35f1771ca2186630a13d14

import cv2

cap = cv2.VideoCapture("runner.mp4")
ret, frame1 = cap.read()
ret, frame2 = cap.read()
color = (0,255,0)


while cap.isOpened():
    
    diff = cv2.absdiff(frame1, frame2)
    cv2.imshow("Diffrence",diff)
    
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    cv2.imshow("Blurred",blur)
    
    _,thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations = 3) 
    
    
    contours,_ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame1, contours, -1, color, 3)
    
    cv2.imshow("Feed",frame1)
    
    frame1 = frame2
    ret, frame2 = cap.read()
    
    if cv2.waitKey(30) & 0XFF == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()
    


# diff = cv2.absdiff(frame1, frame2)

# cv2.imshow("frame1", frame1)
# cv2.imshow("frame2", frame2)
# cv2.imshow("diff", diff)
    















