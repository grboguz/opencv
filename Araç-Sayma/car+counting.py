import cv2
import numpy as np

vid = cv2.VideoCapture("D:\\OpenCV\\test_videos\\traffic.avi")
backsub = cv2.createBackgroundSubtractorMOG2()
c = 0

while True:
    ret,frame = vid.read()
    if ret:
        fgmask = backsub.apply(frame)
        cv2.line(frame,(50,0),(50,300),(0,255,0),2)
        cv2.line(frame,(70,0),(70,300),(0,255,0),2)

        contours,hierarchy = cv2.findContours(fgmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        try : hierarchy = hierarchy[0]
        except: hierarchy=[]

        for contour,hier in zip(contours,hierarchy):
            (x,y,w,h) = cv2.boundingRect(contour)
            if w>40 and h >40:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
                if x>50 and x<70:
                    c+=1

        # cv2.putText(source_image,text,coordinates,font,size,color,thickness,better look)          
        cv2.putText(frame,"car: "+str(c),(90,100),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2,cv2.LINE_AA)
        

        cv2.imshow("Car Counting",frame)
        cv2.imshow("fgmask",fgmask)
        
        if cv2.waitKey(40) & 0xFF==ord('q'):
            break

vid.release()
cv2.destroyAllWindows()      
